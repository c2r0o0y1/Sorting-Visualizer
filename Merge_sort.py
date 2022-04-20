import time

def mergesort(data,drawbar,delay):
    sort_algo(data,0,len(data)-1,drawbar,delay)
    drawbar(data,['green' for i in range(len(data))])
    time.sleep(delay)

def sort_algo(data,low,high,drawbar,delay):
    if(low>=high):
        return
    mid=(low+high)//2
    sort_algo(data,low,mid,drawbar,delay)
    sort_algo(data,mid+1,high,drawbar,delay)
    merge(data,low,mid,high,drawbar,delay)

def merge(data,low,mid,high,drawbar,delay):
    drawbar(data,['red' for i in range(len(data))])
    time.sleep(delay)
    left=data[low:mid+1]
    right=data[mid+1:high+1]

    lf_idx=0
    rt_idx=0

    for i in range(low,high+1):
        if lf_idx<len(left) and rt_idx<len(right):
            if left[lf_idx]<=right[rt_idx]:
                data[i]=left[lf_idx]
                lf_idx=lf_idx+1
            else:
                data[i]=right[rt_idx]
                rt_idx=rt_idx+1
        elif lf_idx<len(left):
            data[i]=left[lf_idx]
            lf_idx=lf_idx+1
        else:
            data[i]=right[rt_idx]
            rt_idx=rt_idx+1
        drawbar(data,['green' if j==i else 'red' for j in range(len(data))])
        time.sleep(delay)