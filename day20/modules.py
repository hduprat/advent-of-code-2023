from __future__ import annotations
from re import compile as create_regex

CONNECTION_REGEX = create_regex("(broadcaster|&[a-z]+|%[a-z]+) -> (.+)")


class Module:
    def __init__(self, name: str) -> None:
        self.name = name
        self.conjunction_modules: list[ConjunctionModule] = []

    def compute_new_pulse(self, pulse: bool) -> bool | None:
        # OVERRIDE THIS
        return None

    def connect_to(self, module: ConjunctionModule):
        self.conjunction_modules.append(module)
        module.add_input_module(self.name)

    def receive_pulse(self, pulse: bool):
        new_pulse = self.compute_new_pulse(pulse)
        for module in self.conjunction_modules:
            if new_pulse is not None:
                module.update_input(self.name, new_pulse)
        return new_pulse


class FlipFlopModule(Module):
    def __init__(self, name: str) -> None:
        self.is_on = False
        super().__init__(name)

    def compute_new_pulse(self, pulse: bool) -> bool | None:
        if pulse:
            return None
        self.is_on = not self.is_on
        return self.is_on


class ConjunctionModule(Module):
    def __init__(self, name: str) -> None:
        self.inputs = dict[str, bool]()
        super().__init__(name)

    def add_input_module(self, module_name: str):
        self.inputs[module_name] = False

    def compute_new_pulse(self, _) -> bool:
        input_values = set(self.inputs.values())
        return False if input_values == {True} else True

    def update_input(self, name: str, pulse: bool):
        self.inputs[name] = pulse


class BroadcasterModule(Module):
    def __init__(self) -> None:
        super().__init__("broadcaster")

    def compute_new_pulse(self, pulse: bool) -> bool | None:
        return pulse


class ModuleMap:
    low_pulses = 0
    high_pulses = 0
    on = False
    watched_modules: dict[str, bool]
    launched_pulses: int
    inputs_on_high: dict[str,int]

    def __init__(self, lines) -> None:
        self.modules = dict[str, Module]()
        self.connections = dict[str, list[str]]()
        self.watched_modules = dict()
        self.inputs_on_high = dict()
        self.launched_pulses = 0

        for line in lines:
            result = CONNECTION_REGEX.match(line)
            if result is None:
                raise Exception(f"Unknown module description: {line}")
            match result.group(1):
                case "broadcaster":
                    id = "broadcaster"
                    self.modules[id] = BroadcasterModule()
                case a if a.startswith("&"):
                    id = a[1:]
                    self.modules[id] = ConjunctionModule(id)
                case a if a.startswith("%"):
                    id = a[1:]
                    self.modules[id] = FlipFlopModule(id)
            self.connections[id] = result.group(2).split(", ")

        for name in self.modules:
            input = self.modules[name]
            for output in self.connections[name]:
                if output in self.modules and isinstance(
                    self.modules[output], ConjunctionModule
                ):
                    input.connect_to(self.modules[output])
        self.watch_rx_parents()

    def find_parents(self, id: str) -> list[str]:
        result = []
        for name, connection in self.connections.items():
            if id in connection:
                result.append(name)
        return result

    def launch_pulse(self):
        self.launched_pulses += 1
        queue: list[dict] = [{"module": "broadcaster", "pulse": False}]
        while len(queue) > 0:
            next_item = queue.pop(0)

            next_pulse = next_item["pulse"]
            if next_pulse is True:
                self.high_pulses += 1
            else:
                self.low_pulses += 1

            next_module = next_item["module"]

            if next_module == "rx" and next_pulse is False:
                self.on = True
            if next_module not in self.connections:
                continue
            pulse = self.modules[next_module].receive_pulse(next_pulse)

            modules_to_unwatch = []
            for module in self.watched_modules:
                if next_module == module and pulse == self.watched_modules[module]:
                    print(f"Module {module} has sent a {"high" if pulse is True else "low"} pulse after {self.launched_pulses} button pushes")
                    self.inputs_on_high[module] = self.launched_pulses
                    modules_to_unwatch.append(module)
            for m in modules_to_unwatch:
                self.unwatch_module(m)

            if pulse is not None:
                if next_module not in self.connections:
                    continue
                queue.extend(
                    [
                        {"module": output, "pulse": pulse}
                        for output in self.connections[next_module]
                    ]
                )

    def watch_rx_parents(self):
        rx_parents = self.find_parents("rx")
        for parent in rx_parents:
            if isinstance(self.modules[parent], ConjunctionModule):
                inputs = list(self.modules[parent].inputs.keys())
                for input in inputs:
                    self.watch_module(input, True)

    def watch_module(self, id, value):
        self.watched_modules[id] = value
    
    def unwatch_module(self, id):
        self.watched_modules.pop(id)
