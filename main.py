from tkinter import *
window = Tk ()
window.geometry("400x400")
window.config(bg="brown")
window.title("My first GUI application")

my_first_text = Label(window, text ="welcome to my first game", bg= "brown", fg="gold" ,font=("cursive", 20))
my_first_text.pack()

def clk():
    print("you just clicked me")


click = Button(window, text="Click me" , bg="red" ,  command = clk)
click.pack()



window.mainloop()