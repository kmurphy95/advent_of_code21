

def read_commands(file):

    input_cmds = []
    with open(file, 'r') as f:

        while 1:
            next_cmd = f.readline()
            if next_cmd:
                input_cmds.append(next_cmd)
            else:
                break

    return input_cmds


def process_commands(horiz_depth, commands):

    for command in commands:
        this_command = command.split()

        if this_command[0] == "up":
            horiz_depth[2] -= int(this_command[1])

        elif this_command[0] == "down":
            horiz_depth[2] += int(this_command[1])

        elif this_command[0] == "forward":
            horiz_depth[0] += int(this_command[1])
            horiz_depth[1] += int(this_command[1])*horiz_depth[2]

    return horiz_depth


if __name__ == "__main__":

    horiz_depth = [0, 0, 0]  # horiz_depth[0] is horizontal, horiz_depth[1] is depth, horiz_depth[2] is aim
    commands = read_commands("input2")

    horiz_depth = process_commands(horiz_depth, commands)

    print(f"Horizontal distance: {horiz_depth[0]} \n Depth: {horiz_depth[1]}\n")

    print(f"Total distance traveled (Horizontal x Depth): {horiz_depth[0] * horiz_depth[1]}")


