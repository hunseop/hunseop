from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480+500+200") # 가로 * 세로 + x좌표 + y좌표

# 메뉴(Menu)
menu = Menu(root)

def create_new_file():
    txt.delete("1.0", END)
    print("파일생성")

def open_file():
    print("파일열기")
    with open('gui_basic/mynote.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
        s = file.read()                     # 파일에서 문자열 읽기
        txt.

def save_file():
    with open('gui_basic/mynote.txt', 'w') as file:
        s = file.write(txt.get("1.0",END))
    print("파일을 저장했습니다.")

# 파일(F)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="새로 만들기(N)", command=create_new_file)
menu_file.add_command(label="새 창(W)")
menu_file.add_command(label="열기(O)...", command=open_file)
menu_file.add_command(label="저장(S)", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="파일(F)", menu=menu_file)

# 편집(E)
menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="편집(E)")

# 서식(O)
menu_format = Menu(menu, tearoff=0)
menu.add_cascade(label="서식(O)")

# 보기(V)
menu_view = Menu(menu, tearoff=0)
menu.add_cascade(label="보기(V)")

# 도움말(H)
menu_help = Menu(menu, tearoff=0)
menu.add_cascade(label="도움말(H)")


frame = Frame(root)
frame.pack(fill="both", expand=True)

# 스크롤 바
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")


# 텍스트 창
txt = Text(frame, yscrollcommand = scrollbar.set)
txt.pack(side="left", fill="both", expand=True)


scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()