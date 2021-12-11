from aoc.util.Day import Day


class Octopuses:
    class Octopus:
        def __init__(self, energy):
            self.energy = int(energy)
        
        def step(self):
            self.energy += 1
        
        def can_flash(self):
            return self.energy > 9
            
        def flash(self):
            self.energy = 0 if self.can_flash() else self.energy
    
    def __init__(self, data):
        self.grid = {}
        self.maxx, self.maxy = len(data[0]), len(data)
        for y, row in enumerate(data):
            for x, energy in enumerate(row):
                self.grid[(x, y)] = self.Octopus(energy)
                
    def __str__(self):
        out = ""
        for y in range(self.maxy):
            out += (" ".join(str(self.grid.get((x,y)).energy) for x in range(self.maxx))) + "\n"
        return out
                
    
    def step(self):
        for pos, octo in self.grid.items():
            octo.step()
        
        to_check = {(x, y): octo for (x, y), octo in self.grid.items() if octo.can_flash()}
        to_flash = []

        cnt = 0
        while len(to_check) > 0:
            for (x, y), octo in to_check.copy().items():
                to_check.pop((x, y))
                to_flash.append((x, y))
                
                neighbours = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)]
                for neighbour in neighbours:
                    if neighbour in self.grid:
                        octo = self.grid.get(neighbour)
                        octo.step()
                        if octo.can_flash() and neighbour not in to_flash:
                            to_check[neighbour] = octo

        cnt = len(to_flash)
        for octo in map(self.grid.get, to_flash):
            octo.flash()
        
        return cnt
                
    
    def cnt_flashes(self, steps):
        return sum(self.step() for _ in range(steps))

    def sim_flash(self):
        step = 1
        while (cnt := self.step()) != (self.maxx * self.maxy):
            step += 1
        return step
 

class Day11(Day):
    def __init__(self, filename):
        super().__init__(filename)
    
    def solve_part1(self):
        return Octopuses(self.data).cnt_flashes(100)

    def solve_part2(self):
        return Octopuses(self.data).sim_flash()


def main():
    day = Day11("day11.in")
    day.run()


if __name__ == "__main__":
    main()
