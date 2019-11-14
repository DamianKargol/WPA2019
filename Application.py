
from Przyciski import *
from tkinter import *



class Application:
    file_lines = [] # zmienna przed definicjami aby potem sie odowlywac do niej w przypadku self




#tworzenie prostego okienko za pomocą bilbioteki tkinter
    def __init__(self):
        self.main = tkinter.Tk()
        self.main.title("DAMIAN KARGOL APKA")
        l = tkinter.Label(self.main, text="Program do rysowania wykresów z wczytanych danych")
        l.pack(side=tkinter.TOP)
        zakoncz = tkinter.Button(self.main, text="zakończ", command=self.Zamknij)
        test_var = StringVar()
        w = Wczytaj
        button1 = tkinter.Button(self.main, text="Szukaj plik z danymi w formacie txt!", command=self.open1)
        button1.pack()
        button2 = tkinter.Button(self.main, text="Narysuj wykres kolowy", command=self.rysuj1)
        button2.pack()
        button3 = tkinter.Button(self.main, text="Narysuj Histogram", command=self.rysuj)
        button3.pack()
        zakoncz.pack(side=tkinter.BOTTOM)
        zakoncz.pack(side=tkinter.BOTTOM)

        self.main.mainloop()

#metody ktore wywołują poszczegolne przyciski
    def Zamknij(self): # zamyka okno
        self.main.destroy()

    def open1(self): # otwiera nam plik z okienka i zapisuje do tablicy naszej zmiennej file_lines
        filename = fd.askopenfilename(filetypes=[("Plik tekstowy", "*.txt")])  # wywołanie okna dialogowego open file

        f = open(filename, "r", -1, "utf-8")
        line = f.readline()
        while line != "":
            n_line = line.replace("\n", "")

            Application.file_lines.append(n_line)
            line = f.readline()

        return Application.file_lines

    def rysuj(self): # rysuje histogram
        d1 = wykresy.histogram(self.file_lines) # wysyła do metody z klasy wykresy naszą zmienną file_lines



    def rysuj1(self): # rysuje kolowy wykres

        d = wykresy.kolowy(self.file_lines) # wysyła do metody z klasy wykresy naszą zmienną file_lines
