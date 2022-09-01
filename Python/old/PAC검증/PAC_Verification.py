import os
import time

date = time.strftime('%Y%m%d', time.localtime(time.time())) # 날짜

# 검증 대상 PAC
original = "C:/Users/HUN/Desktop/PAC검증/대상파일/og.pac" # 임시
test = "C:/Users/HUN/Desktop/PAC검증/대상파일/test.pac" # 임시
# office = "http://12.30.30.150/office.pac"
# otc = "http://12.30.30.150/otc.pac"
# line = "http://12.30.30.150/line.pac"
# office_test = "http://12.30.30.150/office_test.pac"
# otc_test = "http://12.30.30.150/otc_test.pac"
# line_test = "http://12.30.30.150/line_test.pac"

# 저장 경로 지정
result_path = "C:/Users/HUN/Desktop/PAC검증/대상파일/"
os.chdir(result_path)

def listToString(s, add=''):
    '''리스트 원소를 하나의 문자열로 만듭니다'''
    str = ""
    for ele in s:
        str += ele+add
    return str

# def write_data(data, filename, encoding="utf8"):
#     """쓰기 함수"""
#     with open(filename, 'w', encoding=encoding) as f:
#         f.write(data)

def save_result(data1, data2, filename, encoding="utf8"):
    """결과 저장 함수"""
    addcount = data2.count('\n')
    delcount = data1.count('\n')
    with open(filename, 'w', encoding=encoding) as f:
        f.write("date : "+date+"\n")
        f.write("Added count : "+str(addcount)+"\n")
        f.write("Deleted count : "+str(delcount)+"\n")
        f.write("-----------------------------\n")
        f.write(">> Added list\n")
        f.write(data2)
        f.write(">> Deleted list\n")
        f.write(data1)

def compareFiles(file1, file2):
    onlyFile1 = []
    onlyFile2 = []

    # print("삭제된 내용")
    for file1_line in file1:
        file1_line = file1_line.strip('\n')
        found = False
        for file2_line in file2:
            file2_line = file2_line.strip('\n')
            if file1_line == file2_line:
                found = True
                break
        if not found:
            # print(file1_line)
            onlyFile1.append(file1_line)

    # print("추가된 내용")
    for file2_line in file2:
        file2_line = file2_line.strip('\n')
        found = False
        for file1_line in file1:
            file1_line = file1_line.strip('\n')
            if file2_line == file1_line:
                found = True
                break
        if not found:
            # print(file2_line)
            onlyFile2.append(file2_line)
    
    onlyFile1w = listToString(onlyFile1, '\n')
    onlyFile2w = listToString(onlyFile2, '\n')
    print(onlyFile1w)
    print(onlyFile2w)
    # write_data(onlyFile1w, "onlyFile1.txt")
    # write_data(onlyFile2w, "onlyFile2.txt")
    target = "office"
    save_result(onlyFile1w, onlyFile2w, date+"_"+target+".log")

with open ('test1.txt', mode='r', encoding='utf8') as f:
    file1 = f.readlines()

with open ('test2.txt', mode='r', encoding='utf8') as f:
    file2 = f.readlines()

compareFiles(file1, file2)
