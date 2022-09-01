import sys
sys.path.append('D:/02_Programming/Python/pythonRecipes')
import trie
import ipaddress
import time
import pandas as pd
from tqdm import tqdm
import os
import csv

start_time = time.time()
path = 'D:/02_Programming/Python/find_ip_in_list/'
checklist_file = path + 'range.csv'
policy_file = path + 'ips.csv'
result_file = path + 'find_result_2.csv'
policy_list = []

def create_list_as_file(file_name):
    with open(file_name, mode='r') as lines:
        result = [ line.rstrip('\n') for line in lines ]
        
    return result

def create_trie_as_list(trie_name, list_name):
    for data in list_name:
        trie_name.insert(data)

def find_match_ip(ip, network_list):
    for network in network_list:
        match = ipaddress.ip_address(ip) in ipaddress.ip_network(network)
        if match:
            return match, network
    
    return False

function_start_time = time.time()
checklist_trie = trie.Trie()
checklist = create_list_as_file(checklist_file)
create_trie_as_list(checklist_trie, checklist)
print(f'Checklist loading complete! [{round((time.time() - function_start_time),2)}s]')

function_start_time = time.time()
policy_table = pd.read_csv(policy_file, header=None)
target_trie = trie.Trie()

target_dict = {}
for row_index, row in policy_table.iterrows():
    rule_name = row.loc[0].replace(' ','')
    target_list = row.loc[1].replace(' ','')
    target_dict[rule_name] = target_list
    target_trie.insert(target_list)

print(f'Policy file loading complete! [{round((time.time() - function_start_time),2)}s]')

match_count = 0

for i in target_dict:
    print(i)

# i = '11.0.0.0/8'
# netmask = int(i.split('/')[1])

# if netmask >=24:
#     network_range = str(i.split('.')[0])+"."+str(i.split('.')[1])+"."+str(i.split('.')[2])+"."
#     result = target_trie.starts_with(network_range)

# elif netmask >=16:
#     network_range = str(i.split('.')[0])+"."+str(i.split('.')[1])+"."
#     result = target_trie.starts_with(network_range)

# elif netmask >=8:
#     network_range = str(i.split('.')[0])+"."
#     result = target_trie.starts_with(network_range)


print('')
print('[Result]')
print(f'Matched count : {match_count}')
print(f'Total time : {round((time.time() - start_time),2)}s')
os.system('pause')