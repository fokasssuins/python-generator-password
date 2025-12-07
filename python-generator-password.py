import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import string


UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
SYMBOLS = string.punctuation.replace('"', '').replace("'", '')


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        root.title('Password Generator')
        root.geometry('400x300')
        
        self.password_var = tk.StringVar()
        self.password_var.set('Awaiting a generation request')
        
        self.generate_button = tk.Button(root, 
                                         text='Generate a password',
                                         command=self.generate_action,
                                         font=(None, 12, 'bold'),
                                         padx=10, pady=5)
        self.generate_button.pack(pady=20)
        
        self.password_label = tk.Label(root,
                                       textvariable=self.password_var,
                                       font=(None, 14),
                                       padx=10, pady=5,)
        self.password_label.pack(pady=10)
        
        self.copy_button = tk.Button(root,
                                     text='Copy',
                                     command=self.copy_to_clipboard,
                                     state=tk.DISABLED)
        self.copy_button.pack(pady=5)
        
    def generate_password(self, length, use_symbols):
        all_chars = UPPERCASE + LOWERCASE + DIGITS
        guaranteed_chars = []
        
        guaranteed_chars.append(random.choice(UPPERCASE))
        guaranteed_chars.append(random.choice(LOWERCASE))
        guaranteed_chars.append(random.choice(DIGITS))
        
        if use_symbols:
            all_chars += SYMBOLS
            guaranteed_chars.append(random.choice(SYMBOLS))
        
        chars_to_fill = length - len(guaranteed_chars)
        
        if chars_to_fill < 0:
            password_list = guaranteed_chars[:length]
        else:
            password_list = guaranteed_chars
            for _ in range(chars_to_fill):
                password_list.append(random.choice(all_chars))
                
        random.shuffle(password_list)
        return ''.join(password_list)
    
    def generate_action(self):
        
        length = simpledialog.askinteger('Entering the password length',
                                         'Enter the desired password length',
                                         minvalue=1)
        if length is None:
            return
        
        use_symbols = messagebox.askyesno('Special characters',
                                          'Include special characters?')
        
        new_password = self.generate_password(length,use_symbols)
        self.password_var.set(new_password)
        self.copy_button.config(state=tk.NORMAL)
        
    def copy_to_clipboard(self):
        password = self.password_var.get()
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        messagebox.showinfo(None,'The password has been copied to the clipboard!')
        
def create_gui():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
    
if __name__ == '__main__':
    create_gui()