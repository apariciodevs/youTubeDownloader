import tkinter
import customtkinter
from pytube import YouTube



def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")

        video.download()
        finishLabel.configure(text="Downloaded!")    
    except:
        finishLabel.configure(text="Invalid link", text_color="red")



def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(percentage_of_completion)
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()


    # update progress bar
    progressBar.set(float(percentage_of_completion) / 100)
    
    


# system settings
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green




app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")
app.title("Youtube downloader bot")




#Ui elements
title = customtkinter.CTkLabel(app, text='Insert YouTube video link')
title.pack(padx=10, pady=10)


#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()



# progress bar
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)


# download btn

download = customtkinter.CTkButton(app, text='download', command=startDownload)
download.pack(padx=10, pady=10)


app.mainloop()