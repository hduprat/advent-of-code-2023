import re
from math import prod

WORKFLOW_REGEX = re.compile(r"(.+)\{(.+)\}")
RULE_REGEX = re.compile(r"([xmas])([<>])(\d+):(.+)")
PART_REGEX = re.compile(r"([xmas])=(\d+)")

type Repartition = dict[str, tuple[int, int]]


class RatingRule:
    def __init__(self, line: str) -> None:
        result = RULE_REGEX.match(line)
        self.var = result.group(1)
        self.type = "lt" if result.group(2) == "<" else "gt"
        self.val = int(result.group(3))
        self.output = result.group(4)

    def is_condition_ok(self, part) -> bool:
        if self.type == "lt":
            return part[self.var] < self.val
        return part[self.var] > self.val

    def check(self, part) -> str | None:
        return self.output if self.is_condition_ok(part) else None

    def repartition(self, origin: Repartition) -> tuple[Repartition]:
        ok = origin.copy()
        not_ok = origin.copy()

        min, max = origin[self.var]

        if self.type == "lt":
            ok[self.var] = (min, self.val - 1)
            not_ok[self.var] = (self.val, max)
        else:
            not_ok[self.var] = (min, self.val)
            ok[self.var] = (self.val + 1, max)

        return (ok, not_ok)


class RatingWorkflow:
    def __init__(self, line) -> None:
        result = WORKFLOW_REGEX.match(line)
        self.id = result.group(1)

        rules = result.group(2).split(",")
        self.rules = [RatingRule(rule) for rule in rules[:-1]]
        self.default = rules[-1]

    def check(self, part):
        for rule in self.rules:
            output = rule.check(part)
            if output is not None:
                return output
        return self.default

    @property
    def next_workflows(self):
        return set([rule.output for rule in self.rules] + [self.default])

    def repartition(self, origin: Repartition):
        result = dict[str, list[Repartition]]()
        current_repart = origin
        for rule in self.rules:
            (ok, not_ok) = rule.repartition(current_repart)
            if rule.output in result:
                result[rule.output].append(ok)
            else:
                result[rule.output] = [ok]
            current_repart = not_ok
        if self.default in result:
            result[self.default].append(not_ok)
        else:
            result[self.default] = [not_ok]
        return result


class RatingSystem:
    def __init__(self, lines) -> None:
        self.workflows = dict[str, RatingWorkflow]()

        for line in lines:
            workflow = RatingWorkflow(line)
            self.workflows[workflow.id] = workflow

    def check(self, part, workflow_id="in"):
        output = self.workflows[workflow_id].check(part)
        if output in self.workflows:
            return self.check(part, output)
        return output

    def accepted_workflows(self, workflow_id="in"):
        if workflow_id == "A":
            return ["A"]
        if workflow_id == "R":
            return []
        results = []
        for w in self.workflows[workflow_id].next_workflows:
            for v in self.accepted_workflows(w):
                result = [workflow_id]
                result.extend(v)
                results.append(result)
        return results

    def count_accepted_repartitions(self):
        accepted_workflows = self.accepted_workflows()
        total = 0
        for path in accepted_workflows:
            repartitions: list[Repartition] = [
                {
                    "x": (1, 4000),
                    "m": (1, 4000),
                    "a": (1, 4000),
                    "s": (1, 4000),
                }
            ]

            for i, workflow in enumerate(path[:-1]):
                new_repartitions = [
                    self.workflows[workflow].repartition(rep) for rep in repartitions
                ]
                res = []
                for rep in new_repartitions:
                    res.extend(rep[path[i + 1]])
                repartitions = res

            for rep in repartitions:
                intervals = rep.values()
                counts = [b - a + 1 for a, b in intervals]
                total += prod(counts)

        return total
