import sys
sys.path.append('D:/02_Programming/Python/pythonRecipes')
import trie
import ipaddress
import time
import pandas as pd
from tqdm import tqdm
import os, csv

start_time = time.time()
path = 'D:/02_Programming/Python/find_ip_in_list/'
checklist_file = path + 'range.csv'
policy_file = path + 'ips.csv'
result_file = path + 'find_result_1.csv'
policy_list = []

def create_list_as_file(fileName):
    with open(fileName, mode='r') as lines:
        result = [ line.rstrip('\n') for line in lines ]
        
    return result

def create_trie_as_list(trieName, listName):
    for data in listName:
        trieName.insert(data)

def find_match_ip(ip, network_list):
    for network in network_list:
        match = ipaddress.ip_address(ip) in ipaddress.ip_network(network)
        if match:
            return ip, network
    
    return False

function_start_time = time.time()
checklist_trie = trie.Trie()
create_trie_as_list(checklist_trie, create_list_as_file(checklist_file))
print(f'Checklist loading complete! [{round((time.time() - function_start_time),2)}s]')

function_start_time = time.time()
policy_table = pd.read_csv(policy_file, header=None)
rule_list = []
target_list = []

for row_index, row in policy_table.iterrows():
    rule_list.append(row.loc[0].replace(' ',''))
    target_list.append(row.loc[1].replace(' ',''))
print(f'Policy file loading complete! [{round((time.time() - function_start_time),2)}s]')

with open(result_file, mode='w', newline='') as f:
    wr = csv.writer(f)
    match_count = 0
    count = 0
    for target in tqdm(target_list, desc="Searching Progress"):
        count += 1
        class_a = target.split('.')[0]+'.'
        a_checkList = checklist_trie.starts_with(class_a)
        
        if a_checkList:
            match = find_match_ip(target, a_checkList)
            if match:
                match_count += 1
                wr.writerow(match)

print('')
print('[Result]')
print(f'Matched count : {match_count}')
print(f'Total time : {round((time.time() - start_time),2)}s')
os.system('pause')