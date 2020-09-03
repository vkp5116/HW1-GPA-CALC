grade = input("Enter your course 1 letter grade: ")
ca = input("Enter your course 1 credit: ")
ca = float(ca)
if grade == "A":
  gpq = 4.0
  print(f"gradepoint for course 1 is:{gpq}")
elif grade == "A-":
  gpq = 3.67
  print(f"gradepoint for course 1 is:{gpq}")
elif grade == "B+":
  gpq = 3.33
  print(f"gradepoint for course 1 is:{gpq}")
elif grade == "B":
 gpq = 3.0
 print(f"gradepoint for course 1 is:{gpq}") 
elif grade == "B-":
  gpq = 2.67
  print(f"gradepoint for course 1 is:{gpq}")
elif grade == "C+":
  gpq = 2.33
  print(f"gradepoint for course 1 is:{gpq}")
elif grade == "C":
  gpq = 2.0
  print(f"gradepoint for course 1 is:{gpq}")
elif grade == "D":  
 gpq = 1.0
 print(f"gradepoint for course 1 is:{gpq}")
else:
  gpq = 0
  print(f"gradepoint for course 1 is:{gpq}")


  
grade = input("Enter your course 2 letter grade: ")
cb = input("Enter your course 2 credit: ")
cb = float(cb)
if grade == "A":
  gpw = 4
  print(f"gradepoint for course 1 is:{gpw}")

elif grade == "A-": 
  gpw = 3.67
  print(f"gradepoint for course 1 is:{gpw}")
elif grade == "B+":
  gpw = 3.33
  print(f"gradepoint for course 1 is:{gpw}")
elif grade == "B":
  gpw = 3.0
  print(f"gradepoint for course 1 is:{gpw}")
elif grade == "B-":
  gpw = 2.67
  print(f"gradepoint for course 1 is:{gpw}")
elif grade == "C+":
  gpw = 2.33
  print(f"gradepoint for course 1 is:{gpw}")
elif grade == "C":
  gpw = 2.0
  gpw = print(f"gradepoint for course 1 is:{gpw}")
elif grade == "D": 
  gpw = 1.0 
  print(f"gradepoint for course 1 is:{gpw}")
else:
  gpw = 0
  print(f"gradepoint for course 1 is:{gpw}")


grade = input("Enter your course 3 letter grade: ")
cc = input("Enter your course 3 credit: ")
cc = float(cc)
if grade == "A":
 gpe = 4.0
 print(f"gradepoint for course 1 is:{gpe}")
elif grade == "A-":
  gpe = 3.67
  print(f"gradepoint for course 1 is:{gpe}")
elif grade == "B+":
  gpe = 3.33
  print(f"gradepoint for course 1 is:{gpe}")
elif grade == "B": 
  gpe = 3.0
  print(f"gradepoint for course 1 is:{gpe}")
elif grade == "B-":
  gpe = 2.67
  print(f"gradepoint for course 1 is:{gpe}")
elif grade == "C+":
  gpe = 2.33
  print(f"gradepoint for course 1 is:{gpe}")
elif grade == "C":
   gpe = 2.0
   print(f"gradepoint for course 1 is:{gpe}")
elif grade == "D":
  gpe = 1.0
  print(f"gradepoint for course 1 is:{gpe}")
else:
  gpe = 0
  print(f"gradepoint for course 1 is:{gpe}")
print(f"{gpq*ca+gpw*cb+gpe*cc}/{ca+cb+cc}")





















