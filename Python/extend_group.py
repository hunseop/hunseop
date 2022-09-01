import re

groups=[
    ['A',['10.191.10.3','10.191.10.4','10.191.10.5','10.191.10.6-10.191.11.6']],
    ['B',['10.191.10.7','A','10.191.10.0/24']],
    ['C',['10.191.10.9','A','10.191.20.0/32','B']]
]

regex_ip = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
regex_ip_range = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])-((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
regex_ip_netmask = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])/(3[0-2]|2[0-9]|1[0-9]|[1-9])$"

val_state=True
max_loop=0
while val_state and max_loop < 10:
    val_state=False

    for i in range(0,len(groups)):
        for j in groups[i][1]:
            if not(re.search(regex_ip, j) or re.search(regex_ip_range, j) or re.search(regex_ip_netmask, j)):
                for k in groups:
                    if j == k[0]:
                        groups[i][1].remove(j)
                        groups[i][1].extend(k[1])
                val_state=True
    max_loop += 1
    print(max_loop)

for i in groups:
    print(i)