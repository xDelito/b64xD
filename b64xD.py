import base64
from tkinter import Tk, Button, Label, filedialog
from tkinter.scrolledtext import ScrolledText
import pyperclip

def copy_to_clipboard():
    result_text.clipboard_clear()
    result = result_text.get('1.0', 'end')
    pyperclip.copy(result)

def encrypt_file_base64(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # encriptar el archivo en base64
    file_data_base64 = base64.b64encode(file_data)

    return file_data_base64

def select_file():
    file_path = filedialog.askopenfilename(title = "Select a file .exe", filetypes = (("Execs","*.exe"), ("all files","*.*")))
    encryption_output = encrypt_file_base64(file_path)
    result_text.config(state='normal')
    result_text.delete('1.0', 'end')
    result_text.insert('end', encryption_output)
    result_text.config(state='disabled')

root = Tk()
root.title("Encrypt in base64 by xDelito")
root.geometry("530x469")
root.iconbitmap("./pirate.ico") #agregar esta linea para establecer el icono de la aplicacion

select_file_button = Button(root, text="Select file", command=select_file)
select_file_button.pack()

result_text = ScrolledText(root, state='disabled')
result_text.pack()

copy_to_clipboard_button = Button(root, text="Copy", command=copy_to_clipboard)
copy_to_clipboard_button.pack()

root.mainloop()
