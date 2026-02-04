x = input("Enter a string ")
print("your string has about " + str(x.count(" ") + 1) + " words.")

print("")

x = input("Enter a formula ")
if x.count("(") == x.count(")"):
  print("Your formula has the same number of open and closed parentheses.")
else:
  if x.count("(") > x.count(")"):
    print("Your formula has more open parentheses than closed parentheses.")
  else:
    print("Your formula has more closed parentheses than open parentheses.")

print("")

x = input("Enter a word ")
print("your word has vowels in it.")

print("")

x = input("Enter a string ")
y = x[0] + "*" + x[2: ] + "!!!"
print("your string is now " + y)
