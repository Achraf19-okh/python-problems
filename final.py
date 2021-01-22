print("this program calculate your final mark and say if you're admitted in a high engineering school")
import time as t
import matplotlib.pyplot as plt
L = []
valid_data = False
while valid_data == False:
    eng_mark = float(input("type you english mark :"))
    if (eng_mark < 0 or eng_mark > 20):
       print("mark has to be between(0.20)18:22 21/03/2020")
       continue
    else:
        valid_data = True
valid_data = False
while valid_data == False:
    math_mark = float(input("type your math mark :"))
    if (math_mark < 0 or math_mark > 20):
       print("mark has to be between(0.20)")
       continue
    else:
        valid_data = True
valid_data = False
while valid_data == False:
    computersc_mark = float(input("type your CS mark :"))
    if (computersc_mark < 0 or computersc_mark > 20):
       print("mark has to be between(0.20)")
       continue
    else:
        valid_data = True
valid_data = False
while valid_data == False:
    dataanalys_mark = float(input("type you DA mark :"))
    if (dataanalys_mark < 0 or dataanalys_mark > 20):
       print("mark has to be between(0.20)")
       continue
    else:
        valid_data = True
valid_data = False
while valid_data == False:
    total_classes = int(input("type the total number of classes: "))
    if (total_classes <=0):
       print("classe's duration has to be greater than 0")
       continue
    else:
        valid_data = True
valid_data = False
while valid_data == False:
    abscences = int(input("type the number of abscences not justified : "))
    if (abscences <0 or abscences > total_classes):
       print("something is wrong try again")
       continue
    else:
        valid_data = True
print("----------------------------------------------------")
        
ecoef = int(input("type english coeff "))
mcoef = int(input("type Math coeff "))
cscoef = int(input("type computer science coeff "))
dacoef = int(input("type data analyst coeff "))

mark = ((eng_mark*ecoef)+(math_mark*mcoef)+(computersc_mark*cscoef) + (dataanalys_mark*dacoef))/9
attend = (total_classes - abscences) / total_classes
if(0.8 <= attend <= 1):
    mark = mark - 0.10
elif(0.6 <= attend < 0.8):
    mark = mark - 0.3
elif(0.4 <= attend < 0.6):
    mark = mark - 0.50
elif( 0.2 <= attend < 0.4):
    mark = mark - 0.60
else:
    mark = mark - 1
print("you final mark is :" , round(mark,2))
if( mark >= 17.5):
    print("excellent work, wait to see if you are addmited as an exchange student")
    t.sleep(4)
    print("congrats, with your mark" , round(mark,2) , "you are accepted to continue your studies as an exchange")
elif( 15 <= mark < 17.5):
    print("very good work, wait to see if you are addmited as an exchange student")
    t.sleep(4)
    print("sorry but you are not accepted, with your mark" , round(mark,2), ", Good Luck next time")
elif( 13 <= mark < 15):
    print("good work, wait to see if you are addmited as an exchange student")
    t.sleep(4)
    print("sorry but you are not accepted, with your mark" , round(mark,2), " ,Good Luck next time")
elif( 10 <= mark < 13):    
    print("average work, wait to see if you are addmited as an exchange student")
    t.sleep(4)
    print("sorry but you are not accepted, with your mark" , round(mark,2), " ,Good Luck next time")
else:    
    print("Sorry you mark " ,round(mark,2) ,"is not accepted")
print("let's see you evolution")
t.sleep(6)
items = [ "english" , "math" , "computer science" , "data analysis"]
marks = [ round(eng_mark,2) , round(math_mark,2) ,round(computersc_mark,2),round(dataanalys_mark,2) ]
plt.plot(items,marks)
plt.xlabel("items")
plt.ylabel("marks")
plt.title("student evoultion")
plt.show()
