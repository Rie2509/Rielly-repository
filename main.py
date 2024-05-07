score = 0


#Ask the user their name and save it
name = input ("what is your name") 
#Greet the user and introduce the quiz
print ("welcome to this quiz about valorant\n",name)
#Ask the user a question 
answer = input ("what is the most expensive weapon in valorant\n")
if answer == "operator":
    print ("correct!")
    score += 5
elif answer == "":
    print ("you didint answer")
else:
    print ("incorrect")
answer = input ("how many sentinals are in valorant\n")
if answer == "5":
    print ("correct!")
    score += 5
elif answer == "":
    print ("you didint answer")
else:
    print ("incorrect")
answer = input ("how many rounds to you need to win an unrated valorant match\n")
if answer == "13":
    print ("correct!")
    score += 5
elif answer == "":
    print ("you didint answer")
else:
    print ("incorrect")
answer = input ("which agent uses a dash ability\n")
if answer == "jett":
    print ("correct!")
    score += 5
elif answer == "":
    print ("you didint answer")
else:
    print ("incorrect")
answer = input ("which agent burnt down a school building\n")
if answer == "phoenix":
    print ("correct!")
    score += 5
elif answer == "":
    print ("you didint answer")
else:
    print ("incorrect")
#end the quiz
print ("the end",score,"points")