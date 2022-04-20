from os import rename
import time
def insertionsort(data,drawbar,delay):
    k=0
    for i in range(len(data)-1):
        if data[k]>data[k+1]:
            data[k],data[k+1]=data[k+1],data[k]
            drawbar(data,['green' if x==k or x==k+1 else 'red' for x in range(len(data))])
            time.sleep(delay)
            k+=1
            for j in range(len(data[:k])):
                k=0
                if data[k]>data[k+1]:
                    data[k],data[k+1]=data[k+1],data[k]
                    drawbar(data,['green' if x==k or x==k+1 else 'red' for x in range(len(data))])
                    time.sleep(delay)
                    k+=1
                else:
                    k+=1
                    return insertionsort(data,drawbar,delay)
        else:
            k+=1
    drawbar(data,['green' for i in range(len(data))])
    time.sleep(delay)
