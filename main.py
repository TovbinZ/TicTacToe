from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import json


#reset board on load
board = {
   "1-1": "Blank", 
   "1-2": "Blank", 
   "1-3": "Blank", 
   "2-1": "Blank", 
   "2-2": "Blank", 
   "2-3": "Blank", 
   "3-1": "Blank", 
   "3-2": "Blank", 
   "3-3": "Blank"
   }
#write board info to json file
with open("BoardInfo.json", "w") as jsonFile:
   jsonFile.write(json.dumps(board))


def Logic(key,turn,window):
      with open("BoardInfo.json", "r") as jsonFile:
         board = json.load(jsonFile)

      board[f"{key}"] = turn

      with open("BoardInfo.json", "w") as jsonFile:
         jsonFile.write(json.dumps(board))
      
      window.destroy()

      if turn == "X":
         main("O")
      else:
         main("X")


def main(turn):
   root = Tk()
   root.geometry("800x800")
   root.configure(bg='white')
   root.title(f"It's {turn}'s Turn!")

   image = Image.open("Title.jpg")
   TitleImage = ImageTk.PhotoImage(image)
   Title = Label(image=TitleImage,bd=0)
   Title.image = TitleImage
   Title.pack()

   MainFrame = Frame(root,bg='white',width='612',height='612')
   MainFrame.pack(pady='40')
   Blank = PhotoImage(file='Blank.png')
   X = PhotoImage(file='X.png')
   O = PhotoImage(file='O.png')

   jsonFile = open("BoardInfo.json", "r+")
   board = json.load(jsonFile)

   index = 1
   for row in range(3):
      row += 1
      for column in range(3):
         column += 1
         key = f'{row}-{column}'
         if board[key] == "Blank": 
            ButtonImage = Blank
         elif board[key] =="X":
            ButtonImage = X
         elif board[key] == "O":
            ButtonImage = O
         window = root
         button = Button(MainFrame,bg="white",bd='1',image=ButtonImage, height=160,width=160,command=lambda key=key: Logic(key,turn,root))
         button.grid(row=row,column=column)


   #check if won
   def Check(BlankCount):
      won = "Nope"
     
      #rows
      for i in range(3):
         i += 1
         if board[f"{i}-1"] == board[f"{i}-2"] and board[f"{i}-2"] == board[f"{i}-3"] and board[f"{i}-1"] != "Blank":
            won = board[f"{i}-{1}"]
    
      #columns
      for i in range(3):
         i += 1
         if board[f"1-{i}"] == board[f"2-{i}"] and board[f"2-{i}"] == board[f"3-{i}"] and board[f"1-{i}"] != "Blank" :
            won = board[f"1-{i}"] 

      #diagnal
      if board["1-1"] == board["2-2"] and board["2-2"] == board["3-3"] and board["1-1"] != "Blank":
         won = board["1-1"]
      if board["1-3"] == board["2-2"] and board["2-2"] == board["3-1"] and board["1-3"] != "Blank":
         won = board["1-3"] 


      if won != "Nope":
         messagebox.showinfo("showinfo", f"{won} won!!!")


      else:
         if BlankCount == 0:
            messagebox.showinfo("showinfo", "It's a Tie!!!")




   BlankCount = 0
   for value in board:
      if board[value] == "Blank":
         BlankCount += 1

   if BlankCount != 9: 
      Check(BlankCount)




   root.mainloop()




main("X")










