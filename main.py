def load_font(data_list, base="A"):
    ROWS_PER_CHARACTER = 9
    output_dict = {}
    row_list = []
    for i, line in enumerate(data_list):
        if (i+1) % ROWS_PER_CHARACTER == 0:
            index = i // ROWS_PER_CHARACTER
            key = chr( base_index + index)
            output_dict[key] = row_list
            row_list = []
        else:
            line = line.rstrip("\n")
            row = []
            for c in line:
                row.append(0 if c == " " else 1)
            while len(row) < 8:
                row.append(0)
            row_list.append(row)
            row = []
            base_index = ord(base)
    return output_dict


def print_font(data_dict):
    for key, letter in data_dict.items():
        for row in letter:
            for c in row:
                t = "." if c == 0 else "O"
                print(t, end="")
            print("")
        print("-" * 8)


def read(prefix="alpha"):
    with open("data/" + prefix + "_data.txt", "r") as f:
        return f.readlines()


letters = load_font(read("alpha"))
print_font(letters)

numbers = load_font(read("number"), "0")
print_font(numbers)

print(letters)