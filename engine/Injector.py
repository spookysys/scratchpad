from openmdao.api import Group, Problem, Component, IndepVarComp


class Injector(Component):

    def __init__(self):
        super().__init__()
        self.add_output('input_pressure')
        self.add_param('mass_flow')
        self.add_param('combustion_pressure')
