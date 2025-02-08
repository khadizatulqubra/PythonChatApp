import tkinter as tk
import pymongo

#connect to database

client =pymongo.MongoClient("mongodb://localhost:27017/")
db= client ["messageapp"]
message_col=["messages"]

#Tkinter GUI
root=tk.Tk()
root.title("messageapp")

enrty=tk.Entry(root,width=40)
enrty.pack(pady=5)

root.mainloop()