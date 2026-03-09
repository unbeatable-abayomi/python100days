import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

a = 20
b = 10

def addition():
    print(a + b)
def substract():
    print(a - b)

addition()
substract()

