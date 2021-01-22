import random
print('ce jeu consiste à deviner un nombre entre 0 et 1000.\npour abandonner taper 1001')
n = random.randrange(0,1001)
c = 1
x = int(input('essai 1:'))
while x!=n and x!=1001 :
 if x < n :
    print('trop petit')
 else :
   print('trop grand')
 c = c+1
 x= int(input('essai' + str(c) + ':'))
if x == n : 
 print('vous avez réussi en',c,'essais');
else :
 print("C'était n=",n);

    
      
