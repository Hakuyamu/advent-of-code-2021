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


def string_to_bit_array(string):
    arr = []
    for char in string:
        arr.append(int(char))
    return arr


def string_array_to_bit_array_list(array):
    arr = []
    for string in array:
        arr.append(string_to_bit_array(string))
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

    def get_most_common(self):
        most_common = create_empty_bit_array(12)
        for pos, bit in enumerate(self.zeros):
            if self.zeros[pos] > self.ones[pos]:
                most_common[pos] = 0
            else:
                most_common[pos] = 1
        print(str(most_common))
        return most_common

    def get_least_common(self):
        least_common = create_empty_bit_array(12)
        for pos, bit in enumerate(self.zeros):
            if self.ones[pos] < self.zeros[pos]:
                least_common[pos] = 1
            else:
                least_common[pos] = 0
        print(str(least_common))
        return least_common

    def get_oxygen_binary(self):
        most_common = self.get_most_common()
        possible_ratings = string_array_to_bit_array_list(read_puzzle("puzzle_input.txt"))
        index = 0
        while len(possible_ratings) > 1:
            for rating in possible_ratings:
                if len(rating) < 12:
                    break
                elif rating[index] != most_common[index]:
                    possible_ratings.remove(rating)
#                    print(str(string_to_bit_array(rating)[index]) + " <> " + str(most_common[index]))
                else:
                    print("Kept rating " + str(rating) + ", current index: " + str(index))
            print("Possible ratings left: " + str(len(possible_ratings)))
            index = index + 1
            if index > 11:
                break
        print("Possible ratings left: " + str(possible_ratings))
        return possible_ratings[0]

    def get_co2_binary(self, possible_ratings, index):
        least_common = self.get_least_common()
        if index > 11:
            return possible_ratings[0]
        if len(possible_ratings) > 1:
            for rating in possible_ratings:
                if len(rating) < 12:
                    break
                if rating[index] == least_common[index]:
                    print("Kept rating " + str(rating) + ", current index: " + str(index))
                else:
                    if len(possible_ratings) == 1:
                        return possible_ratings[0]
                    else:
                        possible_ratings.remove(rating)
        print("Possible ratings left: " + str(len(possible_ratings)))
        self.get_co2_binary(possible_ratings, index + 1)

    def get_life_support_rating(self):
        oxygen_generator_rating = self.get_oxygen_binary()
        co2_scrubber_rating = self.get_co2_binary(string_array_to_bit_array_list(read_puzzle("puzzle_input.txt")), 0)
        return binary_to_decimal(oxygen_generator_rating) * binary_to_decimal(co2_scrubber_rating)


if __name__ == "__main__":
    submarine = Submarine()
    content = read_puzzle("puzzle_input.txt")
    for line in content:
        submarine.read_binary(line)
    print("Life support rating: " + str(submarine.get_life_support_rating()))
