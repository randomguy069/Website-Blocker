#to edit host files in windows - C:\Windows\System32\drivers\etc
#host file in Mac/Linux - /etc/hosts
#use cron to schedule running this script in mac/linux and use task scheduler to schedule running this script in windows machine. 
# use this link to know how to schedule on windows -> https://stackoverflow.com/questions/44727232/scheduling-a-py-file-on-task-scheduler-in-windows-10

from datetime import datetime as dt #import datetime as dat
hosts_temp = "hosts"
host_path = "C:\Windows\System32\drivers\etc\hosts" #source path of hosts # host_path = "/etc/hosts" in mac/linux
redirect = "127.0.0.1" #localhost ip
print(dt.now())
website_list = ["www.facebook.com","facebook.com","www.goal.com","goal.com"] #add site names you want to block in a list
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,00) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,12): #comparing hours
        print("Working hours")
        with open(host_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass #do nothing
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        with open(host_path,'r+') as file:
            content =  file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list): #searching for the website name from the website list if it is present in every line
                    file.write(line)
                file.truncate() #what does truncate do?
        print("Sleeping hours")
    time.sleep(5)
