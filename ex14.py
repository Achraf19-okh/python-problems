print("Welcome to the Grade Sorter")
L = []
data_valid = False
while data_valid == False:
    first_grade = int(input("What is you first grade(0-100) "))
    if (first_grade>20 or first_grade<0):
        print("grade has to be between 0 and 20")
        continue
    else:
        data_valid=True
data_valid = False
while data_valid == False:
    second_grade = int(input("What is you second grade(0-100) "))
    if (second_grade>20 or second_grade<0):
        print("grade has to be between 0 and 20")
        continue
    else:
        data_valid=True
data_valid = False
while data_valid == False:
    third_grade = int(input("What is you third grade(0-100) "))
    if (third_grade>20 or third_grade<0):
        print("grade has to be between 0 and 20")
        continue
    else:
        data_valid=True
data_valid = False
while data_valid == False:
    fourth_grade = int(input("What is you fourth grade(0-100) "))
    if (fourth_grade>20 or fourth_grade<0):
        print("grade has to be between 0 and 20")
        continue
    else:
        data_valid=True
L.append(first_grade)
L.append(second_grade)
L.append(third_grade)
L.append(fourth_grade)
#idem pour les quatres autres grades    
print("Your grades are :" , L)
L.sort(reverse=True)
print("You grades from highest to lowest are:" , str(L))

