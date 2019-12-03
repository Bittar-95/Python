from tkinter import *
import tkinter.scrolledtext as ScrolledText
# =============================================================================
# Q1

#form = Tk()
#def submit():
#   if txt_name.get()=="Orange" and txt_password.get() =="CodingAcademy" :
#       print("Name: "+ txt_name.get() + "\n"+"Password: "+txt_password.get())
#   else:
#    print("Wrong UserName Or Password")    
#
#lbl_name = Label(form,text="Name")
#lbl_name.grid(row=0,column=0)
#
#txt_name=  StringVar()
#txt_input_name = Entry(form,textvariable=txt_name)
#txt_input_name.grid(row=0,column=1)
#
#lbl_password = Label(form,text="Password")
#lbl_password.grid(row=1,column=0)
#
#
#txt_password=StringVar()
#txt_input_password = Entry(form,textvariable=txt_password)
#txt_input_password.grid(row=1,column=1)
#
#
#btn = Button(form,text="Submit",command=submit)
#btn.grid(row=2,column=0)
#
#
#
#form.geometry("200x200+100+200")
#
#form.mainloop()

# =============================================================================

# =============================================================================
#Q2

#
#form = Tk()
#def message():
#    messagebox.showinfo("","This is a message")
#
#
#def open_second_window():
#    
#    def exit_child():
#        newChild.destroy();
#     
#    newChild = Toplevel(form)
#        
#    lbl_number = Label(newChild,text="Enter Number")
#    lbl_number.grid(row=0,column=0)
#    
#    txt_name=  StringVar()
#    txt_input_number = Entry(newChild,textvariable=txt_name)
#    txt_input_number.grid(row=0,column=1)
#    
#   
#    
#    lbl_name = Label(newChild,text="Password")
#    lbl_name.grid(row=1,column=0)
#    
#    
#    txt_name=StringVar()
#    txt_input_name = Entry(newChild,textvariable=txt_name)
#    txt_input_name.grid(row=1,column=1)
#    
#    
#    btn = Button(newChild,text="Exit",command=exit_child)
#    btn.grid(row=2,column=0)
#        
#    
#     
#def open_third_window():
#    
#    third_child = Toplevel(form)
#    st = ScrolledText.ScrolledText(third_child)
#    st.pack()
#    for x in range(20):
#            st.insert(INSERT, "The Count Is :"+ str(x) + "\n")
#
#
#
#        
#    
#  
# 
#btn_message = Button(form,text="Open Message",command=message)
#btn_message.grid(row=0,column=0)
#
#btn_child_one = Button(form,text="Open Child Window 1",command=open_second_window)
#btn_child_one.grid(row=1,column=0)
#
#
#
#btn_child_two = Button(form,text="Open Child Window 2",command=open_third_window)
#btn_child_two.grid(row=2,column=0)
#
#
#
#
#form.geometry("200x200+100+200")
#
#form.mainloop()
#
#
#
#

# =============================================================================


# =============================================================================
#Q3

#from tkinter.colorchooser import *
#window=Tk()
#window.geometry('350x200')
#
#def getColor():
#    color=askcolor()
#    color_name = color[1]
#    print(color_name)
#    window.configure(background=color_name)
#
#Button(text='Select Color',command=getColor).pack()
#mainloop()
# =============================================================================



