from typing import Callable, TypeVar


def split_list(l: list[str]) -> list[list[str]]:
    output: list[list[str]] = [[]]

    for elt in l:
        if elt.strip() == "":
            output.append([])
        else:
            output[-1].append(elt.strip())

    return output


T = TypeVar("T")


def partition(cond: Callable[[T], bool], l: list[T]) -> tuple[list[T], list[T]]:
    filtered = list[T]()
    removed = list[T]()

    for elt in l:
        if cond(elt):
            filtered.append(elt)
        else:
            removed.append(elt)
    return (filtered, removed)
