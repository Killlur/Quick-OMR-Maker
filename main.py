import string
import tkinter as tk
from tkinter import ttk

global root
root = tk.Tk()
root.title('OMRMAKER')
def make_gui():

    #root.geometry('400x200')

    l1 = tk.Label(root , text='OMR MAKER' , font=50).pack()
    blank = tk.Label(root,text='').pack()
    blank = tk.Label(root,text='').pack()

    typelist = []
    numlist = []
    widgetlist=[]
    numofoptionslist=[]

    tree = ttk.Treeview(root, columns=("Type", "Numbers"), show='headings', height=0)
    tree.column("# 1", anchor='center')
    tree.heading("# 1", text="Type")
    tree.column("# 2", anchor='center')
    tree.heading("# 2", text="Number Of Questions")
    def addcolumn(type,num):
        typelist.append(type)
        numlist.append(num)
        numofoptionslist.append(4) #WIP
        tree.config(height=len(typelist))
        typename = (("Integer Type","Numerical Type","Single Correct Type","Multi Correct Type","Link Comprehension Type{One to One}","Link Comprehension Type{One to Many}")[int(type)-1])
        tree.insert('','end',text="1",values=(typename,num))
        print(typelist,numlist,numofoptionslist)
    def b1def():
        optionroot = tk.Toplevel(root)
        optionroot.title('Add column options')
        optionroot.geometry('300x400')
        la1 = tk.Label(optionroot, text='OPTIONS', font=50).pack()
        la2 = tk.Label(optionroot, text='Type of Question', font=30).pack()
        v = tk.IntVar(optionroot, 1)
        values = {"Integer Type": 1,
                  "Numerical Type": 2,
                  "Single Correct Type": 3,
                  "Multi Correct Type": 4,
                  "Link Comprehension Type{One to One}": 5,
                  "Link Comprehension Type{One to Many}":6}
        for (text, value) in values.items():
            tk.Radiobutton(optionroot, text=text, variable=v,
                        value=value, indicator=0,
                        background="light blue", highlightbackground='Red').pack(fill= 'x', ipady=5)

        blank = tk.Label(optionroot, text='').pack()
        blank = tk.Label(optionroot, text='').pack()
        la2 = tk.Label(optionroot, text='Number Of Questions', font=30).pack()
        ea2 = tk.Entry(optionroot,background='light blue')
        ea2.pack(fill='x', ipady=7)
        blank = tk.Label(optionroot, text='').pack()

        def ba1def():
            addcolumn(v.get(),ea2.get())
            optionroot.destroy()
        ba1 = tk.Button(optionroot, text='Confirm', command=ba1def).pack()

    b1 = tk.Button(root,text='Add New Column' , command=b1def).pack()

    blank = tk.Label(root,text='').pack()
    blank = tk.Label(root,text='').pack()

    tree.pack()

    blank = tk.Label(root,text='').pack()
    blank = tk.Label(root,text='').pack()

    strvariablelist = []
    def b2def():
        optionlistindex=0
        numoftypes=0
        OMRwindow = tk.Toplevel(root)
        lastquestionnum=1
        for i in range(len(typelist)):
            numoftypes+=1
            typeofquestion = typelist[i]
            genvariablelist = list(f"VAR{numoftypes}{typeofquestion}{p+1}" for p in range(int(numlist[i])))
            for k in genvariablelist:
                w = tk.StringVar(OMRwindow,name=k)
                print(w.get())
            strvariablelist.append(genvariablelist)
            print(strvariablelist)

            for x in range(int(numlist[i])):
                tk.Label(OMRwindow,text="Q%s"%(lastquestionnum)).grid(row=x%10+1,column=((2 if typeofquestion in (1,2) else 6)*(x//10) + 1))
                if typeofquestion ==1:
                    tk.Entry(OMRwindow,background='light blue',textvariable=genvariablelist[x]).grid(row=x%10+1,column=(2*(x//10 + 1)))
                elif typeofquestion ==2:
                    tk.Entry(OMRwindow, background='light blue',textvariable=genvariablelist[x]).grid(row=x % 10 + 1, column=(2 * (x // 10 + 1)))
                elif typeofquestion ==3:
                    tk.Radiobutton(OMRwindow,text="UA",value="UA",variable=genvariablelist[x],state="normal").grid(row=x%10 +1 ,column=6*(x//10) + 2)

                    for j in range(numofoptionslist[optionlistindex]):
                       tk.Radiobutton(OMRwindow,text=((("A B C D E F G H I J K L M N O P Q R S T U V Y X Y Z").split())[j]),value=((("A B C D E F G H I J K L M N O P Q R S T U V Y X Y Z").split())[j]),variable=genvariablelist[x],state='normal').grid(row=x%10+1,column=(6*(x//10) + 3+j))
                OMRwindow.setvar(genvariablelist[x],value="UA")
                lastquestionnum += 1
            if typeofquestion in (3,4):
                optionlistindex+=1
            print(lastquestionnum)
            def returnvalue():
                print(list(o for o in strvariablelist))
                print(list(OMRwindow.getvar(name=e) for e in strvariablelist[0]))
            bb1 = tk.Button(OMRwindow,command=returnvalue,text="Submit").grid(row=11,column=1,rowspan=lastquestionnum//10 +1)


    b2 = tk.Button(root,text='Make OMR' , command=b2def).pack()

    def b3def():
        for widget1 in root.winfo_children():
            widget1.destroy()
        make_gui()
    b3 = tk.Button(root,text='Clear List' , command=b3def).pack()

    root.mainloop()

make_gui()