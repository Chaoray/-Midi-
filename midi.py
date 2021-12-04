'''
Midi File to KeyBoard By ChaoRay
github:https://github.com/Chaoray
'''

from mido import MidiFile
import time as t
import win32api
import win32con

mid = None
while True:
    try:
        path = input("你的midi檔路徑:")
        mid = MidiFile(path)
        break
    except:
        pass

data = {
    48:81,
    50:87,
    52:69,
    53:82,
    55:84,
    57:89,
    59:85,

    60:65,
    62:83,
    64:68,
    65:70,
    67:71,
    69:72,
    71:74,

    72:90,
    74:88,
    76:67,
    77:86,
    79:66,
    81:78,
    83:77
}
mididict = []
output = []

print("midi檔處理中...")
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
print("處理完畢")

input("按enter開始...")

startTime = t.perf_counter()

for i in range(len(output)):
    while True:
        if t.perf_counter() - startTime > output[i][1]:
            print(data[output[i][0]])
            try:
                win32api.keybd_event(data[output[i][0]], 0, 0, 0)
                win32api.keybd_event(data[output[i][0]], 0, win32con.KEYEVENTF_KEYUP, 0)
            except:
                pass
            break

print("播放結束")