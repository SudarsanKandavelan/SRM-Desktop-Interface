from tkinter import *
import tkinter.messagebox
import mysql.connector

#Connecting the Python file with the MYSQL DATABASE
db=mysql.connector.connect(host="localhost",user="root",passwd="1234567890",auth_plugin='mysql_native_password',database="srm")
cursor=db.cursor()

#To create a tkinter window
a=Tk()
a.config(bg="#2c3e50")

# 7904903575

#Creating title and icon to the window
a.title("SRM ENTERPRISES")
#a.iconbitmap("download.ico")
imagesrm=PhotoImage(file="SRMLOGO.png")
srm=Label(a,image=imagesrm)
srm.grid(row=0,column=1,columnspan=3)

global name,badd,index;
name="hi"

global total
total=0

index=[]
atc=[];yoy1=[]
        
def sqlselect(s,co,m):
    yoy1.append((s,co,m))
    q="select "+s+" from srm_enterprises where "+co+"="
    c='"';x=c+m+c;d="order by num asc"
    f=q+x+d
    #yoy1.append(f)
    cursor.execute(f)
    v=cursor.fetchall()
    return v

def sql(h):
    cursor.execute(h)
    c=cursor.fetchall()
    return c
    
def converttolist(v):
    brandnames=[]
    m=0
    while(m<len(v)):
        brandnames.append(v[m][0])
        m+=1
    c=[]
    for i in brandnames:
        if (i not in c):
            c.append(i)
    return c;


global num
num=0

#rate,margin,add to cart
def helo(m):
    print(m)
    l='"';d=l+m[1]+l;r=l+m[2]+l;
    v="select * from srm_enterprises where buttonname="+d+" and brandname="+r
    cursor.execute(v)
    v=cursor.fetchall()
    
    axis=[(135,70),(568,70),(1001,70),(135,310),(568,310),(1001,310)]
    q=axis[m[0]]
    x=q[0];y=q[1]
    f=[x,y,v]
    global  num,numb,badd,bp1,bm2,bp2,enc,en,bm1,total;
    global checkout
    index=v.copy()
    if(numb==2):
        badd.destroy()
        bm1.destroy()
        enc.destroy()
        bp1.destroy()
        bm2.destroy()
        bp2.destroy()
        en.destroy()
        add.destroy()
        net.destroy()
        num=0
    if(num==0):
        b1=Label(a,text="image")
        b1.place(x=x-110,y=y,height=80,width=105)
        l67=Label(a,text=v[0][2],font=("Times New Roman",14,"bold"),bg="#2c3e50",fg="white")
        l67.place(x=x,y=y-25,height=25,width=250)
        b2=Label(a,text="Mrp",font=("Times New Roman",12),bg="#2c3e50",fg="white")
        b2.place(x=x,y=y,width=50,height=30)
        b2=Label(a,text="Rate",font=("Times New Roman",12),bg="#2c3e50",fg="white")
        b2.place(x=x+70,y=y,width=50,height=30)
        b2=Label(a,text="Margin",font=("Times New Roman",12),bg="#2c3e50",fg="white")
        b2.place(x=x+140,y=y,width=50,height=30)
        b2=Label(a,text=v[0][7],font=("Times New Roman",12),bg="#2c3e50",fg="white")
        b2.place(x=x,y=y+30,width=50,height=30)
        b2=Label(a,text=v[0][8],font=("Times New Roman",12),bg="#2c3e50",fg="white")
        b2.place(x=x+70,y=y+30,width=50,height=30)
        b2=Label(a,text=v[0][9],font=("Times New Roman",12),bg="#2c3e50",fg="white")
        b2.place(x=x+140,y=y+30,width=50,height=30)
        if(v[0][5] in noi):
            c=str(v[0][11])
            l1=Label(a,text="1Case="+c+" Units",bg="#2c3e50",fg="white")
            l1.place(x=f[0]+60,y=f[1]-20+80)
            bm1=Button(a,text="-",font=("Times New Roman",14,"bold"),bg="#2c3e50",fg="white",command=lambda b=f:buttonminus(b))
            bm1.place(x=f[0]-100,y=f[1]+80,width=35,height=30)
            enc=Entry(a);
            enc.place(x=f[0]-65,y=f[1]+80,width=90,height=30)
            bp1=Button(a,text="+",font=("Times New Roman",14,"bold"),bg="#2c3e50",fg="white",command=lambda b=f:buttonplus(b))
            bp1.place(x=f[0]+25,y=f[1]+80,width=35,height=30)   
            bm2=Button(a,text="-",font=("Times New Roman",14,"bold"),bg="#2c3e50",fg="white",command=lambda b=f:buttonminus(b))
            bm2.place(x=f[0]+60,y=f[1]+80,width=35,height=30)
            en=Entry(a)
            en.place(x=f[0]+95,y=f[1]+80,width=90,height=29)
            bp2=Button(a,text="+",font=("Times New Roman",14,"bold"),bg="#2c3e50",fg="white",command=lambda b=f:buttonplus(b))
            bp2.place(x=f[0]+185,y=f[1]+80,width=35,height=30)
            if(len(noi)>=2):
                i=0
                while(i<len(noi)):
                    if(noi[i]==v[0][5]):
                        s=noi[i+1]
                        en.delete(0,END)
                        en.insert(0,s)
                    i+=1
            else:
                badd=Button(a,text="Add To Cart",font=("Times New Roman",12),bg="#2c3e50",fg="white",command=lambda m=(x,y,v):entry(m))
                badd.place(x=x,y=y+80,width=190,height=35)
        else:
            badd=Button(a,text="Add To Cart",font=("Times New Roman",12),bg="#2c3e50",fg="white",command=lambda m=(x,y,v):entry(m))
            badd.place(x=x,y=y+80,width=190,height=35)


fp=[]
global j
j=0
def buttonminus(f):
    if(bp2["state"]=="disabled"):
       bp2.config(state="normal")
       
    global netrate,yousaved,index,total,checkout
    x=f[0]
    y=f[1]
    v=f[2]
    k=v[0]
    h=en.get()
    h=int(h)
    index=v.copy()
    if(h!=0 and h!=1):
        en.delete(0,END)
        en.insert(0,h-1)
        h=en.get()
        h=int(h)
        nr=(h*v[0][8]);nr=round(nr,2)
        global netrate,yousaved
        netrate=Label(a,text=str(nr)+"     ",fg="white",bg="#2c3e50")
        netrate.place(x=f[0]+95+62,y=f[1]+110,height=19)
        save=(h*v[0][7])-nr;save=round(save,2)
        yousaved=Label(a,text=str(save)+"    ",fg="white",bg="#2c3e50")
        yousaved.place(x=f[0]-110+62,y=f[1]+80+30,height=19)
        j=1
        
        if(len(noi)>=1):
                i=0
                while(i<len(noi)):
                    if(noi[i]==v[0][5]):
                        s=i+1
                        noi[i+1]=h
                        noi[i+2]=nr
                    i+=1
    elif(h==1):
        h=int(h)-1
        if(len(noi)>=2):
                i=0
                while(i<len(noi)):
                    if(noi[i]==v[0][5]):
                        noi.remove(noi[i])
                        noi.remove(noi[i])
                        noi.remove(noi[i])
                    i+=1
        add=Label(a,text="        ",bg="#2c3e50",fg="white")
        add.place(x=f[0]-110,y=f[1]+80+30,height=19,width=62)
        net=Label(a,text="          ",bg="#2c3e50",fg="white")
        net.place(x=f[0]+95,y=f[1]+110,height=19,width=55)
        nr="         ";
        netrate=Label(a,text=nr,fg="white",bg="#2c3e50")
        netrate.place(x=f[0]+95+62,y=f[1]+110,height=19)
        save="    ";
        yousaved=Label(a,text=save,fg="white",bg="#2c3e50")
        yousaved.place(x=f[0]-110+62,y=f[1]+80+30,height=19)
        bm1.destroy()
        bp1.destroy()
        bp2.destroy()
        bm2.destroy()
        en.destroy()
        enc.destroy()
        badd=Button(a,text="Add To Cart",font=("Times New Roman",12),bg="#2c3e50",fg="white",command=lambda m=(x,y,v):entry(m))
        badd.place(x=x,y=y+80,width=190,height=35)
    i=2;total=0
    while(i<len(noi)):
        total=noi[i]+total
        i=i+3
    checkout.config(text="Check Out:Rs."+str(total))

        
noi=[]

def buttonplus(f):
    global total,checkout,j
    v=f[2]
    k=v[0]
    h=en.get()
    h=int(h)
    en.delete(0,END)
    en.insert(0,h+1)
    h=en.get()
    h=int(h)
    nr=(h*v[0][8]);nr=round(nr,2)
    netrate=Label(a,text=str(nr)+"      ",fg="white",bg="#2c3e50")
    netrate.place(x=f[0]+95+62,y=f[1]+110,height=19)
    save=(h*v[0][7])-nr;save=round(save,2)
    yousaved=Label(a,text=str(save)+"    ",fg="white",bg="#2c3e50")
    yousaved.place(x=f[0]-110+62,y=f[1]+80+30,height=19)
    if(len(noi)>=2):
                i=0
                while(i<len(noi)):
                    if(noi[i]==v[0][5]):
                        noi[i+1]=h
                        noi[i+2]=nr
                    i+=1

    if(h>(v[0][12]-10) and h<v[0][12]):
        d=int(v[0][12])-int(h)
        g="(Only "+str(d)+" Left)";
        lab=Label(a,text=g,bg="#2c3e50",fg="red",font=("Times New Roman",8))
        lab.place(x=f[0]+60+60,y=f[1]-20+80)
        
    elif(h==v[0][12]):
        q=int(h/(v[0][12]))
        en.insert(0,h-q*(v[0][12]))
        bp2.config(state="disabled");
        bp1.config(state="disabled");
        
    if(h>=v[0][11] and h<v[0][12]):
        q=int(h/(v[0][12]))
        en.delete(0,END)
        enc.delete(0,END)
        enc.insert(0,q)
        en.insert(0,h-q*(v[0][12]))
        
    i=2;total=0
    while(i<len(noi)):
        total=noi[i]+total
        i=i+3
    checkout.config(text="Check Out:Rs."+str(total))
      
    


def brands(m):
    print(len(noi))
    if (len(noi)>0):
        global checkout
        checkout=Button(a,text="Check Out:Rs.",command=therilaye)
        checkout.place(x=1050,y=600,height=30,width=200)
    
    print("in brand")
    v=sqlselect("brand","company",m)
    c=converttolist(v)
    global name;
    name="helo"
    largebuttons(c)
    
global numb
numb=0

def bp(f):
    global lab,lab0,lab1,lab2;
    x=f[3];y=f[4]
    i=0
    while(i<len(noi)):
        if(f[0]==noi[i]):
             h=noi[i+1]+1
             rate=f[2]/f[1]
             trate=rate*h
             trate=round(trate,2)
             noi[i+2]=trate
             noi[i+1]=noi[i+1]+1
             lab1=Label(a,text="Rs."+str(noi[i+2]),bg="#2c3e50",fg="white",font=("Times New Roman",16,"bold"))
             lab1.place(x=x+85,y=y+30,height=30)
             lab2=Label(a,text=noi[i+1],bg="#2c3e50",fg="white",font=("Times New Roman",16,"bold"))
             lab2.place(x=x+85+50,y=y+70,height=30)
        i=i+1
def bm(f):
    global lab,lab0,lab1,lab2;
    x=f[3];y=f[4]
    i=0
    while(i<len(noi)):
        if(f[0]==noi[i]):
             h=noi[i+1]-1
             if(h!=0):
                 rate=f[2]/f[1]
                 trate=rate*h
                 trate=round(trate,2)
                 noi[i+2]=trate
                 noi[i+1]=noi[i+1]-1
                 lab1=Label(a,text="Rs."+str(noi[i+2])+"             ",bg="#2c3e50",fg="white",font=("Times New Roman",16,"bold"))
                 lab1.place(x=x+85,y=y+30,height=30)
                 lab2=Label(a,text=str(noi[i+1])+"   ",bg="#2c3e50",fg="white",font=("Times New Roman",16,"bold"))
                 lab2.place(x=x+85+50,y=y+70,height=30)
             elif(h==0):
                 rate=f[2]/f[1]
                 trate=rate*h
                 trate=round(trate,2)
                 noi[i+2]=trate
                 noi[i+1]=noi[i+1]-1
                 lab1=Label(a,text="Rs."+str(noi[i+2])+"                      ",bg="#2c3e50",fg="white",font=("Times New Roman",16,"bold"))
                 lab1.place(x=x+85,y=y+30,height=30)
                 lab2=Label(a,text=str(noi[i+1])+"   ",bg="#2c3e50",fg="white",font=("Times New Roman",16,"bold"))
                 lab2.place(x=x+85+50,y=y+70,height=30)
                 noi.remove(noi[i])
                 noi.remove(noi[i])
                 noi.remove(noi[i])
                 therilaye()
        i=i+1
        
def therilaye():
    global lab,lab0,lab1,lab2;
    label=Label(a,text=" ",bg="#2c3e50")
    label.place(x=0,y=45,height=700,width=1500)
    pay=Button(a,text="Check Out",command=finished)
    pay.place(x=1050,y=600,height=30,width=200)
    x=25;y=50
    i=0;j=0;
    while(i<len(noi)):
        lab=Label(a,text="image",fg="white");
        lab.place(x=x,y=y,width=80,height=105)
        lab0=Label(a,text=noi[i],bg="#2c3e50",fg="white",font=("Times New Roman",14,"bold"))
        lab0.place(x=x+85,y=y,height=30)
        noi[i+2]=round(noi[i+2],2)
        lab1=Label(a,text="Rs. "+str(noi[i+2])+"              ",bg="#2c3e50",fg="white",font=("Times New Roman",16,"bold"))
        lab1.place(x=x+85,y=y+30,height=30)
        bp2=Button(a,text="+",font=("Times New Roman",16,"bold"),bg="#2c3e50",fg="white",command=lambda b=(noi[i],noi[i+1],noi[i+2],x,y):bp(b))
        bp2.place(x=x+185,y=y+70,width=25,height=25)
        bp2=Button(a,text="-",font=("Times New Roman",16,"bold"),bg="#2c3e50",fg="white",command=lambda b=(noi[i],noi[i+1],noi[i+2],x,y):bm(b))
        bp2.place(x=x+85,y=y+70,width=25,height=25)
        lab2=Label(a,text=noi[i+1],bg="#2c3e50",fg="white",font=("Times New Roman",16,"bold"))
        lab2.place(x=x+85+50,y=y+70,height=30)
        i=i+3
        x=x+350
        j=j+1
        if(j==4):
            x=25;y=y+200
        
def entry(f):
    global checkout
    checkout=Button(a,text="Check Out:Rs.",command=lambda b=f:therilaye())
    checkout.place(x=1050,y=600,height=30,width=200)
    global numb,bm1,bm2,bp1,bp2,en,enc,add,net
    v=f[2]
    fp.append(v[0])
    badd.destroy()
    c=str(v[0][11])
    l1=Label(a,text="1 Case="+c+"        ",bg="#2c3e50",fg="white")
    l1.place(x=f[0]+60,y=f[1]-20+80,width=80)
    bm1=Button(a,text="-",font=("Times New Roman",14,"bold"),bg="#2c3e50",fg="white",command=lambda b=f:buttonminus(b))
    bm1.place(x=f[0]-100,y=f[1]+80,width=35,height=30)
    enc=Entry(a);
    enc.place(x=f[0]-65,y=f[1]+80,width=90,height=30)
    bp1=Button(a,text="+",font=("Times New Roman",14,"bold"),bg="#2c3e50",fg="white",command=lambda b=f:buttonplus(b))
    bp1.place(x=f[0]+25,y=f[1]+80,width=35,height=30)   
    bm2=Button(a,text="-",font=("Times New Roman",14,"bold"),bg="#2c3e50",fg="white",command=lambda b=f:buttonminus(b))
    bm2.place(x=f[0]+60,y=f[1]+80,width=35,height=30)
    en=Entry(a)
    en.place(x=f[0]+95,y=f[1]+80,width=90,height=29)
    en.insert(0,1)
    bp2=Button(a,text="+",font=("Times New Roman",14,"bold"),bg="#2c3e50",fg="white",command=lambda b=f:buttonplus(b))
    bp2.place(x=f[0]+185,y=f[1]+80,width=35,height=30)
    add=Label(a,text="You Saved=",bg="#2c3e50",fg="white")
    add.place(x=f[0]-110,y=f[1]+80+30,height=19,width=62)
    net=Label(a,text="Net Rate:",bg="#2c3e50",fg="white")
    net.place(x=f[0]+95,y=f[1]+110,height=19,width=55)
    h=en.get()
    h=int(h)
    nr=(h*v[0][8]);nr=round(nr,2)
    global netrate,yousaved;
    netrate=Label(a,text=nr,fg="white",bg="#2c3e50")
    netrate.place(x=f[0]+95+62,y=f[1]+110,height=19)
    save=(h*v[0][7])-nr;save=round(save,2)
    yousaved=Label(a,text=save,fg="white",bg="#2c3e50")
    yousaved.place(x=f[0]-110+62,y=f[1]+80+30,height=19)
    noi.append(v[0][5])
    noi.append(h)
    noi.append(nr)
    numb=2
    i=2;total=0
    while(i<len(noi)):
        total=noi[i]+total
        i=i+3
    checkout.config(text="Check Out:Rs."+str(total))


def products(m):
    if(m in cp):
        brands(m)
    else:
        print("in product")
        global badd,h,bback
        print(m)
        v=sqlselect("brandname","brand",m)
        c=converttolist(v)
        k=[]
        for i in c:
            h='select buttonname from srm_enterprises where brandname='
            s='"';z=s+i+s+"order by num asc"
            h=h+z
            cursor.execute(h)
            v=cursor.fetchall()
            brandnames=[]
            m=0
            while(m<len(v)):
                brandnames.append(v[m][0])
                m+=1
            d=[];
            for i in brandnames:
                if (i not in d):
                    d.append(i)
            j=tuple(d)
            k.append(j)
        ab=Label(a,text="            ",bg="#2c3e50")
        ab.place(x=25,y=50,width=1350,height=700)
        t=len(k)-3
        i=0;m=0;x=25;y=200;xaxis=25;yaxis=200;atcxaxis=135;atcyaxis=150
        while(i<len(k)):
            if(i==len(k)-t and i!=0):
                x=25
                xaxis=x
                yaxis=yaxis+240
                y=yaxis
                atcxaxis=135;atcyaxis=atcyaxis+240
                t=t-3
            x=x;y=y;m=0
            j=0;d=90
            while(j<len(k[i])):
                if(j>7):
                    break;
                if(m<=3):
                    x=x;y=y
                elif(m>3):
                    if(m==4):
                        x=xaxis
                        y=y+40
                    x=x
                    y=y
        
                exo1=Button(a,text=k[i][j],font=("Times New Roman",12),command=lambda m=(i,k[i][j],c[i]):helo(m))
                exo1.place(x=x,y=y,height=35,width=70)
                bback=Button(a,text="<=",padx=15,pady=10,command=backbutton)
                bback.grid(row=0,column=0)      

                if(j<len(k[i])-1):
                    x=x+d
                m+=1
                j=j+1
            xaxis=xaxis+433
            x=xaxis
            y=yaxis
            atcxaxis+=433
            
            i+=1


image=PhotoImage(file="JYOTHYLAB.png")
r=Label(a,image=imagesrm)
                

def backbutton():
    h=yoy1[len(yoy1)-2]
    v=sqlselect(h[0],h[1],h[2])
    v=converttolist(v)
    if(h[0]=="brand"):
        name="hi"
        print("ennama ithu")
        largebuttons(v)
        

def goback():
    print("!#")
    q=yoy[len(yoy)-1]
    if(q=="largebuttons"):
        name="hi"
        print(h9)
        print(name)
        largebuttons(cp)
    elif(q=="largebutton"):
        name="helo"
        largebuttons(h9) 

h9=[];yoy=[]

#Images for Buttons
JYOTHYLABS=PhotoImage(file="JYOTHYLABS.png")
WIPRO=PhotoImage(file="JYOTHYLABS.png")
RECKITTBENKISER=PhotoImage(file="JYOTHYLABS.png")
TATA=PhotoImage(file="JYOTHYLABS.png")
HIMALAYA=PhotoImage(file="JYOTHYLABS.png")
MAMYPOKOPANTS=PhotoImage(file="JYOTHYLABS.png")
CAVINKARE=PhotoImage(file="JYOTHYLABS.png")
MAYORA=PhotoImage(file="JYOTHYLABS.png")
WRIGLEY=PhotoImage(file="JYOTHYLABS.png")

image=[JYOTHYLABS,WIPRO,RECKITTBENKISER,TATA,HIMALAYA,MAMYPOKOPANTS,CAVINKARE,MAYORA,WRIGLEY]

def largebuttons(c):
    if(name=="hi"):
        yoy.append("largebutton")
    elif(name=="helo"):
        yoy.append("largebuttons")
    h9=c.copy()
    ab=Label(a,text="            ",bg="#2c3e50")
    ab.place(x=25,y=50,width=1350,height=700)
    t=len(c)-3
    i=0;m=0;x=25;y=50;xaxis=25;yaxis=50
    while(i<len(c)):
        if(i==len(c)-t and i!=0):
            x=25
            xaxis=x
            yaxis=yaxis+200
            y=yaxis
            t=t-3
        x=x;y=y;m=0
        j=0;d=415
        while(j<len(c[i])):
            if(j>7):
                break;
            L=c[i]
            if(name=="hi"):
                global r,bback
                brand=Button(a,image=image[i],text=c[i],font=("Times New Roman",12,"bold"),borderwidth=0,bg="#2c3e50",fg="white",compound=TOP,command=lambda m=c[i]:brands(m))
                brand.place(x=x,y=y,height=200,width=415)
               
            elif(name=="helo"):
            
                brand=Button(a,text=c[i],font=("Times New Roman",12,"bold"),borderwidth=0,bg="#2c3e50",fg="white",compound=TOP,command=lambda m=c[i]:products(m))
                brand.place(x=x,y=y,height=200,width=415)
                bback=Button(a,text="<=",padx=15,pady=10,command=goback)
                bback.grid(row=0,column=0)
            if(j<len(c[i])-1):
                x=x+d
            m+=1
            j=j+1
        
        xaxis=xaxis+417
        x=xaxis
        y=yaxis
        i+=1
    

def ok():
    largebuttons(cp)

def shopselect(h):
    return
        
cp=["JYOTHYLABS","WIPRO","RECKITTBENKISER","TATA","HIMALAYA","MAMYPOKOPANTS","CAVINKARE","MAYORA","WRIGLEY"]
shop=Label(a,text="SHOP NAME ",font=("Times New Roman",18,"bold"),borderwidth=0,bg="#2c3e50",fg="white")
shop.place(x=425,y=200,width=150,height=22)
global shopname
shopname=Entry(a,text="select")
shopname.place(x=620,y=205,width=150,height=22)

ktm=["SRM Maligai","Thayagam Super Market","Apple Super Market","Mohaideen Maligai"]
click=StringVar()

drop=OptionMenu(a, click , *ktm)
drop.place(x=620,y=205,height=22,width=200)

shop2=Label(a,text="ADDRESS ",font=("Times New Roman",18,"bold"),borderwidth=10,bg="#2c3e50",fg="white")
shop2.place(x=425,y=230,width=150,height=22)

shop=Label(a,text="PHONE ",font=("Times New Roman",18,"bold"),borderwidth=0,bg="#2c3e50",fg="white")
shop.place(x=425,y=260,width=200,height=22)

okay=Button(a,text="OK",font=("Times New Roman",20,"bold"),borderwidth=0,bg="#2c3e50",fg="white",command=ok)
okay.place(x=800,y=280,width=50)




def finished():
    tkinter.messagebox.showinfo("anandh","Are you sure want to checkout ")
    tkinter.messagebox.showinfo("SRM ENTERPRISES","Ordered Successfully\nDo you want to Close")
    print(noi)
    a.destroy()



a.mainloop()

