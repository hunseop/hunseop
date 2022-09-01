from tkinter import *

root = Tk()
root.title("hunseop GUI")
root.geometry("640x480+500+200") # 가로 * 세로 + x좌표 + y좌표

Label1 = Label(root, text="안녕하세요")
Label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
Label2 = Label(root, image=photo)
Label2.pack()

def change():
    Label1.config(text="또 만나요")
    global photo2
    photo2 = PhotoImage(file="gui_basic/img2.png")
    Label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()