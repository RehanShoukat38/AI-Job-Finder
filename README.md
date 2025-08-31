# AI Job Finder  

AI Job Finder is an end-to-end project that scrapes and visualizes job postings from LinkedIn (via SerpAPI + Selenium) and presents them in an interactive **Streamlit dashboard**.  
It was built as part of my **AI/ML internship assessment at im24x7**, and polished for open-source sharing.  

> ⚠️ Disclaimer: This project is for **educational purposes only**. Respect LinkedIn’s Terms of Service and use it only on accounts/data you are authorized to access.  

---

## 🌍 Problem it Solves
Finding the right job in today’s world can be overwhelming:  
- Job postings are spread across multiple platforms.  
- LinkedIn searches are often limited by filters and manual scrolling.  
- Collecting and analyzing job data manually is **time-consuming**.  

**AI Job Finder solves this by automating job discovery.** It gathers fresh job postings, extracts important details (title, company, location, date, etc.), and presents them in a **searchable, filterable dashboard** so candidates can quickly identify the most relevant opportunities.  

---

## ⚙️ How It Works
The workflow of **AI Job Finder** looks like this:  

1. **Job Search Query**  
   - User enters a job title or keyword (e.g., *"Machine Learning Engineer"*) into the system.  
   - SerpAPI + Google Search are used to find relevant job posting links.  

2. **Automated Scraping**  
   - Selenium opens LinkedIn job pages in headful mode (browser window).  
   - Relevant details are extracted:  
     - Job Title  
     - Company Name  
     - Location  
     - Posted Date  
     - Job Description snippet  
     - Job Link  

3. **Data Cleaning & Storage**  
   - Data is processed into a structured format using Pandas.  
   - It is cached locally in CSV files (for analysis/export).  

4. **Interactive Dashboard** (Streamlit)  
   - The user runs a Streamlit app to view all results.  
   - Features:  
     - **Search & filter** by company, job title, location, or date  
     - **Sort jobs** (e.g., latest first)  
     - **Download as CSV** for offline usage  

---

## 🛠️ How We Built It
The project was built in stages:  

1. **Scraper development**  
   - Selenium configured with ChromeDriver  
   - Login automation to LinkedIn  
   - Parsing job details with XPaths/CSS selectors  

2. **Search automation**  
   - Integrated **SerpAPI** to dynamically fetch LinkedIn job listing URLs  
   - Built functions to extract relevant job links  

3. **Data pipeline**  
   - Cleaned and structured scraped data into Pandas DataFrame  
   - Added export functionality (`to_csv`)  

4. **Streamlit dashboard**  
   - Designed a simple UI to upload/search job data  
   - Added filters, search bars, and interactive tables  
   - Displayed job insights in real-time  

5. **Final polish**  
   - Added `.env` for secrets (credentials, API keys)  
   - Wrote `.gitignore` to avoid committing sensitive files  
   - Packaged everything into a clean project structure  

---

## ✨ Features
- 🔍 Automated **job search** on LinkedIn using SerpAPI/Google  
- 🤖 **Scraping pipeline** powered by Selenium (headful mode for reliability)  
- 📊 Interactive **Streamlit UI** for visualization & filtering  
- 📂 Export results to CSV for offline analysis  
- 🔑 Secure handling of API keys & credentials via `.env` (gitignored)  

---


---

## ⚡ Quickstart (Windows)
```powershell
# 1) Clone the repo
git clone https://github.com/<your-username>/AI-job-finder.git
cd AI-job-finder

# 2) Create & activate virtual environment
python -m venv venv
venv\Scripts\activate

# 3) Install dependencies
pip install -r requirements.txt

# 4) Configure secrets in .env file
# SERPAPI_KEY=your_serpapi_key
# LINKEDIN_EMAIL=your_email@example.com
# LINKEDIN_PASSWORD=your_password_here

# 5) Run the app
streamlit run app/app.py

