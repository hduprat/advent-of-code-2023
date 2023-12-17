import re
from dataclasses import dataclass
from .hash import hash


class Instruction:
    def __init__(self, string: str) -> None:
        result = re.fullmatch(r"(.+)(-|=\d)", string)
        if result is None:
            raise Exception("Wrong instruction")
        self.label = result.group(1)

        self.type = result.group(2)[0]
        self.length = int(result.group(2)[1]) if len(result.group(2)) > 1 else 0
        self.box = hash(self.label)

    def __str__(self) -> str:
        if self.type == "-":
            return f"[Instruction] Remove lens {self.label} from box {self.box}"
        return f"[Instruction] Add lens {self.label} in box {self.box} with focal length {self.length}"


@dataclass
class Lens:
    label: str
    length: int

    def replace(self, length: int):
        self.length = length

    def __str__(self) -> str:
        return f"[{self.label} {self.length}]"


class LensBoxes:
    def __init__(self) -> None:
        self.boxes = dict[int, list[Lens]]()

    def execute_instruction(self, instruction: Instruction) -> None:
        box = instruction.box
        if instruction.type == "-":
            if box not in self.boxes:
                return
            self.boxes[box] = list(
                filter(lambda l: l.label != instruction.label, self.boxes[box])
            )
            return

        if box not in self.boxes:
            self.boxes[box] = []

        for lens in self.boxes[box]:
            if lens.label == instruction.label:
                lens.replace(length=instruction.length)
                return

        self.boxes[box].append(Lens(instruction.label, instruction.length))

    @property
    def focusing_power(self) -> int:
        return sum(
            [
                sum(
                    [
                        (index + 1) * n * lens.length
                        for n, lens in enumerate(box, start=1)
                    ]
                )
                for index, box in self.boxes.items()
            ]
        )

    def __str__(self) -> str:
        output = []
        for index, box in self.boxes.items():
            output.append(f"Box {index}: {" ".join([str(lens) for lens in box])}")
        return "\n".join(output)


def solve(lines):
    boxes = LensBoxes()
    instructions = lines[0].strip().split(",")
    for i in instructions:
        # print(Instruction(i))
        boxes.execute_instruction(Instruction(i))
        # print(boxes)

    return boxes.focusing_power
