import os,signal
import subprocess
import cv2

data="gnome-terminal"
def launch_app(data):
    try:
        os.system(data)
    except:
        pass
def take_picture():
    cap=cv2.VideoCapture(0)
    while True:
        ret,img=cap.read()
        cv2.imshow('img',img)
        if cv2.waitKey(1) & 0xFF==ord('s'):
            cv2.imwrite('picture.png',img)
            break
        elif cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def close_application(data):
    try:
        pid=os.popen(f"pidof {data}").read().strip()
        os.system(f"kill -9 {pid}")
    except:
        error_message="No such applicatin is running"
        return error_message

def shutdown():
    os.system("shutdown now")

def restart():
    os.system("reboot")

def manual(command):
    os.system(f'man {command} > output.txt' )

def createuser(username):
    try:
        os.system(f"sudo useradd -m {username}")
    except:
        return f"{username} already exist"

def delete_user(username):
    os.system(f'sudo userdel -rfRZ {username}')

def change_password(username,password):
    try:
        os.system(f"echo '{username}:{password}'| sudo chpasswd")
    except:
        return "no such user is present "

def create_directories(path):
    cwd=os.getcwd()
    user_dir=f"{cwd}/{path}"
    os.makedirs(user_dir,exist_ok=True)

def create_files(filename):
    try:
        cwd=os.getcwd()
        file_path=f"{cwd}/{filename}.txt"
        subprocess.run(["touch",file_path])
    except:
        pass

def delete_files(filename):
    try:
        cwd=os.getcwd()
        file_path=f"{cwd}/{filename}.txt"
        os.system(f'rm {file_path}')
    except:
        return "No such file present"

def change_directories(directory):
    while True:
        cwd=os.getcwd()
        os.system("ls > test.txt")
        files=open('test.txt','r')
        files_contents=files.read()
        if directory in files_contents:
            os.chdir(directory)
            print(os.getcwd())
            break
        else:
            os.chdir("..")
            cwd=os.getcwd()
            os.system("ls > test1.txt")
            files=open('test1.txt','r')
            files_contents=files.read()
            if directory in files_contents:
                os.chdir(directory)
                print(os.getcwd())
                break              
#change_directories('Intent_classification')


if __name__=="_main_":
    shutdown()
    restart()
    close_application(data)
    launch_app(data)
    manual("mkdir")
    change_directories()
    create_files()
    createuser()
    take_picture()
