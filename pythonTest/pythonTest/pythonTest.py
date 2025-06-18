import tkinter as tk
from tkinter import messagebox
import random

PRIMARY_COLOR = "#2E3F4F"
BG_COLOR = "#FFC8A8"
ACCENT_COLOR = "#4CAF50"
TEXT_COLOR = "#212121"
FONT_MAIN = ("Arial", 14)
FONT_TITLE = ("Arial", 20, "bold")
FONT_SUB = ("Arial", 12)

class TestaAplikacija:
    def __init__(self, sakne):
        self.sakne = sakne
        self.sakne.title("Cikls ar priekšnosacījumu - Tests")
        self.sakne.geometry("800x600")
        self.sakne.configure(bg=BG_COLOR)
        
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
    
    def iziet(self):
        for elements in self.sakne.winfo_children():
            elements.destroy()

    def uzstadit_sakuma_ekranu(self):
        self.iziet()
        tk.Label(self.sakne, text="Cikls ar priekšnosacījumu - Tests", font=FONT_TITLE, bg=BG_COLOR, fg=PRIMARY_COLOR).pack(pady=30)

        self._izveidot_pogu("Sākt testu", self.sakt_testu)
        self._izveidot_pogu("Informācija", self.paradit_informaciju)
        self._izveidot_pogu("Iziet", self.sakne.destroy)

    def _izveidot_pogu(self, teksts, komanda):
        return tk.Button(self.sakne, text=teksts, command=komanda,
                         bg=PRIMARY_COLOR, fg="white", font=FONT_MAIN,
                         activebackground=ACCENT_COLOR, activeforeground="white",
                         width=20, height=2, bd=0).pack(pady=10)

    def paradit_informaciju(self):
        informacija = (
            "Šis elektroniskais tests izstrādāts par tēmu \"Cikls ar priekšnosacījumu programmēšanas valodā Python\".\n\n"
            "- Tests satur 10 jautājumus (izstrāde notiek programmēšanas valodā Python).\n"
            "- Katram jautājumam ir 4 atbilžu varianti, no kuriem pareizi ir 2 vai 3 varianti.\n"
            "- Jautājumi tiek attēloti nejaušā secībā.\n"
            "- Lietotājs uz katru jautājumu atbild 1 reizi un uzreiz saņem atgriezenisko saiti – vai atbilde ir pareiza vai nepareiza.\n"
            "- Testa beigās tiek parādīts, cik jautājumu atbildēti pareizi un tiek izdrukāts saraksts ar tiem jautājumiem, kuros tika kļūdīts."
        )
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
        tk.Label(self.sakne, text=f"Jautājums {self.tekstais_jautajums + 1}/{len(self.jautajumi)}",
                 font=FONT_SUB, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

        tk.Label(self.sakne, text=jautajums["jautajums"],
                 font=FONT_MAIN, bg=BG_COLOR, fg=TEXT_COLOR,
                 wraplength=750, justify="left").pack(pady=10, padx=20)

        self.atbildes_var = []
        for i, atbilde in enumerate(jautajums["atbildes"]):
            var = tk.IntVar()
            self.atbildes_var.append(var)
            tk.Checkbutton(self.sakne, text=atbilde, variable=var,
                           font=FONT_SUB, bg=BG_COLOR, fg=TEXT_COLOR,
                           selectcolor=ACCENT_COLOR, anchor="w", padx=20).pack(anchor="w", padx=40, pady=2)

        self._izveidot_pogu("Iesniegt", self.parbaudit_atbildi)

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
        tk.Label(self.sakne, text=f"Tests pabeigts! Pareizo atbilžu skaits: {self.pareizas_atbildes}/{len(self.jautajumi)}",
                 font=FONT_TITLE, bg=BG_COLOR, fg=PRIMARY_COLOR).pack(pady=30)

        if self.nepareizi_jautajumi:
            tk.Label(self.sakne, text="Nepareizi atbildētie jautājumi:", font=FONT_MAIN,
                     bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
            for jaut in self.nepareizi_jautajumi:
                tk.Label(self.sakne, text="• " + jaut, font=FONT_SUB,
                         bg=BG_COLOR, fg=TEXT_COLOR, wraplength=750, justify="left").pack(anchor="w", padx=40, pady=2)

        self._izveidot_pogu("Atgriezties uz sākumu", self.uzstadit_sakuma_ekranu)
        self._izveidot_pogu("Sākt testu no jauna", self.sakt_testu)

if __name__ == "__main__":
    sakne = tk.Tk()
    aplikacija = TestaAplikacija(sakne)
    sakne.mainloop()