from langchain.tools import Tool
from langchain.agents import initialize_agent
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

def write_job_description_fn(role: str) -> str:
    return f"Job Description for a {role}: \n\nWe are looking for a talented {role} to join our growing team..."

def search_resume_database_fn(query: str) -> str:
    return f"Found 5 resumes matching: '{query}'"

# Simulated tool list
tools = [
    Tool(
        name="write_job_description",
        func=write_job_description_fn,
        description="Use this to write a job description. Input should be a role title like 'Data Scientist'"
    ),
    Tool(
        name="search_resume_database",
        func=search_resume_database_fn,
        description="Search resume database. Input should be a skill or role keyword like 'Python Developer'"
    )
]

llm = ChatOpenAI(temperature=0)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",  # or other agent types
    verbose=True
)

response = agent.run("HR: Help me write a job description for a Data Scientist")
print(response)
