word_int_mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def main():
    with open("calibration.txt", "r") as infile:
        lines = infile.readlines()

    total = 0
    for line in lines:
        first = None
        last = None
        for ch in line:
            if ch.isdigit():
                if first is None:
                    first = ch
                last = ch

        total += int(first + last)

    print(total)


if __name__ == '__main__':
    main()
