from collections.abc import MutableMapping
from typing import Dict, MutableMapping, Generator
votes = {
    'otter': 1281,
    'polar bear': 587,
    'fox': 863
}


class SortedDict(MutableMapping[str, int]):
    def __init__(self) -> None:
        self.data: Dict[str, int] = {}

    def __getitem__(self, key: str) -> int:
        return self.data[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.data[key] = value

    def __delitem__(self, key: str) -> None:
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self) -> int:
        return len(self.data)


def populate_ranks(votes: Dict[str, int], ranks: Dict[str, int]) -> None:
    names = list(votes.keys())
    names.sort(key=lambda x: votes[x], reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


def get_winner(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))


sorted_ranks: Dict[str, int] = dict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks)
winner = get_winner(sorted_ranks)
print(winner)