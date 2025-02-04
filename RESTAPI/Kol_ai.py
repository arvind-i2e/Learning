import os
import google.generativeai as genai
import json

genai.configure(api_key='AIzaSyBFJjy2Fygh6FOcc35bn3anbRj5v479oU8') 

# Model Configuration
generation_config = {
    "temperature": 0.95,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 500,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp", 
    generation_config=generation_config
)

def extract_metadata(name, affiliation):
    prompt = f'''
    Given the name "{name}" and primary affiliation "{affiliation}", extract the following metadata from reliable sources:

1. **Full Name**: Look for any salutation (e.g., Dr., Prof.) if available, and ensure the full name is accurate.
2. **Gender**: Identify the gender based on publicly available data or social media profiles.
3. **Qualification**: Search for academic qualifications (e.g., PhD, M.D.) from academic profiles, professional websites, or publications.
4. **Primary Affiliation**: Verify the primary affiliation (university, institution, or company), which can be found in research papers, professional websites, or public records.
5. **Department**: If available, extract the department or division within the primary affiliation from sources like the institutional website or publication.
6. **Title**: Look for the professional title (e.g., Professor, Researcher) from institutional webpages, social media, or public databases.
7. **Contact Details**: Extract any contact details (email, phone, fax) available on public profiles, official websites, or academic publications. Ensure privacy and confidentiality.
8. **Social Media**: Search for public social media profiles (Twitter, Facebook, Instagram) and retrieve the most professional and relevant links if publically available.
9. **Professional Summary**: detailed professional summary of the KOL the professional background by extracting key details from the individual's LinkedIn, personal website, or academic articles,social media handele if publically available.
10. **Education**: Find educational background from verified academic profiles or research papers.
11. **Professional History**: Extract previous positions, affiliations, or roles from professional networks (e.g., LinkedIn), published works, or biography pages.
12. **Conferences & Awards**: Search for relevant conferences attended and awards received from academic profiles, event websites, or research publications.
13. **Areas of Interest & Specialization**: Look for the individual's primary areas of research, specialization, or topics of interest from publications, professional profiles, or project descriptions.

Use the most authoritative and publicly available sources (e.g.,Conference proceedings, Google Scholar,wikipedia,indicure, LinkedIn, institutional websites, academic journals) to gather this information. Ensure that all details are relevant and up-to-date and data should be closer to accuracy if u make an assumption, prioritizing professional and scholarly sources.
 just giveout direct answer i don't need explanation.
    '''
    
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)
    
    try:
        return json.loads(response.text)
    except json.JSONDecodeError:
        return {"error": "Failed to parse JSON response", "raw_response": response.text}

def write_metadata_to_file(metadata, file_path):
    """
    Write the extracted metadata to a text file.
    """
    with open(file_path, "w") as file:
        if isinstance(metadata, dict):
            for key, value in metadata.items():
                file.write(f"{key}: {value}\n")
        else:
            file.write(str(metadata))

if __name__ == "__main__":
    name_input = "Dr. Jitendra Kumar Singh"
    affiliation_input = "Mahavir Cancer Sansthan & Research"
    metadata = extract_metadata(name_input, affiliation_input)
    
    # Write metadata to a text file
    output_file = "kol_meta1.txt"
    write_metadata_to_file(metadata, output_file)
    print(f"Metadata written to {output_file}")
