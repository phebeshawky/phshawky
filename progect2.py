question1 = input("what is your name?\n")
question2 = input ("enter your user name:\n")
question3 = input("enter your passwoed:\n")
count = 0
limit = 3
lose = False


print("welcom to krok")
print(question1)
print(question2)
print(question3)

print("NOW WE WILL STAT")
answer1=("digestive system")
useranswer =("")

while answer1 != useranswer and not lose :
     if count < limit :
        
       useranswer= input("which system is responsible for digestion?\n")
       count += 1
     else :
         lose = True
         useranswer == answer1
print ("<next question>")   

answer2 =("respiratory system")  
useranswer2 = ("")
while useranswer2 != answer2 and not lose :
     if count < limit : 
       useranswer2 = input("which system is responsible for breath?\n")
       count +=1
     else :
        lose = True
        useranswer2 == answer2 

print ("<next question>")    

answer3 =("nerve system")
useranswer3 = ("")
while useranswer3 != answer3 and not lose :
     if count < limit :
       useranswer3 = input("which system is responsible for nerve?\n")
       count +=1
     else :
        lose = True
        useranswer3 == answer3
print ("Quiz is finished")          


