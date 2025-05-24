import fitz  # PyMuPDF
from openai import OpenAI

import gspread
import smtplib
from email.message import EmailMessage
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

# ========== CONFIG ==========
client = OpenAI(api_key = "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") 

GOOGLE_CREDENTIALS = "your-creds.json"  # JSON file from Google Cloud
SPREADSHEET_NAME = "Resume Screener Results"
HR_EMAIL = "hr@email.com"
YOUR_EMAIL = "saivamshijilla04@gmai.com"
YOUR_EMAIL_PASSWORD = "space1psycho"

# ========== FUNCTIONS ==========

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def analyze_resume(resume_text, job_description):
    prompt = f"""
    Job Description:
    {job_description}

    Resume:
    {resume_text}

    Analyze how well this resume matches the job. Score it out of 10 and explain why.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def save_to_google_sheet(name, score, feedback):
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_CREDENTIALS, scope)
    client = gspread.authorize(creds)
    sheet = client.open(SPREADSHEET_NAME).sheet1
    sheet.append_row([name, score, feedback])

def send_email_notification(resume_owner, feedback):
    msg = EmailMessage()
    msg.set_content(f"Resume Match Found:\n\n{feedback}")
    msg['Subject'] = f'Resume Match: {resume_owner}'
    msg['From'] = YOUR_EMAIL
    msg['To'] = HR_EMAIL

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(YOUR_EMAIL, YOUR_EMAIL_PASSWORD)
        smtp.send_message(msg)

def parse_score_from_result(result_text):
    import re
    match = re.search(r"Score\s*[:\-]?\s*(\d+)", result_text)
    return int(match.group(1)) if match else 0

# ========== STREAMLIT UI ==========

st.title("📄 AI Resume Screener")

resume = st.file_uploader("Upload Resume (PDF)", type="pdf")
job_desc = st.text_area("Paste Job Description")
candidate_name = st.text_input("Candidate Name")

if st.button("Analyze Resume"):
    if resume and job_desc and candidate_name:
        with st.spinner("Analyzing..."):
            text = extract_text_from_pdf(resume)
            analysis = analyze_resume(text, job_desc)
            score = parse_score_from_result(analysis)

            save_to_google_sheet(candidate_name, score, analysis)

            st.success("Analysis Complete!")
            st.markdown(f"### Match Score: {score}/10")
            st.write(analysis)

            if score >= 7:
                send_email_notification(candidate_name, analysis)
                st.info("Email sent to HR (Score ≥ 7)")
    else:
        st.warning("Please fill all fields before submitting.")

