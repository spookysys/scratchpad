from openmdao.api import Group, Problem, Component, IndepVarComp


class Turbine(Component):

    def __init__(self):
        super().__init__()
        self.add_output('input_pressure')
        self.add_param('mass_flow')
        self.add_param('rpm')
        self.add_param('output_pressure')
