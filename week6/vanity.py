from random import choice

keypad = {"1" : ["1"], 
          "2" : ["A", "B", "C"],
          "3" : ["D", "E", "F"],
          "4" : ["G", "H", "I"],
          "5" : ["J", "K", "L"],
          "6" : ["M", "N", "O"],
          "7" : ["P", "Q", "R", "S"],
          "8" : ["T", "U", "V"],
          "9" : ["W", "X", "Y", "Z"],
          "0" : ["0"]}

print(keypad)
phone_number = "8675309"

mnemonic = ""
for digit in phone_number:
    # print(digit)
    # print(keypad[digit])
    mnemonic += choice(keypad[digit])
print(mnemonic)