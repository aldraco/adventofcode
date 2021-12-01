def main():
    data = read_file("data.txt")

    print(sum(count_increases(data)))
    print(sum(count_increases_in_threes(data)))

def count_increases(data):
    prev = data[0]
    for i in range(1, len(data)):
        yield 1 if data[i] > prev else 0
        prev = data[i]

def count_increases_in_threes(data):
    prev_window = sum(data[:3])
    for to_add in range(3, len(data)):
        curr_window = prev_window - data[to_add - 3] + data[to_add]
        yield 1 if curr_window > prev_window else 0
        prev_window = curr_window

def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    return [int(item.strip()) for item in lines]


if __name__ == "__main__":
    main()