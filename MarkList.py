m1 = int(input("Enter the Marks: "))
m2 = int(input("Enter the Marks: "))
m3 = int(input("Enter The Marks: "))
total = m1 + m2+ m3
average = total / 3.0
if m1 >= 35 and m2>=35 and m3>=35 and average<=100:
    if average <= 90:
        print("Grade A")
    elif average <= 80:
        print("Grade  B")
    elif average <= 70:
        print("Grade C")
    else:
        print("Grade D")
elif average > 100:
    print("Invalid marks")

else:
    print("Failed")
    print("No Grade")



