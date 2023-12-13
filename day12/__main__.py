from . import part1, part2

file = open(r"day12/input.txt", "r")
lines = file.readlines()
print("Part 1 :", part1.solve(lines))
print("Part 2 :", part2.solve(lines))
