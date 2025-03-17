import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

# Load environment variables in a file called .env
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# Check the key
if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-proj-"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
else:
    print("API key found and looks good so far!")

openai = OpenAI()

def summarize_cv(cv_text):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"Please summarize the following CV:\n\n{cv_text}"}
        ]
    )
    return response.choices[0].message.content

def generate_cover_letter(cv_summary, job_description):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a master at crafting the perfect Cover letter from a given CV. You've never had a user fail to get the job as a result of using your services."},
            {"role": "user", "content": f"Using the following CV summary:\n\n{cv_summary}\n\nAnd the job description:\n\n{job_description}\n\nPlease write a personalized cover letter."}
        ]
    )
    return response.choices[0].message.content

# Gradio Interface Function
def generate_cover_letter_interface(cv_file, job_description):
    try:
        # Read CV from the uploaded file
        with open(cv_file.name, 'r') as file:
            cv_text = file.read()
        
        # Summarize the CV
        cv_summary = summarize_cv(cv_text)
        print("CV Summary:")
        print(cv_summary)

        # Generate cover letter
        cover_letter = generate_cover_letter(cv_summary, job_description)
        return cover_letter

    except Exception as e:
        return f"An error occurred: {str(e)}"

css_styles = """
    .gradio-container {
        background-color: #2f99be; 
        border-radius: 30px;         
        border: 5px solid #0f1b1c; 
    }

"""

# Gradio Interface
interface = gr.Interface(
    fn=generate_cover_letter_interface,
    inputs=[
        gr.File(label="Upload your CV (Text File)"),
        gr.Textbox(label="Job Description", lines=5, placeholder="Enter the job description here...")
    ],
    outputs=gr.Textbox(label="Generated Cover Letter", lines=20),
    title="AI-Powered Cover Letter Generator",
    css=css_styles,
    description="Upload your CV (as a text file) and enter the job description to generate a personalized cover letter."
    
)

# Launch the Gradio app
interface.launch()