from .spring_record import SpringRecords


def expand(line: str) -> str:
    [string, numbers] = line.split(" ")
    new_string = "?".join([string] * 5)
    new_numbers = ",".join([numbers] * 5)

    return " ".join([new_string, new_numbers])


def solve(lines):
    spring_records = SpringRecords([expand(line) for line in lines])

    total = 0
    for n, record in enumerate(spring_records.records, start=1):
        print(
            f"Computing arrangements for record #{n} ({record.string}, {record.damaged_ranges})..."
        )
        total += record.arrangements
    return total
