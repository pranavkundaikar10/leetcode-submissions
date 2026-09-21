class CountSquares:

    def __init__(self):
        self.counts = defaultdict(int)
        self.x_to_ys = defaultdict(set)
        

    def add(self, point: List[int]) -> None:
        x, y = point
        self.counts[(x, y)] += 1
        self.x_to_ys[x].add(y)


    def count(self, point: List[int]) -> int:
        px, py = point
        total = 0
        for y in self.x_to_ys[px]:
            side = abs(y - py)
            if side == 0:
                continue
            for x in (px+side, px-side):
                total += (
                    self.counts[(x, py)] *
                    self.counts[(px, y)] *
                    self.counts[(x, y)]
                )
        return total
        
