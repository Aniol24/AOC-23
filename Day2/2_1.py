
def parseString(line):
    line = line.split(":")
    played = line[1].split(";")
    return played

def getSum(move):
    cubes = move.split(", ")
    rgb = [0, 0, 0]

    for cube in cubes:
        cleaned_cube = cube.strip()
        parts = cleaned_cube.split(" ")
        if len(parts) == 2 and parts[0].isdigit():
            number = int(parts[0])

            if "red" in parts:
                rgb[0] += number
            elif "green" in parts:
                rgb[1] += number
            elif "blue" in parts:
                rgb[2] += number

    if rgb[0] > 12 or rgb[1] > 13 or rgb[2] > 14:
        return 0
    else:
        return 1



def is_possible_game(line):
    game = parseString(line)
    for move in game:
        if getSum(move) == 1:
            continue
        else: return 0
    return 1





with open("input", "r") as file:
    document = file.readlines()

total = 0
id = 1
for line in document:
    if is_possible_game(line) == 1:
        total += id
    id = id + 1


print(total)

