from LanguageModelService import LanguageModelService

class FrameworkCore:
    def __init__(self):
        self.components = {}
        self.lm_service = LanguageModelService(provider='openai')

    def add_component(self, component_name, component):
        self.components[component_name] = component

    def run_component(self, component_name, *args, **kwargs):
        component = self.components[component_name]
        if callable(component):
            return component(*args, **kwargs)
        else:
            raise TypeError(f"The component {component_name} is not callable.")

class ComponentInterface:
    def process(self, input_data):
        raise NotImplementedError("Process method must be implemented.")
