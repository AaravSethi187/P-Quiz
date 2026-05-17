name=input("please enter your name- ")
filesave=open("quiz.txt","a")
scorelist=[1,2,3,4]
optionchosen=[0,0,0,0]

def filewrite(question,options,answer):
    filesave.write(str(question))
    filesave.write(str(options))
    filesave.write(str(answer))
    filesave.write("")
    
def q1():
    score=0
    ques1="Q1 If you get INR5000 from someone, what would u do with that money? write option 1,2,3 or 4"
    print(ques1)
    q1options=["1 spend it all in one place","2 save it all","3 save some amount and spend the rest","4 invest all"]
    for i in q1options:
        print(i)
    answer1=int(input("enter your answer(by writing option number)-"))
    if (answer1 in scorelist):
        score+=scorelist[answer1-1]
        optionchosen[answer1-1]+=1
        filewrite(ques1,q1options,answer1)
        return score
    return 0

def q2(score):
    ques2="Q2 If there is a 50% discount at your favorite shop, what would you do?"
    print(ques2)
    q2options=["1 go all out on that sale","2 dont buy anything and save money","3 compare the prices with other shops","4 buy only the things you need"]
    for i in q2options:
        print(i)
    answer2=int(input("enter your answer(by writing option number)-"))
    if (answer2 in scorelist):
        score+=scorelist[answer2-1]
        optionchosen[answer2-1]+=1
        filewrite(ques2,q2options,answer2)
        return score
    return 0

def q3(score):
    ques3="Q3 At the end of the month, you realise that you overspent. What would you do?"
    print(ques3)
    q3options=["1 ignore and still spend","2 make a plan to save money ","3 cut the expenses of next month","4 borrow money and start saving again"]
    for i in q3options:
        print(i)
    answer3=int(input("enter your answer(by writing option number)-"))
    if (answer3 in scorelist):
        score+=scorelist[answer3-1]
        optionchosen[answer3-1]+=1
        filewrite(ques3,q3options,answer3)
        return score 
    return 0

def q4(score):
    ques4="Q4 Do you usually save money?"
    print(ques4)
    q4options=["1 never","2 yes always","3 set aside a specific amount monthly","4 never"]
    for i in q4options:
        print(i)
    answer4=int(input("enter your answer(by writing option number)-"))
    if (answer4 in scorelist):
        score+=scorelist[answer4-1]
        optionchosen[answer4-1]+=1
        filewrite(ques4,q4options,answer4)
        return score
    return 0

def q5(score):
    ques5="Q5 Your friend tells you a high risk and high return plan. What will you do? "
    print(ques5)
    q5options=["1 invest a large amount quickly","2 dont invest","3 ask before investing","4 Do research and investa small amount"]
    for i in q5options:
        print(i)
    answer5=int(input("enter your answer(by writing option number)-"))
    if (answer5 in scorelist):
        score+=scorelist[answer5-1]
        optionchosen[answer5-1]+=1
        filewrite(ques5,q5options,answer5)
        return score
    return 0

def q6(score):
    ques6="Q6 You are short of money and you need money quickly. What will you do?"
    print(ques6)
    q6options=["1 delay the expense","2 panic and borrow","3 use savings","4 use emergency funds"]
    for i in q6options:
        print(i)
    answer6=int(input("enter your answer(by writing option number)-"))
    if (answer6 in scorelist):
        score+=scorelist[answer6-1]
        optionchosen[answer6-1]+=1
        filewrite(ques6,q6options,answer6)
        return score
    return 0
def graph():
    print(f"Financial Profile for {name}")
    print(f"Spender tendency {"I"*optionchosen[0]}")
    print(f"Saver tendency {"I"*optionchosen[1]}")
    print(f"Judicious person tendency {"I"*optionchosen[2]}")
    print(f"Investor tendency {"I"*optionchosen[3]}")
    
def quiz():
    mainscore=q1()
    score2=q2(mainscore)
    score3=q3(score2)
    score4=q4(score3)
    score5=q5(score4)
    score6=q6(score5)
    print("your final score is ",score6)
    print()
    if (score6<9):
        result="you are a spender Advice-Always think before spending"
    elif (score6<15):
        result="you are a saver Advice-Sometimes, you can be lenient on yourself and spend some amount"
    elif (score6<19):
        result="you are a judicious person(a smart spender and saver) Advice-None needed"
    else:
        result="you are an investor Advice-Gathering info about the investment never hurts"
    print(result)
    print("")
    graph()
    filesave.write(f"Result: {result}")
    filesave.write(str(graph()))


def main():
    play=input("would you like to play a game? write yes or no")
    while (play.lower()=="yes"):
        quiz()
        play=input("would you like to play a game? write yes or no")
    filesave.close()  
    with open("quiz.txt","r") as fileread:
        content=fileread.read()
    print(content)

if __name__=="__main__":
    main()
    
    
