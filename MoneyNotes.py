Amount =int(input("Please enter amount for withdrawal:"))

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//20
note_4 = (((Amount%100)%50)%20)//10
note_5 = ((((Amount%100)%50)%20)%10)//5

print("Notes of 100 AUD", note_1)
print("Notes of 50 AUD", note_2)
print("Notes of 20 AUD", note_3)
print("Notes of 10 AUD", note_4)
print("Notes of 5 AUD", note_5)