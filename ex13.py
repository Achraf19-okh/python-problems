print("welcome to the letter Counter App")
name = input("What is you name:").strip().title()
print("hello, " + name + "!")
message = input("Please enter a message")
letter = input("which letter would yoi like to count the occurences of: ")
message = message.lower()
letter = letter.lower()
letter_count = message.count(letter)
print(name," your message has " + str(letter_count) + " " + letter + "'s in it.")


