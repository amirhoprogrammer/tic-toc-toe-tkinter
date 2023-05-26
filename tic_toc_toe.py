import tkinter as tk
from tkinter.messagebox import showinfo
window = tk.Tk()
window.title("tic-toc-toe game")

global turn , results , points
turn = "X"
results = ["","","","","","","","",""]
points = [0 , 0] 
def clicked(btn):
    global turn,results
    btn = int(btn) ## the function have recevied string 
    if results[btn] == "":
        if turn == "X":
            results[btn] = "X"
            button[btn]["bg"]="red"
            button[btn]["fg"]="white"
            button[btn]["text"] = "X"
            button[btn]["relief"]=tk.GROOVE
            #button[btn]["state"] = tk.DISABLED
            #print(f"{btn} clicked")
            turn = "O"
            ##print(turn)
        elif turn == "O" :
            results[btn] = "O"
            button[btn]["bg"]="yellow"
            button[btn]["fg"]="white"
            button[btn]["text"] = "O"
            #button[btn]["state"] = tk.DISABLED
            turn = "X"
            #print(f"{btn} clicked")
    #print(results)
    rule()
def rule():
    if(results[0]==results[1]==results[2] and results[0]!=0):
        show_winner(results[0])
    elif(results[3]==results[4]==results[5] and results[3]!=0):
        show_winner(results[3])
    elif(results[6]==results[7]==results[8] and results[6]!=0):
        show_winner(results[6])
    elif(results[0]==results[3]==results[6] and results[0]!=0):
        show_winner(results[0])
    elif(results[1]==results[4]==results[7] and results[1]!=0):
        show_winner(results[1])
    elif(results[2]==results[5]==results[8] and results[2]!=0):
        show_winner(results[2])
    elif(results[0]==results[4]==results[8] and results[0]!=0):
        show_winner(results[0])
    elif(results[2]==results[4]==results[6] and results[2]!=0):
        show_winner(results[2])
    else:
        check_draw()
        #print(f"player {results[0]} win!")
    #if(results[3]==results[4]==results[5] and results[3]!=0):
        #print(f"player {results[3]} win!")
def show_winner(winner):
    if winner == "X":
        points [0] += 1
        showinfo("game over","playeer one win!")
        #print(points)
        reset()
    elif winner == "O":
        points[1] += 1
        showinfo("game over","player two win!")
        #print(points)
        reset()
def reset():
    global results ,turn 
    results = ["","","","","","","","",""]
    turn = "X"
    information()
    board()
def check_draw():
    global results
    if "" not in results:
        showinfo("game over","draw")
        reset()

def information():
    global points
    board_frame = tk.Frame(window)
    board_frame.grid(row=0,column=0)
    label_player_one= tk.Label(board_frame, text = "player1" ,font=("italic",20),padx=10)
    label_player_two= tk.Label(board_frame, text = "player2" ,font=("italic",20),padx=20)
    label_player_one.grid(row =0,column=0)
    label_player_two.grid(row =0,column=1)
    point_frame = tk.Frame(window)
    point_frame.grid(row=1)
    point_player_one = tk.Label(point_frame,text=points[0],padx=20 , font=("bold",15))   
    point_player_two = tk.Label(point_frame,text=points[1],padx=20 , font=("bold",15))   
    point_player_one.grid(row=0,column=0) 
    point_player_two.grid(row=0,column=1) 
def board():
    global button
    button = []
    counter = 0
    board_frame = tk.Frame(window)
    board_frame.grid(row=2)
    for row in range(1, 4):
        for column in range(1, 4):
            index = counter
            button.append(index)
            button[index] = tk.Button(board_frame, command = lambda x = f"{index}" : clicked(x) ) ##text=f"btn {index}",
            button[index].config(width=10 ,height =4, font=("italic",18,"bold"))
            button[index].grid(row=row,column=column)
            counter += 1
    
information()
board()

window.mainloop()
