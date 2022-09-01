import csv, ipaddress, time, re
import pandas as pd

start_time = time.time()    # set start time

policy_file = 'D:/02_Programming/Python/find_ip_in_list/ips.csv'
range_file = 'D:/02_Programming/Python/find_ip_in_list/range.csv'
result_file = 'D:/02_Programming/Python/find_ip_in_list/result.csv'
range_list = []

# function
def expand_ip_range(start_ip, end_ip):
    start = ipaddress.IPv4Address(start_ip)
    end = ipaddress.IPv4Address(end_ip)
    ip_list = [str(ipaddress.IPv4Address(int_ip)) for int_ip in range(int(start)+1, int(end)+1)]
    
    return ip_list

def get_ip_from_subnet(ip_subnet):
    ips = ipaddress.ip_network(ip_subnet)
    ip_list = [str(ip) for ip in ips]
    
    return ip_list

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
    
# read policy file
policy_table = pd.read_csv(policy_file, header=None)
rule_list = []
target_list = []

for row_index, row in policy_table.iterrows():
    rule_list.append(row.loc[0].replace(' ',''))

for row_index, row in policy_table.iterrows():
    target_list.append(row.loc[1].replace(' ',''))

# read range file
with open(range_file, mode='r') as f:
    range_dict = range_to_dict(f)
    # for row in f:
    #     range_list.append(row.rstrip('\n'))    # delete newline

# start search
with open(result_file, mode='w', newline='') as result: # CSV 파일에 결과 저장
    wr = csv.writer(result)
    wr.writerow(['Rule', 'Matched', 'Mismatched', 'Unknown'])
    for rule_number in range(0,len(target_list)):
        ip_in_cell = target_list[rule_number].split(',')
        matched = []    # save matched/mismatched ip list
        mismatched = []
        unknown = []

        for single_ip in ip_in_cell:
            progress = str(round(rule_number/len(rule_list)*100,0))    # search progress    
            match_state = False    # Initialize Match Status
            
            # find 'Any' object
            if single_ip == '0.0.0.0-255.255.255.255' or single_ip == 'Any':
                match_state = True
                matched.append(single_ip)
                print(f'[{progress}%][{rule_list[rule_number]}]{single_ip}-Any-True')
                
            # 2. find group object
            elif re.findall (r'[A-Za-z]', single_ip):
                unknown.append(single_ip)
                print(f'[{progress}%][{rule_list[rule_number]}]{single_ip}-Unknown-Unknown')

            # 3. find subnet range object
            elif '_' in single_ip or '/' in single_ip:
                conv_single_ip = single_ip.replace('_', '/')
                if conv_single_ip in range_list:
                    match_state = True
                    matched.append(single_ip)
                    print(f'[{progress}%][{rule_list[rule_number]}]{conv_single_ip}-{conv_single_ip}-True')
                    break
                
                else:
                    ips = get_ip_from_subnet(conv_single_ip)
                    for ip in ips:
                        for ip_range in range_list:
                            ### matching algorithm here ###
                            match = ipaddress.ip_address(single_ip) in ipaddress.ip_network(ip_range) # 하나씩 비교하기
                            if match:
                                match_state = True
                                matched.append(conv_single_ip)
                                print(f'[{progress}%][{rule_list[rule_number]}]{conv_single_ip}-{ip_range}-True')
                                break
            
            # 4. find range object
            elif '-' in single_ip:
                start = single_ip.split('-')[0]
                end = single_ip.split('-')[1]
                ips = expand_ip_range(start, end)
                for ip in ips:
                    for ip_range in range_list:
                        ### matching algorithm here ###
                        match = ipaddress.ip_address(single_ip) in ipaddress.ip_network(ip_range) # 하나씩 비교하기
                        if match:
                            match_state = True
                            matched.append(single_ip)
                            print(f'[{progress}%][{rule_list[rule_number]}]{single_ip}-{ip_range}-True')
                            break
        
            # 5. find single object
            else:
                try:
                    key = single_ip.split('.')[0]
                    if key in range_dict:
                        for ip_range in range_dict[key]:
                            match = ipaddress.ip_address(single_ip) in ipaddress.ip_network(ip_range) # 하나씩 비교하기
                            if match:
                                match_state = True
                                matched.append(single_ip)
                                print(f'[{progress}%][{rule_list[rule_number]}]{single_ip}-{ip_range}-True')
                                break

                    # for ip_range in range_list:
                    # ### matching algorithm here ###
                    #     match = ipaddress.ip_address(single_ip) in ipaddress.ip_network(ip_range) # 하나씩 비교하기
                    #     if match:
                    #         match_state = True
                    #         matched.append(single_ip)
                    #         print(f'[{progress}%][{rule_list[rule_number]}]{single_ip}-{ip_range}-True')
                    #         break
                    
                except:
                    unknown.append(single_ip)
                    print(f'[{progress}%][{rule_list[rule_number]}]{single_ip}-Unknown-Unknown')                

            if match_state == False:
                mismatched.append(single_ip)
                print(f'[{progress}%][{rule_list[rule_number]}]{single_ip}-False-False')
                
        wr.writerow([rule_list[rule_number], matched, mismatched, unknown])
        
print(f'time : {time.time() - start_time}') # 현재시각 - 시작시간 = 실행 시간