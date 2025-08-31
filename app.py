import os
import pandas as pd
from datetime import datetime
from serpapi import GoogleSearch
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
API_KEY = os.getenv("SERPAPI_API_KEY")

# --- Streamlit UI ---
st.set_page_config(page_title="LinkedIn Job Fetcher", layout="wide")
st.markdown(
    "<h1 style='text-align: center; color: #4B8BBE;'>🔎 LinkedIn Job Fetcher</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; font-size: 16px;'>Fetch first 5 job postings including company name, job details, and date.</p>",
    unsafe_allow_html=True
)

job_keyword = st.text_input("Enter job keyword (e.g., Python Developer):")

if st.button("Fetch Jobs"):
    if not job_keyword:
        st.warning("⚠️ Please enter a job keyword to search!")
    else:
        st.info(f"🔍 Searching for jobs with keyword: {job_keyword} ...")

        params = {
            "engine": "google_jobs",
            "q": job_keyword,
            "hl": "en",
            "api_key": API_KEY
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        jobs_data = []

        if "jobs_results" in results and results["jobs_results"]:
            jobs_list = results["jobs_results"][:5]  # First 5 jobs

            # Scrollable container for job cards
            container = st.container()
            with container:
                for idx, job in enumerate(jobs_list, start=1):
                    company_name = job.get("company_name", "N/A")
                    job_description = job.get("description", "N/A")
                    date_today = datetime.today().strftime("%m/%d/%Y")
                    jobs_data.append([company_name, job_description, date_today])

                    # Card style for each job
                    st.markdown(
                        f"""
                        <div style="
                            background: linear-gradient(135deg, #e0f7fa, #b2ebf2);
                            padding: 20px;
                            border-radius: 15px;
                            margin-bottom: 20px;
                            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
                        ">
                            <h3 style='color: #006064;'>Job {idx}: {company_name} ({date_today})</h3>
                            <p style='font-size: 14px; line-height: 1.5; color: #004d40;'>{job_description}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            # Save CSV with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            csv_file = f"linkedin_jobs_{timestamp}.csv"
            df = pd.DataFrame(jobs_data, columns=["Company Name", "Job Details", "Date"])
            df.to_csv(csv_file, index=False, encoding="utf-8")

            st.success(f"✅ Done! Saved {len(jobs_data)} jobs to `{csv_file}`")
            st.download_button(
                label="📥 Download CSV",
                data=df.to_csv(index=False).encode("utf-8"),
                file_name=csv_file,
                mime="text/csv"
            )

        else:
            st.warning("⚠️ No jobs found. Check your API key or keyword.")
