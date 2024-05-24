import random


score = 0
QUESTION_FORMAT = "{}\nA.{}B.{}c.{}d.{}"
agent_list = ["phoenix","jett","reyna","neon","iso","raze","chamber","cypher","killjoy","deadlock","sage","clove","brimstone","harbor","omen","viper","sova","skye","kayo","breach","fade","gekko"]
goodcomments_list = ["good job","nice work","horray"]
badcomments_list = ["wrong","dumb","idiot"]
QUESTIONS = ["what is the most expensive weapon in valorant",
             "how many sentinals are in valorant",
             "how many rounds to you need to win an unrated valorant match",
             "which agent uses a dash ability",
             "which agent burnt down a school building",
             "which sentinal has healing powers"]
OPTIONS = [["operator","Odin","vandal","phantom"],
           ["6","2","4","5"],
           ["15","21","13","27"],
           ["jett","neon","kayo","chamber"],
           ["phoenix","sage","reyna","breach"],
           ["breach","sova","iso","sage"]]
SHORT_OPTIONS = ["a","b","c","d"]
ANSWERS = [0,3,2,0,0,1,3]
random.choice(goodcomments_list)
random.choice(badcomments_list)
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
        print (random.choice(goodcomments_list))
        score += 5
    elif answer == "":
        print ("you didint answer")
    else:
        print (random.choice(badcomments_list))
    answer = input ("how many sentinals are in valorant\n").lower()
    if answer == "5".lower ():
        print (random.choice(goodcomments_list))
        score += 5
    elif answer == "":
        print ("you didint answer")
    else:
        print (random.choice(badcomments_list))
    answer = input ("how many rounds to you need to win an unrated valorant match\n").lower()
    if answer == "13".lower ():
        print (random.choice(goodcomments_list))
        score += 5
    elif answer == "":
        print ("you didint answer")
    else:
        print (random.choice(badcomments_list))
    answer = input ("which agent uses a dash ability\n").lower()
    if answer == "jett".lower ():
        print (random.choice(goodcomments_list))
        score += 5
    elif answer == "":
        print ("you didint answer")
    else:
        print (random.choice(badcomments_list))
    answer = input ("which agent burnt down a school building\n").lower()
    if answer == "phoenix".lower ():
        print (random.choice(goodcomments_list))
        score += 5
    elif answer == "":
        print ("you didint answer")
    else:
        print (random.choice(badcomments_list))
    question = "which sentinal has healing powers"
    a = "sage"
    b = "chamber"
    c = "killjoy"
    d = "deadlock"
    answer = input(QUESTION_FORMAT.format(question, a, b, c, d)).lower()
    if answer == a or answer == "a":
        print (random.choice(goodcomments_list))
        score += 5
    elif answer == "":
        print ("you didint answer")
    else:
        print (random.choice(badcomments_list))
    #end the quiz
    print ("the end",score,"points")
    play = input("do you want to play again").lower()