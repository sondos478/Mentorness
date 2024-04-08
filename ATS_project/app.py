from dotenv import load_dotenv
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai
import re
import csv
import pdfplumber
import docx

load_dotenv()
import os

# Set the environment variable
os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY_HERE"

# Regular expressions for contact information extraction
name_pattern = r'^([A-Z][a-z]+(\s[A-Z][a-z]+)+)'
phone_pattern = r'\(\+\d{1,2}\)\d{10}'
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def extract_contact_info(text):
    name = re.search(name_pattern, text)
    # phone = 0
    phone = re.search(phone_pattern, text)
    email = re.search(email_pattern, text)

    return (
        name.group(1) if name else '',
        phone.group(0) if phone else '',
        email.group(0) if email else ''
    )

def process_file(file):
    text = ''
    if file.name.endswith('.pdf'):
        with pdfplumber.open(file) as pdf:
            text = '\n'.join([page.extract_text() for page in pdf.pages])
    elif file.name.endswith('.docx'):
        doc = docx.Document(file_path)
        text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    elif file.name.endswith('.txt'):
        with open(file_path, 'r') as file:
            text = file.read()
    else:
        raise Exception("unsupported file type (please make sure it's (.pdf-.docx-.txt) file please)")

    return extract_contact_info(text)

def save_to_csv(contact_info):
    with open('Contact_information.csv', 'w', newline='') as csvfile:
        fieldnames = ['Candidate Name', 'Phone Number', 'Email Address']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for filename, info in contact_info.items():
            writer.writerow(info)

def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_text, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read(), poppler_path=r'C:\Users\Sondos\Downloads\Release-24.02.0-0\poppler-24.02.0\Library\bin')
        
        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(page_title="Résumé Rascal")
#st.set_option('theme.primaryColor)  # Mint green
#st.set_option('theme.backgroundColor', '#FFFFFF')  # White
st.header("Résumé Rascal: Your Hiring Sidekick")

input_text = st.text_area("Job Description:")
uploaded_file = st.file_uploader("Upload your résumé (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Analyze the Résumé")
submit2 = st.button("Suggest Improvements")
submit3 = st.button("Percentage Match")
submit4 = st.button("Hiring Recommendations")
submit5 = st.button("Extract Contact Information")

input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided résumé against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are a career coach with expertise in résumé optimization. Your task is to provide constructive feedback on how the applicant can improve their résumé to better match the job description.
Suggest specific areas for improvement, such as skills, experience, and presentation.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the résumé against the providedjob description and calculate the percentage match. 
Highlight the key skills and qualifications that match the job requirements, and identify any areas where the résumé falls short.
"""

input_prompt4 = """
You are an HR manager responsible for shortlisting candidates based on the résumé. 
Your task is to review the résumé and provide hiring recommendations. 
Indicate whether the candidate should be shortlisted, rejected, or further evaluated based on their qualifications and experience.
"""

if submit1:
    if uploaded_file is not None:
        pdf_parts = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_parts, input_prompt1)
        st.write(response)
    else:
        st.write("Please upload the résumé")

if submit2:
    if uploaded_file is not None:
        pdf_parts = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_parts, input_prompt2)
        st.write(response)
    else:
        st.write("Please upload the résumé")

if submit3:
    if uploaded_file is not None:
        pdf_parts = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_parts, input_prompt3)
        st.write(response)
    else:
        st.write("Please upload the résumé")

if submit4:
    if uploaded_file is not None:
        pdf_parts = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_parts, input_prompt4)
        st.write(response)
    else:
        st.write("Please upload the résumé")

if submit5:
    if uploaded_file is not None:
        contact_info = {}
        try:
            name, phone, email = process_file(uploaded_file)
        except Exception as e:
            st.error(f'Unsupported file format: {uploaded_file.name}')
            st.stop()

        contact_info[uploaded_file.name] = {
            'Candidate Name': name,
            'Phone Number': phone,
            'Email Address': email
        }

        save_to_csv(contact_info)
        st.write("Contact information extracted and saved to 'Contact_information.csv'")
    else:
        st.write("Please upload the résumé")