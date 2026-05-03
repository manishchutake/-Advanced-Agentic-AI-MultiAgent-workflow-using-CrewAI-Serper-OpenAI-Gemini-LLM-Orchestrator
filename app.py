## Notebook Version
You can also explore the project in Jupyter Notebook (Code.ipynb)

!nvidia-smi

!pip install crewai

!pip install 'crewai[tools]'

from logging import RootLogger
import os
from crewai import Agent,Task, Crew
from crewai_tools import SerperDevTool
os.environ['SERPER_API_KEY'] = 'ENTER SERPER API KEY'
os.environ['OPENAI_API_KEY'] = 'ENTER OPENAI API KEY'

search_tool = SerperDevTool()

teacher = Agent(role ='Teacher',
                goal = 'Explain concept clearly step by step',
                backstory = 'looking for experience teacher who explain eith example',
                llm = 'gpt-4o-mini',
                verbose = True)
researcher = Agent(role ='Researcher',
                 goal = 'To find latest information',
                 backstory = 'Explain in searching real_world data',
                 tools = [search_tool],
                 llm = 'gpt-4o-mini',
                 verbose = True)

simplifier = Agent(role = 'Simplifier',
                   goal = 'Make thing easy',
                   backstory = 'Break complex ideas into somple language',
                   llm  ='gpt-4o-mini',
                   verbose = 'True')


student = Agent(role = 'Student',
                goal = 'Take notes',
                backstory = 'Writes the simple notes like learner',
                llm = 'gpt-4o-mini',
                verbose = True)



examiner = Agent(role = 'Examiner',
                 goal ='Create a questions',
                 backstory = 'Tests Understanding',
                 llm = 'gpt-4o-mini',
                 verbose = True)



topic = 'What is agents vs agentic ai vs mcp vs generative ai'

task1 = Task(
    description = f'Search and find three important points about {topic}',
    expected_output= 'Three clear points',
    agent = researcher
    )

task2 = Task(
    description = f'Explain{topic} in simple steps with examples',
    expected_output='step by step explanation',
    agent =  teacher
)

task3 = Task(
    description = f'Simplify the explanation of {topic}',
    expected_output = 'very simple explanation',
    agent = simplifier
)

task4 = Task(
    description = f'Write short notes on {topic} like a student',
    expected_output= 'Short notes',
    agent = student
)

task5 = Task(
    description = f'Create three easy questions about {topic}',
    expected_output = 'Three easy questions',
    agent = examiner
)

crew = Crew(
    agents = [teacher,researcher,simplifier,student,examiner],
    tasks = [task1,task2,task3,task4,task5],
    verbose = True,
)

results = crew.kickoff()
print(results)

!pip install gradio

from logging import RootLogger
import gradio as gr
import os
from crewai import Agent,Task, Crew
from crewai_tools import SerperDevTool
os.environ['SERPER_API_KEY'] = 'ENTER SERPER API KEY'
os.environ['OPENAI_API_KEY'] = 'ENTER OPENAI API KEY'
search_tool = SerperDevTool()

def run_multi_agent(topic):


  teacher = Agent(role ='Teacher',
                goal = 'Explain concept clearly step by step',
                backstory = 'looking for experience teacher who explain eith example',
                llm = 'gpt-4o-mini',
                verbose = True)
  researcher = Agent(role ='Researcher',
                 goal = 'To find latest information',
                 backstory = 'Explain in searching real_world data',
                 tools = [search_tool],
                 llm = 'gpt-4o-mini',
                 verbose = True)

  simplifier = Agent(role = 'Simplifier',
                   goal = 'Make thing easy',
                   backstory = 'Break complex ideas into somple language',
                   llm  ='gpt-4o-mini',
                   verbose = 'True')


  student = Agent(role = 'Student',
                goal = 'Take notes',
                backstory = 'Writes the simple notes like learner',
                llm = 'gpt-4o-mini',
                verbose = True)



  examiner = Agent(role = 'Examiner',
                 goal ='Create a questions',
                 backstory = 'Tests Understanding',
                 llm = 'gpt-4o-mini',
                 verbose = True)



#topic = 'What is agents vs agentic ai vs mcp vs generative ai'

  task1 = Task(
    description = f'Search and find three important points about {topic}',
    expected_output= 'Three clear points',
    agent = researcher
    )

  task2 = Task(
    description = f'Explain{topic} in simple steps with examples',
    expected_output='step by step explanation',
    agent =  teacher
)

  task3 = Task(
    description = f'Simplify the explanation of {topic}',
    expected_output = 'very simple explanation',
    agent = simplifier
)

  task4 = Task(
    description = f'Write short notes on {topic} like a student',
    expected_output= 'Short notes',
    agent = student
)

  task5 = Task(
    description = f'Create three easy questions about {topic}',
    expected_output = 'Three easy questions',
    agent = examiner
)

  crew = Crew(
    agents = [teacher,researcher,simplifier,student,examiner],
    tasks = [task1,task2,task3,task4,task5],
    verbose = False,
)

  results = crew.kickoff()
  return str(results)


interface = gr.Interface(
    fn=run_multi_agent,
    inputs=gr.Textbox(
        label='Enter Topic',
        placeholder='What is Agentic AI vs Single Agent'
    ),
    outputs=gr.Textbox(label='Multi-Agent Output'),
    title='Manish Chutake Multiagent Training',
    description='Enter any topic and see multiple AI agents collaborate'
)

if __name__ == '__main__':
    interface.launch()









