print("please typpe correct informations")
user_height = float(input("please enter your height in meters"))
user_weight = float(input("please enter your weight in kg"))
BMI = user_weight/(user_height*user_height)
print("your body mass index is" , round(BMI,2))
if(BMI <= 18.5):
    print("you are under weight")
elif(BMI > 18.5 and BMI <= 24.9):
    print("you are normal weight")
elif(BMI > 24.9 and BMI <= 29.9):
    print("overweight")
else:
   print("Obesity")
   
