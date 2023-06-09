import random

print("H A N G M A N")
print("The game will be available soon.")
list = ["python", "java", "javascript", "swift"]
key = random.choice(list)
word = input("Guess the word:")
if word == key:
    print("You survived!")
else:
    print("You lost!")