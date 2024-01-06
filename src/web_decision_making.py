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

def create_standard_task(task_name, component, instructions):
    return create_task(task_name, [component], {component: instructions})

def execute_component(component_name, user_query, framework, instructions, lm_service):
    component_func = framework.components[component_name]
    component_instructions = instructions.get(component_name, {})

    # Adjust the order of arguments to match the component functions' expectations
    result = component_func(user_query, lm_service, component_instructions, "", "")
    print(f"Output from {component_name}: {result}")  
    return result

def main(user_query):
    framework = FrameworkCore()
    lm_service = LanguageModelService(provider='openai')

    # Read instruction files for each component
    instructions = {
        'research': read_instructions('instructions/research.txt'),
        'analysis': read_instructions('instructions/analysis.txt'),
        'drafting': read_instructions('instructions/drafting.txt'),
        'split': read_instructions('instructions/split.txt')
    }

    # Add component functions to the framework
    framework.add_component('research', research)
    framework.add_component('analysis', analysis)
    framework.add_component('drafting', drafting)
    framework.add_component('split', split)

    intermediate_outputs = []

    # Process input through split component
    split_context = execute_component('split', user_query, framework, instructions, lm_service)
    intermediate_outputs.append(("split", split_context))


    # Use self_talk to refine the response from the split component with the research component
    split_context = self_talk(lambda data, lm: execute_component('split', data, framework, instructions, lm),
                              lambda data, lm: execute_component('research', data, framework, instructions, lm),
                              split_context, lm_service)
    
    # Process split output through analysis component
    analysis_context = execute_component('analysis', split_context, framework, instructions, lm_service)
    
    # Use think_out_loud to further refine the response from the analysis component
    analysis_context = think_out_loud(analysis_context, lambda data: execute_component('analysis', data, framework, instructions, lm_service), 2)
    
    # Final drafting step
    drafting_output = execute_component('drafting', analysis_context, framework, instructions, lm_service)
    final_output = execute_component('drafting', drafting_output, framework, instructions, lm_service)
    intermediate_outputs.append(("drafting", final_output))

    return intermediate_outputs