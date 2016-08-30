from openmdao.api import Group, Problem, Component, IndepVarComp


class HeatExchanger(Component):

    def __init__(self):
        super().__init__()
        self.add_output('input_pressure')
        self.add_param('combustion_temperature')
        self.add_param('mass_flow')
        self.add_param('output_pressure')
        self.add_output('needed_heat')
