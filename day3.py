subject_1 = float(input("Enter marks for subject 1: "))
subject_2 = float(input("Enter marks for subject 2: "))
subject_3 = float(input("Enter marks for subject 3: "))


average_marks = (subject_1 + subject_2 + subject_3) / 3

if average_marks >= 90:
    print("Grade: A")
elif 80 <= average_marks < 90:
    print("Grade: B")
elif 70 <= average_marks < 80:
    print("Grade: C")
else:
    print("Grade: Fail")