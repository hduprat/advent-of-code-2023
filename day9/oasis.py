class OASIS:
    def __init__(self, lines: list[str]) -> None:
        self.sequences = [[int(n) for n in line.strip().split(" ")] for line in lines]

    @classmethod
    def extrapolate(cls, sequence: list[int]) -> list[int]:
        if sequence.count(0) == len(sequence):
            return sequence + [0]
        diff_sequence = [
            sequence[i + 1] - sequence[i] for i in range(0, len(sequence) - 1)
        ]
        return sequence + [sequence[-1] + cls.extrapolate(diff_sequence)[-1]]

    @classmethod
    def extrapolate_backwards(cls, sequence: list[int]) -> list[int]:
        if sequence.count(0) == len(sequence):
            return [0] + sequence
        diff_sequence = [
            sequence[i + 1] - sequence[i] for i in range(0, len(sequence) - 1)
        ]
        return [sequence[0] - cls.extrapolate_backwards(diff_sequence)[0]] + sequence

    @property
    def extrapolations(self) -> list[list[int]]:
        return [self.extrapolate(sequence) for sequence in self.sequences]

    @property
    def backwards_extrapolations(self) -> list[list[int]]:
        return [self.extrapolate_backwards(sequence) for sequence in self.sequences]
