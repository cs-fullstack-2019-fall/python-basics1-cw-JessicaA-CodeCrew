# Create two variables. One should equal “My name is: “ and the other should equal your actual name. Print the two variables in one print message.

v1 = "My name is: "
v2 = "Jessica"
print(v1 + v2)

# Problem 2:
# Ask the user to enter the extra credit they earned. If they entered less than 5 print “That’s not enough extra credit.” If they entered more than 20 print “That’s too much extra credit”.

userGrade = int(input("How much extra credit did you earn?"))
if userGrade < 5 :
    print("That's not enough extra credit")
elif userGrade > 20:
    print("That's too much extra credit")

# Ask a user to enter a password. Enter a password. Ask user to reenter password. Check to see if they are correct.

userInput1 = input("Enter a password: ")
userInput2 = input("Reenter a password: ")
if userInput1 == userInput2:
    print("Correct")
else:
    print("Incorrect")

# Ask for two card numbers. If it equals 21 print BLACKJACK!, if it’s greater than 21 print BUST!, if it’s less than 21 print “The total is [THE TOTAL]”

ask = int(input ("Enter card number 1: "))
ask2 = int(input ("Enter card number 2: "))
sum = ask + ask2
if sum > 21:
    print("BUST!")
elif sum == 21:
    print("BLACKJACK!")
elif sum < 21:
    print("The total is " + str(sum))







