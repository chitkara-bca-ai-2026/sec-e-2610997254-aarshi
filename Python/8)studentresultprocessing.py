print("==========================================================")
print("                 STUDENT RESULT PROCESSING               ")
print("==========================================================")

name = input("ENTER STUDENT NAME = ")
rollno = int(input("ENTER STUDENT ROLL NUMBER = "))

print("-------------student marks for 5 subjects (0-100)----------------")

subject1 = int(input("ENTER MARKS FOR SUBJECT 1 = "))
subject2 = int(input("ENTER MARKS FOR SUBJECT 2 = "))
subject3 = int(input("ENTER MARKS FOR SUBJECT 3 = "))
subject4 = int(input("ENTER MARKS FOR SUBJECT 4 = "))
subject5 = int(input("ENTER MARKS FOR SUBJECT 5 = "))
totalmarks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (totalmarks / 500) * 100
if percentage >=40 and percentage <= 100:
    result ="pass"
else:
    result ="fail"
if percentage >=90:
    GRADE = "A+"
elif percentage >=80:
    GRADE = "A"
elif percentage >=70:
    GRADE = "B"
elif percentage >=60:
    GRADE = "C"
elif percentage >=50:
    GRADE = "D"
else:
    GRADE = "E"

if GRADE =="A+":
   REMARKS = "outstanding"
elif GRADE =="A":  
    REMARKS = "excellent"
elif GRADE =="B":
    REMARKS = "very good"
elif GRADE =="C":
    REMARKS = "good"
elif GRADE =="D":
    REMARKS = "average"
  


print("----------------------------------------------------------")
print("         student report card          ")
print("----------------------------------------------------------")
print("STUDENT NAME = ", name)
print("STUDENT ROLL NUMBER = ", rollno)

print("-----------------------------------------")
print("TOTAL MARKS = ", totalmarks)
print("PERCENTAGE = ", percentage, "%")
print("RESULT:",result)
print("GRADE:",GRADE)
print("REMARKS:",REMARKS)