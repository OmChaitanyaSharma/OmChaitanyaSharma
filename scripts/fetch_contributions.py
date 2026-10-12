import json
import re
import requests
from bs4 import BeautifulSoup

USERNAME = "OmChaitanyaSharma"
URL = f"https://github.com/users/{USERNAME}/contributions"

def fetch_data():
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(URL, headers=headers)
    res.raise_for_status()
    
    soup = BeautifulSoup(res.text, "html.parser")
    days = []
    
    for td in soup.find_all("td", class_="ContributionCalendar-day"):
        date = td.get("data-date")
        level = td.get("data-level")
        if date and level is not None:
            days.append({"date": date, "level": int(level)})
            
    h2 = soup.find("h2", class_="f4 text-normal mb-2")
    total_str = "Contributions active"
    if h2:
        m = re.search(r"([\d,]+)\s+contributions", h2.text)
        if m:
            total_str = f"{m.group(1)} contributions in the last year"
            
    payload = {
        "username": USERNAME,
        "total_summary": total_str,
        "days": days
    }
    
    with open("data/contributions.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(f"[+] Fetched {len(days)} calendar days")

if __name__ == "__main__":
    fetch_data()
