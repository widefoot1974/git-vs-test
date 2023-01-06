import subprocess
import os
import datetime
import time
import schedule


def ebs_record(prog_name, record_time):
    now = datetime.datetime.now()   
    current_time = now.strftime("%Y-%m-%d_%H;%M;%S")
    mp4_file = r"D:\EBS_RECORD\{0}_({1}).mp4".format(prog_name, current_time)
    radio_addr =  r"http://ebsonairiosaod.ebs.co.kr/fmradiobandiaod/bandiappaac/playlist.m3u8"
    record_time = str(record_time)
    print(f'file_name  = [{mp4_file}]', end=" ")
    
    result  =  subprocess.Popen(['ffmpeg', '-y', '-i', radio_addr, '-t', record_time, '-c', 'copy', mp4_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = result.communicate()
    exitcode = result.returncode
    if exitcode != 0:
        print(exitcode, out.decode('utf8'), err.decode('utf8'))
    else:
        print("Completed")
        

#schedule.every().day.at("21:42:00").do(easy_english_record)
job1 =  schedule.every(10).seconds.do(ebs_record, "Start_English", 5)
job2 =  schedule.every(10).seconds.do(ebs_record, "Easy_English",  5)
job3 =  schedule.every(10).seconds.do(ebs_record, "Power_English", 5)

while  True:
    
    schedule.run_pending()
    time.sleep(0.1)
    