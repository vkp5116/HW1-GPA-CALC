grade = input("Enter your course 1 letter grade: ")
ca = input("Enter your course 1 credit: ")
ca = float(ca)
if grade == "A":
  gpq = float(4.0)
  print(f"gradepoint for course 1 is:{gpq}")
elif grade == "A-":
  gpq = float(3.67)
  print(f"gradepoint for course 1 is:{gpq}")
elif grade == "B+":
  gpq = float(3.33)
  print(f"gradepoint for course 1 is:{gpq}")
elif grade == "B":
 gpq = float(3.0)
 print(f"gradepoint for course 1 is:{gpq}") 
elif grade == "B-":
  gpq = float(2.67)
  print(f"gradepoint for course 1 is:{gpq}")
elif grade == "C+":
  gpq = float(2.33)
  print(f"gradepoint for course 1 is:{gpq}")
elif grade == "C":
  gpq = float(2.0)
  print(f"gradepoint for course 1 is:{gpq}")
elif grade == "D":  
 gpq = float(1.0)
 print(f"gradepoint for course 1 is:{gpq}")
else:
  gpq = float(0)
  print(f"gradepoint for course 1 is:{gpq}")
gpq = float(gpq)

  
grade = input("Enter your course 2 letter grade: ")
cb = input("Enter your course 2 credit: ")
cb = float(cb)
if grade == "A":
  gpw = float(4)
  print(f"gradepoint for course 1 is:{gpw}")

elif grade == "A-": 
  gpw = float(3.67)
  print(f"gradepoint for course 1 is:{gpw}")
elif grade == "B+":
  gpw = float(3.33)
  print(f"gradepoint for course 1 is:{gpw}")
elif grade == "B":
  gpw = float(3.0)
  print(f"gradepoint for course 1 is:{gpw}")
elif grade == "B-":
  gpw = float(2.67)
  print(f"gradepoint for course 1 is:{gpw}")
elif grade == "C+":
  gpw = float(2.33)
  print(f"gradepoint for course 1 is:{gpw}")
elif grade == "C":
  gpw = float(2.0)
  gpw = print(f"gradepoint for course 1 is:{gpw}")
elif grade == "D": 
  gpw = float(1.0) 
  print(f"gradepoint for course 1 is:{gpw}")
else:
  gpw = float(0)
  print(f"gradepoint for course 1 is:{gpw}")
gpw = float(gpw) 


grade = input("Enter your course 3 letter grade: ")
cc = input("Enter your course 3 credit: ")
cc = float(cc)
if grade == "A":
 gpe = float(4.0)
 print(f"gradepoint for course 1 is:{gpe}")
elif grade == "A-":
  gpe = float(3.67)
  print(f"gradepoint for course 1 is:{gpe}")
elif grade == "B+":
  gpe = float(3.33)
  print(f"gradepoint for course 1 is:{gpe}")
elif grade == "B": 
  gpe = float(3.0)
  print(f"gradepoint for course 1 is:{gpe}")
elif grade == "B-":
  gpe = float(2.67)
  print(f"gradepoint for course 1 is:{gpe}")
elif grade == "C+":
  gpe = float(2.33)
  print(f"gradepoint for course 1 is:{gpe}")
elif grade == "C":
   gpe = float(2.0)
   print(f"gradepoint for course 1 is:{gpe}")
elif grade == "D":
  gpe = float(1.0)
  print(f"gradepoint for course 1 is:{gpe}")
else:
  gpe = float(0)
  print(f"gradepoint for course 1 is:{gpe}")
gpe = float(gpe)
print(f"{gpq*ca+gpw*cb+gpe*cc}/{ca+cb+cc}")





















