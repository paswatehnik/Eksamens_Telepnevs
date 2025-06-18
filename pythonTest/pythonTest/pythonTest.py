import tkinter as tk
from tkinter import messagebox

class TestaAplikacija:
    def __init__(self, sakne):
        self.sakne = sakne
        self.sakne.title("Cikls ar priekšnosacījumu - Tests")
        self.sakne.geometry("800x600")
        
        self.uzstadit_sakuma_ekranu()
    
    def uzstadit_sakuma_ekranu(self):
        self.iziet()
        
        tk.Label(self.sakne, text="Cikls ar priekšnosacījumu - Tests", 
                font=("Arial", 20)).pack(pady=20)
        
        tk.Button(self.sakne, text="Sākt testu", command=self.sakt_testu,
                 height=2, width=20).pack(pady=10)
        tk.Button(self.sakne, text="Informācija", command=self.paradit_informaciju,
                 height=2, width=20).pack(pady=10)
        tk.Button(self.sakne, text="Iziet", command=self.sakne.destroy,
                 height=2, width=20).pack(pady=10)
    
    def paradit_informaciju(self):
        informacija = "Testa nosacījumi..."
        messagebox.showinfo("Informācija", informacija)
    
    def sakt_testu(self):
        messagebox.showinfo("Paziņojums", "Tests tiks sākts!")
    
    def iziet(self):
        for elements in self.sakne.winfo_children():
            elements.destroy()

if __name__ == "__main__":
    sakne = tk.Tk()
    aplikacija = TestaAplikacija(sakne)
    sakne.mainloop()