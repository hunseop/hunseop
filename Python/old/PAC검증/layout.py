import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("PAC File Verification")  # 프로그램 제목
root.geometry("640x480") # 가로 * 세로

# 검증 대상 프레임
frame_option = LabelFrame(root, text="검증 대상")
frame_option.pack(fill="x", padx=5, pady=5, ipady=5)

label_target = Label(frame_option, text="대상 선택")
label_target.pack(side="left", padx=5, pady=5)

target = ["오피스","준사내","라인"]
cmb_target = ttk.Combobox(frame_option, values=target, state="readonly", width=15) # 읽기전용
cmb_target.current(0) # 0번째 인덱스 값 선택
cmb_target.pack(side="left", padx=5, pady=5)

# 저장 경로 프레임
frame_path = LabelFrame(root, text="결과 파일 저장 경로")
frame_path.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(frame_path)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경

btn_dest_path = Button(frame_path, text="찾아보기", width=10)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 비교 프레임
frame_compare = LabelFrame(root, text="비교 결과")
frame_compare.pack(fill="both", padx=5, pady=5, ipady=5)

txt_compare11 = Label(frame_compare, text="추가")
txt_compare11.pack(side="left", fill="x")
txt_compare22 = Label(frame_compare, text="삭제")
txt_compare22.pack(side="right", fill="x")

txt_compare1 = Text(frame_compare)
txt_compare1.pack(side="left", fill="both", padx=5, pady=5, ipady=5)

txt_compare2 = Text(frame_compare)
txt_compare2.pack(side="right", fill="both", padx=5, pady=5, ipady=5)

# 시작&종료 버튼 프레임
frame_btn = Frame(root)
frame_btn.pack(fill="both", padx=5, pady=5) # 간격 띄우기

btn_start = Button(frame_btn, padx=5, pady=5, width=15, text="검증 시작")
btn_start.pack(side="left", padx=5, pady=5)

btn_end = Button(frame_btn, padx=5, pady=5, width=15, text="종료")
btn_end.pack(side="right", padx=5, pady=5)

root.mainloop()