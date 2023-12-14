def split_list(l: list[str], start: list[str] = [list()]) -> list[list[str]]:
    output: list[list[str]] = [[]]

    for elt in l:
        if elt.strip() == "":
            output.append([])
        else:
            output[-1].append(elt.strip())

    return output
