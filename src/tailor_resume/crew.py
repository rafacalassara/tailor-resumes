from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, PDFSearchTool, FileReadTool
import os

from .llm import create_claude_llm, create_groq_llm
from .tools.custom_tool import create_markdown_file

pdf_config = dict(
    llm=dict(
        provider="groq",
        config=dict(
            model="llama3-70b-8192",
            temperature=0.1,
            api_key=os.getenv('GROQ_API_KEY'),
        ),
    ),
    embedder=dict(
        # or openai, ollama, ...
        provider="huggingface",
        config=dict(
            model="BAAI/bge-small-en-v1.5",
        ),
    ),
)


@CrewBase
class TailorResumeCrew():
    """TailorResume crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def linkedin_pdf_cv_reader(self) -> Agent:
        return Agent(
            config=self.agents_config['linkedin_pdf_cv_reader'],
            allow_delegation=False,
            verbose=True,
            llm=create_claude_llm(),
            # llm=create_groq_llm('llama3-70b-8192', temperature=0.01)
        )

    @agent
    def job_requirements_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['job_requirements_extractor'],
            tools=[ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
            llm=create_claude_llm(),
            # llm=create_groq_llm(model_name='llama3-groq-70b-8192-tool-use-preview', temperature=0.01)
        )

    @agent
    def resume_tailor(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_tailor'],
            allow_delegation=False,
            verbose=True,
            tools=[create_markdown_file, FileReadTool()],
            # llm=create_groq_llm(model_name='llama-3.1-70b-versatile'),
            llm=create_claude_llm()
        )

    @task
    def pdf_to_md_cv_task(self) -> Task:
        return Task(
            config=self.tasks_config['pdf_to_md_cv_task'],
            agent=self.linkedin_pdf_cv_reader(),
            tools=[PDFSearchTool(config=pdf_config), create_markdown_file],
            # output='crew_generated_resume.md'
        )

    @task
    def extract_job_requirements_task(self) -> Task:
        return Task(
            config=self.tasks_config['extract_job_requirements_task'],
            agent=self.job_requirements_extractor()
        )

    @task
    def tailor_resume_task(self) -> Task:
        return Task(
            config=self.tasks_config['tailor_resume_task'],
            agent=self.resume_tailor(),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TailorResume crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
