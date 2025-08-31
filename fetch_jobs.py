import os
import pandas as pd
from datetime import datetime
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("SERPAPI_API_KEY")

# Ask for job keyword
job_keyword = input("🔎 Enter job keyword to search (e.g., Python Developer): ").strip()

params = {
    "engine": "google_jobs",
    "q": job_keyword,
    "hl": "en",
    "api_key": API_KEY
}

search = GoogleSearch(params)
results = search.get_dict()

jobs_data = []

if "jobs_results" in results:
    jobs_list = results["jobs_results"][:5]  # Fetch first 5 jobs
    for job in jobs_list:
        company_name = job.get("company_name", "N/A")
        job_description = job.get("description", "N/A")
        date_today = datetime.today().strftime("%m/%d/%Y")
        jobs_data.append([company_name, job_description, date_today])

    # Save to CSV with timestamp to avoid overwriting
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_file = f"linkedin_jobs_{timestamp}.csv"
    df = pd.DataFrame(jobs_data, columns=["Company Name", "Job Details", "Date"])
    df.to_csv(csv_file, index=False, encoding="utf-8")
    print(f"\n✅ Done. Saved {len(jobs_data)} jobs to {csv_file}")

else:
    print("⚠️ No jobs found. Check your API key or keyword.")
