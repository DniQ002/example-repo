### THE STRING & NUMERICAL DATA TYPE TASK ###

# --- Auto-graded Task 1 ---

# The string sentence
string = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Output - The quick brown fox jumps over the lazy dog.
new_string = string.replace("!", " ")

# Output - THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
new_string2 = new_string.upper()

# Output - .GOD YZAL EHT REVO SPMUJ XOF NWORB KCIUQ EHT
new_string3 = new_string2[::-1]

print(string)
print(new_string)
print(new_string2)
print(new_string3)
