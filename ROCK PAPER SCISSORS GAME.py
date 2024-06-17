#ROCK PAPER SCISSORS GAME
import tkinter as tk
import tkinter.messagebox as messagebox
import random

player_score = 0
computer_score = 0

def play_game(player_choice):
    global player_score, computer_score

    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    result = ""
    if player_choice == computer_choice:
        result = "It's a tie!\nLet's Try Again"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "Hurrah! You Win!!!!!"
        player_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Player Score: {player_score}\nComputer Score: {computer_score}")


    if messagebox.askyesno("Rock, Paper, Scissors", "Do you want to continue playing?"):
        pass  
    else:
        messagebox.showinfo("Rock, Paper, Scissors", f"\nTHANKS FOR PLAYING\nFinal Scores:\nPlayer Score: {player_score}\nComputer Score: {computer_score}")
        root.quit()

def start_game():
    start_button.destroy()  

    heading_label.config(text="\n***Choose One Among Them*\n",font=('arial',40),pady=20)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    rock_button = tk.Button(button_frame, text="Rock", command=lambda: play_game("Rock"),font=("arial bold",25),bg='#93abe4',width=10,height=5,highlightthickness=5,highlightbackground="#db1b1b", highlightcolor="#db1b1b")
    rock_button.grid(row=0, column=0,padx=2,pady=5)
    paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_game("Paper"),font=("arial bold",25),bg='#93abe4',width=10,height=5,highlightthickness=5,highlightbackground="#db1b1b", highlightcolor="#db1b1b")
    paper_button.grid(row=0, column=1,padx=2,pady=5)

    scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play_game("Scissors"),font=("arial bold",25),bg='#93abe4',width=10,height=5,highlightthickness=5,highlightbackground="#db1b1b", highlightcolor="#db1b1b")
    scissors_button.grid(row=0, column=2,padx=2,pady=5)

root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.configure(bg="#a6e8eb") 


heading_label = tk.Label(root, text="***Welcome To Rock Paper Scissor Game**\n\nClick On START Button*", font=('Arial', 40),bg='#07a4bf',pady=20)
heading_label.pack(pady=10)

start_button = tk.Button(root, text="Start Game", command=start_game, width=25, height=5,pady=50,bg='#2e86f9',font=("arial bold",20))
start_button.pack(pady=50)

result_label = tk.Label(root, text="", font=('Arial', 20), bg="#a6e8eb")
result_label.pack()

score_label = tk.Label(root, text="", font=('Arial', 20), bg="#a6e8eb")
score_label.pack()

# Run the main loop
root.mainloop()