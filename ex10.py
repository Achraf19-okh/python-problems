import matplotlib.pyplot as plt
import time as t
times = []
mistakes = 0
print(" write programming as fast as you can")
input("press a key to continue.")

while len(times) < 5:
    start = t.time()
    word = input("Type the word:")
    end = t.time()
    time_elapsed = end - start

    times.append(time_elapsed)

    if (word.lower() != "programming"):
         mistakes +=1
print("you made" + str(mistakes) + " mistake(s).")
print("Now let's see your evolution")
t.sleep(5)

x =[1,2,3,4,5]
y = times
plt.plot(x,y)
legend = ["1","2","3","4","5"]
plt.xticks(x,legend)
plt.ylabel("Times (s)")
plt.xlabel("Attempts")
plt.title("your typing evoultion")
plt.show()

