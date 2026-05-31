name=input("please enter your name- ")
filesave=open("quiz2.txt","a")
scorelist=[1,2,3,4]
optionchosen=[0,0,0,0]

def filewrite(question,options,answer):
    filesave.write(str(question)+"\n")
    filesave.write("Options: "+str(options)+"\n")
    filesave.write("User answer: "+str(answer)+"\n")
    filesave.write("-"*100+"\n")

#defining the first question
def q1():
    score=0
    ques1="Q1 If you get INR5000 from someone, what would you do with that money? Write option 1,2,3 or 4"
    print(ques1)
    q1options=["1 Spend it all in one place","2 Save it all","3 Save some amount and spend the rest","4 Invest all"]
    for i in q1options:
        print(i)
    answer1=int(input("Enter your answer(by writing option number)-"))
    if (answer1 in scorelist):
        score+=scorelist[answer1-1]
        optionchosen[answer1-1]+=1
        filewrite(ques1,q1options,answer1)
        return score
    return 0

def q2(score):
    ques2="Q2 If there is a 50% discount at your favorite shop, what would you do?"
    print(ques2)
    q2options=["1 Go all out on that sale","2  Save money and not buy anything","3 Compare the prices with other shops","4 Buy only the things you need"]
    for i in q2options:
        print(i)
    answer2=int(input("Enter your answer(by writing option number)-"))
    if (answer2 in scorelist):
        score+=scorelist[answer2-1]
        optionchosen[answer2-1]+=1
        filewrite(ques2,q2options,answer2)
        return score
    return 0

def q3(score):
    ques3="Q3 At the end of the month, you realise that you overspent. What would you do?"
    print(ques3)
    q3options=["1 Ignore and still spend","2 Make a plan to save money ","3 Cut the expenses of next month","4 Borrow money and start saving again"]
    for i in q3options:
        print(i)
    answer3=int(input("Enter your answer(by writing option number)-"))
    if (answer3 in scorelist):
        score+=scorelist[answer3-1]
        optionchosen[answer3-1]+=1
        filewrite(ques3,q3options,answer3)
        return score 
    return 0

def q4(score):
    ques4="Q4 Do you usually save money?"
    print(ques4)
    q4options=["1 Never","2 Yes always","3 Set aside a specific amount monthly","4 Sometimes"]
    for i in q4options:
        print(i)
    answer4=int(input("Enter your answer(by writing option number)-"))
    if (answer4 in scorelist):
        score+=scorelist[answer4-1]
        optionchosen[answer4-1]+=1
        filewrite(ques4,q4options,answer4)
        return score
    return 0

def q5(score):
    ques5="Q5 Your friend tells you a high risk and high return plan. What will you do? "
    print(ques5)
    q5options=["1 Invest a large amount quickly","2 DO not invest","3 Ask before investing","4 Do research and invest a small amount"]
    for i in q5options:
        print(i)
    answer5=int(input("Enter your answer(by writing option number)-"))
    if (answer5 in scorelist):
        score+=scorelist[answer5-1]
        optionchosen[answer5-1]+=1
        filewrite(ques5,q5options,answer5)
        return score
    return 0

def q6(score):
    ques6="Q6 You are short of money and you need money quickly. What will you do?"
    print(ques6)
    q6options=["1 Delay the expense","2 Panic and borrow","3 Use savings","4 Use emergency funds"]
    for i in q6options:
        print(i)
    answer6=int(input("Enter your answer(by writing option number)-"))
    if (answer6 in scorelist):
        score+=scorelist[answer6-1]
        optionchosen[answer6-1]+=1
        filewrite(ques6,q6options,answer6)
        return score
    return 0
def graph():
    title=f'Financial Profile for {name}'
    print(title)
    filesave.write(title+"\n")
    print()
    a=f'Spender tendency {"I"*optionchosen[0]}'
    b="-->Spender tendency means how much do you spend given the circumstances."
    c=f'Saver tendency {"I"*optionchosen[1]}'
    d="-->Saver tendency means how much can you save and not spend money all the time."
    e=f'Judicious person tendency {"I"*optionchosen[2]}'
    f="-->Judicious person tendency means that you can balance your spending and savings easily and wisely."
    g=f'Investor tendency {"I"*optionchosen[3]}'
    h="-->Investor tendency means that you invest more and have a good knowledge of what you are doing. "
    i="*Each 'I' shows the level of each tendency. The more the 'I' the more you have that trait of money managing"
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(i)
    filesave.write(a+"\n")
    filesave.write(b+"\n")
    filesave.write(c+"\n")
    filesave.write(d+"\n")
    filesave.write(e+"\n")
    filesave.write(f+"\n")
    filesave.write(g+"\n")
    filesave.write(h+"\n")
    filesave.write(i+"\n")
    
    
def quiz():
    mainscore=q1()
    score2=q2(mainscore)
    score3=q3(score2)
    score4=q4(score3)
    score5=q5(score4)
    score6=q6(score5)
    print("your final score is ",score6)
    print()
    filesave.write("Your final score is:"+str(score6)+"\n")
    filesave.write("-"*100+"\n")
    
    if (score6<9):
        result="you are a spender \nAdvice-Always think before spending"
    elif (score6<15):
        result="you are a saver \nAdvice-Sometimes, you can be lenient on yourself and spend some amount"
    elif (score6<19):
        result="you are a judicious person(a smart spender and saver) \nAdvice-None needed"
    else:
        result="you are an investor \nAdvice-Gathering info about the investment never hurts"
    print(result)
    print("")
    graph()
    filesave.write(f"Result: {result}"+"\n")


def main():
    play=input("would you like to play a game? write yes or no")
    filesave.write("PERSONALITY QUIZ ANALYSIS"+"\n")
    filesave.write("~"*100+"\n\n")
    while (play.lower()=="yes"):
        quiz()
        play=input("would you like to play a game? write yes or no")
    filesave.close()  
    with open("quiz2.txt","r") as fileread:
        content=fileread.read()
    print(content)

if __name__=="__main__":
    main()
    
    
