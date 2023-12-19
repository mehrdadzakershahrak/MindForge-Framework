class Task:
    def __init__(self, name, components, instructions, task_type='standard'):
        self.name = name
        self.components = components
        self.instructions = instructions
        self.task_type = task_type

    def execute(self, framework, initial_input):
        if self.task_type == 'self_talk':
            return self_talk_improved(*self.components, initial_input, framework.lm_service)
        elif self.task_type == 'think_out_loud':
            return think_out_loud_improved(initial_input, self.components[0], 3, framework.lm_service)
        else:
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
