def read_puzzle(path):
    with open(path, 'r+') as file:
        return file.read().split('\n')


if __name__ == '__main__':
    content = read_puzzle('puzzle_input.txt')
    larger = 0
    previous = content[0]
    for pos, num in enumerate(content):
        if pos + 3 < len(content):
            print('')
            first_sum = int(content[pos]) + int(content[pos + 1]) + int(content[pos + 2])
            second_sum = int(content[pos + 1]) + int(content[pos + 2]) + int(content[pos + 3])
            if second_sum > first_sum:
                larger = larger + 1
                print(str(second_sum) + '>' + str(first_sum))
            else:
                print(str(second_sum) + '<' + str(first_sum))
    print(larger)
