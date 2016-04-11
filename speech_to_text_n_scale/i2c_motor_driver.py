# coding: utf-8

import smbus
import time

bus_number = 1
addr = 0x64
bus = smbus.SMBus(bus_number)
cmd = 0x00
normal_values = (0x19, 0x35, 0x65, 0xC9, 0xFD)
reverse_values = (0x1A, 0x36, 0x66, 0xCA, 0xFE)
stop_values = (0x18, 0x1B)

def start():
    send_vals(normal_values[:4])
    #send_vals(normal_values)

def reverse():
    send_vals(reverse_values[:4])
    #send_vals(reverse_values)

def stop():
    send_vals(stop_values)

def accelerate():
    current = get_current_val()
    try:
        i = normal_values.index(current)
        send_vals(normal_values[i + 1:])
        return
    except ValueError:
        pass
    try:
        i = reverse_values.index(current)
        send_vals(reverse_values[i + 1:])
        return
    except ValueError:
        pass

def decelerate():
    current = get_current_val()
    try:
        i = normal_values.index(current)
        if i == (len(normal_values) - 1):
            send_vals(normal_values[2:][::-1])
        return
    except ValueError:
        pass
    try:
        i = reverse_values.index(current)
        if i == (len(reverse_values) - 1):
            send_vals(reverse_values[2:][::-1])
        return
    except ValueError:
        pass

def send_vals(vals):
    for v in vals:
        bus.write_byte_data(addr, cmd, v);
        time.sleep(0.01)

def get_current_val():
    return bus.read_byte_data(addr, cmd)
        
__all__ = ["start", "reverse", "stop", "accelerate", "decelerate"]

if __name__ == '__main__':
    start()
    time.sleep(3)
    accelerate()
    time.sleep(2)
    decelerate()
    time.sleep(2)
    decelerate()
    time.sleep(2)
    stop()
    time.sleep(2)
    reverse()
    time.sleep(3)
    accelerate()
    time.sleep(2)
    decelerate()
    time.sleep(2)
    stop()
