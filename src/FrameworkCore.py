class FrameworkCore:
    def __init__(self):
        self.components = {}

    def add_component(self, component_name, component):
        self.components[component_name] = component

    def run_component(self, component_name, input_data):
        return self.components[component_name].process(input_data)

class ComponentInterface:
    def process(self, input_data):
        raise NotImplementedError("Process method must be implemented.")
