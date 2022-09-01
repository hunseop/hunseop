rule_dict = {'rule_1':['192.168.1.1','192.168.1.2','192.168.1.3'],'rule_2':['192.168.1.4','192.168.1.3','192.168.1.6'], 'rule_3':'192.168.1.3'}

list_of_key = list(rule_dict.keys())
list_of_value = list(rule_dict.values())

# print(list_of_key)
# print(list_of_value)

search = '192.168.1.3'
for key, values in rule_dict.items():
    if type(values) is list:
        if search in values:
            print(key)
    else:
        if search == values:
            print(key)