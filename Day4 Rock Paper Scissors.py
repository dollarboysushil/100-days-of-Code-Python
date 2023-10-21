import random


print("Type 0 for ROCK , 1 for PAPER or 2 for SCISSORS")
user = int(input("What do you choose?"))
print("Your Choice: ")
if user == 1:
    print('''
     /| | | |_
     || | | | |
     || | | | |
    _||     ` |
   \\`\       ;
    \\        |
     \\      /
     | |    |
     | |    | ''')


elif user == 0:
        print(''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')


elif user == 2:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)


print("Computer Choice: ")
cmp = random.randint(0,2)
if cmp == 1:
    print('''
     /| | | |_
     || | | | |
     || | | | |
    _||     ` |
   \\`\       ;
    \\        |
     \\      /
     | |    |
     | |    | ''')


elif cmp == 0:
        print(''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')


elif cmp == 2:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

if user == cmp:
    print("Draw!!")


elif (user == 0  and cmp == 2) or (user == 2 and cmp == 1) or (user == 1 and cmp == 0):
    print("You Win!!")


else:
    print ( "Computer Win!!")