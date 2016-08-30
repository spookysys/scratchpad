from openmdao.api import Group, Problem, Component, IndepVarComp
import Pump from Pump
import Turbine from Turbine
import FeedLine from FeedLine
import HeatExchanger from HeatExchanger
import Injector from Injector
import CombustionChamber from CombustionChamber
import Nozzle from Nozzle


class RocketEngine(Group):

    def __init__(self):
        super().__init__()
        self.add('f_feedline', FeedLine())
        self.add('f_pump', Pump())
        self.add('f_heatex', HeatExchanger())
        self.add('f_turbine', Turbine())
        self.add('f_injector', Injector())
        self.add('o_feedline', FeedLine())
        self.add('o_pump', Pump())
        self.add('o_heatex', HeatExchanger())
        self.add('o_turbine', Turbine())
        self.add('o_injector', Injector())
        self.add('combustion_chamber', CombustionChamber())
        self.add('nozzle', Nozzle())
