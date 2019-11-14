
import matplotlib.pyplot as plt


class wykresy: # klasa z wykresanu z pomocą bublioteki matplot



    def histogram(self): ## metoda rysujaca histogram
        x = self   # nasz paramter self przypisujemy do X

        plt.hist(x, bins=50, facecolor='g', alpha=0.75)
        plt.xlabel('Wartości liczbowe') # zbiór belek jako macier
        plt.ylabel('Ilość wystąpień')
        plt.title('Histogram')
        # wyświatlanie siatki
        plt.grid(True)

        plt.show()


    def kolowy(self): # rysuje wykres kolowy
        x = self # nasz paramter self przypisujemy do X
        histogram = wykresy.histogramtablica(x) # tworzymy obiket histogram ktory  zawiera histogram w formie tablicy
        wedges, texts, autotexts = plt.pie(histogram.values(), labels=histogram.keys(),   # odwolujemy sie do values wartosci w obiekcie i keys rodzaju
                                           autopct=lambda pct:
        "{:.1f}%".format(pct), textprops=dict(color="black"))
        plt.setp(autotexts, size=14, weight="bold")
        plt.title("Wykres kołowy")
        plt.legend(title='Liczby')
        plt.show()

    def histogramtablica(self): # metoda obliczająca nam histogram
        result = []
        wystapienia = {}
        for elem in sorted(self):
            wystapienia[elem] = wystapienia.get(elem, 0) + 1
        m = max(wystapienia.values())
        [result.append(a) for a in wystapienia.keys() if wystapienia[a] == m]
        return wystapienia