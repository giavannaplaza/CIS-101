import random

a = 30
b = int(imput("how many people might show up?"))
c = random.randint(1,16)


food = ["turkey", "Apple pie","MAshed Potatos","Cranberry SAuce"]
        
total = a + b + c
        
print("welcome to my program for thanksgiving")

answer = "n"

while answer != "y":
      for item in food:
          print("We need " + str(total) + " " + item)
    answer = input("do you want to keep going? Type y to exit")
    
      

      

      
