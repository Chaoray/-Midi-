'''
Midi File to KeyBoard By ChaoRay
github:https://github.com/Chaoray
'''

from mido import MidiFile
import time as t
import win32api
import win32con

def countDown(n):
    while n > 0:
        t.sleep(1)
        print(f'in {i} sec')
        n = n - 1

mid = None
while True:
    try:
        path = input("midi File Path:")
        mid = MidiFile(path)
        break
    except:
        pass

offset = 60
data = {
    12:81,
    14:87,
    16:69,
    17:82,
    19:84,
    21:89,
    23:85,

    0:65,
    2:83,
    4:68,
    5:70,
    7:71,
    9:72,
    11:74,

    -12:90,
    -10:88,
    -8:67,
    -7:86,
    -5:66,
    -3:78,
    -1:77
}
mididict = []
output = []

print("\nmidi File Processing...")
for i in mid:
    if i.type == 'note_on' or i.type == 'note_off' or i.type == 'time_signature':
        mididict.append(i.dict())

mem1 = 0
for i in mididict:
    time = i['time'] + mem1
    i['time'] = time
    mem1 = i['time']
    mem2=[]
    if i['type'] == 'note_on':
        mem2.append(i['note'])
        mem2.append(i['time'])
        output.append(mem2)
print("Process is done\n")

while True:
    choose = input("Do you wanna set the offset?(y/n)")
    if choose == 'y':
        buffer = input("offset:")
        if type(buffer) == type(1):
            offset = buffer
            break
    elif choose == 'n':
        break

input("Press enter to start...")
print("in 5 sec")
countDown(5)

print("Start play")
startTime = t.perf_counter()

for i in range(len(output)):
    while True:
        if t.perf_counter() - startTime > output[i][1]:
            try:
                win32api.keybd_event(data[output[i][0] - offset], 0, 0, 0)
                win32api.keybd_event(data[output[i][0] - offset], 0, win32con.KEYEVENTF_KEYUP, 0)
            except:
                pass
            break

input("End play")