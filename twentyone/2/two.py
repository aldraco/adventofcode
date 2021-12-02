# problem part one
OPERATIONS = {
    "up": lambda x, y, amt: (x, y - amt),
    "down": lambda x, y, amt: (x, y + amt),
    "forward": lambda x, y, amt: (x + amt, y),
}

# problem part two
OPERATIONS_AIM = {
    "down": lambda x, y, aim, amt: (x, y, aim+amt),
    "up": lambda x, y, aim, amt: (x, y, aim-amt),
    "forward": lambda x, y, aim, amt: (x + amt, y + (aim * amt), aim),
}

def main(ops):
    x = y = aim = 0

    for op in ops:
        dir, amt = op
        amt = int(amt)
        x, y, aim = OPERATIONS_AIM[dir](x, y, aim, amt)
        # print(f"x: {x}, y: {y}, aim: {aim}")
    
    return x * y


def read_data():
    with open("data.txt", "r") as f:
        data = f.readlines()
    return [line.strip().split(' ') for line in data]

if __name__ == "__main__":
    test_ops = [("forward", 5), ("down", 5), ("forward", 8), ("up", 3), ("down", 8), ("forward", 2)]
    assert main(test_ops) == 900

    print(main(read_data()))