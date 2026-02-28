text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)

text = "Python is awesome"
words = text.split()
print("Words:", words)

text = "   Some spaces around   "
#print(text)
stripped_text = text.strip()
print("Stripped text:", stripped_text)

text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")