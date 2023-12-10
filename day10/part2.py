from .pipe_field import PipeField


def solve(lines):
    field = PipeField(lines)
    return len(field.inner_area)
