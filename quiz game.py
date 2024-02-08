print("welcome to my computer qizz! ")

playing = input("Do you want to play? ")

if playing !="yes":
    quit()

print("ok lets play ") 
score = 0   

answer = input("what does cpu stands for? ")
if answer =="central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")    

 
answer = input("what does gpu stands for? ")
if answer =="graphics processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")    


answer = input("what does ram stands for? ")
if answer =="random access memory":
    print("correct")
    score += 1
else:
    print("incorrect") 


answer = input("what does psc stands for? ")
if answer =="power supply":
    print("correct")
    score += 1
else:
    print("incorrect")  

print("you got " + str(score) + "questions correct")       
