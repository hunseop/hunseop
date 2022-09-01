import csv, ipaddress, time, re
import pandas as pd

start_time = time.time()    # set start time
range_file = 'D:/02_Programming/Python/find_ip_in_list/range.csv'

def range_to_dict(range_list):
    x = dict()
    for row in range_list:
        ip_range = row.strip('\n')
        class_a = ip_range.split('.')[0]
        x.setdefault(class_a)

        if ip_range.startswith(class_a):
            if x[class_a] is None:
                x[class_a] = [ip_range]
            else:
                temp_list = []
                temp_list = x[class_a]
                temp_list.append(ip_range)
                x[class_a] = temp_list

    return x

with open(range_file, mode='r') as f:
    result = range_to_dict(f)

print(result)
print(f'time : {time.time() - start_time}') # 현재시각 - 시작시간 = 실행 시간