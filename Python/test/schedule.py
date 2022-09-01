# # 사용방법

# # 스케줄 종류에는 여러가지가 있는데 대표적으로 BlockingScheduler, BackgroundScheduler 입니다
# # BlockingScheduler 는 단일수행에, BackgroundScheduler은 다수 수행에 사용됩니다.
# # 여기서는 BackgroundScheduler 를 사용하겠습니다.
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.jobstores.base import JobLookupError
# import time


# def job():
#     print("I'm working...", "| [time] "
#           , str(time.localtime().tm_hour) + ":"
#           + str(time.localtime().tm_min) + ":"
#           + str(time.localtime().tm_sec))

# # BackgroundScheduler 를 사용하면 stat를 먼저 하고 add_job 을 이용해 수행할 것을 등록해줍니다.
# sched = BackgroundScheduler()
# sched.start()

# # cron 사용 - 매 5초마다 job 실행
# # 	: id 는 고유 수행번호로 겹치면 수행되지 않습니다.
# # 	만약 겹치면 다음의 에러 발생 => 'Job identifier (test_1) conflicts with an existing job'
# sched.add_job(job, 'cron', minute='*', id="test_1")

# # 반복문에서 시간이 지나면 job 을 지워주는 코드를 넣어줍니다.
# count = 0
# while True:
#     print("Running main process...............")
#     time.sleep(1)
#     count += 1
#     if count == 10:
#         sched.remove_job("test_1")
#         print("jobs done")
#         exit()

import psutil,time, datetime, os

def findProcessIdByName(processName):
    '''
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    '''
    listOfProcessObjects = []
    #Iterate over the all the running process
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           # Check if process name contains the given name string.
           if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
    return listOfProcessObjects

# Find PIDs od all the running instances of process that contains 'chrome' in it's name
listOfProcessIds = findProcessIdByName('chrome')
currentTime = datetime.datetime.now()

if len(listOfProcessIds) > 0:
   print('Process Exists | PID and other details are')
   for elem in listOfProcessIds:
       processID = elem['pid']
       processName = elem['name']
       # processCreationTime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(elem['create_time']))
       processCreationTime = elem['create_time']
       timestamp = datetime.datetime.fromtimestamp(processCreationTime)
       durationTime = (currentTime - timestamp)
       if durationTime > datetime.timedelta(minutes=15):
           print(f'{processID} - {processName} ({durationTime}) process terminated...')
           #os.kill(processID, 9)   
       
else :
   print('No Running Process found with given text')