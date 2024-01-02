from FrameworkCore import FrameworkCore
from LanguageModelService import LanguageModelService
from halo import Halo
from utils import create_task, self_talk, think_out_loud
from components.research import research
from components.analysis import analysis
from components.drafting import drafting
from components.split import split


def read_instructions(file_path):
    with open(file_path, 'r') as file:
        return {line.split(None, 1)[0].strip('#').replace(' ', '').lower(): line.split(None, 1)[1].strip()
                for line in file if line.startswith('#')}

def create_standard_task(task_name, components, instructions):
    return create_task(task_name, components, {c: instructions[c] for c in components})

def main():
    framework = FrameworkCore()
    lm_service = LanguageModelService(provider='openai')

    # Add components to the framework
    for component in ['split', 'research', 'analysis', 'drafting']:
        framework.add_component(component, globals()[component])

    # Read and set instructions for all components, including 'drafting'
    instructions = {task: read_instructions(f'instructions/{task}.txt') 
                    for task in ['split', 'research', 'analysis', 'drafting']}
    
    # Create standard tasks for all components, including 'drafting'
    tasks = {task: create_standard_task(f"{task.capitalize()} Task", [task], instructions) 
             for task in instructions}

    user_input = input("What would you like to discuss? ")
    spinner = Halo(text='Thinking...', spinner='dots')
    spinner.start()

    # Execute Split, then Think Out Loud and Self Talk
    split_output = tasks['split'].execute(framework, (user_input, '', '', lm_service, instructions['split']))
    tol_output = think_out_loud(split_output, lambda data: tasks['analysis'].execute(framework, (data, '', '', lm_service, instructions['analysis'])), 2)
    print("TOL Output:", tol_output)

    st_output = self_talk(lambda data, lm: tasks['research'].execute(framework, (data, '', '', lm, instructions['research'])), 
                          lambda data, lm: tasks['drafting'].execute(framework, (data, '', lm, instructions['drafting'])), 
                          tol_output, lm_service)
    print("ST Output:", st_output)
    spinner.stop()

if __name__ == "__main__":
    main()