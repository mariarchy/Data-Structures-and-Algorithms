class Solution:
    neighbors = [
        [4, 6],
        [6, 8],
        [7, 9],
        [4, 8],
        [0, 3, 9],
        [],
        [0, 1, 7],
        [2, 6],
        [1, 3],
        [2, 4],
                ]
    mod = 10**9 + 7

    def knightDialer(self, N: int) -> int:
        num_paths = 0
        if N == 1: return 10
        for i in range(10):
            num_paths = num_paths + self.numPaths(i, N - 1) % self.mod
        return num_paths % self.mod

    def numPaths(self, posn: int, hops: int) -> int:
        combos = 0
        if hops == 0:
            return 1
        for nbr in self.neighbors[posn]:
                combos = combos + self.numPaths(nbr, hops - 1) % self.mod
        return combos % self.mod
