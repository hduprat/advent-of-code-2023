from .mirror import MirrorField


def is_almost_symmetry_axis(y: int, lines: list[str]) -> bool:
    smudge_fixed = False
    for i in range(0, y + 1):
        if y + 1 + i == len(lines):
            return smudge_fixed
        if lines[y - i] != lines[y + 1 + i]:
            if smudge_fixed:
                return False

            line = lines[y - i]
            other_line = lines[y + 1 + i]
            for x, char in enumerate(line):
                if other_line[x] != char:
                    if smudge_fixed:
                        return False
                    smudge_fixed = True

    return smudge_fixed


def solve(lines):
    field = MirrorField(lines, is_almost_symmetry_axis)
    return field.score
