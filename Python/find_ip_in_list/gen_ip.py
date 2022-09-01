import random, csv

num = 0
with open('D:/02_Programming/Python/find_ip_in_list/ips.csv', mode='w', newline='') as f:
    wr = csv.writer(f)
    while num < 100000:
        a = random.randrange(10,192)
        b = random.randrange(1,255)
        c = random.randrange(1,255)
        d = random.randrange(1,255)
        ip = str(f'{a}.{b}.{c}.{d}')
        rule = 'rule_'+str(num)
        wr.writerow([rule, ip])
        num += 1