months = ("jan", "feb" , "March", "april", "may" , "june" , "july" , "august" ,"sept" , "oct" , "nov" , "december" )
birthday = input("type your birthday month in that form DD-MM-YYYY: ")
index = int(birthday[3:5]) - 1
bd_month = months[index]
index2 = int(birthday[-4:])
print(" you were born in",bd_month, "and you year of birth is" ,index2)
