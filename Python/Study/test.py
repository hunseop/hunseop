import csv, ipaddress

# 변수
ip_file = 'D:/02_Programming/Python/Study/ip.csv'
range_file = 'D:/02_Programming/Python/Study/range.csv'
result_file = 'D:/02_Programming/Python/Study/result.csv'
range_list = []

# 대역 불러오기
with open(range_file, mode='r') as f:
    for row in f:
        range_list.append(row.rstrip('\n')) # 개행 제거 후 리스트에 저장

with open(result_file, mode='w', newline='') as result: # CSV 파일에 결과 저장
    wr = csv.writer(result)
    with open(ip_file, mode='r') as f:  # IP 리스트 불러오기
        for ip in f:
            ip = ip.replace('\n', '')   # 개행 제거
            for range in range_list:
                match = ipaddress.ip_address(ip) in ipaddress.ip_network(range) # 하나씩 비교하기
                if match:   # 매치되면 결과 출력 및 저장
                    print(ip+' - '+range+' - True')
                    wr.writerow([ip,range,"True"])
                    break   # 매치되면 다음 비교
                else:
                    print(ip+' - '+range+' - False')
                    #wr.writerow([ip,range,"False"])