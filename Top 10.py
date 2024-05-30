BIGGEST_COUNTRIES_ANSWERS = ["russia","canada","chine","us","brazil","brazil","australia","india","argentina","kazakhstan"]
score = 0
# ------FUNCTIONS---------
#welcome the users
def intro():
    print("hello")
    #ask the users there name
    name = input("what is your name")
    #greet the users and introduce the quiz


def getLives():
    while True:
        live = input("how many chances do you want")
        try:
            lives = int(lives)
            if lives >= 0:
                return lives
            else:
                print("please choose a positive number")
        except:
            print("that wasnt a number")


def addFive(number):
    return number + 5

def isCorrect(answers, list):
    if answer in list:
        return True
    else:
        return False



# -------- MAIN CODE ------------
intro()
lives = getLives()
num = addFive ()
while lives > 0:
    answer = input("name one of the top ten biggest countries in the world:\n").lower()
    
    if isCorrect(answer, BIGGEST_COUNTRIES_ANSWERS) == True:
        print("correct")
