##!FAIL: IndexingError[Iterable[T]]@13:18

def renverse(l : Iterable[T]) -> List[T]:
    """Renverse la liste (l'itérable) L.
    """
    lr : List[T]  # liste résultat
    lr = []

    i : int # position
    i = len(l) - 1

    while i >= 0:
        lr.append(l[i])
        i = i - 1

    return lr

# Jeu de tests
assert renverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
assert renverse([]) == []
assert renverse("toto") == ["o", "t", "o", "t"]
