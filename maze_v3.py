from tkinter import *
#from Oxygen import *

root=Tk()
root.title("Asteroid Course")
root.config(background="black")
root.resizable(0,0)

def checkAnswers():
    try:
        if(chall3.get("1.0","end-1c")=="c"):
            BlastOff()
            ALERT()
        elif(chall2.get("1.0","end-1c")=="b"):
            BlastOff()
            chall3.config(state=NORMAL)
            chall2.delete('1.0',END)
            chall2.config(state=DISABLED)
            check.grid(row=7,column=10)
        elif(chall1.get("1.0","end-1c")=="a"):
            BlastOff()
            chall2.config(state=NORMAL)
            chall1.delete('1.0',END)
            chall1.config(state=DISABLED)
            check.grid(row=6,column=10)
    except:
        return
        

def BlastOff():
    print("Lift off!")
    #goBot()

def ALERT():
    ALERT=Tk()
    ALERT.geometry("1280x100")
    ALERT.title("Space Console")
    ALERT.config(bg="red")
    text=Label(ALERT,fg="black",bg="red",text="ERROR: OXYGEN TANK MALFUNCTIONING",font=("Comic Sans",40))
    text.pack()
##    img=PhotoImage(file="hazard.jpeg",width=300, height=100)
##    imgDisplay=Label(image=img)
##    imgDisplay.image=img
##    imgDisplay.pack()
    ALERT.resizable(0,0)
    ALERT.mainloop()
    

top=Label(root, text="Input answers here",font=("Arial",25),background="black", fg="red")
top.grid(row=3,column=9, columnspan=1)
instr=Label(root, text="Check button will move as answers are correct!\nDO NOT PRESS ENTER, CLICK 'CHECK'",font=("Arial",25), background="black", fg="red")
instr.grid(row=4,column=9, columnspan=1)
chall1=Text(root, state=NORMAL, width=65, height=1, background="white",highlightthickness=1)
chall1.grid(row=5, column=9, columnspan=1)
text1=Label(root, text="Challenge 1", background="black",fg="white",font=("Arial",25))
text1.grid(row=5,column=8)
text2=Label(root, text="Challenge 2", background="black",fg="white",font=("Arial",25))
text2.grid(row=6,column=8)
chall2=Text(root, state=DISABLED, width=65, height=1, background="white",highlightthickness=1)
chall2.grid(row=6, column=9, columnspan=1)
text3=Label(root, text="Challenge 3", background="black",fg="white",font=("Arial",25))
text3.grid(row=7,column=8)
chall3=Text(root, state=DISABLED, width=65, height=1, background="white",highlightthickness=1)
chall3.grid(row=7, column=9, columnspan=1)
check=Button(root, text="Check", background="white", width=11, command= lambda:checkAnswers())
check.grid(row=5,column=10)
mainloop()
