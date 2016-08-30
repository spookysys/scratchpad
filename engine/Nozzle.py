from openmdao.api import Group, Problem, Component, IndepVarComp


class Nozzle(Component):

    def __init__(self):
        super().__init__()
        self.add_output('mass_flow')
        self.add_output('inlet_radius')
        self.add_param('combustion_pressure')
        self.add_param('atmospheric_pressure')
        self.add_param('target_thrust')
        self.add_output('outlet_radius')
