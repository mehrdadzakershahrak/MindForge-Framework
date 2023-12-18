class Task:
    def __init__(self, name, components, instructions):
        self.name = name
        self.components = components
        self.instructions = instructions

    def execute(self, framework, initial_input):
        result = initial_input
        for i, component_name in enumerate(self.components):
            component_instructions = self.instructions.get(component_name, {})
            result = framework.run_function(component_name, *result, **component_instructions)
        return result
    
    # Dynamic task composition
    def create_task(name, component_sequence, instructions):
        return Task(name, component_sequence, instructions)