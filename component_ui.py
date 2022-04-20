from tkinter import *
from tkinter import ttk
import random
import time
from Bubble_sort import bubblesort
from Merge_sort import mergesort
from Insertion_sort import insertionsort




root=Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(900,600)
root.config(bg='black')

select_algo=StringVar()
arr=[]
# ***************************************************************************
#Generating array

def generate_array():
    global arr
    lowest=int(lowest_input_val.get())
    highest=int(highest_input_val.get())
    array_size=int(array_size_input.get())

    arr=[]
    for i in range(array_size):
        arr.append(random.randrange(lowest,highest+1))
        
    drawbar(arr,['red' for i in range(len(arr))])

# ***********************************************************************************************************
#Drawing the bars
def drawbar(arr,colorarr):
    array_box.delete("all")
    box_height=380
    box_width=600
    bar_width=box_width/(len(arr)+1)
    border=30
    normalized_array=[i/max(arr) for i in arr]
    for i, height in enumerate(normalized_array):
        # top left
        x0=i*bar_width+border
        y0=box_height-height*340
        # bottom right
        x1=(i+1)*bar_width+border
        y1=box_height
        array_box.create_rectangle(x0,y0,x1,y1,fill=colorarr[i])
        array_box.create_text(x0+2,y0,anchor=SW,text=str(arr[i]))

    root.update_idletasks()    

# ************************************************************************************************
def sorting():
    global arr
    if sorting_algos.get()=='Bubble Sort':
        bubblesort(arr,drawbar,sortingspeed.get())
    if sorting_algos.get()=='Merge Sort':
        mergesort(arr,drawbar,sortingspeed.get())
    if sorting_algos.get()=='Insertion Sort':
        insertionsort(arr,drawbar,sortingspeed.get())



# ******************************************************************************************************
# UI PART

upper_frame=Frame(root,width=700,height=240,bg='orange')
upper_frame.grid(row=0,column=0,padx=10,pady=5)

array_box=Canvas(root,width=700,height=440,bg='white')
array_box.grid(row=1,column=0,padx=10,pady=5)


sortingspeed=Scale(upper_frame,from_=0.1, to=4.90,length=100,digits=4,orient=HORIZONTAL,label="Speed")
sortingspeed.grid(row=0,column=1,padx=10,pady=10)




Label(upper_frame,text="Algorithms:",).grid(row=0,column=2,padx=10,pady=10)


sorting_algos=ttk.Combobox(upper_frame,textvariable=select_algo,values=['Bubble Sort','Insertion Sort','Merge Sort'],width=10)
sorting_algos.grid(row=0,column=2,padx=5,pady=5)
sorting_algos.current(0)

lowest_input_val=Scale(upper_frame,from_=2, to=10,resolution=1, orient=HORIZONTAL, label="Lower Limit")
lowest_input_val.grid(row=0,column=3,padx=5,pady=5)


highest_input_val=Scale(upper_frame,from_=10, to=250,resolution=1, orient=HORIZONTAL, label="Upper Limit")
highest_input_val.grid(row=0,column=4,padx=5,pady=5)

array_size_input=Scale(upper_frame,from_=3, to=50,resolution=1, orient=HORIZONTAL, label="Array Size")
array_size_input.grid(row=1,column=1,padx=5,pady=5)

Button(upper_frame,text="Start Sorting",command=sorting,bg='green',height=3).grid(row=1,column=2,padx=10,pady=10)

Button(upper_frame,text="Make Array",command=generate_array,bg='pink',height=3).grid(row=1,column=3,padx=10,pady=10)


root.mainloop()