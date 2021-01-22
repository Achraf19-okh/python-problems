aperson = {"name": "ahmed","gender": "male", "age" : "27" , "adress" : "alwahda", "phone": "062"}
var = input("what information you want to know about ").lower()
result = aperson.get(var,"that information is not found")
print(result)
