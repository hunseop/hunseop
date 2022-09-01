import os.path
import csv

TARGET_FILE = '.\\submission.txt'   # 추출되는 파일(고정)

# 파일 검사
if os.path.isfile(TARGET_FILE)==False:
  print("The file does not exist.")
  print("Program exit...")
  exit()

with open(TARGET_FILE, 'r') as file:    #  파일을 읽기 모드(r)로 열기
    lines = file.readlines()

#각 나타낼 결과값을 리스트로 선언
date=list()
start_time=list()
end_time=list()
submission=list()
rate=list()

#한줄 씩 검증하면서 추출
for i in lines:
    if 'Cumulative Stats in timespan' in i:
        date.append(i.split(' ')[4])
        start_time.append(i.split(' ')[5])
        end_time.append(i.split(' ')[8].rstrip('\n'))
    elif 'Submissions                                       ' in i:
        submission.append(i.split(':')[1].replace(" ",""))
        rate.append(i.split(':')[2].replace(" ","").rstrip('\n'))

def export_csv (boolen):
    
    if boolen == True:
        mode = 'a'
    else:
        mode = 'w'

    f = open('Submission_Result.csv', mode, newline='')
    wr = csv.writer(f)
    if boolen == False:
        wr.writerow(['Date','Start Time','End Time','Submissions', 'Rate'])

    for j in range(0,len(date)):
        wr.writerow([date[j], start_time[j], end_time[j], submission[j], rate[j]])

    print("Export is complete.")

    f.close()

# 파일 검사
if os.path.isfile('.\\Submission_Result.csv'):
    export_csv(True)
else:
    export_csv(False)
