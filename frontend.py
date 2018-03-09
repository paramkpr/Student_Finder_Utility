#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Created on Sat Oct 28 00:55:37 2017

#@author: Param Kapur, paramkapur2002@gmail.com

from tkinter import *
import backend
global row

#=============================================================================
#BACKEND CONNECTION FOR BUTTON COMMANDS
#=============================================================================

def get_selected_row(event):
    try:
        global selected_tuple
        index = display_list1.curselection()[0]
        selected_tuple = display_list1.get(index)
        #CLASS
        classe1.delete(0, END)
        classe1.insert(END, selected_tuple[1])
        #SECTION
        sece1.delete(0, END)
        sece1.insert(END, selected_tuple[2])
        #NAME
        namee1.delete(0, END)
        namee1.insert(END, selected_tuple[3])
        #PHONE NUMBER
        noe1.delete(0, END)
        noe1.insert(END, selected_tuple[4])
        #GENDER
        gendere1.delete(0, END)
        gendere1.insert(END, selected_tuple[5])
        #CATEGORY
        cate1.delete(0, END)
        cate1.insert(END, selected_tuple[6])
        #ACTIVITES
        baskete1.delete(0, END)
        baskete1.insert(END, selected_tuple[7])
        voce1.delete(0, END) 
        voce1.insert(END, selected_tuple[8])    
        feilde1.delete(0, END)
        feilde1.insert(END, selected_tuple[9])
        quize1.delete(0, END)
        quize1.insert(END, selected_tuple[10])
        otre1.delete(0, END)
        otre1.insert(END, selected_tuple[11])
        tte1.delete(0, END)
        tte1.insert(END, selected_tuple[12])
        dre1.delete(0, END)
        dre1.insert(END, selected_tuple[13])
        trke1.delete(0, END)
        trke1.insert(END, selected_tuple[14])
        bate1.delete(0, END)
        bate1.insert(END, selected_tuple[15])
        swime1.delete(0, END)
        swime1.insert(END, selected_tuple[16])
        foote1.delete(0, END)
        foote1.insert(END, selected_tuple[17])
        musice1.delete(0, END)
        musice1.insert(END, selected_tuple[18])
        #EMAIL
        maile1.delete(0, END)
        maile1.insert(END, selected_tuple[19])
    except IndexError: 
        pass
        
def view_command():
    display_list1.delete(0, END)
    for row in backend.view():
        display_list1.insert(END, row)

def search_command():
    display_list1.delete(0, END)
    for row in backend.search(class_text.get(), sec.get(), name_text.get(), 
                              no.get(), gender_text.get(), category.get(),
                              bb_intrest.get(), voc_interest.get(), 
                              feild_interest.get(), quiz_interest.get(), 
                              otr_interest.get(), tt_interest.get(), 
                              dr_interest.get(), trk_interest.get(),
                              bat_interest.get(), swim_interest.get(), 
                              foot_interest.get(), music_interest.get(), 
                              mail.get()
                              ):
        display_list1.insert(END, row)
        
def add_command():
    backend.insert(class_text.get(), sec.get(), name_text.get(), 
                   no.get(), gender_text.get(), category.get(),
                   bb_intrest.get(), voc_interest.get(), 
                   feild_interest.get(), quiz_interest.get(), 
                   otr_interest.get(), tt_interest.get(), 
                   dr_interest.get(), trk_interest.get(),
                   bat_interest.get(), swim_interest.get(), 
                   foot_interest.get(), music_interest.get(), mail.get())
    display_list1.delete(0, END)
    display_list1.insert(END, (class_text.get(), sec.get(), name_text.get(), 
                   no.get(), gender_text.get(), category.get(),
                   bb_intrest.get(), voc_interest.get(), 
                   feild_interest.get(), quiz_interest.get(), 
                   otr_interest.get(), tt_interest.get(), 
                   dr_interest.get(), trk_interest.get(),
                   bat_interest.get(), swim_interest.get(), 
                   foot_interest.get(), music_interest.get(), 
                   mail.get()))

def delete_command():
    backend.delete(selected_tuple[0])
    
def update_command():
    backend.update(selected_tuple[0], class_text.get(), sec.get(), 
                   name_text.get(),no.get(), gender_text.get(), category.get(),
                   bb_intrest.get(), voc_interest.get(), 
                   feild_interest.get(), quiz_interest.get(), 
                   otr_interest.get(), tt_interest.get(), 
                   dr_interest.get(), trk_interest.get(),
                   bat_interest.get(), swim_interest.get(), 
                   foot_interest.get(), music_interest.get(), 
                   mail.get())

def clear():
    #CLASS
    classe1.delete(0, END)
    classe1.insert(0, "")
    #SECTION
    sece1.delete(0, END)
    sece1.insert(0, "")
    #NAME
    namee1.delete(0, END)
    namee1.insert(0, "")
    #PHONE NUMBER
    noe1.delete(0, END)
    noe1.insert(0, "")
    #GENDER
    gendere1.delete(0, END)
    gendere1.insert(0, "")
    #CATEGORY
    cate1.delete(0, END)
    cate1.insert(0, "")
    #ACTIVITES
    baskete1.delete(0, END)
    baskete1.insert(0, "")
    voce1.delete(0, END) 
    voce1.insert(0, "")    
    feilde1.delete(0, END)
    feilde1.insert(0, "")
    quize1.delete(0, END)
    quize1.insert(0, "")
    otre1.delete(0, END)
    otre1.insert(0, "")
    tte1.delete(0, END)
    tte1.insert(0, "")
    dre1.delete(0, END)
    dre1.insert(0, "")
    trke1.delete(0, END)
    trke1.insert(0, "")
    bate1.delete(0, END)
    bate1.insert(0, "")
    swime1.delete(0, END)
    swime1.insert(0, "")
    foote1.delete(0, END)
    foote1.insert(0, "")
    musice1.delete(0, END)
    musice1.insert(0, "")
    #EMAIL
    maile1.delete(0, END)
    maile1.insert(0, "")
    
    execpt 
def cred():
    cwin = Tk()
    
    cwin.wm_title("Credits")
    
    credl1 = Label(cwin, text = """This program was created by Param Kapur\n
                   Email: paramkapur2002@gmail.com""")
    credl1.grid(row = 0, column = 0)
    cwin.mainloop()
#=============================================================================
#GUI CODE
#=============================================================================

global window
window= Tk()

window.wm_title("Student Lookup")


#NAME-------------------------------------------------------------------------

namel1= Label(window,text = "Name")
namel1.grid(row = 0,column = 0)

name_text = StringVar()
namee1 = Entry(window, textvariable = name_text)
namee1.grid(row = 0, column = 1)

#MISC-------------------------------------------------------------------------

nosearchl1 = Label(window, text="No-Search Feilds:")
nosearchl1.grid(row = 15, column = 0)

#CLASS------------------------------------------------------------------------

classl1 = Label(window, text = "Grade")
classl1.grid(row = 0, column = 2)

class_text = StringVar()
classe1 = Entry(window, textvariable = class_text, width = 4)
classe1.grid(row = 0, column = 3)

#GENDER-----------------------------------------------------------------------

genderl1 = Label(window, text = "Gender in M/F")
genderl1.grid(row = 0, column = 4)


gender_text = StringVar()
gendere1 = Entry(window, textvariable = gender_text, width = 4)
gendere1.grid(row = 0, column = 5)

#SECTION----------------------------------------------------------------------

secl1 = Label(window, text = "Section")
secl1.grid(row = 0, column = 8)

sec = StringVar()
sece1 = Entry(window, textvariable = sec, width = 2)
sece1.grid(row = 0, column = 9)

#PHONE NUMBER-----------------------------------------------------------------

nol1 = Label(window, text = "Phone Number")
nol1.grid(row = 15, column = 1)

no = StringVar()
noe1 = Entry(window, textvariable = no, width = 10)
noe1.grid(row = 15, column = 2)

#EMAIL-----------------------------------------------------------------------

maill1 = Label(window, text= "Email")
maill1.grid(row = 15, column = 3)

mail = StringVar()
maile1 = Entry(window, textvariable = mail, width =27)
maile1.grid(row = 15, column = 4)

#CATEGORY---------------------------------------------------------------------

catl1 = Label(window, text = "Category")
catl1.grid(row = 16, column = 1)

category = StringVar()
cate1 = Entry(window, textvariable = category, width = 8)
cate1.grid(row = 16, column = 2)

#BASKETBALL-------------------------------------------------------------------

basketl1 = Label(window, text = "Basketball")
basketl1.grid(row = 3, column = 0)

bb_intrest = IntVar()
baskete1 = Entry(window, textvariable = bb_intrest, width = 2)
baskete1.grid(row = 3, column = 1)

#VOCATIONAL-------------------------------------------------------------------

vocl1 = Label(window, text = "Vocational")
vocl1.grid(row = 4, column = 0)

voc_interest = IntVar()
voce1 = Entry(window,textvariable = voc_interest, width = 2)
voce1.grid(row = 4, column = 1)

#FEILD------------------------------------------------------------------------

feildl1 = Label(window,text = "Feild")
feildl1.grid(row = 5, column = 0)

feild_interest = IntVar()
feilde1 = Entry(window,textvariable = feild_interest, width = 2)
feilde1.grid(row = 5, column = 1)

#QUIZ-------------------------------------------------------------------------

quizl1 = Label(window,text = "Quiz")
quizl1.grid(row = 6, column = 0)

quiz_interest = IntVar()
quize1 = Entry(window,textvariable = quiz_interest, width = 2)
quize1.grid(row = 6, column = 1)

#OTHER EVENTS-----------------------------------------------------------------

otrl1 = Label(window,text= "Other Events")
otrl1.grid(row = 7, column = 0)

otr_interest = IntVar()
otre1 = Entry(window,textvariable = otr_interest, width = 2)
otre1.grid(row = 7, column = 1)

#TABLE TENNIS-----------------------------------------------------------------

ttl1 = Label(window,text="Table Tennis")
ttl1.grid(row = 8, column = 0)

tt_interest = IntVar()
tte1 = Entry(window,textvariable = tt_interest, width = 2)
tte1.grid(row = 8, column = 1)

#DRAMA------------------------------------------------------------------------

drl1 = Label(window,text = "Drama")
drl1.grid(row = 9, column = 0)

dr_interest = IntVar()
dre1 = Entry(window,textvariable = dr_interest, width = 2)
dre1.grid(row = 9, column = 1)

#TRACK------------------------------------------------------------------------

trkl1 = Label(window, text = "Track")
trkl1.grid(row = 10, column = 0)

trk_interest = IntVar()
trke1 = Entry(window, textvariable = trk_interest, width = 2)
trke1.grid(row = 10, column = 1)

#CRICKET----------------------------------------------------------------------

batl1 = Label(window, text = "Cricket")
batl1.grid(row = 11, column = 0)

bat_interest = IntVar()
bate1 = Entry(window, textvariable = bat_interest, width = 2)
bate1.grid(row = 11, column = 1)

#SWIMMING---------------------------------------------------------------------

swiml1 = Label(window, text = "Swimming")
swiml1.grid(row = 12, column = 0)

swim_interest = IntVar()
swime1 = Entry(window, textvariable = swim_interest, width = 2)
swime1.grid(row = 12, column = 1)

#FOOTBALL---------------------------------------------------------------------

footl1 = Label(window, text= "Football")
footl1.grid(row =13, column= 0)

foot_interest = IntVar()
foote1 = Entry(window, textvariable = foot_interest, width = 2)
foote1.grid(row = 13, column = 1)

#MUSIC------------------------------------------------------------------------

musicl1 = Label(window, text = "Music")
musicl1.grid(row = 14, column = 0)

music_interest = IntVar()
musice1 = Entry(window, textvariable = music_interest, width = 2)
musice1.grid(row = 14, column = 1)

#LISTBOX----------------------------------------------------------------------

display_list1 = Listbox(window, height = 20, width = 40)
display_list1.grid(row = 1, column = 2, columnspan = 5, rowspan = 14)

#SCROLLBAR FOR LISTBOX
scroll1 = Scrollbar(window)
scroll1.grid(row = 1 ,column = 6, rowspan = 13)

#CONNECTION LISTBOX AND SCROLLBAR
display_list1.config(yscrollcommand=scroll1.set)
scroll1.config(command = display_list1.yview)

display_list1.bind('<<ListboxSelect>>',get_selected_row)

#SEARCH BUTTON----------------------------------------------------------------

b1 = Button(window, text = "Search", width = 12, command = search_command)
b1.grid(row = 3, column = 8)

b2 = Button(window, text = "View All", width = 12, command = view_command)
b2.grid(row = 4, column = 8)

b3 = Button(window, text = "Delete Selected", width = 12, 
            command = delete_command)
b3.grid(row = 5, column = 8)

b4 = Button(window, text = "Update Selected", width = 12, 
            command = update_command)
b4.grid(row = 6, column = 8)

b5 = Button(window, text = "Add Entry", width = 12, command = add_command)
b5.grid(row = 7, column = 8)

b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row = 14, column = 8)

b7 = Button(window, text = "Clear All", width = 12, command = clear)
b7.grid(row = 8, column = 8)

b8 = Button(window, text = "Credits", width = 12, command = cred)
b8.grid(row =13, column = 8)

window.mainloop()