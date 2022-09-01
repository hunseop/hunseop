import random, os, time
import numpy as np
import matplotlib.pyplot as plt

def get_traffic_values():
    http_traffic = []
    https_traffic = []
    ftp_traffic = []

    for i in range(1,25):
        http_traffic.append(random.randrange(10000,100000))
        https_traffic.append(random.randrange(10000,100000))
        ftp_traffic.append(random.randrange(10,1000))
    
    return http_traffic, https_traffic, ftp_traffic

update = 0
while True:
    os.system('cls')
    update += 1
    print(f'{update} 번째...')

    http_traffic, https_traffic, ftp_traffic = get_traffic_values()
    
    for i in range(0, len(http_traffic)):
        print(f'{i + 1} : {http_traffic[i]} - {https_traffic[i]} - {ftp_traffic[i]}')

    time.sleep(5)
