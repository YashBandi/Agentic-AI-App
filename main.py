# main.py

import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, Tool
from langchain.memory import ConversationBufferMemory
from tools import generate_job_description, suggest_sourcing_strategy, plan_interview_process

# Load environment variables from .env
load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

# Define tools for the agent (make sure your functions accept one argument if needed)
tools = [
    Tool(
        name="GenerateJobDescription",
        func=lambda x: generate_job_description("Backend Engineer", "Mid-level", "early"),
        description="Generate job description for a given role, level, and startup stage"
    ),
    Tool(
        name="SuggestSourcingStrategy",
        func=lambda x: suggest_sourcing_strategy("Backend Engineer"),
        description="Suggests sourcing channels for the specified role"
    ),
    Tool(
        name="PlanInterviewProcess",
        func=lambda x: plan_interview_process("Backend Engineer", "Mid-level"),
        description="Plans an interview process for a specific role"
    ),
]

# Initialize LLM with the API key from environment variable
llm = ChatOpenAI(
    model="gpt-3.5-turbo",  # or "gpt-4-turbo" if you have access
    temperature=0,
    openai_api_key=openai_api_key
)

# Add conversation memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Initialize the conversational agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# Interactive CLI
if __name__ == "__main__":
    print("👋 HR Assistant Agent is ready. Type 'exit' to stop.")
    while True:
        user_input = input("HR: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = agent.invoke({"input": user_input})
        print("AI:", response)


