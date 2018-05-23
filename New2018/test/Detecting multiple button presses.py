import os
import time
##import RPi.GPIO as GPIO
from EmulatorGUI import GPIO
import subprocess
import re


GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN,pull_up_down=GPIO.PUD_UP)
accept_inputs = GPIO.input(2)
velocity_inputs = GPIO.input(3)
position_inputs = GPIO.input(4)
gps_inputs = GPIO.input(15)
checkpoint_inputs = GPIO.input(18)
misc_inputs = GPIO.input(17)
emergency_inputs = GPIO.input(27)
reject_inputs = GPIO.input(22)
print('initializing')
try:
    while True:
        accept_counts = 0
        velocity_counts = 0
        position_counts = 0
        gps_counts = 0
        checkpoint_counts = 0
        misc_counts = 0
        emergency_counts = 0
        reject_counts = 0
        if accept_inputs == True:
            ##subprocess.call("omxplayer ~/jasper/static/voiceaudio/beep_hi.wav",shell=True)
            print("start inputs")
            control_time_start = time.monotonic()
            control_time = time.monotonic() - control_time_start
            while control_time <= 3:
                last_state_velocity = velocity_inputs
                last_state_position = position_inputs
                last_state_gps = gps_inputs
                last_state_checkpoint = checkpoint_inputs
                last_state_misc = misc_inputs
                last_state_emergency = emergency_inputs
                last_state_accept = accept_inputs
                last_state_reject = reject_inputs
                if velocity_inputs == True and last_state_velocity == False:
                    velocity_counts = velocity_counts+1
                if position_inputs == True and last_state_position == False:
                    position_counts = position_counts+1
                if gps_inputs == True and last_state_gps == False:
                    gps_counts = gps_counts+1
                if checkpoint_inputs == True and last_state_checkpoint == False:
                    checkpoint_counts = checkpoint_counts+1
                if misc_inputs == True and last_state_misc == False:
                    misc_counts = misc_counts+1
                if emergency_inputs == True and last_state_emergency == False:
                    emergency_counts = emergency_counts+1
                if accept_inputs == True and last_state_accept == False:
                    accept_counts = accept_counts+1
                if reject_inputs == True and last_state_reject == False:
                    reject_counts = reject_counts+1
                time.sleep(.01)
            ##subprocess.call("omxplayer ~/jasper/static/voiceaudio/beep_lo.wav",shell=True)
            print("halt inputs")
            if reject_counts >= 2:
                break
            elif velocity_counts == 1:
                print('current velocity triggered')
            elif velocity_counts == 2:
                print('max velocity last run triggered')
            elif velocity_counts == 3:
                print('max velocity today triggered')
            elif position_counts == 1:
                print('current position triggered')
            elif position_counts == 2:
                print('current location triggered')
            elif gps_counts == 1:
                print('GPS status triggered')
            elif gps_counts == 2:
                print('start GPS triggered')
            elif checkpoints_counts == 1:
                print('set velocity checkpoint triggered')
            elif checkpoints_counts == 2:
                print('set position checkpoint triggered')
            elif checkpoints_counts == 3:
                print('set altitude checkpoint triggered')
            elif misc_counts == 3:
                print('restart triggered')
                accept_counts = 0
                reject_counts = 0
                restart_time_start = time.monotonic()
                restart_time = time.monotonic() - restart_time_start
                while restart_time <= 3:
                    if accept_inputs == True:
                        accept_counts = accept_counts+1
                    if reject_inputs == True:
                        reject_counts = reject_counts+1
                if reject_counts > accept_counts:
                    print('restart cancelled')
                if reject_counts < accept_counts:
                    print('restart confirmed')
            elif misc_counts == 4:
                print('shutdown triggered')
                accept_counts = 0
                reject_counts = 0
                shut_time_start = time.monotonic()
                shut_time = time.monotonic() - shut_time_start
                while shut_time <= 3:
                    if accept_inputs == True:
                        accept_counts = accept_counts+1
                    if reject_inputs == True:
                        reject_counts = reject_counts+1
                if reject_counts > accept_counts:
                    print('shutdown cancelled')
                if reject_counts < accept_counts:
                    print('shutdown confirmed')
            elif misc_counts == 1:
                print('clear triggered')
            elif misc_counts == 2:
                print('restore triggered')
            elif emergency_counts == 4:
                print('emergency triggered')
                accept_counts = 1
                reject_counts = 0
                emerg_time_start = time.monotonic()
                emerg_time = time.monotonic() - emerg_time_start
                while emerg_time <= 3:
                    if accept_inputs == True:
                        accept_counts = accept_counts+1
                    if reject_inputs == True:
                        reject_counts = reject_counts+1
                if reject_counts > accept_counts:
                    print('emergency cancelled')
                else:
                    print('emergency confirmed')
            else:
                print('no valid input detected')
        print('no action taken')
        print('-----------------------------------------')
        time.sleep(.05)

except:
    print('error occured, restarting program')
    pass