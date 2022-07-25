from tkinter import *
import playlist_download as pd
import threading

window = Tk()
window.title("Youtube Video Downloader")
window.minsize(500, 200)

urltext = Label(text="Enter Playlist URL");
urltext.pack()

url_box = Entry(width=50)
url_box.pack()

class List_Box():
    def __init__(self, list):
        self.list = list

    def show_listbox(self):
        self.scrollbar = Scrollbar()
        self.scrollbar.pack(side = RIGHT, fill = Y)
        self.listbox = Listbox(width=100, selectmode=EXTENDED, yscrollcommand = self.scrollbar.set)
        for video in self.list:
            self.listbox.insert(END, video[0])
            # label = Label(text = video[0]).pack()
        self.listbox.pack(side=LEFT, fill=BOTH)
        self.scrollbar.config(command = self.listbox.yview)

    def remove_listbox(self):
        self.scrollbar.destroy();
        self.listbox.destroy();

    def get_selected_items(self):
        self.selected_item_indices = self.listbox.curselection();
        print(self.selected_item_indices)

def download_videos():
    playlist_url = url_box.get()
    label = Label(text="Please wait...")
    label.pack()
    link_list = pd.fetch_videos(playlist_url)

    label.destroy()
    Label(text="Videos found in the playlist are:").pack()

    list_box = List_Box(link_list)
    list_box.show_listbox()

    getButton = Button(text = "Get", command = list_box.get_selected_items())
    getButton.pack()


def start_new_thread():
    x = threading.Thread(target=download_videos)
    x.start()


url_submit_button = Button(text = "Submit", command = start_new_thread)
url_submit_button.pack()


window.mainloop()
