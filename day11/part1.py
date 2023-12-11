from .telescope import TelescopeReport


def solve(lines):
    report = TelescopeReport(lines)
    return sum(report.distances_between_galaxies)
