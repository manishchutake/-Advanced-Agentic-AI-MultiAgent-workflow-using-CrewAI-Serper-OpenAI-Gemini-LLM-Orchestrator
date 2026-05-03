import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

os.environ['SERPER_API_KEY'] = 'ENTER_SERPER_API_KEY'
os.environ['OPENAI_API_KEY'] = 'ENTER_OPENAI_API_KEY'

search_tool = SerperDevTool()

teacher = Agent(
    role='Teacher',
    goal='Explain concept clearly step by step',
    backstory='Experienced teacher who explains with examples',
    llm='gpt-4o-mini',
    verbose=True
)

researcher = Agent(
    role='Researcher',
    goal='Find latest information',
    backstory='Searches real-world data',
    tools=[search_tool],
    llm='gpt-4o-mini',
    verbose=True
)

simplifier = Agent(
    role='Simplifier',
    goal='Make things easy',
    backstory='Breaks complex ideas into simple language',
    llm='gpt-4o-mini',
    verbose=True
)

student = Agent(
    role='Student',
    goal='Take notes',
    backstory='Writes simple notes',
    llm='gpt-4o-mini',
    verbose=True
)

examiner = Agent(
    role='Examiner',
    goal='Create questions',
    backstory='Tests understanding',
    llm='gpt-4o-mini',
    verbose=True
)

topic = 'What is agentic AI vs generative AI'

task1 = Task(
    description=f'Search and find key points about {topic}',
    expected_output='Key points',
    agent=researcher
)

task2 = Task(
    description=f'Explain {topic} in simple steps',
    expected_output='Step by step explanation',
    agent=teacher
)

task3 = Task(
    description=f'Simplify the explanation of {topic}',
    expected_output='Simple explanation',
    agent=simplifier
)

task4 = Task(
    description=f'Write short notes on {topic}',
    expected_output='Short notes',
    agent=student
)

task5 = Task(
    description=f'Create 3 easy questions about {topic}',
    expected_output='Questions',
    agent=examiner
)

crew = Crew(
    agents=[teacher, researcher, simplifier, student, examiner],
    tasks=[task1, task2, task3, task4, task5],
    verbose=True
)

result = crew.kickoff()
print(result)






