def intersect(a: range, b: range) -> range | None:
    result = range(max(a.start, b.start), min(a.stop, b.stop))
    return result if result.stop >= result.start else None


def cut(a: range, b: range):
    intersection = intersect(a, b)
    if intersection is None:
        return (None, [a])
    before = (
        range(a.start, intersection.start) if a.start < intersection.start else None
    )
    after = range(intersection.stop, a.stop) if intersection.stop < a.stop else None
    out = list()
    if before is not None:
        out.append(before)
    if after is not None:
        out.append(after)
    return (intersection, out if len(out) > 0 else None)
