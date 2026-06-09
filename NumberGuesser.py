secretnumber=27
lives=5

print("Guess a number between 1 and 50.")

while lives > 0:
    guess=int(input("Enter your guess: "))
    if guess == secretnumber:
        print("Good Job you guessed it right!")
    break

lives=lives-1
difference = abs(guess-secretnumber)

if difference <=3:
    print("HInt: Hot")
elif difference <=7:
    print("HInt: warm")
elif difference <=15:
    print("Hint: cOld")
else:
    print("Hint: Very cold")

if lives > 0:
    print("Lives left: ", end="")
    for i in range(lives):
        print("Life", end="")
    print("\ngood job :)")

if lives == 0:
    print("Game over! you no more lives")
    print("The Secret number was:", secretnumber)



