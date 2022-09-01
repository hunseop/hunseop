import pandas as pd
import os.path

# 변환할 파일명 입력
file_name = input("Filename : ")
file = '.\\'+file_name+'.xlsx'     # 대상 파일 디렉토리

# 파일 검사
if os.path.isfile(file):
  print("Start applications split")
else :
  print("The file does not exist.")
  print("Program exit...")
  exit()

# 어플리케이션 중복 제거
Total_df = pd.read_excel(file) # 파일 불러오기
uq_app = Total_df['application'].drop_duplicates()

# 어플리케이션 별로 시트 생성
for i in uq_app:
    app = Total_df[Total_df['application'] == i]
    with pd.ExcelWriter(file, mode='a', engine='openpyxl') as writer:
        app.to_excel(writer, index=False, sheet_name=i)

print("Split is complete!!")