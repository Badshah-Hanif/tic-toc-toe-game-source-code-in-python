import random
import os



tic=[" "," "," "," "," "," "," "," "," "]
def display():
    print("\t==== tic toc toe ====\n")
    print("\t---1------2------3----")
    print(f"\t|  {tic[0]}   |   {tic[1]}   |   {tic[2]}   |")
    #print(f"\t|  1   |   2   |   3   |")
    print("\t-=-4------5------6----")
    print(f"\t|  {tic[3]}   |   {tic[4]}   |   {tic[5]}   |")
    #print(f"\t|  4   |   5   |   6   |")
    print("\t---7------8------9----")
    print(f"\t|  {tic[6]}   |   {tic[7]}   |   {tic[8]}   |")
#print(f"\t|  7   |   8   |   9   |")



  
def winner_cond(tic):
    # CHECK WIN CONDITION IN ROW FORM
    if tic[0] == tic[1] == tic[2] and tic[0] in ['X', 'O']:
        return True
    elif tic[3] == tic[4] == tic[5] and tic[3] in ['X', 'O']:
        return True
    elif tic[6] == tic[7] == tic[8] and tic[6] in ['X', 'O']:
        return True

    # CHECK WIN CONDITION IN COLUMN FORM
    elif tic[0] == tic[3] == tic[6] and tic[0] in ['X', 'O']:
        return True
    elif tic[1] == tic[4] == tic[7] and tic[1] in ['X', 'O']:
        return True
    elif tic[2] == tic[5] == tic[8] and tic[2] in ['X', 'O']:
        return True

    # CHECK WIN CONDITION IN DIAGONAL FORM
    elif tic[0] == tic[4] == tic[8] and tic[0] in ['X', 'O']:
        return True
    elif tic[2] == tic[4] == tic[6] and tic[2] in ['X', 'O']:
        return True    

#draw match condition
def draw_cond():
    if(tic[0]!=" " and tic[1]!=" " and tic[2]!=" " and tic[3]!=" " and tic[4]!=" " and tic[5]!=" " and tic[6]!=" " and tic[7]!=" " and tic[8]!=" "):
        return True 
    elif(tic[0]==tic[1]==tic[5]==tic[6]) and (tic[2]==tic[3]==tic[4]==tic[7])==('X' or 'O'):
        return True
    return False 
    
            
        

# TAKE INPUYT FROM USER
def user_input(count,player1,player2):

    next_turn=False
    current_player_symbol=player1 if  count%2==0 else player2
    current_player=player1 if current_player_symbol=='X' else player2
    print(f"***** {current_player} Player Turn  *****")
    placebox=(int(input("Enter a number  from 1 to 9:  ")))-1

    if  count%2==0:
        if tic[placebox]!=" ":
            print("this place is already filled. choose another one.")
        else:
            tic[placebox]=player2
            count+=1
            next_turn=True
    else:
        if tic[placebox]!=" ":
            print("this place is already filled. choose another one.")
        else:
            tic[placebox]=player1
            count+=1
            next_turn=True
    return next_turn



            
# clear screen function
def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')

 

def main():
    global win_toss
    player1=input("Enter  player1 name : ")
    player2=input("Enter  player2 name : ")
    toss=random.randint(0,2)
    if toss==1:
        print(f"*** {player1} win the toss ***")
        win_toss=player1
        print(f"{player1} is X")
        print(f"{player2} is O")
        pl1='X'
        pl2='O'
    else:
        print(f"*** {player2} win the toss ***")
        win_toss=player2
        print(f"{player2} is X")
        print(f"{player1} is O")
        pl1='O'
        pl2='X'
    count=0
    #display()
    #turn=user_input(toss,player1,player2,win_toss,toss)
    while True:
        display()
        turn=user_input(count,pl1,pl2)
               
        if winner_cond(tic)==True:
            if  toss==1:
                if count%2==1:
                    print(f"***{player2} won the match ***")
                elif count%2==0:
                    print(f"***{player1} won the match ***")
                display()
                break
            elif toss==0:
                if count%2==1:
                    print(f"***{player1} won the match ***")
                elif count%2==0:
                    print(f"***{player2} won the match ***")
                display()
                break
        elif draw_cond()==True:
            print("the match is draw")
            display()
            break
        if turn==True:
            count+=1
        clear_screen()
        
if __name__ == "__main__":
    main()  