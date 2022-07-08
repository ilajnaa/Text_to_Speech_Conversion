from tkinter import *
from tkinter import filedialog
import pyttsx3
import PyPDF2
import tkinter as tk

root = Tk()
root.title("TEXT TO SPEECH CONVERSION")
root.geometry('350x350')

label_page = Label(root, text="Starting Page Number").pack()
start_page_number = Entry(root)
start_page_number.pack()

label_page = Label(root, text="Ending Page Number").pack()
end_page_number = Entry(root)
end_page_number.pack()

label = Label(root, text="Which PDF Document do you want to read?").pack()

def fileDialog():
    path = filedialog.askopenfilename()
    book = open(path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speaker = pyttsx3.init()
    
    for num in range(int(start_page_number.get()), int(end_page_number.get())+1):
        page = pdfReader.getPage(num-1)
        txt = page.extractText()
        speaker.say(txt)
        speaker.runAndWait()
Button(root, text="Choose PDF", command=fileDialog).pack()

label_page = Label(root, text="OR\nEnter Text Manually").pack()
inputtxt = tk.Text(root,height = 5,width = 20)
inputtxt.pack()

def manual_text():
    answer = inputtxt.get(1.0, "end-1c")
    text_speech = pyttsx3.init()
    text_speech.say(answer)
    text_speech.runAndWait()

Button(root, text="Listen", command=manual_text).pack()

root.mainloop()