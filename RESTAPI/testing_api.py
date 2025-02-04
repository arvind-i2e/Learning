from flask import Flask, request, jsonify
import os
import google.generativeai as genai
import json

genai.configure(api_key='AIzaSyBFJjy2Fygh6FOcc35bn3anbRj5v479oU8')  

# Model Configuration 
generation_config = {
    "temperature": 0.3,  # Lower temperature for more factual responses
    "top_p": 0.7,
    "top_k": 20,
    "max_output_tokens": 8000,
    "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest", 
    generation_config=generation_config
)

def extract_metadata(name):
    prompt = f'''Given the name "{name}", extract the following 
    metadata from reliable public sources. Return ONLY a JSON object with these fields:
    {{
        "full_name": "string (include salutations)",
        "gender": "string",
        "qualification": "array of strings",
        "primary_affiliation": "string(Look into institutional website for it or Google scholar)",
        "department": "string",
        "title": "string",
        "contact_details": {{
            "email": "string",
            "phone": "string",
            "fax": "string"
        }},
        "social_media": {{
            "twitter": "url",
            "linkedin": "url",
            "other": "url"
        }},
        "professional_summary": "string(More detailed information around 200-400 words)",
        "education": "array of strings",
        "professional_history": "array of strings",
        "conferences_awards": "array of strings",
        "areas_of_interest": "array of strings"
    }}

    Instructions:
    1. Use verified sources like (institutional websites,Wikipedia,Google Scholar,yashfiin.com,ClinicalTrials.gov)
    2. Return "Not found" for missing fields
    3. Never invent information
    4. Maintain strict JSON format
    5. Escape special characters
    '''

    try:
        response = model.generate_content(prompt)
        
        # Clean response text
        json_str = response.text.replace('```json', '').replace('```', '').strip()
        
        return json.loads(json_str)
    except Exception as e:
        return {"error": str(e), "raw_response": response.text if 'response' in locals() else None}

app = Flask(__name__)

@app.route("/get_kol_metadata", methods=["GET"])
def get_kol_metadata():
    kol_name = request.args.get("kol_name")
    # affiliation = request.args.get("affiliation")
    
    if not kol_name :
        return jsonify({"error": "Missing required parameters: kol_name and affiliation"}), 400
    
    try:
        metadata = extract_metadata(kol_name)
        return jsonify(metadata)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)