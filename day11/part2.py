from .telescope import TelescopeReport


def solve(lines):
    report = TelescopeReport(lines, spacing=1000000)
    return sum(report.distances_between_galaxies)
