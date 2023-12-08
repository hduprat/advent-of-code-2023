from .network import Network
from math import lcm


def is_starting(node: str) -> bool:
    return node.endswith("A")


def is_ending(node: str) -> bool:
    return node.endswith("Z")


def solve(lines):
    network = Network(lines)
    nodes = network.nodes
    positions = list(filter(is_starting, nodes))
    cycle_lengths = [
        len(network.walk_through(lines[0].strip(), position, is_ending)) - 1
        for position in positions
    ]

    # It's a pure coincidence! There is indeed a cycle from a Z to another Z, and no node leads to an A.
    return lcm(*cycle_lengths)
