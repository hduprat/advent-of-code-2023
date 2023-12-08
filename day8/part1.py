from .network import Network


def solve(lines):
    path = Network(lines).walk_through(lines[0].strip())
    return len(path) - 1
