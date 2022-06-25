from cProfile import run
import tkinter as tk
from tkinter import CENTER, NO, ttk
from tkinter import * 
from tkinter.ttk import *
from numpy import pad
import main as sa
root = tk.Tk()
canvas = tk.Canvas(root, width=350, height=600)

count = False
def run_sentiment_analisis():
    quantity = int(input.get("1.0","end-1c"))
    if quantity < 1 or quantity > 1000:
        print("Quantity value too big or small")
        result_text.config(text="Quantity value too big or small")
    else:
        value, df = sa.main(quantity)
        result.set(value)
        result_text.config(text=result.get())
        print(result.get())
        load_dataframe(df)
    

def load_dataframe(df):
    print(df)
    for id, row in df.iterrows():
        print(id, row['Tweet'])
        if id == 0:
            print("Skipping...")
        else:
            tree.insert(parent='', index=id, text='', values=(row['Tweet'], row['polarity'], row['subjectivity']))

result = tk.StringVar()

canvas.grid(columnspan=3, rowspan=4)

title = tk.Label(root, text="Crypto Sentiment Analysis", font=('Helvetica 20'))
run_button = tk.Button(root, text="Run", font=(
    'Helvetica 14'), width=15, height=2, command=run_sentiment_analisis)

run_button.grid(column=2, row=1, padx=50)
title.grid(column=1, row=0)

quantity_label = tk.Label(root, text="Tweets quantity", font=('Helvetica 16'))
quantity_label.grid(column=0, row=1, sticky = E, padx=50)

input = tk.Text(root, height = 2, width = 15, font=(
    'Helvetica 14'))
input.grid(column=1, row=1)

result_text = tk.Label(root, text=count, font=('Helvetica 14'))
result_text.config(text="Click run to start")
result_text.grid(column=1, row=2)



tree = ttk.Treeview(root)
tree['columns']=('tweet', 'polarity', 'subjectivity')
tree.column('#0', width=0, stretch=NO)
tree.heading('tweet', text='Tweet', anchor=CENTER)
tree.heading('polarity', text='Polarity', anchor=CENTER)
tree.heading('subjectivity', text='Subjectivity', anchor=CENTER)
tree.grid(column=1, row=3)

root.mainloop()
