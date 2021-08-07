import tkinter as tk
import math

root= tk.Tk()
root.title('Trigonometry Calculate | darrellhl082')
canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Calculate sin(), cos(), tan()', font=('helvetica', 16))
canvas1.create_window(200, 25, window=label1)


label2 = tk.Label(root, text='Input sin / cos / tan:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)
entry1 = tk.Entry (root) 
canvas1.create_window(200, 120, window=entry1)

label3 = tk.Label(root, text='Input Degree:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 160, window=label3)
entry2 = tk.Entry (root) 
canvas1.create_window(200, 180, window=entry2)

ansLabel = tk.Label(root)
canvas1.create_window(200,250, window= ansLabel)

def calc():
    
    oprs = entry1.get()
    input = entry2.get()
    def getAns(input, opr):
        inputDeg = float(input)
        degree = math.radians(inputDeg)
        global ansLabel
        if opr == "sin":
             ans = math.sin(degree)
        elif opr == "cos":
             ans = math.cos(degree)
        elif opr == "tan":
             ans = math.tan(degree)
        else:
             ans = "Error"
        
        if ans == "Error":
             errText = "Error"
             ansLabel.config(text = errText)
        else:
            text = f"{opr}({inputDeg}) = {ans:.2}"
            ansLabel.config(text = text, font=('helvatica', 10))
    getAns(opr = oprs, input = input)


button1 = tk.Button(text='Get Ans', command=calc, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 220, window=button1)

root.mainloop()