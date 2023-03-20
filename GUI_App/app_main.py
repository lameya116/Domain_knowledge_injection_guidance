
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import guidance_result
import webbrowser
import os

def viewSelected():
   label_3.config(text="")
   label_4.config(text="")
   label_5.config(text="")
   label_b.config(text="")
   label_c.config(text="")
   label_d.config(text="")
   label_e.config(text="")
   label_6.config(text="")
   label_7.config(text="")

def view_knw():    
    label_3.config(text="")
    label_4.config(text="")
    label_5.config(text="")
    label_b.config(text="")
    label_c.config(text="")
    label_d.config(text="")
    label_e.config(text="")
    label_6.config(text="")
    label_7.config(text="")

def show_msg(arrm):
    webbrowser.open_new(arrm)

def get_link(algos):
    '''Returns links of paper for corresponding algorithm '''
    if algos=="TSAK-SVM":
        link="https://ieeexplore.ieee.org/document/9253527"
    elif algos=="SAE":
        link="https://www.mdpi.com/2076-3417/10/19/6789"
    elif algos=="kmeans":
        link="https://www.sciencedirect.com/science/article/pii/S2351978918305262"
    elif algos=="SVM":
        link="https://ieeexplore.ieee.org/abstract/document/8627962"
    elif algos=="GA":
            link="https://link.springer.com/article/10.1007/s10921-020-0665-7"
    elif algos=="ANN":
        link="https://link.springer.com/article/10.1007/s40436-017-0203-8"
    elif algos=="PCA":
        link="https://journals.sagepub.com/doi/full/10.1177/1687814020919207"
    elif algos=="KNN":
            link="https://ieeexplore.ieee.org/document/9625679"
    elif algos=="BPNN":
        link="https://www.sciencedirect.com/science/article/pii/S0888327017305034"
    elif algos=="RF":
        link="https://www.sciencedirect.com/science/article/pii/S1877050922002198"

    elif algos=="SVR":
        link="https://iopscience.iop.org/article/10.1088/1757-899X/533/1/012032/meta"
    elif algos=="LSTM":
        link="https://ieeexplore.ieee.org/document/7998311"
    elif algos=="MLP":
            link="https://www.mdpi.com/1424-8220/19/19/4342"

    elif algos=="HMM-POMDP":
        link="https://papers.phmsociety.org/index.php/phmconf/article/view/851"
    elif algos=="POMDP":
        link="https://papers.phmsociety.org/index.php/phmconf/article/view/851"
    elif algos=="DPCA":
        link="https://ieeexplore.ieee.org/document/8710319"
    
    else:
        link="https://www.tutorialspoint.com/how-to-create-a-hyperlink-with-a-label-in-tkinter"
    return link

def callback():
    '''Provides suitable knowledge injection phase and ML models with corresponding ranking'''
    
    choice1  = var.get()
    choice2  = var2.get()
    if choice2==0 or choice1==0:
        return messagebox.showinfo('Decision Guidance', f'Please enter all information.')
    else:
        # Type of input application
        if choice1 == 2:
            app_type = "diagnosis"
        elif choice1 == 3:
            app_type =  "predictive"    
        elif choice1 == 4:
            app_type =  "prescriptive"
        elif choice1 == 1:
            app_type = "descriptive"

        #Form of available domain knowledge
        if choice2 == 6:
            knw_type = "informal"
        elif choice2 == 7:
            knw_type =  "semiformal"   
        elif choice2 == 8:
            knw_type =  "formal"
        res, r2, rv=guidance_result.app_input(app_type,knw_type)
        
        phases=str(res)
        phases=phases.replace("[","")
        phases=phases.replace("]","")
        p="Possible injection phases : "+phases
        algos="& Possible algorithms with ranking : "
        label_3.config(text=p)
        label_4.config(text=algos)
        lnk_set=[]
        nm_l=[]

        for al in range (len(r2)):
            algs=str(r2[al])
            algs=algs.replace("'","")
            algs=algs.replace("'","")
            ln=get_link(algs)
            lnk_set.append(ln)
            r_v=str(rv[al])
            ab=r2[al]+" ="+r_v
            nm_l.append(ab)
        
        len_chk=len(r2)
        chk_cnt=0
        if chk_cnt<len_chk:
            chk_cnt=chk_cnt+1
            label_5.config(text=str(nm_l[0]),fg="blue")
            label_5.bind("<Button-1>", lambda event, k=k: webbrowser.open_new(lnk_set[1]))
        if chk_cnt<len_chk:
            chk_cnt=chk_cnt+1
            label_b.config(text=str(nm_l[1]),fg="blue")
            label_b.bind("<Button-1>", lambda event, k=k: webbrowser.open_new(lnk_set[0]))
        if chk_cnt<len_chk:
            chk_cnt=chk_cnt+1
            label_c.config(text=str(nm_l[2]),fg="blue")
            label_c.bind("<Button-1>", lambda event, k=k: webbrowser.open_new(lnk_set[1]))
        if chk_cnt<len_chk:
            chk_cnt=chk_cnt+1
            label_d.config(text=str(nm_l[3]),fg="blue")
            label_d.bind("<Button-1>", lambda event, k=k: webbrowser.open_new(lnk_set[1]))
        if chk_cnt<len_chk:
            chk_cnt=chk_cnt+1
            label_e.config(text=str(nm_l[4]),fg="blue")
            label_e.bind("<Button-1>", lambda event, k=k: webbrowser.open_new(lnk_set[1]))

        label_6.config(text="PP = Pre-Processing,    FE = Feature Engineering,   HS = Hypothesis Space,")
        label_7.config(text="CS = Constraint Setting,    RZ = Regularization,    DM = Decision Making")
        
knowledge=""
app=""
ws = Tk()
ws.title('Domain Knowledge Injection & ML Model Selector')
ws.geometry('600x600')
ws.resizable(0,0)
lnk_set=[]
nm_l=[]
notebook = ttk.Notebook(ws)
notebook.pack(pady=10, expand=True)

frame1 = ttk.Frame(notebook, width=600, height=570)
frame2 = ttk.Frame(notebook, width=600, height=570)
frame3 = ttk.Frame(notebook, width=600, height=570)
frame4 = ttk.Frame(notebook, width=600, height=570)
frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)
message = Label(frame1, text="Domain Knowledge Injection & ML Model Selector",width=55,font=("bold", 15))
message.place(x=0,y=30)
 
label_1 = Label(frame1, text="Please select type of your application",width=40,font=("bold", 12))
label_1.place(x=30,y=100) 
var = IntVar()
Radiobutton(frame1, text="Descriptive", variable=var, value=1, command=viewSelected).place(x=80,y=130)
Radiobutton(frame1, text="Diagnosis", variable=var, value=2, command=viewSelected).place(x=200,y=130)
Radiobutton(frame1, text="Predictive", variable=var, value=3, command=viewSelected).place(x=320,y=130)
Radiobutton(frame1, text="Prescriptive", variable=var, value=4, command=viewSelected).place(x=430,y=130)
label_2 = Label(frame1, text="Please select the form of knowledge",width=40,font=("bold", 12))
label_2.place(x=30,y=180) 

var2 = IntVar()
Radiobutton(frame1, text="Informal", variable=var2, value=6, command=viewSelected).place(x=80,y=210)
Radiobutton(frame1, text="Semi-formal", variable=var2, value=7, command=viewSelected).place(x=200,y=210)
Radiobutton(frame1, text="Formal", variable=var2, value=8,command=viewSelected).place(x=320,y=210)
p=""
MyButton1 = Button(frame1, text="Submit", width=30, command=callback) .place(x=180,y=250)
label_3 = Label(frame1, text=p,width=50,font=("bold", 12))
label_3.place(x=30,y=310) 
label_4 = Label(frame1, text=p,width=50,font=("bold", 12))
label_4.place(x=30,y=350)
label_5 = Label(frame1, text=p,width=20,font=("bold", 12))
label_5.place(x=30,y=380)
label_b = Label(frame1, text="",width=20,font=("bold", 12))
label_b.place(x=200,y=380)
label_c = Label(frame1, text="",width=20,font=("bold", 12))
label_c.place(x=370,y=380)
label_d = Label(frame1, text="",width=20,font=("bold", 12))
label_d.place(x=60,y=410)
label_e = Label(frame1, text="",width=20,font=("bold", 12))
label_e.place(x=260,y=410)
all_inj=""
label_6 = Label(frame1, text=all_inj,width=70,font=("bold", 10))
label_6.place(x=10,y=500)
label_7 = Label(frame1, text=all_inj,width=66,font=("bold", 10))
label_7.place(x=10,y=530)
notebook.add(frame1, text='Decision Guidance')


# General Information 

text = tk.Text(frame2, height=580, width=540,font=("bold", 10))
scroll = tk.Scrollbar(frame2)
text.configure(yscrollcommand=scroll.set)
text.pack(side=tk.LEFT) 
scroll.config(command=text.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
  
insert_text = """\nDESCRIPTIVE USECASE :
Use cases those are related to condition monitoring. Main purpose of this type of use cases is to find out what is happening in anufacturing environent.

DIAGNOSIS USECASE : 
Use cases those primary purpose is to find out the presence of different types of faults and analysis of underlying reason for occuring those faults.

PREDICTIVE USECASE :
Use cases those are related to predictive analysis such as how long the machine will perform, when a possible fault condition will occure.

PRESCRIPTIVE USECASE :
Use cases those are able to take prescribtive decidion by analysing current environmental situation.



INFORMAL DOMAIN KNOWLEDGE :
Knowledge is loosely coupled and has no direct impact on the input dataset. 
Examples : standard techniques such as FFT, STFT, WPT, etc. 

SEMI-FORMAL DOMAIN KNOWLEDGE : 
knowledge is more structured and explicitly available for injection.
Examples : predefined threshold value, expert knowledge for establising logic rules or labeling data 

FORMAL DOMAIN KNOWLEDGE :
knowledge which is injected in a standardized/established form
Examples : Simulator generated machine data with define experimental boundaries, expert suggested formulas or physics based equations 
""" 
text.insert(tk.END, insert_text)
text.config(state=DISABLED)
notebook.add(frame2, text='General Information')


# Window for additional suggestions

text = tk.Text(frame4, height=580, width=540,font=("bold", 12))
scroll = tk.Scrollbar(frame4)
text.configure(yscrollcommand=scroll.set)
text.pack(side=tk.LEFT) 
scroll.config(command=text.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
  
insert_tet = """\nSome additional suggesstions:

1. Unsupervised models such as kmeans, and autoencoders might perform well 
   than traditional supervised techniques for labeling time series data.

2. For reducing data variation, logarithmic transformation is usually helpful.

3. FFT can be a good option if frequency domain data needs to be analyzed only,
   however STFT, WT or another decomposition techniques, like EMD, would be a 
   better pre-processing technique if time domain also needs to be considered.

4. Statistical variables such as RMS, and kurtosis are widely preferred for 
   vibration analysis since they can detect rapid changes in the data stream.

5. For analyzing specific fault type frequency domain data proves to be more efficient
   and time domain for detecting faulty conditions.

6. LDA, PCA, Chi-square, and XGBoost are some popular feature selection methods
   which are used for dimension reduction.

7. Statistical variables such as RMS, and kurtosis are widely preferred features 
   for analysing vibration because they can detect rapid changes in the data stream.

8. In addition to accuracy, other suitable metrics such as precision, f1 score, RMSE, 
   and MAE often needed to be evaluated to ensure whether the model isn’t overfitted.
""" 
text.insert(tk.END, insert_tet)
text.config(state=DISABLED)
notebook.add(frame4, text='Suggesitions')

# Window for ML list with corresponding link

filepath = os.path.dirname(__file__)
file=open(filepath+'/model.txt', 'r')
c=0
num_line = sum(1 for line in open(filepath+'/model.txt'))
rows, cols = (num_line, 3) 
arr = [["" for i in range(cols)] for j in range(rows)]

for line in file:
    word_list = line.split(";")
    arr[c][0]=word_list[0]
    arr[c][1]=word_list[1]
    arr[c][2]=word_list[2]
    c=c+1  
i=0

for k in range(0,c):
    url=arr[k][2]
    for j,url in enumerate(arr[k]):#for j in range (0,3):
        if j==0:
            my_link= tk.Label(frame3, text=arr[k][j], fg="blue", cursor="hand2",font=('Arial',9))
            p=k
            my_link.bind("<Button-1>", lambda event, k=k: webbrowser.open_new(arr[k][2]))
            i=i+1
            
        elif j==1:
            my_link = tk.Label(frame3, width=70,font=('Arial',9),foreground='black', text=arr[k][1])

        my_link.grid(row=k, column=j)

notebook.add(frame3, text='Model List')
ws.mainloop()