
from crewai import Agent, Task, Crew

# Retriever agent
retriever = Agent(
    role="Retriever",
    goal="Find the most relevant documents for the user's query",
    backstory="An expert in semantic search and document retrieval",
    tools=[your_vector_search_tool],
    verbose=True
)

# Generator agent
generator = Agent(
    role="Answer Generator",
    goal="Generate accurate answers grounded in retrieved context",
    backstory="A careful and precise language model",
    verbose=True
)

# Optional verifier agent
verifier = Agent(
    role="Verifier",
    goal="Ensure the generated answer is fully supported by the context",
    backstory="A critical thinker who checks for hallucinations",
    verbose=True
)

# Define tasks and crew
task = Task(description="Answer the user's question using retrieved documents", agent=generator)
crew = Crew(agents=[retriever, generator, verifier], tasks=[task])
