import tkinter as tk
import pymongo

#connect to database

client =pymongo.MongoClient("mongodb://localhost:27017/")
db= client ["messageapp"]
message_col=db["messages"]

#Tkinter GUI
root=tk.Tk()
root.title("messageapp")

enrty=tk.Entry(root,width=40)
enrty.pack(pady=5)

def send_message():
    if enrty.get():
        message_col.insert_one ({"text":enrty.get()})
        enrty.delete(0,tk.END)

#steg 1 stage code = git add .
#steg 2 commit code= git commit -m "commit done"
#steg 3 push code = git push


send_button=tk.Button(root,text= "send", command=send_message)
send_button.pack(pady=5)

messages_label=tk.Label(root, text="Messages:\n" ,justify="left")
messages_label.pack()

root.mainloop()