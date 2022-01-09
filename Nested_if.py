# Nested If Statements in Python
"""
3 Marks as Input
Total
Average
Result
If Pass Grade
    90-100 A
    80-89  B
    70-79  C
    Else   D
"""
m1 = int(input("Enter Mark-1: "))
m2 = int(input("Enter Mark-2: "))
m3 = int(input("Enter Mark-3: "))
total = m1 + m2 + m3
average = total / 3.0
print("Total: ", total)
print("Average; ", average)
if m1 >=35 and m2 >= 35 and m3 >= 35 and average<=100:
    print("Result : Pass")
    if 90 <= average:
        print("Grade : A ")
    elif 80 <= average:
        print("Grade : B ")
    elif 70 <= average:
        print("Grade : C ")
    else:
        print("Grade: D ")

elif(total>100):
    print("invalid marks")

else:
    print("Result : Fail")
    print("Grdade:  No Grdade")