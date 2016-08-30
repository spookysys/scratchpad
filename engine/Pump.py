from openmdao.api import Group, Problem, Component, IndepVarComp


class Pump(Component):

    def __init__(self):
        super().__init__()
        self.add_param('mass_flow')
        self.add_param('input_pressure')
        self.add_param('output_pressure')
        self.add_output('rpm')
