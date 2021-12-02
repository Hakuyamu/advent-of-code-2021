def read_puzzle(path):
    with open(path, 'r+') as file:
        return file.read().split('\n')


class Submarine:
    horizontal = 0
    depth = 0
    aim = 0

    def forward(self, x):
        self.horizontal = self.horizontal + x
        self.depth = self.depth + self.aim * x

    def down(self, y):
        self.aim = self.aim + y

    def up(self, y):
        self.aim = self.aim - y

    def get_multiplied(self):
        return self.horizontal * self.depth


if __name__ == "__main__":
    submarine = Submarine()
    content = read_puzzle("puzzle_input.txt")
    for line in content:
        commands = line.split(" ")
        if commands[0] == "forward":
            submarine.forward(int(commands[1]))
        elif commands[0] == "down":
            submarine.down(int(commands[1]))
        elif commands[0] == "up":
            submarine.up(int(commands[1]))
    print("Final location of the submarine: Horizontal: " + str(submarine.horizontal) + ", Depth: " + str(submarine.depth) +
          ", Multiplied: " + str(submarine.get_multiplied()))
