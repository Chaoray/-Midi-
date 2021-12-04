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
        time.sleep(1)
        print(n)
        n = n - 1

mid = None
while True:
    try:
        path = input("你的midi檔路徑:")
        mid = MidiFile(path)
        break
    except:
        pass

data = {
    72:81,
    74:87,
    76:69,
    77:82,
    79:84,
    81:89,
    83:85,

    60:65,
    62:83,
    64:68,
    65:70,
    67:71,
    69:72,
    71:74,

    48:90,
    50:88,
    52:67,
    53:86,
    55:66,
    57:78,
    59:77
}
mididict = []
output = []

print("\nmidi檔處理中...")
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
print("檔案處理完畢\n")

input("按enter開始...")
print("倒數5秒")
countDown(5)

startTime = t.perf_counter()

for i in range(len(output)):
    while True:
        if t.perf_counter() - startTime > output[i][1]:
            try:
                win32api.keybd_event(data[output[i][0]], 0, 0, 0)
                win32api.keybd_event(data[output[i][0]], 0, win32con.KEYEVENTF_KEYUP, 0)
            except:
                pass
            break

print("播放結束")