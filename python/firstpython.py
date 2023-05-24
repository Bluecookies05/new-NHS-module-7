#operators

firstNumber = 18
secondNumber = 20

print ( firstNumber, secondNumber, 78, "Another String", sep="--", end="THE END" )
print ( "Line 2", end = "Line 2 end" )
print ( "Another Line" )

#Logical applicator

REQUIRED_MONEY = 20
REQUIRED_AGE = 18

userAge = 17
userMoney = 100

if userAge < REQUIRED_AGE or userMoney <REQUIRED_MONEY:
    print ( "you have to meet the requirements" )
else:
    print ( "Enjoy the Party" )

