# TailorResume Crew

TailorResume Crew is an advanced AI-powered system designed to tailor resumes for specific job postings. This program leverages the crewAI framework to create a multi-agent AI system that collaborates to produce customized resumes.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Advanced Features](#advanced-features)
- [Tools and Technologies](#tools-and-technologies)
- [Contributing](#contributing)
- [License](#license)

## Features

- Reads a PDF resume and converts it to Markdown format
- Extracts job requirements from a given job posting URL
- Tailors the resume based on the extracted job requirements
- Utilizes multiple AI agents for different tasks:
  - LinkedIn PDF CV Reader
  - Job Requirements Extractor
  - Resume Tailor

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/TailorResume-Crew.git
   cd TailorResume-Crew
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

5. Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

   First, if you haven't already, install Poetry:

   ```bash
   pip install poetry
   ```

   1. First lock the dependencies and then install them:
   ```bash
   poetry lock
   ```
   ```bash
   poetry install
   ```

5. Set up environment variables:
   Create a copy of `.env` file in the project root directory and add the following variables:
   ```
   OPENAI_API_KEY=YOUR-API-KEY
   GROQ_API_KEY=YOUR-API-KEY
   ANTHROPIC_API_KEY=YOUR-API-KEY

   JOB_POSTING_URL=YOUR-JOB-POSTING-URL
   ```
   Replace `YOUR-API-KEY` with your actual API key and `YOUR-JOB-POSTING-URL` with your desired job.

## Usage

1. Ensure you're in the project directory and your virtual environment is activated.

2. Download your resume from your Linkedin Profile in PDF format and put it on `/src/resumes`.

3. On `src/tailor_resume/main.py` modify:
   - `base_resume` to the path of your base resume
   - `linkedin_source_cv_filename` to the path of your Linkedin resume 
   - `linkedin_target_cv_filename` to the path of your target resume in MD format


4. Run the main script:
   ```bash
   poetry run tailor_resume
   ```

5. The program will generate a tailored resume based on your Linkedin resume and the job description.

6. The tailored resume will be saved as a Markdown file in the root directory.

## Configuration

Users can customize the program by modifying:
- Agent definitions in `config/agents.yaml`
- Task definitions in `config/tasks.yaml`
- The `crew.py` file to add custom logic or tools

## Advanced Features

- The program includes a training function that can improve the AI agents' performance over multiple iterations
- It uses various AI models, including Claude from Anthropic and Llama3 from Groq, for different tasks

## Tools and Technologies

- Web scraping for job requirement extraction
- PDF parsing for resume reading
- Markdown file creation for output
- Integration with various AI models and APIs

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the