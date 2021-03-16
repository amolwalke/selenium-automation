import serial
import time

def onMCUCommByte(ser, command='SrLS\n', ack='L 0\n', fluahall=True, wrTimes=2, rdTimes=2, easyQuit=False, clearSerial=True):

    ack = str([ord(i) for i in ack])[1:-1]
    end = False
    for __ in range(wrTimes):
        ser.write( str.encode(command))
        ret = ''
        for __ in range(rdTimes):
            ret = ''
            try: ret = str(list(ser.readline()))
            except: pass
            print('\n Rec Data', ret, ack)
            if ack in ret:
                end = True
                break
        if easyQuit and ret == '[]': return True
        if end: break
    return end



ser = serial.Serial('COM6', 9600, timeout=2)
ser.flush()

onMCUCommByte(ser)
ser.write( str.encode("SrLS\n"))
for i in range(3):
    # val = str(list(ser.readline()))#Capture serial output as a decoded string
    val = ser.readline().decode('utf-8')#Capture serial output as a decoded string
    print('Here', val)
time.sleep(2)

ser.write( str.encode("SrMD\n"))
val = ser.readline().decode('utf-8')#Capture serial output as a decoded string
print(val)
ser.write(b'SrPs\n')
val = ser.readline().decode('utf-8')#Capture serial output as a decoded string
print(val)
ser.write(b'SrRS\n')
val = ser.readline().decode('utf-8')#Capture serial output as a decoded string
print(val)

