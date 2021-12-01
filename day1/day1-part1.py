def read_puzzle(path):
    with open(path, 'r+') as file:
        return file.read().split('\n')


if __name__ == '__main__':
    content = read_puzzle('puzzle_input.txt')
    larger = 0
    previous = content[0]
    for pos, num in enumerate(content):
        print('')
        if pos > 0:
            previous = content[pos - 1]
        if num > previous:
            larger = larger + 1
            print(num + '>' + previous)
        else:
            print(num + '<' + previous)
    print(larger)
