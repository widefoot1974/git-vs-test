import subprocess
import os
import datetime

'''
set PROGRAM_NAME=Easy_English
set MP3_FILE_NAME="Z:\EBS_(2023)\%PROGRAM_NAME%_(%date:~0,10%).mp3"
set MP4_FILE_NAME="Z:\EBS_(2023)\%PROGRAM_NAME%_(%date:~0,10%).mp4"
set RECORD_MINS=1120
set RADIO_ADDR="http://ebsonairiosaod.ebs.co.kr/fmradiobandiaod/bandiappaac/playlist.m3u8"
ffmpeg -i %RADIO_ADDR% -t %RECORD_MINS% -y -c copy %MP4_FILE_NAME%
'''

if __name__ == "__main__":
    now = datetime.datetime.now()
    #current_time = now.strftime("%Y-%m-%d_%H:%M:%S")
    current_time = now.strftime("%Y-%m-%d_%H;%M;%S")
    mp4_file = r"D:\EBS_RECORD\Easy_English_({0}).mp4".format(current_time)
    radio_addr =  r"http://ebsonairiosaod.ebs.co.kr/fmradiobandiaod/bandiappaac/playlist.m3u8"
    record_time = str(10)
    print(mp4_file)
    
    result  =  subprocess.Popen(['ffmpeg', '-y', '-i', radio_addr, '-t', record_time, '-c', 'copy', mp4_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = result.communicate()
    exitcode = result.returncode
    if exitcode != 0:
        print(exitcode, out.decode('utf8'), err.decode('utf8'))
    else:
        print("Completed")