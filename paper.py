# pyinstaller --onefile --add-data="tkcode/schemes;./tkcode/schemes" --icon=assets/logo.ico paper.py

 
import tkinter as tk
from tkinter import ttk 
from tkcode import CodeEditor  
import os

def init(): 
    # code=input("Enter file name (index.html) : ")
    code = 'code.html'
    if '.html' in code:
        language = 'html'
    elif '.js' in code:
        language = 'js'
    elif '.py' in code:
        language = 'py'
    elif '.css' in code:
        language = 'css'
    elif '.scss' in code:
        language = 'scss'
    root = tk.Tk()
    # root.iconbitmap("assets/logo.ico")
    root.title("Code Editor")
    root.option_add("*tearOff", 0)

    notebook = ttk.Notebook(root)
    tab_1 = ttk.Frame(notebook)
    notebook.add(tab_1, text=code)

    notebook.pack(fill="both", expand=True)

    highlighter = [
        'dracula',
        'mariana',
        'monokai',
        'azure',
        'monokai-plus-plus',
        'dracula'
    ]
    code_editor = CodeEditor(
        tab_1, 
        width=99,
        height=30,
        language=language,
        background="black",
        highlighter=highlighter[0],
        font="Consolas",
        autofocus=True,
        blockcursor=True,
        insertofftime=0,
        padx=10,
        pady=10, 
    )  
    code_editor.pack(fill="both", expand=True)  
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.mainloop()
    init()

if __name__ == '__main__': 
    init()
