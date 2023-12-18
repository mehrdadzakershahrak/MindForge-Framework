class Task:
    def __init__(self, name, components, instructions):
        self.name = name
        self.components = components
        self.instructions = instructions

    def execute(self, framework, initial_input):
        result = initial_input
        for component_name in self.components:
            component = framework.components[component_name]
            component_instructions = self.instructions.get(component_name, {})

            if component_name == 'research':
                if isinstance(result, tuple):
                    result = component(*result[:4], component_instructions)  
                else:
                    result = component(result, "", "", lm_service, component_instructions)
        
        return result
