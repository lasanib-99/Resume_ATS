# Resume_ATS

**ATS Tracking System** is an application designed to help users analyze their resumes against job descriptions using AI technology. This project simplifies the hiring process by providing insightful feedback on resumes and calculating a match percentage between the resume and the job description.

## Features

- **Job Description Input**: Add a job description to analyze.
- **Resume Upload**: Upload resumes in PDF format for evaluation.
- **Resume Analysis**: Provides detailed feedback about your resume's alignment with the job description.
- **Match Percentage**: Calculates and displays how well the resume fits the job description.

## Technologies Used

- **Backend**: Python with Google Gemini AI (Gemini 1.5 Pro Model for NLP tasks).
- **Frontend**: Streamlit for creating the user interface.
- **Libraries**: 
  - `google-generative-ai` for integrating Gemini models.
  - `PyPDF2` for handling PDF parsing.

## How to Use

1. Input the job description in the designated text area.
2. Upload your resume (PDF format).
3. Click on **"Tell Me About My Resume"** to receive detailed feedback.
4. Use the **"Percentage Match"** button to assess how well your resume aligns with the job description.

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```
   
2. Install required Python dependencies:
  ```bash
  pip install -r requirements.txt
  ```

3. Run the application:
  ```bash
  streamlit run app.py
  ```
