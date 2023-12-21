
def parseString(line):
    line = line.split(":")
    played = line[1].split(";")
    return played

def getBigger(move):
    cubes = move.split(", ")
    rgb = [0, 0, 0]

    for cube in cubes:
        cleaned_cube = cube.strip()
        parts = cleaned_cube.split(" ")
        if len(parts) == 2 and parts[0].isdigit():
            number = int(parts[0])

            if "red" in parts:
                if(rgb[0] < number):
                    rgb[0] = number
            elif "green" in parts:
                if(rgb[1] < number):
                    rgb[1] = number
            elif "blue" in parts:
                if(rgb[2] < number):
                    rgb[2] = number

    return rgb

def get_power(line):
    game = parseString(line)
    final_array = [0, 0, 0]
    for move in game:
        new_array =  getBigger(move)
        if new_array[0] > final_array[0]:
            final_array[0] = new_array[0]
        if new_array[1] > final_array[1]:
            final_array[1] = new_array[1]
        if new_array[2] > final_array[2]:
            final_array[2] = new_array[2]

    return final_array[0] * final_array[1] * final_array[2]
        


with open("C:/Users/Aniol/Desktop/Personal/AOC-23/Day2/input", "r") as file:
    document = file.readlines()

total = 0
id = 1
for line in document:
    total += get_power(line)
    print(total)



print(total)

