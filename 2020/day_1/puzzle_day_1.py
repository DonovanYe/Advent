class Day1:

    filename = 'input_1.txt'

    def __init__(self):
        self.num_list = []
        with open(self.filename, 'r') as infile:
            nums = infile.readlines()

        for num in nums:
            self.num_list.append(int(num))

    def puzzle_1(self):
        a, b = Day1.find_addends(self.num_list, 2020)
        return a * b

    def puzzle_2(self):
        for i in range(len(self.num_list) - 1):
            a, b = Day1.find_addends(self.num_list[i+1:], 2020 - self.num_list[i])
            if a is not None and b is not None:
                return a * b * self.num_list[i]

    @staticmethod
    def find_addends(num_list, target):
        complement = set()
        for num in num_list:
            if num in complement:
                return num, target - num
            else:
                complement.add(target - num)
        return None, None

if __name__ == '__main__':
    puzzle = Day1()
    print(puzzle.puzzle_1())
    print(puzzle.puzzle_2())