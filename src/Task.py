class Task:
    def __init__(self, name, components, instructions, task_type='standard'):
        self.name = name
        self.components = components
        self.instructions = instructions
        self.task_type = task_type

    def execute(self, framework, initial_input, lm_service=None):
        result, notes, queries, _ = initial_input  # Ignore the fourth element as it's a placeholder
        for component_name in self.components:
            component_func = framework.components[component_name]
            component_instructions = self.instructions.get(component_name, {})

            # Call the component function with appropriate arguments
            result = component_func(result, notes, queries, lm_service, component_instructions)

        return result