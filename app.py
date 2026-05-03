import gradio as gr
import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

os.environ['OPENAI_API_KEY'] = "YOUR_API_KEY"
os.environ['SERPER_API_KEY'] = "YOUR_API_KEY"

search_tool = SerperDevTool()

def run_multi_agent(topic):

    teacher = Agent(
        role='Teacher',
        goal='Explain clearly',
        backstory='Explains with examples',
        llm='gpt-4o-mini',
        verbose=True
    )

    researcher = Agent(
        role='Researcher',
        goal='Find info',
        backstory='Search expert',
        tools=[search_tool],
        llm='gpt-4o-mini',
        verbose=True
    )

    simplifier = Agent(
        role='Simplifier',
        goal='Make easy',
        backstory='Simplifies things',
        llm='gpt-4o-mini',
        verbose=True
    )

    student = Agent(
        role='Student',
        goal='Take notes',
        backstory='Writes notes',
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

    task1 = Task(
        description=f'Find key points about {topic}',
        expected_output='Key points',
        agent=researcher
    )

    task2 = Task(
        description=f'Explain {topic}',
        expected_output='Explanation',
        agent=teacher
    )

    task3 = Task(
        description=f'Simplify {topic}',
        expected_output='Simple explanation',
        agent=simplifier
    )

    task4 = Task(
        description=f'Write notes on {topic}',
        expected_output='Notes',
        agent=student
    )

    task5 = Task(
        description=f'Create questions on {topic}',
        expected_output='Questions',
        agent=examiner
    )

    crew = Crew(
        agents=[teacher, researcher, simplifier, student, examiner],
        tasks=[task1, task2, task3, task4, task5],
        verbose=False
    )

    result = crew.kickoff()
    return str(result)


interface = gr.Interface(
    fn=run_multi_agent,
    inputs=gr.Textbox(label="Enter Topic"),
    outputs=gr.Textbox(label="Output"),
    title="Multi-Agent AI"
)

if __name__ == "__main__":
    interface.launch()
