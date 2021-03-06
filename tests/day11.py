import unittest

from aoc.days.day11 import Day11


class Day11Test(unittest.TestCase):
    example_day = Day11("../input/test/day11.in")
    real_day = Day11("../input/day11.in")

    def test_example_1(self):
        example_answer1 = 1656
        self.assertEqual(self.example_day.solve_part1(), example_answer1, f"The example test for part 1 should return {example_answer1}")

    def test_example_2(self):
        example_answer2 = 195
        self.assertEqual(self.example_day.solve_part2(), example_answer2, f"The example test for part 2 should return {example_answer2}")

    def test_part1(self):
        answer1 = 1749
        self.assertEqual(self.real_day.solve_part1(), answer1, f"The test for part 1 should return {answer1}")

    def test_part2(self):
        answer2 = 285
        self.assertEqual(self.real_day.solve_part2(), answer2, f"The test for part 2 should return {answer2}")


if __name__ == '__main__':
    unittest.main()
