from FrameworkCore import FrameworkCore
from TaskPipeline import TaskPipeline
from ResourceManager import ResourceManager
from LanguageModelService import LanguageModelService
from utils import self_talk, think_out_loud, create_task
from Task import Task
from components.research import research
from components.analysis import analysis
from components.drafting import drafting
from halo import Halo
from dotenv import load_dotenv

from flask import Flask
app = Flask(__name__)

def read_instructions(file_path):
    instructions = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('#'):
                key, value = line.split(None, 1)
                formatted_key = key.strip('#').replace(' ', '').lower()
                if formatted_key:  # Ensure the key is not empty
                    instructions[formatted_key] = value.strip()
    return instructions


def decison_making(user_input):
    framework = FrameworkCore()
    lm_service = LanguageModelService(provider='openai')

    # Add components to the framework
    framework.add_component('research', research)
    framework.add_component('analysis', analysis)
    framework.add_component('drafting', drafting)

    # Read instructions
    research_instructions = read_instructions('src/instructions/analysis.txt')
    analysis_instructions = read_instructions('src/instructions/analysis.txt')
    drafting_instructions = read_instructions('src/instructions/analysis.txt')

    # Create standard tasks
    research_task = create_task("Research Task", ['research'], {'research': research_instructions})
    analysis_task = create_task("Analysis Task", ['analysis'], {'analysis': analysis_instructions})
    drafting_task = create_task("Drafting Task", ['drafting'], {'drafting': drafting_instructions})

    # user_input = input("What would you like to discuss? ")
    # data = request.json
    # spinner = Halo(text='Thinking...', spinner='dots')
    # spinner.start()

    # Execute TOL and ST
    tol_output = think_out_loud(user_input, lambda data: analysis_task.execute(framework, (data, '', '', lm_service, analysis_instructions)), 2)
    # print("TOL Output:", tol_output)

    st_output = self_talk(lambda data, lm: research_task.execute(framework, (data, '', '', lm, research_instructions)), 
                          lambda data, lm: drafting_task.execute(framework, (data, '', lm, drafting_instructions)), 
                          tol_output, lm_service)
    # print("ST Output:", st_output)
    return st_output
    # spinner.stop()
    
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/final_decision', methods=['POST'])
def get_decision():
    # Extract data from the request
    user_input = request.json.get('user_input')

    st_output = decison_making(user_input)

    # Return the result in JSON format
    return jsonify({"ST Output": st_output})



if __name__ == '__main__':
    app.run(debug=True)