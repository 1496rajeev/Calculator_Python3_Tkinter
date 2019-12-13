from tkinter import *
import parser

root = Tk()
root.title('calculator')

#Take user input and put into inputbox
i=0
def get_variable(num):
    global i
    entry.insert(i,num)
    i+=1
    
def get_operation(operator):
    global i
    length = len(operator)
    entry.insert(i,operator)
    i+=length

#calculate the value
def calculate():
    entire_input = entry.get()
    try:
        result = parser.expr(entire_input).compile()
        result=eval(result)
        clear_all()
        entry.insert(0,result)
    except:
        clear_all()
        entry.insert(0,"Syntax error,Press AC")
        
    
#Clear all input (workig of AC button)
def clear_all():
    entry.delete(0,END)

#Back button 
def back_button():
    all_input = entry.get()
    if len(all_input):
        new_input = all_input[:-1]
        clear_all()
        entry.insert(0,new_input)
    else:
        clear_all()
        
# Adding input field
entry = Entry(root)
entry.grid(row=0,columnspan=6,sticky=W+E)

#Adding buttons to the calculator
Button(root,text="1",command=lambda:get_variable(1)).grid(row=1,column=0)
Button(root,text="2",command=lambda:get_variable(2)).grid(row=1,column=1)
Button(root,text="3",command=lambda:get_variable(3)).grid(row=1,column=2)

Button(root,text="4",command=lambda:get_variable(4)).grid(row=2,column=0)
Button(root,text="5",command=lambda:get_variable(5)).grid(row=2,column=1)
Button(root,text="6",command=lambda:get_variable(6)).grid(row=2,column=2)

Button(root,text="7",command=lambda:get_variable(7)).grid(row=3,column=0)
Button(root,text="8",command=lambda:get_variable(8)).grid(row=3,column=1)
Button(root,text="9",command=lambda:get_variable(9)).grid(row=3,column=2)

#Adding other buttons
Button(root,text="AC",command=lambda:clear_all()).grid(row=4,column=0)
Button(root,text="0", command=lambda:get_variable(0)).grid(row=4,column=1)
Button(root,text="=", command=lambda:calculate()).grid(row=4,column=2)

Button(root,text="+", command = lambda:get_operation("+")).grid(row=1,column=3)
Button(root,text="-", command = lambda:get_operation("-")).grid(row=2,column=3)
Button(root,text="*", command = lambda:get_operation("*")).grid(row=3,column=3)
Button(root,text="/", command = lambda:get_operation("/")).grid(row=4,column=3)

Button(root,text="<-", command = lambda:back_button()).grid(row=1,column=5)
Button(root,text="Pi", command = lambda:get_operation("*3.14")).grid(row=2,column=5)
Button(root,text="exp", command = lambda:get_operation("**")).grid(row=3,column=5)
Button(root,text="^2", command = lambda:get_operation("**2")).grid(row=4,column=5)

root.mainloop()