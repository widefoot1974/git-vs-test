import subprocess
import datetime
import time
import schedule
import sys


record_time = "1120"
record_dir = r"E:\EBS_RECORD_(2023)"

def ebs_record(prog_name, index):
    now = datetime.datetime.now()   
    current_time = now.strftime("%Y-%m-%d_%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")

    mp4_file = r"{0}\{1}_({2}_{3}).mp4".format(record_dir, prog_name, current_date, index)
    print(f'[{current_time}]: {mp4_file} recoding ....')
    
    # 반디 외국어 전문
    radio_addr =  r"https://ebsonair.ebs.co.kr/iradio/iradiolive_m4a/playlist.m3u8"    
    
    result  =  subprocess.Popen(['ffmpeg', '-y', '-i', radio_addr, '-t', record_time, '-c', 'copy', mp4_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = result.communicate()
    exitcode = result.returncode
    if exitcode != 0:
        print(exitcode, out.decode('utf8'), err.decode('utf8'))
    else:
        now = datetime.datetime.now()
        current_time = now.strftime("%Y-%m-%d_%H:%M:%S")
        print(f'[{current_time}]: {mp4_file} Completed')
        
def exit():
    print("program exit")
    sys.exit()


schedule.every().day.at("09:00:30").do(ebs_record, "진짜_미국_영어", 1)
schedule.every().day.at("09:20:30").do(ebs_record, "진짜_미국_영어", 2)
schedule.every().day.at("09:40:30").do(ebs_record, "진짜_미국_영어", 3)
schedule.every().day.at("10:00:30").do(ebs_record, "진짜_미국_영어", 4)
schedule.every().day.at("10:20:30").do(ebs_record, "진짜_미국_영어", 5)
schedule.every().day.at("10:40:30").do(ebs_record, "진짜_미국_영어", 6)

schedule.every().day.at("11:00:30").do(ebs_record, "Start_English", 1)
schedule.every().day.at("11:20:30").do(ebs_record, "Start_English", 2)
schedule.every().day.at("11:40:30").do(ebs_record, "Start_English", 3)
schedule.every().day.at("12:00:30").do(ebs_record, "Start_English", 4)
schedule.every().day.at("12:20:30").do(ebs_record, "Start_English", 5)
schedule.every().day.at("12:40:30").do(ebs_record, "Start_English", 6)

schedule.every().day.at("13:00:30").do(ebs_record, "Easy_English", 1)
schedule.every().day.at("13:20:30").do(ebs_record, "Easy_English", 2)
schedule.every().day.at("14:40:30").do(ebs_record, "Easy_English", 3)
schedule.every().day.at("14:00:30").do(ebs_record, "Easy_English", 4)
schedule.every().day.at("14:20:30").do(ebs_record, "Easy_English", 5)
schedule.every().day.at("14:40:30").do(ebs_record, "Easy_English", 6)

schedule.every().day.at("15:00:30").do(ebs_record, "Power_English", 1)
schedule.every().day.at("15:20:30").do(ebs_record, "Power_English", 2)
schedule.every().day.at("15:40:30").do(ebs_record, "Power_English", 3)
schedule.every().day.at("16:00:30").do(ebs_record, "Power_English", 4)
schedule.every().day.at("16:20:30").do(ebs_record, "Power_English", 5)
schedule.every().day.at("16:40:30").do(ebs_record, "Power_English", 6)

schedule.every().day.at("17:00:30").do(ebs_record, "Easy_Writing", 1)
schedule.every().day.at("17:20:30").do(ebs_record, "Easy_Writing", 2)
schedule.every().day.at("17:40:30").do(ebs_record, "Easy_Writing", 3)
schedule.every().day.at("18:00:30").do(ebs_record, "Easy_Writing", 4)
schedule.every().day.at("18:20:30").do(ebs_record, "Easy_Writing", 5)
schedule.every().day.at("18:40:30").do(ebs_record, "Easy_Writing", 6)

schedule.every().day.at("19:00:30").do(ebs_record, "입이_트이는_영어", 1)
schedule.every().day.at("19:20:30").do(ebs_record, "입이_트이는_영어", 2)
schedule.every().day.at("19:40:30").do(ebs_record, "입이_트이는_영어", 3)
schedule.every().day.at("20:00:30").do(ebs_record, "입이_트이는_영어", 4)
schedule.every().day.at("20:20:30").do(ebs_record, "입이_트이는_영어", 5)
schedule.every().day.at("20:40:30").do(ebs_record, "입이_트이는_영어", 6)

schedule.every().day.at("21:00:30").do(ebs_record, "귀가_트이는_영어", 1)
schedule.every().day.at("21:20:30").do(ebs_record, "귀가_트이는_영어", 2)
schedule.every().day.at("21:40:30").do(ebs_record, "귀가_트이는_영어", 3)
schedule.every().day.at("22:00:30").do(ebs_record, "귀가_트이는_영어", 4)
schedule.every().day.at("22:20:30").do(ebs_record, "귀가_트이는_영어", 5)
schedule.every().day.at("22:40:30").do(ebs_record, "귀가_트이는_영어", 6)

schedule.every().day.at("23:00:30").do(exit)

while  True:
    
    schedule.run_pending()
    time.sleep(0.1)
    