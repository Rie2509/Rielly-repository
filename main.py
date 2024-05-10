score = 0
QUESTION_FORMAT = "{}\nA.{}B.{}c.{}d.{}"

#Ask the user their name and save it
name = input ("what is your name") 
#Greet the user and introduce the quiz
print ("welcome to this quiz about valorant\n",name)
#Ask the user a question 
answer = input ("what is the most expensive weapon in valorant\n")
if answer == "operator".upper ():
    print ("correct!")
    score += 5
elif answer == "":
    print ("you didint answer")
else:
    print ("incorrect")
answer = input ("how many sentinals are in valorant\n")
if answer == "5".upper ():
    print ("correct!")
    score += 5
elif answer == "":
    print ("you didint answer")
else:
    print ("incorrect")
answer = input ("how many rounds to you need to win an unrated valorant match\n")
if answer == "13".upper ():
    print ("correct!")
    score += 5
elif answer == "":
    print ("you didint answer")
else:
    print ("incorrect")
answer = input ("which agent uses a dash ability\n")
if answer == "jett".upper ():
    print ("correct!")
    score += 5
elif answer == "":
    print ("you didint answer")
else:
    print ("incorrect")
answer = input ("which agent burnt down a school building\n")
if answer == "phoenix".upper ():
    print ("correct!")
    score += 5
elif answer == "":
    print ("you didint answer")
else:
    print ("incorrect")
answer == input ("which sentinal places a trap")
if answer == "cypher" or answer == "deadlock" or answer == "chamber". upper:
    print ("correct!")
    score += 5
elif answer == "":
    print ("you didint answer")
else:
    print ("incorect")
question = "which sentinal has healing powers"
a = "sage"
b = "chamber"
c = "killjoy"
d = "deadlock"
answer = input(QUESTION_FORMAT.format(question, a, b, c, d).upper)
#end the quiz
print ("the end",score,"points")