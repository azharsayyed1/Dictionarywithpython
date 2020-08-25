from tkinter import *
from tkinter import messagebox
import json
from difflib import get_close_matches  # for close matches

#tect to specch
import  pyttsx3
#we need to instantiate the engine which will helo to convert text into speech
engine=pyttsx3.init() # we will be able use al meothods of engine
voicess=engine.getProperty('voices')
engine.setProperty('voice',voicess[1].id)

#rate=engine.getProperty('rate') for the speed
#engine.setProperty('rate',300)

def wordaudio():
    engine.say(enterwordentry.get())
    engine.runAndWait()

def readout():
    engine.say(textarea.get(1.0,END))
    engine.runAndWait()



# defining funtion for xit button
def iexit():
    res = messagebox.askyesno('confirm', 'Do you want to exit?')  # if it returns true exit stire in res
    if res == True:
        root.destroy()
    else:
        pass


def clear():
    textarea.config(state=NORMAL)
    enterwordentry.delete(0, END)  # to clear from start to end
    textarea.delete(1.0, END)  # to clear textarea from end # text start with 1.0 2.0 it takes float values
    textarea.config(state=DISABLED)

# search first data will be loaded , whatever we wtite in entery will store in word , check if word exsit in data  then we will pass the word and will be stored in meaning varibale we dont want list we want meaning to be displyed
def Search():
    data = json.load(open('data.json'))  # load data from json file first import #store in data varibale
    word = enterwordentry.get()

    word = word.lower()  # to convert uppercase into lower case

    if word in data:
        meaning = data[word]  # print(data[word]) #        textarea.insert(END,data[word])
        textarea.config(state=NORMAL)
        textarea.delete(1.0, END)  # if anything is left in text area
        for item in meaning:
            textarea.insert(END, u'\u2022' + item + '\n\n')  # u20200 represnation of bullet symbo

        textarea.config(state=DISABLED) # to let not edit it

    elif len(get_close_matches(word, data.keys())) > 0:

        close_match = get_close_matches(word, data.keys())[0]
        res = messagebox.askyesno('confirm', 'Did you mean' + '\n\n ' + close_match + 'instead ?')

        if res == True:
            meaning = data[close_match]
            textarea.delete(1.0, END)
            textarea.config(state=NORMAL)
            for item in meaning:
                textarea.insert(END, u'\u2022' + item + '\n\n')

                textarea.config(state=DISABLED)

                # textarea.insert(END,data[close_match])

        else:
            messagebox.showinfo('Information', 'Please type correct words')
            enterwordentry.delete(0, END)

    else:
        messagebox.showerror('Error', 'The word doesnt exisit please check again')
        enterwordentry.delete(0, END)


root = Tk()

root.geometry('1000x626+100+50')
root.title('talking dic by azzy')
root.resizable(0, 0)  # for fix size
bgimage = PhotoImage(file='bg.png')
bglabel = Label(root, image=bgimage)  # grid place pack
bglabel.place(x=0, y=0)
# entry filed and text filed

enterwordlabel = Label(root, text='Enter the word', font=('casetellar', 29, 'bold'), fg='red3', bg='whitesmoke')
enterwordlabel.place(x=530, y=20)  # distance in our root

enterwordentry = Entry(root, font=('arial', 20, 'bold'), bd=8, relief=GROOVE,
                       justify='center')  # text filed is known as entry fileied
# relief is giving styling justify will center thext

enterwordentry.place(x=510, y=80)

enterwordentry.focus_set()

searchimage = PhotoImage(file='search.png')
searchButton = Button(root, image=searchimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                      command=Search)
searchButton.place(x=650, y=150)

micimage = PhotoImage(file='mic.png')
micButoon = Button(root, image=micimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',command=wordaudio)
micButoon.place(x=710, y=153)

meaningLabel = Label(root, text='Meaning', font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')
meaningLabel.place(x=580, y=240)

textarea = Text(root, font=('arial', 18, 'bold'), height=8, width=34, bd=8, relief=GROOVE, wrap='word')
textarea.place(x=460, y=300)

audioimage = PhotoImage(file='microphone.png')
audiobutton = Button(root, image=audioimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',command=readout)
audiobutton.place(x=530, y=555)

clearimage = PhotoImage(file='clear.png')
clearbutton = Button(root, image=clearimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                     command=clear)
clearbutton.place(x=660, y=555)

exitimage = PhotoImage(file='exit.png')
exitbutton = Button(root, image=exitimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                    command=iexit)
exitbutton.place(x=790, y=555)

root.mainloop()
