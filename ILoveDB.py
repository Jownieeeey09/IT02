# Pattern 1
print("Pattern 1:")
for i in range(1, 6):
    for j in range(i):
        print(" * ", end="")
    print()

# Pattern 2
print("\nPattern 2:")
for i in range(5, 0, -1):
    for j in range(i):
        print(" * ", end="")
    print()

# Pattern 3
print("\nPattern 3:")
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print()

# Pattern 4
print("\nPattern 4:")


word = "I LOVE DB"
printed_words = set()

for i in range(len(word)):
    if word[i] != " ": 
        substring = word[:i+1]
        if substring not in printed_words:
            print(substring)
            printed_words.add(substring)