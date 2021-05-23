# pkumar.link
## Find Shortest Path ##
from tkinter import *
import random
import time

window = Tk()
window.title("Shortest Path")
window.maxsize(800, 800)
window.config(bg="black")

canvas = Canvas(window, height="700", width="700", bg="black")
canvas.grid(row=1, column=0, padx=5, pady=5)

frame = Frame(window, height=50, width=700, bg='pink')
frame.grid(row=0, column=0, padx=5, pady=5)

xy = 25
h, w = 700, 700
maxBdr = 100 # [0 < maxBar <= 1225]
queue = []
temp = []

def rect(x1, y1, x2, y2, color):
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)

def generateWindow():
    queue.clear()
    temp.clear()
    canvas.delete("all")
    global list
    list = []
    for x in range(0, h, xy):
        for y in range(0, w, xy):
            list.append([x, y+xy, x+xy, y])
            rect(x, y+xy, x+xy, y, "white")
# generateWindow()

#For Border
def generateBorder():
    global borderList, pathList
    borderList = []
    pathList = []
    for n in range(maxBdr):
        r=random.randrange(len(list))
        borderList.append(list[r])
        list.pop(r)

    for b in range(len(borderList)):
        x, y_xy, x_xy, y = borderList[b][0], borderList[b][1], borderList[b][2], borderList[b][3]
        rect(x, y_xy, x_xy, y, "black")

    for l in list:
        if(l not in borderList):
            pathList.append(l)
# generateBorder()

def generateTargets():
    global rs, re
    rs = random.randrange(len(pathList))
    canvas.create_oval(pathList[rs][0], pathList[rs][1], pathList[rs][2], pathList[rs][3], fill="green")
    re = random.randrange(len(pathList))
    canvas.create_oval(pathList[re][0], pathList[re][1], pathList[re][2], pathList[re][3], fill="red")
# generateTargets()
# print((pathList))

generateWindow()
generateBorder()
generateTargets()

pp = []
n = 0
def setInQ(x1, y1, x2, y2):
    c = "blue"
    p = []
    p.append([x1, y1, x2, y2])
    if [x1+xy, y1, x2+xy, y2] in pathList and [x1+xy, y1, x2+xy, y2] not in temp and [x1+xy, y1, x2+xy, y2] not in queue:
        queue.append([x1+xy, y1, x2+xy, y2])
        p.append([x1+xy, y1, x2+xy, y2])
        canvas.create_oval(x1+xy+(xy/3), y1-(xy/3), x2+xy-(xy/3), y2+(xy/3), fill=c)
    if [x1, y1+xy, x2, y2+xy] in pathList and [x1, y1+xy, x2, y2+xy] not in temp and [x1, y1+xy, x2, y2+xy] not in queue:
        queue.append([x1, y1+xy, x2, y2+xy])
        p.append([x1, y1+xy, x2, y2+xy])
        canvas.create_oval(x1+(xy/3), y1+xy-(xy/3), x2-(xy/3), y2+xy+(xy/3), fill=c)
    if [x1-xy, y1, x2-xy, y2] in pathList and [x1-xy, y1, x2-xy, y2] not in temp and [x1-xy, y1, x2-xy, y2] not in queue:
        queue.append([x1-xy, y1, x2-xy, y2])
        p.append([x1-xy, y1, x2-xy, y2])
        canvas.create_oval(x1-xy+(xy/3), y1-(xy/3), x2-xy-(xy/3), y2+(xy/3), fill=c)
    if [x1, y1-xy, x2, y2-xy] in pathList and [x1, y1-xy, x2, y2-xy] not in temp and [x1, y1-xy, x2, y2-xy] not in queue:
        queue.append([x1, y1-xy, x2, y2-xy])
        p.append([x1, y1-xy, x2, y2-xy])
        canvas.create_oval(x1+(xy/3), y1-xy-(xy/3), x2-(xy/3), y2-xy+(xy/3), fill=c)
    pp.append(p)

def find():
    global fond
    fond = False
    setInQ(pathList[rs][0], pathList[rs][1], pathList[rs][2], pathList[rs][3])
    while len(queue) != 0:
        q = queue.pop(0)
        if([q[0], q[1], q[2], q[3]] == [pathList[re][0], pathList[re][1], pathList[re][2], pathList[re][3]]):
            rect(q[0], q[1], q[2], q[3], "blue")
            fond = True
            break
        elif [q[0], q[1], q[2], q[3]] == [pathList[rs][0], pathList[rs][1], pathList[rs][2], pathList[rs][3]]:
            rect(q[0], q[1], q[2], q[3], "green")
        else:
            setInQ(q[0], q[1], q[2], q[3])
            rect(q[0], q[1], q[2], q[3], "aqua")
            canvas.update()
            # time.sleep(0.1)
        temp.append(q)

    # Sotest Path
    point = [pathList[re][0], pathList[re][1], pathList[re][2], pathList[re][3]]
    sotestPath = []
    if fond == True:
        for n in range(len(pp), 0, -1):
            if point in pp[n-1] and point not in sotestPath:
                sotestPath.append(point)
                point = pp[n-1][0]
                canvas.create_rectangle(point[0], point[1], point[2], point[3], fill="orange")
                canvas.update()
    canvas.create_oval(pathList[rs][0], pathList[rs][1], pathList[rs][2], pathList[rs][3], fill="green")
    canvas.create_oval(pathList[re][0], pathList[re][1], pathList[re][2], pathList[re][3], fill="red")

btn1 = Button(frame, text='Window', bg='blue', command=generateWindow)
btn1.grid(row=0, column=0)
btn2 = Button(frame, text='Border', bg='blue', command=generateBorder)
btn2.grid(row=0, column=1)
btn3 = Button(frame, text='Target', bg='blue', command=generateTargets)
btn3.grid(row=0, column=2)
btn4 = Button(frame, text='Find', bg='blue', command=find)
btn4.grid(row=0, column=3)

window.mainloop()
