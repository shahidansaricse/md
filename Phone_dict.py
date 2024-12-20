from tkinter import *
from tkinter import messagebox
a=Tk()
def save_data():
    name = e1.get()
    phone = e2.get()
    if len(phone) != 10 or not phone.isdigit():
        messagebox.showerror("Invalid number", "Phone number must be exactly 10 digits.")
    else:
        with open('Phone_directory.txt', 'a+') as f:
            f.write(f"Name: {name}, Phone: {phone}\n")
            messagebox.showinfo("Valid number", "Data successfully added.")
        e1.delete(0, END)
        e2.delete(0, END)
        display_data()

def delete_data():
    name = e1.get()
    phone = e2.get()
    if not name or not phone:
        messagebox.showerror("Input Error", "Please enter a name and phone number to delete.")
        return

    try:
        found=False
        with open('Phone_directory.txt', 'r') as f:
            lines = f.readlines()
        with open('Phone_directory.txt', 'w') as f:
            for line in lines:
                if not (name in line and phone in line):
                    f.write(line)
                else:
                    found=True
        if(found==True):                 
            messagebox.showinfo("Success", "Data deleted successfully.")
        else:
            messagebox.showinfo("Invalid","Record not found")
        print(name)
        print(phone)
        e1.delete(0, END)
        e2.delete(0, END)
        display_data()
    except FileNotFoundError:
        messagebox.showerror("File Error", "Phone directory file not found.")

def display_data():
    listbox.delete(0, END)
    
    try:
        with open('Phone_directory.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                listbox.insert(END, line.strip())  
    except FileNotFoundError:
        messagebox.showerror("File Error", "Phone directory file not found.")


l=Label(a,text="Phonebook Directory")
l.grid(row=0,column=1)
name=Label(a,text="Enter Name",font="Lucido 13")
name.grid(row=1,column=1,pady=10)
e1=Entry(a,font=("Lucido 10"))
e1.grid(row=1,column=2)
phone_num=Label(a,text="Enter Phone number",font="Lucido 12")
phone_num.grid(row=2,column=1,pady=10)
e2=Entry(a,font=("Lucido 10"))
e2.grid(row=2,column=2)
bt1=Button(a,text="Save",font="Lucido 10",command=save_data)
bt1.grid(row=4,column=1,pady=15)
bt2=Button(a,text="Delete",font="Lucido 10",command=delete_data)
bt2.grid(row=4,column=2,pady=15)
listbox = Listbox(a, width=50, height=10, font=("Lucido 10"))
listbox.grid(row=5, column=1, columnspan=2, pady=15)
display_data()
a.geometry("500x500")
a.mainloop()
