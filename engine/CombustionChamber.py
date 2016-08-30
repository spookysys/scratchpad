from openmdao.api import Group, Problem, Component, IndepVarComp


class CombustionChamber(Component):

    def __init__(self):
        super().__init__()
        self.add_output('oxidizer_mass_flow')
        self.add_output('fuel_mass_flow')
        self.add_param('combustion_pressure')
        self.add_param('fuel_mixture', val=.5)
        self.add_param('stolen_heat_fuel')
        self.add_param('stolen_heat_oxidizer')
        self.add_param('exhaust_mass_flow')
        self.add_output('combustion_temperature')
