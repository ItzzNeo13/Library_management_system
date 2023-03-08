# importing modules
import tkinter
import os
import mysql.connector 

# Importing env values
host = os.environ['host']
user = os.environ['user']
psswd = os.environ['psswd']

# Connecting to DB
creds=mysql.connector.connect(host=host, user=user, password=psswd)
cur=creds.cursor(buffered=True)

# Logic for logging in DB
try:
  cur.execute("USE library_management;")
except:
  cur.execute("CREATE DATABASE member;")
  cur.execute("USE library_management;")
try:
  cur.execute("DESCRIBE member;")
except:
  cur.execute("CREATE TABLE member( member_id INT PRIMARY KEY AUTO_INCREMENT, first_name VARCHAR(255), last_name VARCHAR(255), member_age INT,      email_id VARCHAR(255), member_since DATE );")
  creds.commit()

# Defining Registration
def Registration():
  creds.execute(f"INSERT INTO Member (first_name, last_name, member_age, email_id, member_since) VALUES ('{e1.get()}', '{e2.get()}', {e3.get()}, {e4.get()}, {e5.get()})")

# Creating UI Window
window=tkinter.Tk()
window.geometry("500x500")
window.title("Add new members")
l1=tkinter.Label(window, text="First Name:")
l2=tkinter.Label(window, text="Last Name:")
l3=tkinter.Label(window, text="Age:")
l4=tkinter.Label(window, text="Email:")
l5=tkinter.Label(window, text="Date:")

# Placing labels
l1.grid(row=3, column=1)
l2.grid(row=4, column=1)
l3.grid(row=5, column=1)
l4.grid(row=6, column=1)
l5.grid(row=7, column=1)

# Adding entry fields
e1=tkinter.Entry(window)
e2=tkinter.Entry(window)
e3=tkinter.Entry(window)
e4=tkinter.Entry(window)
e5=tkinter.Entry(window)

# Placing entry fields
e1.grid(row=3, column=2)
e2.grid(row=4, column=2)
e3.grid(row=5, column=2)
e4.grid(row=6, column=2)
e5.grid(row=7, column=2)

# Submit Button
b=tkinter.Button(window, text="Submit data", command=Registration)
b.grid(row=8, column=2)

# Calling UI Window
window.mainloop()