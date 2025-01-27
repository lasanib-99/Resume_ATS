'''
Procedure:
1. Field to put my JD
2. Upload PDF
3. PDF to image ---> Processing ---> Google Gemini Pro
4. Prompts Template [Multiple Prompts]
'''

from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import io
import pdf2image
import google.generativeai as genai
import base64

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# Configure the new Gemini 2.0 Flash Experimental model
def get_gemini_response(input, pdf_content, prompt):

    model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

    # Generate the response using the model
    response = model.generate_content(
        [input, pdf_content[0], prompt]
    )

    return response.text

def input_pdf_setup(uploaded_file):

    if uploaded_file is not None:

        # Convert the PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format = 'JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode() # Encode to base64
            }
        ]

        return pdf_parts

    else:
        raise FileNotFoundError("No file uploaded!")
    
# Streamlit app

st.set_page_config(page_title = "ATS Resume Expert")

st.header("ATS Tracking System")

input_text = st.text_area("Job Description: ", key = "input")

uploaded_file = st.file_uploader("Upload your resume (PDF)...", type = ["pdf"])

# Condition in file upload
if uploaded_file is not None:
    st.write("PDF Uploaded Successfully!")

submit1 = st.button("Tell Me About My Resume")

submit2 = st.button("Percentage Match")

input_prompt1 = """
You are an experienced HR with tech experience in any of the job roles in Data Science, Full Stack Web development, Big Data Engineering, DEVOPS and Data Analyst.
Your task is to review the provided resume against the job description for these profiles. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding in any of the job roles in Data Science, Full Stack Web development, Big Data Engineering, DEVOPS and Data Analyst along with deep ATS functionality. 
Your task is to evaluate the resume against the provided job description. 
Give me the percentage of match if the resume matches the job description. 
First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1:

    if uploaded_file is not None:

        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response: ")
        st.write(response)
    
    else:
        st.write("Please upload the resume...")

elif submit2:

    if uploaded_file is not None:

        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("The Response: ")
        st.write(response)
    
    else:
        st.write("Please upload the resume...")