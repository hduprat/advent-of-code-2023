from .spring_record import SpringRecords


def solve(lines):
    spring_records = SpringRecords(lines)

    return sum([record.arrangements for record in spring_records.records])
