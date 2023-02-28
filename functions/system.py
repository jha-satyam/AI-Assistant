import os,signal
import talkback
import subprocess

data="gnome-terminal"

def launch_app(data):
    try:
        os.system(data)
    except:
        pass

def close_application(data):
    try:
        pid=os.popen(f"pidof {data}").read().strip()
        os.system(f"kill -9 {pid}")
    except:
        error_message="No such applicatin is running"
        return error_message

def shutdown():
    talkback.talkback("Shutting down this pc")
    os.system("shutdown now")

def restart():
    talkback.talkback("Restarting the pc")
    os.system("reboot")


def manual(command):
    os.system(f'man {command} > output.txt' )

def createuser(username):
    try:
        os.system(f"sudo useradd -m {username}")
    except:
        return f"{username} already exist"

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
        os.remove(file_path)
    except:
        return "No such file present"

def change_directories(directory):
    try:
        cwd=os.getcwd()
        os.system("ls > test.txt")
        files=open('test.txt','r')
        files_contents=files.read()
        if directory in files_contents:
            os.chdir(directory)
            print(os.getcwd())
        else:
            os.chdir(os.path.expanduser("~"))
            cwd=os.getcwd()
            dirc=f"{cwd}/{directory}"
            os.chdir(dirc)
            print(os.getcwd()) 

        '''elif directory not in files_contents:
            os.chdir("..")
            cwd=os.getcwd()
            dirc=f"{cwd}/{directory}"
            os.chdir(dirc)
            print(os.getcwd())'''                
    except:
        return "No such directory is present"
change_directories("Desktop")

if __name__=="_main_":
    shutdown()
    restart()
    close_application(data)
    launch_app(data)
    manual("mkdir")

