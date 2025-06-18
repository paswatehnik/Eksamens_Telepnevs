import tkinter as tk
from tkinter import messagebox
import random

class TestaAplikacija:
    def __init__(self, sakne):
        self.sakne = sakne
        self.sakne.title("Cikls ar priekšnosacījumu - Tests")
        self.sakne.geometry("800x600")
        
        self.jautajumi = [
            {
                "jautajums": "Kāda ir while cikla sintakse?",
                "atbildes": ["a) while x > 0:", "b) for x in range(10):", 
                           "c) while (x > 0)", "d) while True:"],
                "pareizas_atbildes": [0, 3]
            }
        ]
        self.tekstais_jautajums = 0
        self.pareizas_atbildes = 0
        self.nepareizi_jautajumi = []

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
        random.shuffle(self.jautajumi)
        self.tekstais_jautajums = 0
        self.pareizas_atbildes = 0
        self.nepareizi_jautajumi = []
        self.paradit_jautajumu()

    def paradit_jautajumu(self):
        self.iziet()
        
        if self.tekstais_jautajums >= len(self.jautajumi):
            self.paradit_rezultatus()
            return
            
        jautajums = self.jautajumi[self.tekstais_jautajums]
        
        tk.Label(self.sakne, text=f"Jautājums {self.tekstais_jautajums + 1}/{len(self.jautajumi)}", 
                font=("Arial", 14)).pack(pady=10)
        
        tk.Label(self.sakne, text=jautajums["jautajums"], 
                wraplength=750, justify="left", font=("Arial", 12)).pack(pady=10, padx=20)
        
        self.atlase = tk.IntVar(value=-1)
        for i, atbilde in enumerate(jautajums["atbildes"]):
            tk.Radiobutton(self.sakne, text=atbilde, variable=self.atlase, 
                         value=i, font=("Arial", 11)).pack(pady=5, padx=20, anchor="w")
        
        tk.Button(self.sakne, text="Iesniegt",
                 height=2, width=15).pack(pady=20)
    
    def iziet(self):
        for elements in self.sakne.winfo_children():
            elements.destroy()

if __name__ == "__main__":
    sakne = tk.Tk()
    aplikacija = TestaAplikacija(sakne)
    sakne.mainloop()