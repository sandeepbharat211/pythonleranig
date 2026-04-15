# thish game name is stone, peper, scissor
import random as r
l=["stone","paper","scissor"]

"""
Logic:
stone vs paper->win paper
stone vs scisser->win stone
paper vs scisser->win sciccor"""

while True:
    ccount=0
    ucount=0
    uc=int(input('''
    Game Start....
    1 Yes
    2 No | Exit
                 '''))
    if uc==1:
        for a in range(1,6):
            userinput=int(input('''
1 Stone
2 Paper
3 Scissor
        '''))
            if userinput==1:
                uchoice="stone"
            elif userinput==2:
                uchoice="paper"
            elif userinput==3:
                uchoice="scissor"
            Cchoice=r.choice(l)
            if Cchoice==uchoice:
                print("Computer Value",Cchoice)
                print("User Value",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif(uchoice=="stone" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="stone") or (uchoice=="seissor" and Cchoice=="paper"):
                print("Computer Value",Cchoice)
                print("User Value",uchoice)
                print("You Win")
                ucount=ucount+1
            else:
                print("Computer Value",Cchoice)
                print("User Value",uchoice)
                print("Computer Win")
                ccount=ccount+1
        print("======================================")
        
        if ccount==ucount:
            print("Final Game Draw")
            print("User Score: ",ucount)
            print("Computer Score: ",ccount)
        elif ucount>ccount:
            print("Final You Win The Game")
            print("User Score: ",ucount)
            print("Computer Score: ",ccount)
        else:
            print("Final Computer Win The Game")
            print("User Score: ",ucount)
            print("Computer Score: ",ccount)

    else:
        break