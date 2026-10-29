print("Enter the scores of 5 students")

score1 = float(input("Enter score for student 1: "))
score2 = float(input("Enter score for student 2: "))
score3 = float(input("Enter score for student 3: "))
score4 = float(input("Enter score for student 4: "))
score5 = float(input("Enter score for student 5: "))

total = score1 + score2 + score3 + score4 + score5
average = total / 5

print("The average score is " + str(average))