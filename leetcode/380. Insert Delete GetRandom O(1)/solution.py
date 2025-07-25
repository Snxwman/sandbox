from random import randint

class RandomizedSet:
    def __init__(self):
        self.vals: list[int] = []
        self.dict: dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False

        self.dict[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False

        index = self.dict[val]
        self.vals[index] = self.vals[-1]
        self.dict[self.vals[-1]] = index

        _ = self.dict.pop(val)
        _ = self.vals.pop()

        return True

    def getRandom(self) -> int:
        index = randint(0, len(self.vals) - 1)  # noqa: S311
        return self.vals[index]
