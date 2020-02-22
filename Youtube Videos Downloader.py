import pytube
import tkinter
from tkinter import *
window = Tk()
window.geometry("400x400")
window.title("YouTube-Download")

def download():
    video_url = fn.get()
    youtube = pytube.YouTube(video_url)
    video = youtube.streams.first()
    video.download("C:/Users/PeakyBlinder/Downloads")


fn = StringVar()
text = Label(window, text = "Download videos",fg = 'pink', bg = 'purple', font = ("arial", 15, "bold")).pack()
text2 = Label(window, text = "Insert URL",fg = 'black', font = ("arial", 10, "bold")).place(x =0 , y = 50)
urlll = Entry(window, textvar= fn).place(x = 100, y= 50)

download = Button(window, text = "Download", fg = 'white', bg = 'pink', font = ("arial", 10, "bold"), command = download). place(x=250, y= 45)
window.mainloop()




