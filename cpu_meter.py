#!/usr/bin/python2.7
# -*- coding:utf-8 -*-
import psutil
import commands
import smbus
import time

ADDRESS    = 0x40
RCH        = 0x08
LCH        = 0x0C
GETCMD = "cat /sys/class/thermal/thermal_zone0/temp"

def main():
    
    # PCA9685イニシャライズ
    bus = smbus.SMBus(1)
    bus.write_byte_data(ADDRESS, 0x00, 0x81) # reset
    bus.write_byte_data(ADDRESS, 0x00, 0x01) # mode1
    bus.write_byte_data(ADDRESS, 0x01, 0x05) # mode2
    bus.write_byte_data(ADDRESS, 0xFE, 0x05) # pwm freq.

    time.sleep(0.25)

    while True:
        # CPU負荷、CPU温度データ取得
        cpu_percent = psutil.cpu_percent(interval=0.2)
        cpu_temp = float(commands.getoutput(GETCMD))/1000

#        print "CPU=",cpu_percent
        cpu_percent = cpu_percent*4095/100
        cpu_h = int(cpu_percent/256)
        cpu_l = int(cpu_percent)-cpu_h
        
#        print "TEMP=",cpu_temp
        cpu_temp = cpu_temp*4095/100
        temp_h = int(cpu_temp/256)
        temp_l = int(cpu_temp)-temp_h
        
        # 針メーター駆動
        bus.write_byte_data(ADDRESS, LCH, cpu_l) # CH1
        bus.write_byte_data(ADDRESS, LCH+1, cpu_h) # CH1
        bus.write_byte_data(ADDRESS, RCH, temp_l) # CH0
        bus.write_byte_data(ADDRESS, RCH+1, temp_h) # CH0

if __name__ == '__main__':
    main()

