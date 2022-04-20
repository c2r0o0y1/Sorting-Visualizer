import time


def bubblesort(data,drawbar,delay):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                drawbar(data,['green' if k==j or k==j+1 else 'red' for k in range(len(data))])
                time.sleep(delay)
    drawbar(data,['green' for i in range(len(data))]) 

