#!/usr/bin/env python
from tailor_resume.crew import TailorResumeCrew
import os
from dotenv import load_dotenv

load_dotenv()

def run():
    inputs = {
        "job_posting": os.getenv('JOB_POSTING_URL'),
        "base_resume": "/src/resumes/base_resume.md",
        "linkedin_source_resume_filename": "/src/resumes/source_resume.pdf",
        "linkedin_target_resume_filename": "/src/resumes/target_resume.md",
        "crew_generated_resume": "crew_generated_resume.md",
    }
    TailorResumeCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "job_posting": os.getenv('JOB_POSTING_URL'),
        "base_resume": "/src/resumes/base_resume.md",
        "linkedin_source_resume_filename": "/src/resumes/source_resume.pdf",
        "linkedin_target_resume_filename": "/src/resumes/target_resume.md",
        "crew_generated_resume": "crew_generated_resume.md",
    }
    try:
        TailorResumeCrew().crew().train(
            n_iterations=3,
            inputs=inputs,
            filename="trained_agents_data.pkl",
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
