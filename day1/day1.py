

# Any time the depth increases from one reading to the next, inc_count increases by one.
# Do this for every depth.
def count_increases(depths):

    inc_count = 0
    n = 0
    while n < len(depths):
        if depths[n] > depths[n-1]:
            inc_count += 1
        n += 1

    return inc_count


# File is raw text, read line-by-line with one depth measurement value per line.
def read_depths(file):

    input_depths = []
    with open(file, 'r') as f:

        while 1:
            next_depth = f.readline()
            if next_depth:
                input_depths.append(int(next_depth))
            else:
                break

    return input_depths


def sliding_windows(depths):

    sums = []
    n = 0
    while n < len(depths)-2:
        sums.append(depths[n] + depths[n+1] + depths[n+2])
        n += 1

    return sums


if __name__ == "__main__":
    measured_depths = read_depths("input1")
    count = count_increases(measured_depths)

    measured_windows = sliding_windows(measured_depths)
    window_count = count_increases(measured_windows)

    print(f"There were {count} increases in depth.")
    print(f"There were {window_count} increases in depth across all three-window measurements.")
