import random
from itertools import count
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import datetime

plt.style.use('fivethirtyeight')

def now():
    return datetime.datetime.now().strftime("%X")

x_vals = []
y1_vals = []
y2_vals = []
y3_vals = []
y4_vals = []
y5_vals = []
y6_vals = []
y7_vals = []
y8_vals = []
y9_vals = []
y10_vals = []
y11_vals = []
y12_vals = []
y13_vals = []
y14_vals = []
y15_vals = []
y16_vals = []
y17_vals = []
y18_vals = []
y19_vals = []
y20_vals = []
y21_vals = []
y22_vals = []
y23_vals = []
y24_vals = []

frame_len = 200
fig = plt.figure(figsize=(10, 5))

def animate(i):
    x_vals.append(now())
    y1_vals.append(random.randint(0, 10000))
    y2_vals.append(random.randint(0, 10000))
    y3_vals.append(random.randint(0, 10000))
    y4_vals.append(random.randint(0, 10000))
    y5_vals.append(random.randint(0, 10000))
    y6_vals.append(random.randint(0, 10000))
    y7_vals.append(random.randint(0, 10000))
    y8_vals.append(random.randint(0, 10000))
    y9_vals.append(random.randint(0, 10000))
    y10_vals.append(random.randint(0, 10000))
    y11_vals.append(random.randint(0, 10000))
    y12_vals.append(random.randint(0, 10000))
    y13_vals.append(random.randint(0, 10000))
    y14_vals.append(random.randint(0, 10000))
    y15_vals.append(random.randint(0, 10000))
    y16_vals.append(random.randint(0, 10000))
    y17_vals.append(random.randint(0, 10000))
    y18_vals.append(random.randint(0, 10000))
    y19_vals.append(random.randint(0, 10000))
    y20_vals.append(random.randint(0, 10000))    
    y21_vals.append(random.randint(0, 10000))
    y22_vals.append(random.randint(0, 10000))
    y23_vals.append(random.randint(0, 10000))
    y24_vals.append(random.randint(0, 10000))

    if len(y1_vals) <= frame_len:
        plt.cla()
        plt.plot(x_vals, y1_vals, label='proxy 1')
        plt.plot(x_vals, y2_vals, label='proxy 2')
        plt.plot(x_vals, y3_vals, label='proxy 3')
        plt.plot(x_vals, y4_vals, label='proxy 4')
        plt.plot(x_vals, y5_vals, label='proxy 5')
        plt.plot(x_vals, y6_vals, label='proxy 6')
        plt.plot(x_vals, y7_vals, label='proxy 7')
        plt.plot(x_vals, y8_vals, label='proxy 8')
        plt.plot(x_vals, y9_vals, label='proxy 9')
        plt.plot(x_vals, y10_vals, label='proxy 10')
        plt.plot(x_vals, y11_vals, label='proxy 11')
        plt.plot(x_vals, y12_vals, label='proxy 12')
        plt.plot(x_vals, y13_vals, label='proxy 13')
        plt.plot(x_vals, y14_vals, label='proxy 14')
        plt.plot(x_vals, y15_vals, label='proxy 15')
        plt.plot(x_vals, y16_vals, label='proxy 16')
        plt.plot(x_vals, y17_vals, label='proxy 17')
        plt.plot(x_vals, y18_vals, label='proxy 18')
        plt.plot(x_vals, y19_vals, label='proxy 19')
        plt.plot(x_vals, y20_vals, label='proxy 20')
        plt.plot(x_vals, y21_vals, label='proxy 21')
        plt.plot(x_vals, y22_vals, label='proxy 22')
        plt.plot(x_vals, y23_vals, label='proxy 23')
        plt.plot(x_vals, y24_vals, label='proxy 24')

    else:
        plt.cla()
        plt.plot(x_vals, y1_vals[-frame_len:], label='proxy 1')
        plt.plot(x_vals, y2_vals[-frame_len:], label='proxy 2')
        plt.plot(x_vals, y3_vals[-frame_len:], label='proxy 3')
        plt.plot(x_vals, y4_vals[-frame_len:], label='proxy 4')
        plt.plot(x_vals, y5_vals[-frame_len:], label='proxy 5')
        plt.plot(x_vals, y6_vals[-frame_len:], label='proxy 6')
        plt.plot(x_vals, y7_vals[-frame_len:], label='proxy 7')
        plt.plot(x_vals, y8_vals[-frame_len:], label='proxy 8')
        plt.plot(x_vals, y9_vals[-frame_len:], label='proxy 9')
        plt.plot(x_vals, y10_vals[-frame_len:], label='proxy 10')
        plt.plot(x_vals, y11_vals[-frame_len:], label='proxy 11')
        plt.plot(x_vals, y12_vals[-frame_len:], label='proxy 12')
        plt.plot(x_vals, y13_vals[-frame_len:], label='proxy 13')
        plt.plot(x_vals, y14_vals[-frame_len:], label='proxy 14')
        plt.plot(x_vals, y15_vals[-frame_len:], label='proxy 15')
        plt.plot(x_vals, y16_vals[-frame_len:], label='proxy 16')
        plt.plot(x_vals, y17_vals[-frame_len:], label='proxy 17')
        plt.plot(x_vals, y18_vals[-frame_len:], label='proxy 18')
        plt.plot(x_vals, y19_vals[-frame_len:], label='proxy 19')
        plt.plot(x_vals, y20_vals[-frame_len:], label='proxy 20')
        plt.plot(x_vals, y21_vals[-frame_len:], label='proxy 21')
        plt.plot(x_vals, y22_vals[-frame_len:], label='proxy 22')
        plt.plot(x_vals, y23_vals[-frame_len:], label='proxy 23')
        plt.plot(x_vals, y24_vals[-frame_len:], label='proxy 24')
    
    plt.xlabel('Time (s)')
    plt.ylabel('Traffic (bytes)')
    plt.legend(loc='upper right')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.show()