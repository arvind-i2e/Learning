import requests
from bs4 import BeautifulSoup
import json

# URL of the page to scrape
url = "https://www.indicure.com/best-cardiologist-india/"
headers = {"User-Agent": "Mozilla/5.0"}

# Send GET request
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    doctors_data = []

    # Modify these selectors based on the website's actual structure
    doctors = soup.find_all("div", class_="doctor-box")  # Adjust based on inspection

    for doctor in doctors:
        name = doctor.find("h3").text.strip() if doctor.find("h3") else "N/A"
        specialty = doctor.find("h4").text.strip() if doctor.find("h4") else "N/A"
        experience = doctor.find("p", class_="experience").text.strip() if doctor.find("p", class_="experience") else "N/A"
        location = doctor.find("p", class_="location").text.strip() if doctor.find("p", class_="location") else "N/A"
        summary = doctor.find("p", class_="summary").text.strip() if doctor.find("p", class_="summary") else "N/A"

        # Store data
        doctors_data.append({
            "name": name,
            "specialty": specialty,
            "experience": experience,
            "location": location,
            "summary": summary
        })

    # Save data to JSON
    with open("cardiologists.json", "w", encoding="utf-8") as f:
        json.dump(doctors_data, f, ensure_ascii=False, indent=4)

    print("Scraping completed. Data saved to cardiologists.json.")

else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
