'''
'''

import os
import psutil
import sys
import time
import schedule
import smtplib
from email.message import EmailMessage

#Periodic email reporting

def SendMail(logfile,receiver_email,Data):

    sender_email = "nilapwarmitali@gmail.com"
    sender_password = "pfwl kyuo konn hpea"

    msg = EmailMessage()
    msg["Subject"] = "Platform Surveillance System Report"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    #Summary
    total_processes = len(Data)

    #Top CPU
    top_cpu = sorted(Data,key= lambda x: x.get("cpu_percent",0), reverse = True)

    #Top Memory
    top_mem = sorted(Data,key= lambda x: x.get("memory_percent",0), reverse = True)

    #Top threads
    top_threads = sorted(Data,key= lambda x: x.get("threads",0), reverse = True)

    #Top Open files
    def safe_open_files(x):
        return x.get("open_files") if isinstance(x.get("open_files"),int) else 0
    
    top_files = sorted(Data, key= safe_open_files,reverse=True)[:5]

    body = f"""
Platform Surveillance Report

Total processes : {total_processes}

Top CPU Processes:
"""
    for p in top_cpu:
        body+= f"{p['name']} (PID {p['pid']}) -> {p['cpu_percent']}%\n"

    body += "\nTop Memory Processes: \n"
    for p in top_mem:
        body += f"{p['name']} (PID {p['pid']}) -> {p['memory_percent']}%\n"

    body += "\nTop Thread Processes:\n"
    for p in top_threads:
        body += f"{p['name']} (PID {p['pid']}) -> {p['threads']}\n"

    body += "\nTop Open File Processes:\n"
    for p in top_files:
        body += f"{p['name']} (PID {p['pid']}) -> {p['open_files']}\n"

    msg.set_content(body)

    #Attach logfile
    with open(logfile,"rb") as f:
        file_data = f.read()
        file_name = os.path.basename(logfile)

    msg.add_attachment(file_data,
                       maintype="applicatiomn",
                       subtype="octet-stream",
                       filename=file_name
                       )
    
    #Send mail
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(sender_email,sender_password)
        smtp.send_message(msg)

    print("Email sent successfully!")


  
def CreateLog(FolderName,receiver_email=None):
    Border = "-"*50

    Ret = False
    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create folder")
            return
    
    else:
        os.mkdir(FolderName)
        print("Directory for log files gets created successfully")

    #Timestamp based log filename
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName,"Surveillance_%s.log" %timestamp)
    print("Log file gets created with name : ", FileName)

    fobj= open(FileName,"w")
    fobj.write(Border + "\n")
    fobj.write("-----Marvellous Platform Surveillance System------\n")
    fobj.write("Log Created at : "+ time.ctime() + "\n")
    fobj.write(Border + "\n\n")

    fobj.write("------------------System Report---------------------\n")

    #CPU
    #print("CPU Usage : ", psutil.cpu_percent())
    fobj.write("CPU Usage :%s %%\n" %psutil.cpu_percent())
    fobj.write(Border + "\n")

    #RAM
    mem = psutil.virtual_memory()
    #print("RAM usage:  ", mem.percent)
    fobj.write("RAM Usage :%s %%\n" %mem.percent)
    fobj.write(Border + "\n")

    #Disk
    fobj.write("\nDisk Usage Report : \n")

    fobj.write(Border + "\n")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
               # print(f"{part.mountpoint} used {usage.percent}%%")
            fobj.write("%s -> %s %% used\n "%(part.mountpoint,usage.percent))
        except:
            pass
    fobj.write(Border + "\n")

    
    net = psutil.net_io_counters()
    fobj.write("\nNetwork Usage Report\n")
    fobj.write("Sent : %.2f MB\n" %(net.bytes_sent/(1024*1024)))
    fobj.write("Recv : %.2f MB\n" %(net.bytes_recv/(1024*1024)))
    fobj.write(Border + "\n")


    #Process LOG
    Data = ProcessScan()

    for info in Data:
        fobj.write("pid : %s\n" %info.get("pid"))
        fobj.write("name : %s\n" %info.get("name"))
        fobj.write("username : %s\n" %info.get("username"))
        fobj.write("status : %s\n" %info.get("status"))
        fobj.write("start time : %s\n" %info.get("create_time"))
        fobj.write("CPU %%: %s\n" %info.get("cpu_percent"))
        fobj.write("Memory %%: %s\n" %info.get("memory_percent"))
        fobj.write("RSS (MB) : %s\n" %info.get("rss"))
        fobj.write("VMS (MB) : %s\n" %info.get("vms"))
        fobj.write("Threads : %s\n" %info.get("threads"))
        fobj.write("Open Files : %s\n" %info.get("open_files"))
        fobj.write("Timestamp : %s\n" %info.get("timestamp"))
        fobj.write(Border + "\n")

    #top 10 memory consuming processes
    fobj.write("================ TOP 10 MEMORY PROCESSES ================\n")

    #filter valid numeric memory%
    valid_processes = [p for p in Data if isinstance(p.get("memory_percent"),float)]

    #sort descending
    top_mem = sorted(valid_processes,
                     key=lambda x: x.get("memory_percent",0),
                     reverse = True )[:10]
    
    for proc in top_mem:
        fobj.write("Name : %s | PID : %s | Memory %% : %.2f | RSS : %s MB\n" %
                   (proc.get("name"),
                    proc.get("pid"),
                    proc.get("memory_percent"),
                    proc.get("rss")))

    fobj.write(Border + "\n")
    fobj.write("----------------End of log file-------------------\n")
    fobj.write(Border + "\n")

    fobj.close()

    if receiver_email:
        SendMail(FileName,receiver_email,Data)

def ProcessScan():
    listprocess = []

    #warm up for CPU percent
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter():  #like walk in os we use, this will iterate over all the processes 
                                                                      #we get after typint talklist on cmd
        try:                                                              
            info= proc.as_dict(attrs=["pid","name","username","status","create_time"])  # Treat it as dictionary
            # convert create time
            try:
                info["create_time"]= time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(info["create_time"]))
            except:
                info["create_time"]= "NA"

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()

            #Thread count
            try:
                info["threads"] = proc.num_threads()
            except:
                info["threads"] = "NA"


            open_files_count = 0
            connections_count = 0
            access_denied = True

            #Open files count
            try:
                files = proc.open_files()
                open_files_count = len(files)
                access_denied = False
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                pass
                
            try:
                conns = proc.net_connections()
                connections_count = len(conns)
                access_denied = False
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                pass

            # Final assignment
            if access_denied:
                info["open_files"] = "Access Denied"
            else:
                info["open_files"] = open_files_count + connections_count
               
            #Actual memory (RSS + VMS)

            try:
                mem_info = proc.memory_info()
                info["rss"] = round(mem_info.rss / (1024 * 1024),2)
                info["vms"] = round(mem_info.vms / (1024 * 1024),2)
            except(psutil.AccessDenied,psutil.NoSuchProcess):
                info["rss"] = "NA"
                info["vms"] = "NA"

            #Timestamp(log time)
            info["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")

            listprocess.append(info)

        except(psutil.NoSuchProcess, psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return listprocess


def main():

    Border = "-"*50
    print(Border)
    print("-----Marvellous Platform Surveillance System------")
    print(Border)


    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]== "--H"):
            print("This script is used to :  ")
            print("1 : Create automatic logs")
            print("2 : Executes periodically")
            print("3 : Sends mail with the log")
            print("4 : Store information about processes")
            print("5 : Store information about CPU")
            print("6 : Store information about RAM usage")
            print("7 : Store information about secondary storage")


        elif(sys.argv[1]=="--u" or sys.argv[1]== "--U"):
            print("Use the automation script as  ")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : the time in minutes for periodic scheduling")
            print("DirectoryName : Name of directory to create auto logs")
            print("\nFor email feature:")
            print("ScriptName.py DirectoryName receiver_email TimeInterval")

        else:
            print("unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
    
    # python Demo.py 5 Marvellous
    elif(len(sys.argv)==3):
        print("Inside projects logic")
        print("time interval : ", sys.argv[1])
        print("Directory name : ", sys.argv[2])

        #Apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog,sys.argv[2])
        
        print("Platform Surveillance System started successfully")
        print("Directory created with name :",sys.argv[2])
        print("Time interval in minutes :", sys.argv[1])
        print("press Ctrl + C to stop the execution.")


        # wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    # EMAIL FEATURE LOGIC
    elif(len(sys.argv)==4):
        FolderName = sys.argv[1]
        receiver_email = sys.argv[2]
        interval = int(sys.argv[3])

        print("Starting Platform Surveillance System with Email Feature...")
        print("Directory:", FolderName)
        print("Receiver Email:", receiver_email)
        print("Interval:", interval, "minutes")

        schedule.every(interval).minutes.do(CreateLog, FolderName, receiver_email)

        print("System started successfully. Press Ctrl + C to stop.")

        while True:
            schedule.run_pending()
            time.sleep(1)
 

    else:
        print("Invalid number of command line arguments.")
        print("unable to proceed as there is no such option.")
        print("Please use --h or --u to get more details.")


    print(Border)
    print("---------Thank you for using our script-----------")
    

if __name__ == "__main__":
    main()


'''
- python Platform_Surveillance_System.py LogFiles mitaliunilapwar@gmail.com 1
'''