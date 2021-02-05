import font

def load_font(data, base="A"):
  letters = {}
  letter = []
  for i, line in enumerate(data.split("\n")):
    if i == 0:
      continue
    row = []
    for c in line:
      if c == " ":
        row.append(0)
      else:
        row.append(1)
    while len(row) < 8:
      row.append(0)
    letter.append(row)
    row = []
    if i % 9 == 0:
      letters[chr( ord(base) + (i // 9) )] = letter
      letter = []
  return letters


def print_font(letters):
  for key, letter in letters.items():
    for row in letter:
      for c in row:
        t = "." if c == 0 else "O"
        print(t, end = "")
      print("")
    print("-" * 8)

#letters = load_font(font.alpha_data, "A")
#print_font(letters)  
      
numbers = load_font(font.number_data, "0")
print_font(numbers)  
