# AI-Powered Cover Letter Generator

## Overview

This project is an AI-powered tool that generates personalized cover letters based on a user's CV and a job description. It uses OpenAI's GPT-4 model to summarize the CV and create a tailored cover letter. The tool is built with Python and provides a user-friendly web interface using **Gradio**.

## Features

- **CV Summarization**: Automatically summarizes the uploaded CV.
- **Personalized Cover Letter**: Generates a cover letter tailored to the job description.
- **User-Friendly Interface**: Simple web interface for uploading CVs and entering job descriptions.
- **Error Handling**: Provides clear error messages if something goes wrong.

---

## Prerequisites

Before running the project, ensure you have the following:

1. **Python 3.7 or higher** installed on your system.
2. An **OpenAI API key**. You can get one from [OpenAI's website](https://platform.openai.com/).
3. Required Python libraries installed.

---

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/kkariyawasam/cover-letter-from-cv.git
   cd cover-letter-from-cv
   ```

2. **Set Up API Key**

   - Create a `.env` file in the project directory and add:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

3. **Run the Chatbot**

   ```bash
   python cover_letter_from_cv.py
   ```

4. **UI Preview**

   <img width="920" alt="image" src="https://github.com/user-attachments/assets/f1e0841e-4ecd-4e56-a8b1-80bcbc27ac9a" />

