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
            },
            {
                "jautajums": "Kuri no šiem ir loģiskie operatori Python valodā?",
                "atbildes": ["a) and", "b) or", "c) plus", "d) not"],
                "pareizas_atbildes": [0, 1, 3]
            },
            {
                "jautajums": "Kā var iziet no while cikla?",
                "atbildes": ["a) exit()", "b) break", "c) continue", "d) return"],
                "pareizas_atbildes": [1, 3]
            },
            {
                "jautajums": "Kādi ir nosacījumi, kad while cikls neizpildīsies?",
                "atbildes": ["a) Nosacījums ir False", "b) Nosacījums ir 0", "c) Nosacījums ir True", "d) Nosacījums ir None"],
                "pareizas_atbildes": [0, 1, 3]
            },
            {
                "jautajums": "Kādi mainīgie tiek uzskatīti par False Python valodā?",
                "atbildes": ["a) 0", "b) \"\" (tukša virkne)", "c) [1]", "d) [] (tukšs saraksts)"],
                "pareizas_atbildes": [0, 1, 3]
            },
            {
                "jautajums": "Kādi ir iespējamie cikla veidi Python valodā?",
                "atbildes": ["a) while", "b) repeat", "c) for", "d) loop"],
                "pareizas_atbildes": [0, 2]
            },
            {
                "jautajums": "Kāds ir pareizs veids, kā izvairīties no bezgalīga cikla while?",
                "atbildes": ["a) Palielināt mainīgo cikla iekšienē", "b) Neiekļaut nosacījumu", "c) Iekļaut break", "d) Lietot for ciklu"],
                "pareizas_atbildes": [0, 2]
            },
            {
                "jautajums": "Kāda ir funkcija 'continue' ciklā?",
                "atbildes": ["a) Pārtrauc programmu", "b) Pārlec uz nākamo cikla iterāciju", "c) Iziet no cikla", "d) Izlaiž turpmāko kodu ciklā un turpina ar nākamo iterāciju"],
                "pareizas_atbildes": [1, 3]
            },
            {
                "jautajums": "Kas ir patiesi par break un continue?",
                "atbildes": ["a) break iziet no cikla", "b) continue izpilda kodu pēc cikla", "c) break un continue var tikt lietoti for un while", "d) continue izlaiž nākamo cikla iterāciju"],
                "pareizas_atbildes": [0, 2, 3]
            },
            {
                "jautajums": "Kas no zemāk minētajām ir pareizi izmantojot while ciklu?",
                "atbildes": ["a) Nepieciešams nosacījums", "b) Var lietot else ar while", "c) Cikls vienmēr izpildās vismaz vienu reizi", "d) Nosacījums jāmaina cikla iekšienē"],
                "pareizas_atbildes": [0, 1, 3]
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
            self.paradit_rezultatu()
            return

        jautajums = self.jautajumi[self.tekstais_jautajums]
        tk.Label(self.sakne, text=f"Jautājums {self.tekstais_jautajums + 1}/{len(self.jautajumi)}", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.sakne, text=jautajums["jautajums"], wraplength=750, justify="left", font=("Arial", 12)).pack(pady=10, padx=20)

        self.atbildes_var = []
        for i, atbilde in enumerate(jautajums["atbildes"]):
            var = tk.IntVar()
            self.atbildes_var.append(var)
            tk.Checkbutton(self.sakne, text=atbilde, variable=var, font=("Arial", 11)).pack(pady=5, padx=20, anchor="w")

        tk.Button(self.sakne, text="Iesniegt", command=self.parbaudit_atbildi, height=2, width=15).pack(pady=20)
    
    def parbaudit_atbildi(self):
        atbildes = [i for i, var in enumerate(self.atbildes_var) if var.get() == 1]

        if not atbildes:
            messagebox.showwarning("Brīdinājums", "Izvēlieties vismaz vienu atbildi!")
            return

        pareizas = set(self.jautajumi[self.tekstais_jautajums]["pareizas_atbildes"])
        if set(atbildes) == pareizas:
            self.pareizas_atbildes += 1
            messagebox.showinfo("Rezultāts", "Pareizi!")
        else:
            self.nepareizi_jautajumi.append(self.jautajumi[self.tekstais_jautajums]["jautajums"])
            messagebox.showinfo("Rezultāts", "Nepareizi.")

        self.tekstais_jautajums += 1
        self.paradit_jautajumu()

    def paradit_rezultatu(self):
        self.iziet()
        tk.Label(self.sakne, text=f"Tests pabeigts! Pareizo atbilžu skaits: {self.pareizas_atbildes}/{len(self.jautajumi)}", font=("Arial", 16)).pack(pady=20)
        if self.nepareizi_jautajumi:
            tk.Label(self.sakne, text="Nepareizi atbildētie jautājumi:", font=("Arial", 12)).pack(pady=10)
            for jaut in self.nepareizi_jautajumi:
                tk.Label(self.sakne, text=jaut, wraplength=750, justify="left", font=("Arial", 11)).pack(pady=5, padx=20)
        tk.Button(self.sakne, text="Atgriezties uz sākumu", command=self.uzstadit_sakuma_ekranu, height=2, width=20).pack(pady=20)

    def iziet(self):
        for elements in self.sakne.winfo_children():
            elements.destroy()

    def iziet(self):
        for elements in self.sakne.winfo_children():
            elements.destroy()

if __name__ == "__main__":
    sakne = tk.Tk()
    aplikacija = TestaAplikacija(sakne)
    sakne.mainloop()