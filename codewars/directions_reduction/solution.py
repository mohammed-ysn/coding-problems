def dirReduc(arr):
    opposite = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"
    }
    res = []
    for direction in arr:
        if res and (opposite[direction] == res[-1]):
            res.pop()
        else:
            res.append(direction)
    return res


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))
