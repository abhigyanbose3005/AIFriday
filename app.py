
import streamlit as st
from crewai import Agent, Task, Crew
from crewai_tools import RagTool

st.set_page_config(page_title="GenInsurance Assistant", layout="centered")
st.title("📄 GenInsurance PDF Assistant")

rag_tool = RagTool(
    persist_directory="./vector_db",
    embedding_model="openai"
)

try:
    rag_tool.add(data_type="file", path="geninsurance_policy.pdf")
except Exception as e:
    st.error(f"Error loading PDF: {e}")

pdf_agent = Agent(
    role="Insurance Analyst",
    goal="Answer questions based on the GenInsurance PDF",
    backstory="An expert in insurance policy analysis.",
    tools=[rag_tool],
    verbose=True,
    allow_delegation=False,
    model="gpt-4",
    temperature=0.5
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

user_input = st.chat_input("Ask something about the GenInsurance PDF...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    task = Task(
        description=user_input,
        expected_output="Answer based on the GenInsurance PDF content.",
        agent=pdf_agent
    )

    crew = Crew(agents=[pdf_agent], tasks=[task])
    result = crew.kickoff()

    st.chat_message("assistant").markdown(result)
    st.session_state.messages.append({"role": "assistant", "content": result})
