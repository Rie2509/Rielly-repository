score = 0
import random
QUESTION_FORMAT = "{}\nA.{}B.{}c.{}d.{}"
agent_list = ["phoenix","jett","reyna","neon","iso","raze","chamber","cypher","killjoy","deadlock","sage","clove","brimstone","harbor","omen","viper","sova","skye","kayo","breach","fade","gekko"]
goodcomments_list = ["good job","nice work","horray"]
badcomments_list = ["wrong","dumb","idiot"]
#Ask the user their name and save it
name = input ("what is your name") 
#Greet the user and introduce the quiz
print ("welcome to this quiz about valorant\n",name)
#Ask the user a question
play = "yes"
while play == "yes":
    while True:
        try: 
            tries = int(input("how many attempts to you want at each question"))
            break
        except:
            print("thats not a number")
    answer = input ("what is the most expensive weapon in valorant\n").lower()
    if answer == "operator".lower ():
        print (goodcomments_list[0])
        score += 5
    elif answer == "":
        print ("you didint answer")
    else:
        print (badcomments_list[0])
    answer = input ("how many sentinals are in valorant\n").lower()
    if answer == "5".lower ():
        print (goodcomments_list[0])
        score += 5
    elif answer == "":
        print ("you didint answer")
    else:
        print ("incorrect its 5")
    answer = input ("how many rounds to you need to win an unrated valorant match\n").lower()
    if answer == "13".lower ():
        print (goodcomments_list[0])
        score += 5
    elif answer == "":
        print ("you didint answer")
    else:
        print (badcomments_list[0])
    answer = input ("which agent uses a dash ability\n").lower()
    if answer == "jett".lower ():
        print (goodcomments_list[0])
        score += 5
    elif answer == "":
        print ("you didint answer")
    else:
        print (badcomments_list[0])
    answer = input ("which agent burnt down a school building\n").lower()
    if answer == "phoenix".lower ():
        print (goodcomments_list[0])
        score += 5
    elif answer == "":
        print ("you didint answer")
    else:
        print ("incorrect its phoenix")
    answer == input ("which sentinal places a trap\n").lower()
    if answer == "cypher" or answer == "deadlock" or answer == "chamber". lower:
        print (goodcomments_list[0])
        score += 5
    elif answer == "":
        print ("you didint answer")
    else:
        print (badcomments_list[0])
    question = "which sentinal has healing powers"
    a = "sage"
    b = "chamber"
    c = "killjoy"
    d = "deadlock"
    answer = input(QUESTION_FORMAT.format(question, a, b, c, d)).lower()
    if answer == a or answer == "a":
        print (goodcomments_list[0])
        score += 5
    elif answer == "":
        print ("you didint answer")
    else:
        print (badcomments_list[0])
    #end the quiz
    print ("the end",score,"points")
    play = input("do you want to play again").lower()