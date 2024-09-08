#!/usr/bin/env python
import sys
from tailor_resume.crew import TailorResumeCrew


def run():
    inputs = {
        "job_posting": "https://www.linkedin.com/jobs/view/4004986314/",
        "linkedin_source_cv_filename": "src/resumes/linkedin_cv_rafael_pt_br.pdf",
        "linkedin_target_cv_filename": "src/resumes/linkedin_cv.md",
        "crew_generated_resume": "crew_generated_resume.md",
        # "target_language" : "pt-BR",
    }
    TailorResumeCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "job_posting": "https://www.linkedin.com/jobs/view/4004986314/",
        "linkedin_source_cv_filename": "src/resumes/linkedin_cv_rafael_pt_br.pdf",
        "linkedin_target_cv_filename": "src/resumes/linkedin_cv.md",
        "crew_generated_resume": "crew_generated_resume.md",
        # "target_language" : "pt-BR",
    }
    try:
        TailorResumeCrew().crew().train(
            n_iterations=3,
            inputs=inputs,
            filename="trained_agents_data.pkl",
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
