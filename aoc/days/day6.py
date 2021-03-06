from aoc.util.Day import Day


class LanternFishGrow:
    def __init__(self, data):
        self.days = None
        self.data = data
        self._set_initial_data()

    def _set_initial_data(self):
        self.days = 1
        self.population = [0 for i in range(0, 9)]
        for fish in map(int, self.data[0].split(",")):
            self.population[fish] += 1

    def __str__(self):
        return '\t'.join(map(lambda f: str(f[0]) + ": " + str(f[1]), self.population))

    def _age(self):
        init_day0 = self.population[0]
        for day in range(0, 9):
            if day == 0:
                self.population[day] = 0
            else:  # (day > 0)
                self.population[day - 1] += self.population[day]
                self.population[day] = 0
        self.population[8] += init_day0  # new population
        self.population[6] += init_day0

    def age(self, days):
        if self.days < days:
            self._set_initial_data()

        while self.days <= days:
            self._age()
            self.days += 1

    def size(self):
        return sum(self.population)


class Day6(Day):
    def __init__(self, filename):
        super().__init__(filename)
        self.grow = LanternFishGrow(self.data)
        
    def solve_part1(self):
        self.grow.age(80)
        return self.grow.size()

    def solve_part2(self):
        self.grow.age(256)
        return self.grow.size()


def main():
    day = Day6("day6.in")
    day.run()


if __name__ == "__main__":
    main()
