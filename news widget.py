from tkinter import *
import json
import requests

root=Tk()
root.title("News Widget")
root.geometry("600x500")
root.overrideredirect(FALSE)

label = Label(root,text="BBC NEWS UPDATE")
label.place(relx=0.5,rely=0.1,anchor=CENTER)

news1 = Label(root,wraplength=500)
news1.place(relx=0.1,rely=0.25,anchor=W)

des1 = Label(root,wraplength=500)
des1.place(relx=0.1,rely=0.3,anchor=W) 

news2 = Label(root,wraplength=500)
news2.place(relx=0.1,rely=0.4,anchor=W)

des2 = Label(root,wraplength=500)
des2.place(relx=0.1,rely=0.45,anchor=W)

news3 = Label(root,wraplength=500)
news3.place(relx=0.1,rely=0.6,anchor=W)

des3 = Label(root,wraplength=500)
des3.place(relx=0.1,rely=0.65,anchor=W)

news4 = Label(root,wraplength=500)
news4.place(relx=0.1,rely=0.8,anchor=W)

des4 = Label(root,wraplength=500)
des4.place(relx=0.1,rely=0.85,anchor=W)

api = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4d10d1b71dc046d3b5258ed7bafb9bf7")
api_json = json.loads(api.content)

n1 = api_json["articles"][0]["title"]
n2 = api_json["articles"][1]["title"]
n3 = api_json["articles"][2]["title"]
n4 = api_json["articles"][3]["title"]

d1 = api_json["articles"][0]["description"]
d2 = api_json["articles"][1]["description"]
d3 = api_json["articles"][2]["description"]
d4 = api_json["articles"][3]["description"]

news1["text"] = "Title: " + str(n1)
news2["text"] = "Title: " + str(n2)
news3["text"] = "Title: " + str(n3)
news4["text"] = "Title: " + str(n4)

des1["text"] = "Description: " + str(d1)
des2["text"] = "Description: " + str(d2)
des3["text"] = "Description: " + str(d3)
des4["text"] = "Description: " + str(d4)

root.mainloop()