from .modules import ModuleMap
from math import lcm


def solve(lines):
    module_map = ModuleMap(lines)
    i = 0
    while module_map.on is False:
        module_map.launch_pulse()
        if len(module_map.inputs_on_high) > 0 and len(module_map.watched_modules) == 0:
            return lcm(*module_map.inputs_on_high.values())
