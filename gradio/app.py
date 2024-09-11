import gradio as gr
import os
from tailor_resume.crew import TailorResumeCrew

# add a BASE_DIR dinamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# input variables
base_resume =  os.path.join(BASE_DIR, "base_resume.md")
linkedin_target_resume_filename =  os.path.join(BASE_DIR,"target_resume.md")
crew_generated_resume =  os.path.join(BASE_DIR, "crew_generated_resume.md")

def tailor_resume(job_posting, linkedin_pdf_cv):
    crew = TailorResumeCrew()
    resume = crew.crew().kickoff({
        "job_posting": job_posting,
        "base_resume": base_resume,
        "linkedin_source_resume_filename": linkedin_pdf_cv,
        "linkedin_target_resume_filename": linkedin_target_resume_filename,
        "crew_generated_resume": crew_generated_resume,
    })
    # Return the resume as a string and the file as a bytes object
    return resume, crew_generated_resume

demo = gr.Interface(
    fn=tailor_resume,
    inputs=[
        gr.Textbox(label="Job Posting URL"),
        gr.File(label="Linkedin PDF CV"),
    ],
    outputs=[
        gr.Textbox(label="Tailored Resume"),
        gr.File(label="Download Tailored Resume"),
    ],
    title="Resume Tailor Crew",
    description="Tailor your resume to a specific job posting",
)

if __name__ == "__main__":
    demo.launch()
