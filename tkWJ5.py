from tkinter import *
import random
from operator import itemgetter
import os
from os import path
import io
import sys
import datetime

def open_window_0():
    if (window0 is not None) and window0.winfo_exists():
        window0.withdraw()
        window0.deiconify()
    else:
        wjWindow0()
    return
def open_window_1():
    if (window3 is not None) and window1.winfo_exists():
        window1.withdraw()
        window1.deiconify()
    else:
        wjWindow1()
    return
def open_window_2():
    if (window2 is not None) and window2.winfo_exists():
        window2.withdraw()
        window2.deiconify()
    else:
        wjWindow2()
    return
def open_window_3():
    if (window3 is not None) and window3.winfo_exists():
        window3.withdraw()
        window3.deiconify()
    else:
        wjWindow3()
    return
def open_window_4():
    if (window4 is not None) and window4.winfo_exists():
        window4.withdraw()
        window4.deiconify()
    else:
        wjWindow4()
    return
def open_window_5():
    if (window5 is not None) and window5.winfo_exists():
        window5.withdraw()
        window5.deiconify()
    else:
        wjWindow5()
    return
    
app = Tk()
app.title(string="Writers Jumbler")
    
def wjWindow0():
    global window0
    
    window0 = Toplevel(app)
    window0.title(string="Color Background")
    window0.geometry("240x220")
    message2 = Label(window0, text=" ").pack()
    
    var1 = DoubleVar()
    var2 = DoubleVar()
    var3 = DoubleVar()

    colorSlide1 = Scale(window0, label="RED", orient=HORIZONTAL, from_=0, to=255, variable=var1)
    colorSlide1.pack()
    colorSlide2 = Scale(window0, label="GREEN", orient=HORIZONTAL, from_=0, to=255, variable=var2)
    colorSlide2.pack()
    colorSlide3 = Scale(window0, label="BLUE", orient=HORIZONTAL, from_=0, to=255, variable=var3)
    colorSlide3.pack()

    def colorRGB():
        colorRa = int(var1.get())
        colorGa = int(var2.get())
        colorBa = int(var3.get())
        colorAa = "{:#04x}"
        colorRb = int(hex(colorRa), 16)
        colorGb = int(hex(colorGa), 16)
        colorBb = int(hex(colorBa), 16)
        colorRab = colorAa.format(colorRb)
        colorGab = colorAa.format(colorGb)
        colorBab = colorAa.format(colorBb)
        colorRc = "".join(repr(colorRab).replace("0x", "").replace("'", ""))
        colorGc = "".join(repr(colorGab).replace("0x", "").replace("'", ""))
        colorBc = "".join(repr(colorBab).replace("0x", "").replace("'", ""))
        colorRd = colorRc
        colorGd = colorGc
        colorBd = colorBc
        colorCTa = (colorRd, colorGd, colorBd)
        colorCTb = "".join(repr(colorCTa).replace(",", "").replace("('", "").replace("' '", "").replace("')", ""))
        colorCTc = "#" + colorCTb
        window2.config(bg=colorCTc)
        message1.config(bg=colorCTc)
        message2z.config(bg=colorCTc)
        message3z.config(bg=colorCTc)
        message4z.config(bg=colorCTc)
        message5z.config(bg=colorCTc)
        return

    color_text = Button(window0, command=colorRGB, text="Color This Window Background").pack()
    return

wj0 = wjWindow0()
window0.withdraw()

def wjWindow1():
    global window1
    
    window1 = Toplevel(app)
    window1.title(string="Color Font")
    window1.geometry("240x220")
    message2 = Label(window1, text=" ").pack()
    
    var4 = DoubleVar()
    var5 = DoubleVar()
    var6 = DoubleVar()

    colorSlide4 = Scale(window1, label="RED", orient=HORIZONTAL, from_=0, to=255, variable=var4)
    colorSlide4.pack()
    colorSlide5 = Scale(window1, label="GREEN", orient=HORIZONTAL, from_=0, to=255, variable=var5)
    colorSlide5.pack()
    colorSlide6 = Scale(window1, label="BLUE", orient=HORIZONTAL, from_=0, to=255, variable=var6)
    colorSlide6.pack()

    def colorRGB2():
        colorRa = int(var4.get())
        colorGa = int(var5.get())
        colorBa = int(var6.get())
        colorAa = "{:#04x}"
        colorRb = int(hex(colorRa), 16)
        colorGb = int(hex(colorGa), 16)
        colorBb = int(hex(colorBa), 16)
        colorRab = colorAa.format(colorRb)
        colorGab = colorAa.format(colorGb)
        colorBab = colorAa.format(colorBb)
        colorRc = "".join(repr(colorRab).replace("0x", "").replace("'", ""))
        colorGc = "".join(repr(colorGab).replace("0x", "").replace("'", ""))
        colorBc = "".join(repr(colorBab).replace("0x", "").replace("'", ""))
        colorRd = colorRc
        colorGd = colorGc
        colorBd = colorBc
        colorCTa = (colorRd, colorGd, colorBd)
        colorCTb = "".join(repr(colorCTa).replace(",", "").replace("('", "").replace("' '", "").replace("')", ""))
        colorCTc = "#" + colorCTb
        message1.config(fg=colorCTc)
        message2z.config(fg=colorCTc)
        message3z.config(fg=colorCTc)
        message4z.config(fg=colorCTc)
        message5z.config(fg=colorCTc)
        return

    color_text = Button(window1, command=colorRGB2, text="Color Fonts").pack()
    return

wj1 = wjWindow1()
window1.withdraw()

def savas5():
    aValue = text1.get()
    bValue = text2.get()
    cValue = text3.get()
    dValue = text4.get()
    eValue = text5.get()
    fValue = text6.get()
    gValue = text7.get()
    hValue = text8.get()
    iValue = text9.get()
    jValue = text10.get()
    kValue = text11.get()
    lValue = text12.get()
    mValue = text13.get()
    nValue = text14.get()
    oValue = text15.get()
    pValue = text16.get()
    qValue = text17.get()
    rValue = text18.get()
    sValue = text19.get()
    tValue = text20.get()
    uValue = text21.get()
    vValue = text22.get()
    wValue = text23.get()
    xValue = text24.get()
    yValue = text25.get()
    zValue = text26.get()
    aaValue = text27.get()
    abValue = text28.get()
    acValue = text29.get()
    adValue = text30.get()
    aeValue = text31.get()
    afValue = text32.get()
    agValue = text33.get()
    ahValue = text34.get()
    aiValue = text35.get()
    ajValue = text36.get()
    akValue = text37.get()
    alValue = text38.get()
    amValue = text39.get()
    anValue = text40.get()
    aoValue = text41.get()
    apValue = text42.get()
    aqValue = text43.get()
    arValue = text44.get()
    asValue = text45.get()
    atValue = text46.get()
    auValue = text47.get()
    avValue = text48.get()
    awValue = text49.get()
    axValue = text50.get()

    word = "WJ5_inOrder_5c_"
    dthm = datetime.datetime.now()
    m = str(dthm.strftime("%m"))
    dy = str(dthm.strftime("%d"))
    y = str(dthm.strftime("%Y"))
    h = str(dthm.strftime("%I"))
    mins = str(dthm.strftime("%M"))
    amPm = str(dthm.strftime("%p"))
    sec = str(dthm.strftime("%S"))
    dash = "-"
    d = str(m + dash + dy + dash + y + dash + h + dash + mins + dash + sec + dash + amPm)
    z = word + d + ".csv"

    file = open(z, "w")

    allMessages = str(aValue) + ";" +  str(bValue) + ";" +  str(cValue) + ";" +  str(dValue) + ";" +  str(eValue) + ";" +  str(fValue) + ";" +  str(gValue) + ";" +  str(hValue) + ";" +  str(iValue) + ";" +  str(jValue) + ";" +  str(kValue) + ";" +  str(lValue) + ";" + str(mValue) + ";" +  str(nValue) + ";" +  str(oValue) + ";" +  str(pValue) + ";" +  str(qValue) + ";" +  str(rValue) + ";" +  str(sValue) + ";" +  str(tValue) + ";" +  str(uValue) + ";" +  str(vValue) + ";" +  str(wValue) + ";" +  str(xValue) + ";" +  str(yValue) + ";" +  str(zValue) + ";" +  str(aaValue) + ";" +  str(abValue) + ";" +  str(acValue) + ";" +  str(adValue) + ";" +  str(aeValue) + ";" +  str(afValue) + ";" +  str(agValue) + ";" +  str(ahValue) + ";" +  str(aiValue) + ";" +  str(ajValue) + ";" +  str(akValue) + ";" +  str(alValue) + ";" +  str(amValue) + ";" +  str(anValue) + ";" +  str(aoValue) + ";" +  str(apValue) + ";" +  str(aqValue) + ";" +  str(arValue) + ";" +  str(asValue) + ";" +  str(atValue) + ";" +  str(auValue) + ";" +  str(avValue) + ";" +  str(awValue) + ";" +  str(axValue)
    file.write(allMessages)
    file.close()
    return

def getfiles7():
    global text11z

    list_a = []
    list_b = []
    list_c = []
    list_d = []
    list_e = []
    list_f = []
    list_g = []
    list_h = []
    list_i = []
    list_j = []
    list_k = []
    list_l = []
    list_m = []
    list_n = []
    list_o = []
    list_p = []
    list_q = []
    list_r = []
    list_s = []
    list_t = []
    list_u = []
    list_v = []
    list_w = []
    list_x = []
    list_y = []
    list_z = []
    list_aa = []
    list_ab = []
    list_ac = []
    list_ad = []
    list_ae = []
    list_af = []
    list_ag = []
    list_ah = []
    list_ai = []
    list_aj = []
    list_ak = []
    list_al = []
    list_am = []
    list_an = []
    list_ao = []
    list_ap = []
    list_aq = []
    list_ar = []
    list_as = []
    list_at = []
    list_au = []
    list_av = []
    list_aw = []
    list_ax = []
    abz = text11z.get()
    with open(abz, "r") as tz:
        for line in tz:
            words = line.split(";")
            word_1 = words[0]
            word_2 = words[1]
            word_3 = words[2]
            word_4 = words[3]
            word_5 = words[4]
            word_6 = words[5]
            word_7 = words[6]
            word_8 = words[7]
            word_9 = words[8]
            word_10 = words[9]
            word_11 = words[10]
            word_12 = words[11]
            word_13 = words[12]
            word_14 = words[13]
            word_15 = words[14]
            word_16 = words[15]
            word_17 = words[16]
            word_18 = words[17]
            word_19 = words[18]
            word_20 = words[19]
            word_21 = words[20]
            word_22 = words[21]
            word_23 = words[22]
            word_24 = words[23]
            word_25 = words[24]
            word_26 = words[25]
            word_27 = words[26]
            word_28 = words[27]
            word_29 = words[28]
            word_30 = words[29]
            word_31 = words[30]
            word_32 = words[31]
            word_33 = words[32]
            word_34 = words[33]
            word_35 = words[34]
            word_36 = words[35]
            word_37 = words[36]
            word_38 = words[37]
            word_39 = words[38]
            word_40 = words[39]
            word_41 = words[40]
            word_42 = words[41]
            word_43 = words[42]
            word_44 = words[43]
            word_45 = words[44]
            word_46 = words[45]
            word_47 = words[46]
            word_48 = words[47]
            word_49 = words[48]
            word_50 = words[49]
            a.set(word_1)
            b.set(word_2)
            c.set(word_3)
            d.set(word_4)
            e.set(word_5)
            f.set(word_6)
            g.set(word_7)
            h.set(word_8)
            i.set(word_9)
            j.set(word_10)
            k.set(word_11)
            l.set(word_12)
            m.set(word_13)
            n.set(word_14)
            o.set(word_15)
            p.set(word_16)
            q.set(word_17)
            r.set(word_18)
            s.set(word_19)
            t.set(word_20)
            u.set(word_21)
            v.set(word_22)
            w.set(word_23)
            x.set(word_24)
            y.set(word_25)
            z.set(word_26)
            aa.set(word_27)
            ab.set(word_28)
            ac.set(word_29)
            ad.set(word_30)
            ae.set(word_31)
            af.set(word_32)
            ag.set(word_33)
            ah.set(word_34)
            ai.set(word_35)
            aj.set(word_36)
            ak.set(word_37)
            al.set(word_38)
            am.set(word_39)
            an.set(word_40)
            ao.set(word_41)
            ap.set(word_42)
            aq.set(word_43)
            ar.set(word_44)
            as2.set(word_45)
            at.set(word_46)
            au.set(word_47)
            av.set(word_48)
            aw.set(word_49)
            ax.set(word_50)	
    return

def getfiles5():
    global message4
    
    files = []
    files = os.listdir(os.getcwd())
    files = "".join(repr(files).replace(",", "\n").replace("[", "").replace("]", "").replace("'", "").replace(" ", ""))
    message4.config(state=NORMAL)
    message4.delete(1.0, END)
    message4.insert(END, files + "\n")
    message4.config(state=DISABLED)

exitWindow = exit

menuBar = Frame(app, relief=RAISED, borderwidth=1)
menuBar.grid(row=0, column=0, sticky=W)
FileMenu = Menubutton(menuBar, text="FILE")
FileMenu.grid(row=0, column=0)
FileMenu.menu = Menu(FileMenu)
FileMenu.menu.add_command(label="SAVE, WITH DATE AND TIME", command=savas5)
FileMenu.menu.add_command(label="LIST FILES IN DIRECTORY WINDOW", command=getfiles5)
FileMenu.menu.add_command(label="OPEN, FROM FILE, FROM DIRECTORY INPUT", command=getfiles7)
FileMenu.menu.add_command(label="EXIT, WRITERS JUMBLER", command=exitWindow)
FileMenu['menu'] = FileMenu.menu
OpenMenu = Menubutton(menuBar, text="OPEN")
OpenMenu.grid(row=0, column=1)
OpenMenu.menu = Menu(OpenMenu)
OpenMenu.menu.add_command(label="OPEN REARRANGEMENTS", command=open_window_2)
OpenMenu.menu.add_command(label="OPEN ACTION BUTTONS", command=open_window_5)
OpenMenu.menu.add_command(label="OPEN COLOR BACKGROUND", command=open_window_0)
OpenMenu.menu.add_command(label="OPEN COLOR FONT", command=open_window_1)
OpenMenu.menu.add_command(label="OPEN DIRECTORY WINDOW", command=open_window_3)
OpenMenu.menu.add_command(label="OPEN DIRECTORY INPUT", command=open_window_4)
OpenMenu['menu'] = OpenMenu.menu

a = StringVar()
text1 = Entry(app, textvariable=a, width=30)
text1.grid(row=1, column=0)
b = StringVar()
text2 = Entry(app, textvariable=b, width=30)
text2.grid(row=2, column=0)
c = StringVar()
text3 = Entry(app, textvariable=c, width=30)
text3.grid(row=3, column=0)
d = StringVar()
text4 = Entry(app, textvariable=d, width=30)
text4.grid(row=4, column=0)
e = StringVar()
text5 = Entry(app, textvariable=e, width=30)
text5.grid(row=5, column=0)
f = StringVar()
text6 = Entry(app, textvariable=f, width=30)
text6.grid(row=6, column=0)
g = StringVar()
text7 = Entry(app, textvariable=g, width=30)
text7.grid(row=7, column=0)
h = StringVar()
text8 = Entry(app, textvariable=h, width=30)
text8.grid(row=8, column=0)
i = StringVar()
text9 = Entry(app, textvariable=i, width=30)
text9.grid(row=9, column=0)
j = StringVar()
text10 = Entry(app, textvariable=j, width=30)
text10.grid(row=10, column=0)
k = StringVar()
text11 = Entry(app, textvariable=k, width=30)
text11.grid(row=1, column=1)
l = StringVar()
text12 = Entry(app, textvariable=l, width=30)
text12.grid(row=2, column=1)
m = StringVar()
text13 = Entry(app, textvariable=m, width=30)
text13.grid(row=3, column=1)
n = StringVar()
text14 = Entry(app, textvariable=n, width=30)
text14.grid(row=4, column=1)
o = StringVar()
text15 = Entry(app, textvariable=o, width=30)
text15.grid(row=5, column=1)
p = StringVar()
text16 = Entry(app, textvariable=p, width=30)
text16.grid(row=6, column=1)
q = StringVar()
text17 = Entry(app, textvariable=q, width=30)
text17.grid(row=7, column=1)
r = StringVar()
text18 = Entry(app, textvariable=r, width=30)
text18.grid(row=8, column=1)
s = StringVar()
text19 = Entry(app, textvariable=s, width=30)
text19.grid(row=9, column=1)
t = StringVar()
text20 = Entry(app, textvariable=t, width=30)
text20.grid(row=10, column=1)
u = StringVar()
text21 = Entry(app, textvariable=u, width=30)
text21.grid(row=1, column=2)
v = StringVar()
text22 = Entry(app, textvariable=v, width=30)
text22.grid(row=2, column=2)
w = StringVar()
text23 = Entry(app, textvariable=w, width=30)
text23.grid(row=3, column=2)
x = StringVar()
text24 = Entry(app, textvariable=x, width=30)
text24.grid(row=4, column=2)
y = StringVar()
text25 = Entry(app, textvariable=y, width=30)
text25.grid(row=5, column=2)
z = StringVar()
text26 = Entry(app, textvariable=z, width=30)
text26.grid(row=6, column=2)
aa = StringVar()
text27 = Entry(app, textvariable=aa, width=30)
text27.grid(row=7, column=2)
ab = StringVar()
text28 = Entry(app, textvariable=ab, width=30)
text28.grid(row=8, column=2)
ac = StringVar()
text29 = Entry(app, textvariable=ac, width=30)
text29.grid(row=9, column=2)
ad = StringVar()
text30 = Entry(app, textvariable=ad, width=30)
text30.grid(row=10, column=2)
ae = StringVar()
text31 = Entry(app, textvariable=ae, width=30)
text31.grid(row=1, column=3)
af = StringVar()
text32 = Entry(app, textvariable=af, width=30)
text32.grid(row=2, column=3)
ag = StringVar()
text33 = Entry(app, textvariable=ag, width=30)
text33.grid(row=3, column=3)
ah = StringVar()
text34 = Entry(app, textvariable=ah, width=30)
text34.grid(row=4, column=3)
ai = StringVar()
text35 = Entry(app, textvariable=ai, width=30)
text35.grid(row=5, column=3)
aj = StringVar()
text36 = Entry(app, textvariable=aj, width=30)
text36.grid(row=6, column=3)
ak = StringVar()
text37 = Entry(app, textvariable=ak, width=30)
text37.grid(row=7, column=3)
al = StringVar()
text38 = Entry(app, textvariable=al, width=30)
text38.grid(row=8, column=3)
am = StringVar()
text39 = Entry(app, textvariable=am, width=30)
text39.grid(row=9, column=3)
an = StringVar()
text40 = Entry(app, textvariable=an, width=30)
text40.grid(row=10, column=3)
ao = StringVar()
text41 = Entry(app, textvariable=ao, width=30)
text41.grid(row=1, column=4)
ap = StringVar()
text42 = Entry(app, textvariable=ap, width=30)
text42.grid(row=2, column=4)
aq = StringVar()
text43 = Entry(app, textvariable=aq, width=30)
text43.grid(row=3, column=4)
ar = StringVar()
text44 = Entry(app, textvariable=ar, width=30)
text44.grid(row=4, column=4)
as2 = StringVar()
text45 = Entry(app, textvariable=as2, width=30)
text45.grid(row=5, column=4)
at = StringVar()
text46 = Entry(app, textvariable=at, width=30)
text46.grid(row=6, column=4)
au = StringVar()
text47 = Entry(app, textvariable=au, width=30)
text47.grid(row=7, column=4)
av = StringVar()
text48 = Entry(app, textvariable=av, width=30)
text48.grid(row=8, column=4)
aw = StringVar()
text49 = Entry(app, textvariable=aw, width=30)
text49.grid(row=9, column=4)
ax = StringVar()
text50 = Entry(app, textvariable=ax, width=30)
text50.grid(row=10, column=4)

def messagesC1():
    value1 = str(random.randint(0, 9))
    value2 = str(random.randint(0, 9))
    value3 = str(random.randint(0, 9))
    value4 = str(random.randint(0, 9))
    value5 = str(random.randint(0, 9))
    value6 = str(random.randint(0, 9))
    value7 = str(random.randint(0, 9))
    value8 = str(random.randint(0, 9))
    value9 = str(random.randint(0, 9))
    value10 = str(random.randint(0, 9))

    aValue = text1.get()
    bValue = text2.get()
    cValue = text3.get()
    dValue = text4.get()
    eValue = text5.get()
    fValue = text6.get()
    gValue = text7.get()
    hValue = text8.get()
    iValue = text9.get()
    jValue = text10.get()

    za = []
    zb = []
    zc = []
    zd = []
    ze = []
    zf = []
    zg = []
    zh = []
    zi = []
    zj = []

    ya = [za, zb, zc, zd, ze, zf, zg, zh, zi, zj]
    za = [value1, aValue, '\n']
    zb = [value2, bValue, '\n']
    zc = [value3, cValue, '\n']
    zd = [value4, dValue, '\n']
    ze = [value5, eValue, '\n']
    zf = [value6, fValue, '\n']
    zg = [value7, gValue, '\n']
    zh = [value8, hValue, '\n']
    zi = [value9, iValue, '\n']
    zj = [value10, jValue, '\n']
    ya = [za, zb, zc, zd, ze, zf, zg, zh, zi, zj]

    zzx = sorted(ya, key=itemgetter(0), reverse=False)
    zzz = zzx

    qa = zzx[0]
    qb = zzx[1]
    qc = zzx[2]
    qd = zzx[3]
    qe = zzx[4]
    qf = zzx[5]
    qg = zzx[6]
    qh = zzx[7]
    qi = zzx[8]
    qj = zzx[9]

    xa = qa[-2]
    xb = qb[-2]
    xc = qc[-2]
    xd = qd[-2]
    xe = qe[-2]
    xf = qf[-2]
    xg = qg[-2]
    xh = qh[-2]
    xi = qi[-2]
    xj = qj[-2]

    ka = [xa]
    kb = [xb]
    kc = [xc]
    kd = [xd]
    ke = [xe]
    kf = [xf]
    kg = [xg]
    kh = [xh]
    ki = [xi]
    kj = [xj]

    xxxx = (ka, kb, kc, kd, ke, kf, kg, kh, ki, kj)

    xxxxx0 = "".join(repr(xxxx).replace("(['","\n").replace('(["','\n').replace("'], ['", "\n\n").replace('"])', '\n').replace("'])", "\n").replace("'],","\n").replace(" ['","\n").replace('"],','\n').replace(' ["','\n'))
    zzzzz0.set(xxxxx0)
    return

def messagesC2():
    value11 = str(random.randint(0, 9))
    value12 = str(random.randint(0, 9))
    value13 = str(random.randint(0, 9))
    value14 = str(random.randint(0, 9))
    value15 = str(random.randint(0, 9))
    value16 = str(random.randint(0, 9))
    value17 = str(random.randint(0, 9))
    value18 = str(random.randint(0, 9))
    value19 = str(random.randint(0, 9))
    value20 = str(random.randint(0, 9))

    kValue = text11.get()
    lValue = text12.get()
    mValue = text13.get()
    nValue = text14.get()
    oValue = text15.get()
    pValue = text16.get()
    qValue = text17.get()
    rValue = text18.get()
    sValue = text19.get()
    tValue = text20.get()

    za2 = []
    zb2 = []
    zc2 = []
    zd2 = []
    ze2 = []
    zf2 = []
    zg2 = []
    zh2 = []
    zi2 = []
    zj2 = []

    ya2 = [za2, zb2, zc2, zd2, ze2, zf2, zg2, zh2, zi2, zj2]
    za2 = [value11, kValue, '\n']
    zb2 = [value12, lValue, '\n']
    zc2 = [value13, mValue, '\n']
    zd2 = [value14, nValue, '\n']
    ze2 = [value15, oValue, '\n']
    zf2 = [value16, pValue, '\n']
    zg2 = [value17, qValue, '\n']
    zh2 = [value18, rValue, '\n']
    zi2 = [value19, sValue, '\n']
    zj2 = [value20, tValue, '\n']
    ya2 = [za2, zb2, zc2, zd2, ze2, zf2, zg2, zh2, zi2, zj2]

    zzx2 = sorted(ya2, key=itemgetter(0), reverse=False)
    zzz2 = zzx2

    qa2 = zzx2[0]
    qb2 = zzx2[1]
    qc2 = zzx2[2]
    qd2 = zzx2[3]
    qe2 = zzx2[4]
    qf2 = zzx2[5]
    qg2 = zzx2[6]
    qh2 = zzx2[7]
    qi2 = zzx2[8]
    qj2 = zzx2[9]

    xa2 = qa2[-2]
    xb2 = qb2[-2]
    xc2 = qc2[-2]
    xd2 = qd2[-2]
    xe2 = qe2[-2]
    xf2 = qf2[-2]
    xg2 = qg2[-2]
    xh2 = qh2[-2]
    xi2 = qi2[-2]
    xj2 = qj2[-2]

    ka2 = [xa2]
    kb2 = [xb2]
    kc2 = [xc2]
    kd2 = [xd2]
    ke2 = [xe2]
    kf2 = [xf2]
    kg2 = [xg2]
    kh2 = [xh2]
    ki2 = [xi2]
    kj2 = [xj2]

    xxxx2 = (ka2, kb2, kc2, kd2, ke2, kf2, kg2, kh2, ki2, kj2)

    xxxxx1 = "".join(repr(xxxx2).replace("(['","\n").replace('(["','\n').replace("'], ['", "\n\n").replace('"])', '\n').replace("'])", "\n").replace("'],","\n").replace(" ['","\n").replace('"],','\n').replace(' ["','\n'))
    zzzzz1.set(xxxxx1)
    return

def messagesC3():
    value21 = str(random.randint(0, 9))
    value22 = str(random.randint(0, 9))
    value23 = str(random.randint(0, 9))
    value24 = str(random.randint(0, 9))
    value25 = str(random.randint(0, 9))
    value26 = str(random.randint(0, 9))
    value27 = str(random.randint(0, 9))
    value28 = str(random.randint(0, 9))
    value29 = str(random.randint(0, 9))
    value30 = str(random.randint(0, 9))

    uValue = text21.get()
    vValue = text22.get()
    wValue = text23.get()
    xValue = text24.get()
    yValue = text25.get()
    zValue = text26.get()
    aaValue = text27.get()
    abValue = text28.get()
    acValue = text29.get()
    adValue = text30.get()

    za3 = []
    zb3 = []
    zc3 = []
    zd3 = []
    ze3 = []
    zf3 = []
    zg3 = []
    zh3 = []
    zi3 = []
    zj3 = []

    ya3 = [za3, zb3, zc3, zd3, ze3, zf3, zg3, zh3, zi3, zj3]
    za3 = [value21, uValue, '\n']
    zb3 = [value22, vValue, '\n']
    zc3 = [value23, wValue, '\n']
    zd3 = [value24, xValue, '\n']
    ze3 = [value25, yValue, '\n']
    zf3 = [value26, zValue, '\n']
    zg3 = [value27, aaValue, '\n']
    zh3 = [value28, abValue, '\n']
    zi3 = [value29, acValue, '\n']
    zj3 = [value30, adValue, '\n']
    ya3 = [za3, zb3, zc3, zd3, ze3, zf3, zg3, zh3, zi3, zj3]

    zzx3 = sorted(ya3, key=itemgetter(0), reverse=False)
    zzz3 = zzx3

    qa3 = zzx3[0]
    qb3 = zzx3[1]
    qc3 = zzx3[2]
    qd3 = zzx3[3]
    qe3 = zzx3[4]
    qf3 = zzx3[5]
    qg3 = zzx3[6]
    qh3 = zzx3[7]
    qi3 = zzx3[8]
    qj3 = zzx3[9]

    xa3 = qa3[-2]
    xb3 = qb3[-2]
    xc3 = qc3[-2]
    xd3 = qd3[-2]
    xe3 = qe3[-2]
    xf3 = qf3[-2]
    xg3 = qg3[-2]
    xh3 = qh3[-2]
    xi3 = qi3[-2]
    xj3 = qj3[-2]

    ka3 = [xa3]
    kb3 = [xb3]
    kc3 = [xc3]
    kd3 = [xd3]
    ke3 = [xe3]
    kf3 = [xf3]
    kg3 = [xg3]
    kh3 = [xh3]
    ki3 = [xi3]
    kj3 = [xj3]

    xxxx3 = (ka3, kb3, kc3, kd3, ke3, kf3, kg3, kh3, ki3, kj3)

    xxxxx2 = "".join(repr(xxxx3).replace("(['","\n").replace('(["','\n').replace("'], ['", "\n\n").replace('"])', '\n').replace("'])", "\n").replace("'],","\n").replace(" ['","\n").replace('"],','\n').replace(' ["','\n'))
    zzzzz2.set(xxxxx2)
    return

def messagesC4():
    value31 = str(random.randint(0, 9))
    value32 = str(random.randint(0, 9))
    value33 = str(random.randint(0, 9))
    value34 = str(random.randint(0, 9))
    value35 = str(random.randint(0, 9))
    value36 = str(random.randint(0, 9))
    value37 = str(random.randint(0, 9))
    value38 = str(random.randint(0, 9))
    value39 = str(random.randint(0, 9))
    value40 = str(random.randint(0, 9))

    aeValue = text31.get()
    afValue = text32.get()
    agValue = text33.get()
    ahValue = text34.get()
    aiValue = text35.get()
    ajValue = text36.get()
    akValue = text37.get()
    alValue = text38.get()
    amValue = text39.get()
    anValue = text40.get()

    za4 = []
    zb4 = []
    zc4 = []
    zd4 = []
    ze4 = []
    zf4 = []
    zg4 = []
    zh4 = []
    zi4 = []
    zj4 = []

    ya4 = [za4, zb4, zc4, zd4, ze4, zf4, zg4, zh4, zi4, zj4]
    za4 = [value31, aeValue, '\n']
    zb4 = [value32, afValue, '\n']
    zc4 = [value33, agValue, '\n']
    zd4 = [value34, ahValue, '\n']
    ze4 = [value35, aiValue, '\n']
    zf4 = [value36, ajValue, '\n']
    zg4 = [value37, akValue, '\n']
    zh4 = [value38, alValue, '\n']
    zi4 = [value39, amValue, '\n']
    zj4 = [value40, anValue, '\n']
    ya4 = [za4, zb4, zc4, zd4, ze4, zf4, zg4, zh4, zi4, zj4]

    zzx4 = sorted(ya4, key=itemgetter(0), reverse=False)
    zzz4 = zzx4

    qa4 = zzx4[0]
    qb4 = zzx4[1]
    qc4 = zzx4[2]
    qd4 = zzx4[3]
    qe4 = zzx4[4]
    qf4 = zzx4[5]
    qg4 = zzx4[6]
    qh4 = zzx4[7]
    qi4 = zzx4[8]
    qj4 = zzx4[9]

    xa4 = qa4[-2]
    xb4 = qb4[-2]
    xc4 = qc4[-2]
    xd4 = qd4[-2]
    xe4 = qe4[-2]
    xf4 = qf4[-2]
    xg4 = qg4[-2]
    xh4 = qh4[-2]
    xi4 = qi4[-2]
    xj4 = qj4[-2]

    ka4 = [xa4]
    kb4 = [xb4]
    kc4 = [xc4]
    kd4 = [xd4]
    ke4 = [xe4]
    kf4 = [xf4]
    kg4 = [xg4]
    kh4 = [xh4]
    ki4 = [xi4]
    kj4 = [xj4]

    xxxx4 = (ka4, kb4, kc4, kd4, ke4, kf4, kg4, kh4, ki4, kj4)

    xxxxx3 = "".join(repr(xxxx4).replace("(['","\n").replace('(["','\n').replace("'], ['", "\n\n").replace('"])', '\n').replace("'])", "\n").replace("'],","\n").replace(" ['","\n").replace('"],','\n').replace(' ["','\n'))
    zzzzz3.set(xxxxx3)
    return

def messagesC5():
    value41 = str(random.randint(0, 9))
    value42 = str(random.randint(0, 9))
    value43 = str(random.randint(0, 9))
    value44 = str(random.randint(0, 9))
    value45 = str(random.randint(0, 9))
    value46 = str(random.randint(0, 9))
    value47 = str(random.randint(0, 9))
    value48 = str(random.randint(0, 9))
    value49 = str(random.randint(0, 9))
    value50 = str(random.randint(0, 9))

    aoValue = text41.get()
    apValue = text42.get()
    aqValue = text43.get()
    arValue = text44.get()
    asValue = text45.get()
    atValue = text46.get()
    auValue = text47.get()
    avValue = text48.get()
    awValue = text49.get()
    axValue = text50.get()

    za5 = []
    zb5 = []
    zc5 = []
    zd5 = []
    ze5 = []
    zf5 = []
    zg5 = []
    zh5 = []
    zi5 = []
    zj5 = []

    ya5 = [za5, zb5, zc5, zd5, ze5, zf5, zg5, zh5, zi5, zj5]
    za5 = [value41, aoValue, '\n']
    zb5 = [value42, apValue, '\n']
    zc5 = [value43, aqValue, '\n']
    zd5 = [value44, arValue, '\n']
    ze5 = [value45, asValue, '\n']
    zf5 = [value46, atValue, '\n']
    zg5 = [value47, auValue, '\n']
    zh5 = [value48, avValue, '\n']
    zi5 = [value49, awValue, '\n']
    zj5 = [value50, axValue, '\n']
    ya5 = [za5, zb5, zc5, zd5, ze5, zf5, zg5, zh5, zi5, zj5]

    zzx5 = sorted(ya5, key=itemgetter(0), reverse=False)
    zzz5 = zzx5

    qa5 = zzx5[0]
    qb5 = zzx5[1]
    qc5 = zzx5[2]
    qd5 = zzx5[3]
    qe5 = zzx5[4]
    qf5 = zzx5[5]
    qg5 = zzx5[6]
    qh5 = zzx5[7]
    qi5 = zzx5[8]
    qj5 = zzx5[9]

    xa5 = qa5[-2]
    xb5 = qb5[-2]
    xc5 = qc5[-2]
    xd5 = qd5[-2]
    xe5 = qe5[-2]
    xf5 = qf5[-2]
    xg5 = qg5[-2]
    xh5 = qh5[-2]
    xi5 = qi5[-2]
    xj5 = qj5[-2]

    ka5 = [xa5]
    kb5 = [xb5]
    kc5 = [xc5]
    kd5 = [xd5]
    ke5 = [xe5]
    kf5 = [xf5]
    kg5 = [xg5]
    kh5 = [xh5]
    ki5 = [xi5]
    kj5 = [xj5]

    xxxx5 = (ka5, kb5, kc5, kd5, ke5, kf5, kg5, kh5, ki5, kj5)

    xxxxx4 = "".join(repr(xxxx5).replace("(['","\n").replace('(["','\n').replace("'], ['", "\n\n").replace('"])', '\n').replace("'])", "\n").replace("'],","\n").replace(" ['","\n").replace('"],','\n').replace(' ["','\n'))
    zzzzz4.set(xxxxx4)
    return

def messagesCa():
    value1 = str(random.randint(0, 9))
    value2 = str(random.randint(0, 9))
    value3 = str(random.randint(0, 9))
    value4 = str(random.randint(0, 9))
    value5 = str(random.randint(0, 9))
    value6 = str(random.randint(0, 9))
    value7 = str(random.randint(0, 9))
    value8 = str(random.randint(0, 9))
    value9 = str(random.randint(0, 9))
    value10 = str(random.randint(0, 9))

    aValue = text1.get()
    bValue = text2.get()
    cValue = text3.get()
    dValue = text4.get()
    eValue = text5.get()
    fValue = text6.get()
    gValue = text7.get()
    hValue = text8.get()
    iValue = text9.get()
    jValue = text10.get()

    za = []
    zb = []
    zc = []
    zd = []
    ze = []
    zf = []
    zg = []
    zh = []
    zi = []
    zj = []

    ya = [za, zb, zc, zd, ze, zf, zg, zh, zi, zj]
    za = [value1, aValue, '\n']
    zb = [value2, bValue, '\n']
    zc = [value3, cValue, '\n']
    zd = [value4, dValue, '\n']
    ze = [value5, eValue, '\n']
    zf = [value6, fValue, '\n']
    zg = [value7, gValue, '\n']
    zh = [value8, hValue, '\n']
    zi = [value9, iValue, '\n']
    zj = [value10, jValue, '\n']
    ya = [za, zb, zc, zd, ze, zf, zg, zh, zi, zj]

    zzx = sorted(ya, key=itemgetter(0), reverse=False)
    zzz = zzx

    qa = zzx[0]
    qb = zzx[1]
    qc = zzx[2]
    qd = zzx[3]
    qe = zzx[4]
    qf = zzx[5]
    qg = zzx[6]
    qh = zzx[7]
    qi = zzx[8]
    qj = zzx[9]

    xa = qa[-2]
    xb = qb[-2]
    xc = qc[-2]
    xd = qd[-2]
    xe = qe[-2]
    xf = qf[-2]
    xg = qg[-2]
    xh = qh[-2]
    xi = qi[-2]
    xj = qj[-2]

    ka = [xa]
    kb = [xb]
    kc = [xc]
    kd = [xd]
    ke = [xe]
    kf = [xf]
    kg = [xg]
    kh = [xh]
    ki = [xi]
    kj = [xj]

    xxxx = (ka, kb, kc, kd, ke, kf, kg, kh, ki, kj)

    xxxxx0 = "".join(repr(xxxx).replace("(['","\n").replace('(["','\n').replace("'], ['", "\n\n").replace('"])', '\n').replace("'])", "\n").replace("'],","\n").replace(" ['","\n").replace('"],','\n').replace(' ["','\n'))
    zzzzz0.set(xxxxx0)

    value11 = str(random.randint(0, 9))
    value12 = str(random.randint(0, 9))
    value13 = str(random.randint(0, 9))
    value14 = str(random.randint(0, 9))
    value15 = str(random.randint(0, 9))
    value16 = str(random.randint(0, 9))
    value17 = str(random.randint(0, 9))
    value18 = str(random.randint(0, 9))
    value19 = str(random.randint(0, 9))
    value20 = str(random.randint(0, 9))

    kValue = text11.get()
    lValue = text12.get()
    mValue = text13.get()
    nValue = text14.get()
    oValue = text15.get()
    pValue = text16.get()
    qValue = text17.get()
    rValue = text18.get()
    sValue = text19.get()
    tValue = text20.get()

    za2 = []
    zb2 = []
    zc2 = []
    zd2 = []
    ze2 = []
    zf2 = []
    zg2 = []
    zh2 = []
    zi2 = []
    zj2 = []

    ya2 = [za2, zb2, zc2, zd2, ze2, zf2, zg2, zh2, zi2, zj2]
    za2 = [value11, kValue, '\n']
    zb2 = [value12, lValue, '\n']
    zc2 = [value13, mValue, '\n']
    zd2 = [value14, nValue, '\n']
    ze2 = [value15, oValue, '\n']
    zf2 = [value16, pValue, '\n']
    zg2 = [value17, qValue, '\n']
    zh2 = [value18, rValue, '\n']
    zi2 = [value19, sValue, '\n']
    zj2 = [value20, tValue, '\n']
    ya2 = [za2, zb2, zc2, zd2, ze2, zf2, zg2, zh2, zi2, zj2]

    zzx2 = sorted(ya2, key=itemgetter(0), reverse=False)
    zzz2 = zzx2

    qa2 = zzx2[0]
    qb2 = zzx2[1]
    qc2 = zzx2[2]
    qd2 = zzx2[3]
    qe2 = zzx2[4]
    qf2 = zzx2[5]
    qg2 = zzx2[6]
    qh2 = zzx2[7]
    qi2 = zzx2[8]
    qj2 = zzx2[9]

    xa2 = qa2[-2]
    xb2 = qb2[-2]
    xc2 = qc2[-2]
    xd2 = qd2[-2]
    xe2 = qe2[-2]
    xf2 = qf2[-2]
    xg2 = qg2[-2]
    xh2 = qh2[-2]
    xi2 = qi2[-2]
    xj2 = qj2[-2]

    ka2 = [xa2]
    kb2 = [xb2]
    kc2 = [xc2]
    kd2 = [xd2]
    ke2 = [xe2]
    kf2 = [xf2]
    kg2 = [xg2]
    kh2 = [xh2]
    ki2 = [xi2]
    kj2 = [xj2]

    xxxx2 = (ka2, kb2, kc2, kd2, ke2, kf2, kg2, kh2, ki2, kj2)

    xxxxx1 = "".join(repr(xxxx2).replace("(['","\n").replace('(["','\n').replace("'], ['", "\n\n").replace('"])', '\n').replace("'])", "\n").replace("'],","\n").replace(" ['","\n").replace('"],','\n').replace(' ["','\n'))
    zzzzz1.set(xxxxx1)

    value21 = str(random.randint(0, 9))
    value22 = str(random.randint(0, 9))
    value23 = str(random.randint(0, 9))
    value24 = str(random.randint(0, 9))
    value25 = str(random.randint(0, 9))
    value26 = str(random.randint(0, 9))
    value27 = str(random.randint(0, 9))
    value28 = str(random.randint(0, 9))
    value29 = str(random.randint(0, 9))
    value30 = str(random.randint(0, 9))

    uValue = text21.get()
    vValue = text22.get()
    wValue = text23.get()
    xValue = text24.get()
    yValue = text25.get()
    zValue = text26.get()
    aaValue = text27.get()
    abValue = text28.get()
    acValue = text29.get()
    adValue = text30.get()

    za3 = []
    zb3 = []
    zc3 = []
    zd3 = []
    ze3 = []
    zf3 = []
    zg3 = []
    zh3 = []
    zi3 = []
    zj3 = []

    ya3 = [za3, zb3, zc3, zd3, ze3, zf3, zg3, zh3, zi3, zj3]
    za3 = [value21, uValue, '\n']
    zb3 = [value22, vValue, '\n']
    zc3 = [value23, wValue, '\n']
    zd3 = [value24, xValue, '\n']
    ze3 = [value25, yValue, '\n']
    zf3 = [value26, zValue, '\n']
    zg3 = [value27, aaValue, '\n']
    zh3 = [value28, abValue, '\n']
    zi3 = [value29, acValue, '\n']
    zj3 = [value30, adValue, '\n']
    ya3 = [za3, zb3, zc3, zd3, ze3, zf3, zg3, zh3, zi3, zj3]

    zzx3 = sorted(ya3, key=itemgetter(0), reverse=False)
    zzz3 = zzx3

    qa3 = zzx3[0]
    qb3 = zzx3[1]
    qc3 = zzx3[2]
    qd3 = zzx3[3]
    qe3 = zzx3[4]
    qf3 = zzx3[5]
    qg3 = zzx3[6]
    qh3 = zzx3[7]
    qi3 = zzx3[8]
    qj3 = zzx3[9]

    xa3 = qa3[-2]
    xb3 = qb3[-2]
    xc3 = qc3[-2]
    xd3 = qd3[-2]
    xe3 = qe3[-2]
    xf3 = qf3[-2]
    xg3 = qg3[-2]
    xh3 = qh3[-2]
    xi3 = qi3[-2]
    xj3 = qj3[-2]

    ka3 = [xa3]
    kb3 = [xb3]
    kc3 = [xc3]
    kd3 = [xd3]
    ke3 = [xe3]
    kf3 = [xf3]
    kg3 = [xg3]
    kh3 = [xh3]
    ki3 = [xi3]
    kj3 = [xj3]

    xxxx3 = (ka3, kb3, kc3, kd3, ke3, kf3, kg3, kh3, ki3, kj3)

    xxxxx2 = "".join(repr(xxxx3).replace("(['","\n").replace('(["','\n').replace("'], ['", "\n\n").replace('"])', '\n').replace("'])", "\n").replace("'],","\n").replace(" ['","\n").replace('"],','\n').replace(' ["','\n'))
    zzzzz2.set(xxxxx2)

    value31 = str(random.randint(0, 9))
    value32 = str(random.randint(0, 9))
    value33 = str(random.randint(0, 9))
    value34 = str(random.randint(0, 9))
    value35 = str(random.randint(0, 9))
    value36 = str(random.randint(0, 9))
    value37 = str(random.randint(0, 9))
    value38 = str(random.randint(0, 9))
    value39 = str(random.randint(0, 9))
    value40 = str(random.randint(0, 9))

    aeValue = text31.get()
    afValue = text32.get()
    agValue = text33.get()
    ahValue = text34.get()
    aiValue = text35.get()
    ajValue = text36.get()
    akValue = text37.get()
    alValue = text38.get()
    amValue = text39.get()
    anValue = text40.get()

    za4 = []
    zb4 = []
    zc4 = []
    zd4 = []
    ze4 = []
    zf4 = []
    zg4 = []
    zh4 = []
    zi4 = []
    zj4 = []

    ya4 = [za4, zb4, zc4, zd4, ze4, zf4, zg4, zh4, zi4, zj4]
    za4 = [value31, aeValue, '\n']
    zb4 = [value32, afValue, '\n']
    zc4 = [value33, agValue, '\n']
    zd4 = [value34, ahValue, '\n']
    ze4 = [value35, aiValue, '\n']
    zf4 = [value36, ajValue, '\n']
    zg4 = [value37, akValue, '\n']
    zh4 = [value38, alValue, '\n']
    zi4 = [value39, amValue, '\n']
    zj4 = [value40, anValue, '\n']
    ya4 = [za4, zb4, zc4, zd4, ze4, zf4, zg4, zh4, zi4, zj4]

    zzx4 = sorted(ya4, key=itemgetter(0), reverse=False)
    zzz4 = zzx4

    qa4 = zzx4[0]
    qb4 = zzx4[1]
    qc4 = zzx4[2]
    qd4 = zzx4[3]
    qe4 = zzx4[4]
    qf4 = zzx4[5]
    qg4 = zzx4[6]
    qh4 = zzx4[7]
    qi4 = zzx4[8]
    qj4 = zzx4[9]

    xa4 = qa4[-2]
    xb4 = qb4[-2]
    xc4 = qc4[-2]
    xd4 = qd4[-2]
    xe4 = qe4[-2]
    xf4 = qf4[-2]
    xg4 = qg4[-2]
    xh4 = qh4[-2]
    xi4 = qi4[-2]
    xj4 = qj4[-2]

    ka4 = [xa4]
    kb4 = [xb4]
    kc4 = [xc4]
    kd4 = [xd4]
    ke4 = [xe4]
    kf4 = [xf4]
    kg4 = [xg4]
    kh4 = [xh4]
    ki4 = [xi4]
    kj4 = [xj4]

    xxxx4 = (ka4, kb4, kc4, kd4, ke4, kf4, kg4, kh4, ki4, kj4)

    xxxxx3 = "".join(repr(xxxx4).replace("(['","\n").replace('(["','\n').replace("'], ['", "\n\n").replace('"])', '\n').replace("'])", "\n").replace("'],","\n").replace(" ['","\n").replace('"],','\n').replace(' ["','\n'))
    zzzzz3.set(xxxxx3)
    
    value41 = str(random.randint(0, 9))
    value42 = str(random.randint(0, 9))
    value43 = str(random.randint(0, 9))
    value44 = str(random.randint(0, 9))
    value45 = str(random.randint(0, 9))
    value46 = str(random.randint(0, 9))
    value47 = str(random.randint(0, 9))
    value48 = str(random.randint(0, 9))
    value49 = str(random.randint(0, 9))
    value50 = str(random.randint(0, 9))

    aoValue = text41.get()
    apValue = text42.get()
    aqValue = text43.get()
    arValue = text44.get()
    asValue = text45.get()
    atValue = text46.get()
    auValue = text47.get()
    avValue = text48.get()
    awValue = text49.get()
    axValue = text50.get()

    za5 = []
    zb5 = []
    zc5 = []
    zd5 = []
    ze5 = []
    zf5 = []
    zg5 = []
    zh5 = []
    zi5 = []
    zj5 = []

    ya5 = [za5, zb5, zc5, zd5, ze5, zf5, zg5, zh5, zi5, zj5]
    za5 = [value41, aoValue, '\n']
    zb5 = [value42, apValue, '\n']
    zc5 = [value43, aqValue, '\n']
    zd5 = [value44, arValue, '\n']
    ze5 = [value45, asValue, '\n']
    zf5 = [value46, atValue, '\n']
    zg5 = [value47, auValue, '\n']
    zh5 = [value48, avValue, '\n']
    zi5 = [value49, awValue, '\n']
    zj5 = [value50, axValue, '\n']
    ya5 = [za5, zb5, zc5, zd5, ze5, zf5, zg5, zh5, zi5, zj5]

    zzx5 = sorted(ya5, key=itemgetter(0), reverse=False)
    zzz5 = zzx5

    qa5 = zzx5[0]
    qb5 = zzx5[1]
    qc5 = zzx5[2]
    qd5 = zzx5[3]
    qe5 = zzx5[4]
    qf5 = zzx5[5]
    qg5 = zzx5[6]
    qh5 = zzx5[7]
    qi5 = zzx5[8]
    qj5 = zzx5[9]

    xa5 = qa5[-2]
    xb5 = qb5[-2]
    xc5 = qc5[-2]
    xd5 = qd5[-2]
    xe5 = qe5[-2]
    xf5 = qf5[-2]
    xg5 = qg5[-2]
    xh5 = qh5[-2]
    xi5 = qi5[-2]
    xj5 = qj5[-2]

    ka5 = [xa5]
    kb5 = [xb5]
    kc5 = [xc5]
    kd5 = [xd5]
    ke5 = [xe5]
    kf5 = [xf5]
    kg5 = [xg5]
    kh5 = [xh5]
    ki5 = [xi5]
    kj5 = [xj5]

    xxxx5 = (ka5, kb5, kc5, kd5, ke5, kf5, kg5, kh5, ki5, kj5)

    xxxxx4 = "".join(repr(xxxx5).replace("(['","\n").replace('(["','\n').replace("'], ['", "\n\n").replace('"])', '\n').replace("'])", "\n").replace("'],","\n").replace(" ['","\n").replace('"],','\n').replace(' ["','\n'))
    zzzzz4.set(xxxxx4)
    return
	
def wjWindow2():
    global window2, zzzzz0, zzzzz1, zzzzz2, zzzzz3, zzzzz4, message1, message2z, message3z, message4z, message5z
    
    window2 = Toplevel(app)
    window2.title(string="WJ-Rearrangements")
    window2.geometry("900x280")
    zzzzz0 = StringVar()
    message1 = Label(window2, textvariable=zzzzz0)
    message1.pack(side=LEFT)
    zzzzz1 = StringVar()
    message2z = Label(window2, textvariable=zzzzz1)
    message2z.pack(side=LEFT)
    zzzzz2 = StringVar()
    message3z = Label(window2, textvariable=zzzzz2)
    message3z.pack(side=LEFT)
    zzzzz3 = StringVar()
    message4z = Label(window2, textvariable=zzzzz3)
    message4z.pack(side=LEFT)
    zzzzz4 = StringVar()
    message5z = Label(window2, textvariable=zzzzz4)
    message5z.pack(side=LEFT)
    return

wj2 = wjWindow2()
window2.withdraw()

def wjWindow3():
    global window3, message4
    
    window3 = Toplevel(app)
    window3.title(string="WJ-Directory")
    message2 = Label(window3, text=" ").pack()
    message2 = Label(window3, text="Current Directory").pack()
    message2 = Label(window3, text="CTRL-C to Copy, CTRL-V to Paste").pack()
    message2 = Label(window3, text=" ").pack()
    message4 = Text(window3, height=30, width=45)
    scroll3 = Scrollbar(window3, command=message4.yview)
    message4.configure(yscrollcommand=scroll3.set)
    message4.pack(side=LEFT)
    scroll3.pack(side=RIGHT, fill=Y)
    return

wj3 = wjWindow3()
window3.withdraw()

def wjWindow4():
    global window4, text11z
    
    window4 = Toplevel(app)
    window4.title(string="WJ-From The Directory")
    window4.geometry("240x140")
    message2 = Label(window4, text=" ").pack()
    message2 = Label(window4, text="Working Data File:").pack()
    message2 = Label(window4, text="Include extension").pack()
    message2 = Label(window4, text=" ").pack()
    someFile = StringVar()
    text11z = Entry(window4, textvariable=someFile)
    text11z.config(width=30)
    text11z.pack()
    return

wj4 = wjWindow4()
window4.withdraw()

def wjWindow5():
    global window5
    
    window5 = Toplevel(app)
    window5.title(string="WJ-Action Buttons")
    window5.geometry("200x390")
    message2 = Label(window5, text=" ").pack()
    save_text = Button(window5, command=savas5, text="Save, With Date And Time").pack()
    message2 = Label(window5, text=" ").pack()
    update_text = Button(window5, command=messagesCa, text="Rearrange, All Rows").pack()
    message2 = Label(window5, text=" ").pack()
    update1_text = Button(window5, command=messagesC1, text="Rearrange, Column 1").pack()
    message2 = Label(window5, text=" ").pack()
    update2_text = Button(window5, command=messagesC2, text="Rearrange, Column 2").pack()
    message2 = Label(window5, text=" ").pack()
    update3_text = Button(window5, command=messagesC3, text="Rearrange, Column 3").pack()
    message2 = Label(window5, text=" ").pack()
    update4_text = Button(window5, command=messagesC4, text="Rearrange, Column 4").pack()
    message2 = Label(window5, text=" ").pack()
    update5_text = Button(window5, command=messagesC5, text="Rearrange, Column 5").pack()
    message2 = Label(window5, text=" ").pack()
    fill_text = Button(window5, command=getfiles7, text="Fill All Rows From File").pack()
    message2 = Label(window5, text=" ").pack()
    getThose_files = Button(window5, command=getfiles5, text="List Files Of Current Directory").pack()
    return

wj5 = wjWindow5()
window5.withdraw()

app.mainloop()
