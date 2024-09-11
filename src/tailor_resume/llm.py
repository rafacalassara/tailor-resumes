import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_anthropic import ChatAnthropic

load_dotenv()


def create_claude_llm(model="claude-3-5-sonnet-20240620", temperature=0.75):
    return ChatAnthropic(
        model=model,
        temperature=temperature,
        max_tokens=1024,
        timeout=None,
        max_retries=2,
        cache=True,
        api_key=os.getenv('ANTHROPIC_API_KEY'),
    )


def create_groq_llm(model_name="llama3-70b-8192", temperature=0.75):
    return ChatGroq(
        api_key=os.getenv('GROQ_API_KEY'),
        model_name=model_name,
        temperature=temperature,
        max_retries=2,
    )
