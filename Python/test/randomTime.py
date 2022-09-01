import datetime, csv, random

def get_now_date():
    currentTime = datetime.datetime.now().strftime("%Y/%m/%d %X")
    return currentTime

def create_loading_time(time):
    loading_time = []
    loading_time.append(time)

    for j in range(72):
        for i in range(1,6):
            List = [1, 2, 3, 4, 5, 10]
            weight = random.choices(List, weights=(150, 100, 10, 3, 2, 1), k=1)
            data = i * weight[0]
            loading_time.append(data)
    
    return loading_time

currentTime = datetime.datetime.now()
initTime = currentTime - datetime.timedelta(days=90)

while initTime != currentTime:
    five = initTime + datetime.timedelta(minutes=5)
    initTime = five

    with open("./time_log.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(create_loading_time(initTime))
