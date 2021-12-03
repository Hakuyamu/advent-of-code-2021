def read_puzzle(path):
    with open(path, 'r+') as file:
        return file.read().split('\n')


def binary_to_decimal(bit_array):
    decimal = 0
    array = bit_array[::-1]
    for pos, bit in enumerate(array):
        factor = 2 ** pos
        decimal = decimal + bit * factor
    return decimal


def create_empty_bit_array(length):
    arr = []
    for i in range(length):
        arr.append(0)
    return arr


class Submarine:
    zeros = create_empty_bit_array(12)
    ones = create_empty_bit_array(12)

    def read_binary(self, binary):
        for pos, bit in enumerate(binary):
            if int(bit) == 0:
                self.zeros[pos] = self.zeros[pos] + 1
            if int(bit) == 1:
                self.ones[pos] = self.ones[pos] + 1

    def get_gamma(self):
        gamma = create_empty_bit_array(12)
        for pos, bit in enumerate(self.zeros):
            if self.zeros[pos] > self.ones[pos]:
                gamma[pos] = 0
            else:
                gamma[pos] = 1
        return gamma

    def get_epsilon(self):
        epsilon = create_empty_bit_array(12)
        for pos, bit in enumerate(self.zeros):
            if self.ones[pos] < self.zeros[pos]:
                epsilon[pos] = 1
            else:
                epsilon[pos] = 0
        return epsilon

    def get_power_consumption(self):
        return binary_to_decimal(self.get_gamma()) * binary_to_decimal(self.get_epsilon())


if __name__ == "__main__":
    submarine = Submarine()
    content = read_puzzle("puzzle_input.txt")
    for line in content:
        submarine.read_binary(line)
    print("Gamma: " + str(submarine.get_gamma()) + ", Epsilon: " + str(submarine.get_epsilon()) +
          ", Power: " + str(submarine.get_power_consumption()))
