from openmdao.api import Group, Problem, Component, IndepVarComp


class FeedLine(Component):

    def __init__(self):
        super().__init__()
        self.add_param('mass_flow')
        self.add_param('pressure')
