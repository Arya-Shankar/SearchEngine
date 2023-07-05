arr = []

with open("prob.txt", "r") as file:
    for line in file:
        arr.append(line)


arr = list(set(arr))

def remove_pattern(arr, pattern):
    new_arr = []
    for line in arr:
        if pattern not in line:
            new_arr.append(line)
        else:
            pass

    return new_arr

arr = remove_pattern(arr, "/solution")

# print(len(final_arr))

with open("lc.txt", "a") as file:
    for line in arr:
        file.write(line)
