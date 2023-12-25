from .modules import ModuleMap


def solve(lines):
    print("")
    module_map = ModuleMap(lines)
    for _ in range(0, 1000):
        module_map.launch_pulse()
    print(f"{module_map.low_pulses=}, {module_map.high_pulses=}")
    return module_map.low_pulses * module_map.high_pulses
