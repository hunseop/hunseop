import paramiko
import getpass

def connectServer(server, user, pwd):
    cli = paramiko.SSHClient()
    cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    try:
        cli.connect(server, port=22, username=user, password=pwd)
    except paramiko.ssh_exception.AuthenticationException:
        print("정보를 다시 확인해주세요!")
        quit()
    except TimeoutError:
        print("서버와의 연결을 확인해주세요!")
        quit()
    except:
        print("Error!!")
        quit()
        
    stdin, stdout, stderr = cli.exec_command("ls -la")
    lines = stdout.readlines()
    print(''.join(lines))
    
    cli.close()

server = input("Server: ")  # 호스트명이나 IP 주소
user = input("Username: ")  
pwd = getpass.getpass("Password: ") # 암호입력 숨김

connectServer(server, user, pwd)

print("프로그램이 끝났습니다.")