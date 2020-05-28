import numpy as np
import cv2

class sudokuC():
    def __init__(self):
        self.color=(0,0,0)
        self.plansza = np.zeros((660, 480, 3), np.uint8)
        self.plansza[:] = (255, 255, 255)
        self.sudoku = np.zeros((9, 9), int)


    def wypisanie(self):
        for i in range(9):
            if i<8:
                cv2.line(self.plansza, ((i+1) * 50 + 15, 20), ((i+1) * 50 + 15, 640),self.color,5)
                cv2.line(self.plansza, (20, (i+1)* 70 + 15), (460, (i+1) * 70 + 15), self.color, 5)
            for j in range(9):
                if self.sudoku[j][i]!=0:
                    cv2.putText(self.plansza,str(self.sudoku[j][i]),(i*50+20,j*70+70),cv2.FONT_HERSHEY_COMPLEX,2,self.color,3)
        cv2.line(self.plansza, ((3) * 50 + 15, 20), ((3) * 50 + 15, 640), (0, 0, 255), 5)
        cv2.line(self.plansza, (20, (3) * 70 + 15), (460, (3) * 70 + 15), (0, 0, 255), 5)
        cv2.line(self.plansza, ((6) * 50 + 15, 20), ((6) * 50 + 15, 640), (0, 0, 255), 5)
        cv2.line(self.plansza, (20, (6) * 70 + 15), (460, (6) * 70 + 15), (0, 0, 255), 5)


    def spr(self):
        #sprawdzenie wierszy
        for j in range(9):
            liczba = 0
            for i in range(9):
                liczba = liczba + self.sudoku[j][i]
                #print("liczba-",j,liczba)
                if self.sudoku[j][i]==0:
                    liczba=45
                    break
            if liczba != 45:
                return 0
        for i in range(9):
            liczba = 0
            for j in range(9):
                liczba = liczba + self.sudoku[j][i]
                #print("liczba|",i,liczba)
                if self.sudoku[j][i]==0:
                    liczba=45
                    break
            if liczba != 45:
                return 0
        for n in range(3):
            for m in range(3):
                liczba = 0
                for i in range(n*3,n*3+3):
                    for j in range(m*3,m*3+3):
                        liczba = liczba + self.sudoku[j][i]
                        #print("liczba<>",m,n,",",j,i,liczba)
                        if self.sudoku[j][i] == 0:
                            liczba = 45
                            break
                    if self.sudoku[j][i] == 0:
                        liczba = 45
                        break
                if liczba != 45:
                     return 0
        return 1


    #rozwiązywanie przez sprawdzanie pustego pola (eliminowanie możliwości)
    def roz1(self):
        #wybieranie pustego pola
        flaga=0
        for j in range(9):
            for i in range(9):
                if self.sudoku[j][i]==0:
                    flaga=1
                    #sprawdzanie liczb w rzędach i kolumnach i kratkach
                    wykresl = np.zeros((9), int)
                    for n in range(9):
                        if self.sudoku[j][n]!=0:
                            pod=self.sudoku[j][n]-1
                            wykresl[pod]=1
                            #print("-",j,i,n,pod)
                    for n in range(9):
                        if self.sudoku[n][i]!=0:
                            pod=self.sudoku[n][i]-1
                            wykresl[pod]=1
                            #print("|",j,i,n,pod)
                    if j>=0 and j<=2:
                        if i >= 0 and i <= 2:
                            for kratka_j in range(0,3):
                                for kratka_i in range(0,3):
                                    if self.sudoku[kratka_j][kratka_i] != 0:
                                        pod = self.sudoku[kratka_j][kratka_i] - 1
                                        wykresl[pod] = 1
                                        #print("k", j, i,"(",kratka_j,kratka_i,")", pod)
                        if i >= 3 and i <= 5:
                            for kratka_j in range(0, 3):
                                for kratka_i in range(3, 6):
                                    if self.sudoku[kratka_j][kratka_i] != 0:
                                        pod = self.sudoku[kratka_j][kratka_i] - 1
                                        wykresl[pod] = 1
                                        #print("k", j, i, "(", kratka_j, kratka_i, ")", pod)
                        if i >= 6 and i <= 8:
                            for kratka_j in range(0, 3):
                                for kratka_i in range(6, 9):
                                    if self.sudoku[kratka_j][kratka_i] != 0:
                                        pod = self.sudoku[kratka_j][kratka_i] - 1
                                        wykresl[pod] = 1
                                        #print("k", j, i, "(", kratka_j, kratka_i, ")", pod)
                    if j >= 3 and j <= 5:
                        if i >= 0 and i <= 2:
                            for kratka_j in range(3, 6):
                                for kratka_i in range(0, 3):
                                    if self.sudoku[kratka_j][kratka_i] != 0:
                                        pod = self.sudoku[kratka_j][kratka_i] - 1
                                        wykresl[pod] = 1
                                        #print("k", j, i, "(", kratka_j, kratka_i, ")", pod)
                        if i >= 3 and i <= 5:
                            for kratka_j in range(3, 6):
                                for kratka_i in range(3, 6):
                                    if self.sudoku[kratka_j][kratka_i] != 0:
                                        pod = self.sudoku[kratka_j][kratka_i] - 1
                                        wykresl[pod] = 1
                                        #print("k", j, i, "(", kratka_j, kratka_i, ")", pod)
                        if i >= 6 and i <= 8:
                            for kratka_j in range(3, 6):
                                for kratka_i in range(6, 9):
                                    if self.sudoku[kratka_j][kratka_i] != 0:
                                        pod = self.sudoku[kratka_j][kratka_i] - 1
                                        wykresl[pod] = 1
                                        #print("k", j, i, "(", kratka_j, kratka_i, ")", pod)
                    if j >= 6 and j <= 9:
                        if i >= 0 and i <= 2:
                            for kratka_j in range(6, 9):
                                for kratka_i in range(0, 3):
                                    if self.sudoku[kratka_j][kratka_i] != 0:
                                        pod = self.sudoku[kratka_j][kratka_i] - 1
                                        wykresl[pod] = 1
                                        #print("k", j, i, "(", kratka_j, kratka_i, ")", pod)
                        if i >= 3 and i <= 5:
                            for kratka_j in range(6, 9):
                                for kratka_i in range(3, 6):
                                    if self.sudoku[kratka_j][kratka_i] != 0:
                                        pod = self.sudoku[kratka_j][kratka_i] - 1
                                        wykresl[pod] = 1
                                        #print("k", j, i, "(", kratka_j, kratka_i, ")", pod)
                        if i >= 6 and i <= 8:
                            for kratka_j in range(6, 9):
                                for kratka_i in range(6, 9):
                                    if self.sudoku[kratka_j][kratka_i] != 0:
                                        pod = self.sudoku[kratka_j][kratka_i] - 1
                                        wykresl[pod] = 1
                                        #print("k", j, i, "(", kratka_j, kratka_i, ")", pod)

                    #print(wykresl)
                    #przypisanie ewentualnej liczby
                    liczba=0
                    for n in range(9):
                        if wykresl[n] == 0:
                            liczba=liczba+1
                            zap=n
                    if liczba==1:
                        self.sudoku[j][i]=zap+1
                        if self.sudoku[j][i]!=0:
                            cv2.putText(self.plansza, str(self.sudoku[j][i]), (i * 50 + 20, j * 70 + 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255),3)
        return flaga


    #rozwiązywanie poprzez wykreślenie tych pól na których nie może być danej liczby
    def roz2(self):
        #znalezienie konkretnej liczby
        #print(2)
        pokaz=3
        wynik=1
        for l in range(9):
            wykresl2 = np.zeros((9, 9), int)
            for j in range(9):
                for i in range(9):
                    if self.sudoku[j][i]==l+1:
                        #wykreslenie kolumny i rzędu
                        for n in range(9):
                            wykresl2[n][i]=1
                            wykresl2[j][n]=1
                            #print("roz2||", l+1, j, i,n)

                            if l+1==pokaz:
                                cv2.putText(self.plansza, "-", (i * 50 + 20, n * 70 + 70), cv2.FONT_HERSHEY_COMPLEX, 2,(0, 0, 255), 3)
                                cv2.putText(self.plansza,"-", (n * 50 + 20, j * 70 + 70), cv2.FONT_HERSHEY_COMPLEX, 2,(0, 0, 255), 3)


                        if j >= 0 and j <= 2:
                            if i >= 0 and i <= 2:
                                for kratka_j in range(0, 3):
                                    for kratka_i in range(0, 3):
                                       wykresl2[kratka_j][kratka_i]=1
                                       if pokaz==l+1:
                                            cv2.putText(self.plansza, "-", (kratka_i * 50 + 20, kratka_j * 70 + 70), cv2.FONT_HERSHEY_COMPLEX, 2,(0, 0, 255), 3)
                            if i >= 3 and i <= 5:
                                for kratka_j in range(0, 3):
                                    for kratka_i in range(3, 6):
                                        wykresl2[kratka_j][kratka_i] = 1
                                        if pokaz == l+1:
                                            cv2.putText(self.plansza, "-", (kratka_i * 50 + 20, kratka_j * 70 + 70), cv2.FONT_HERSHEY_COMPLEX, 2,(0, 0, 255), 3)
                            if i >= 6 and i <= 8:
                                for kratka_j in range(0, 3):
                                    for kratka_i in range(6, 9):
                                        wykresl2[kratka_j][kratka_i] = 1
                                        if pokaz == l+1:
                                            cv2.putText(self.plansza, "-", (kratka_i * 50 + 20, kratka_j * 70 + 70), cv2.FONT_HERSHEY_COMPLEX, 2,(0, 0, 255), 3)
                        if j >= 3 and j <= 5:
                            if i >= 0 and i <= 2:
                                for kratka_j in range(3, 6):
                                    for kratka_i in range(0, 3):
                                        wykresl2[kratka_j][kratka_i] = 1
                                        if pokaz == l+1:
                                            cv2.putText(self.plansza, "-", (kratka_i * 50 + 20, kratka_j * 70 + 70), cv2.FONT_HERSHEY_COMPLEX, 2,(0, 0, 255), 3)
                            if i >= 3 and i <= 5:
                                for kratka_j in range(3, 6):
                                    for kratka_i in range(3, 6):
                                        wykresl2[kratka_j][kratka_i] = 1
                                        if pokaz == l+1:
                                            cv2.putText(self.plansza, "-", (kratka_i * 50 + 20, kratka_j * 70 + 70), cv2.FONT_HERSHEY_COMPLEX, 2,(0, 0, 255), 3)
                            if i >= 6 and i <= 8:
                                for kratka_j in range(3, 6):
                                    for kratka_i in range(6, 9):
                                        wykresl2[kratka_j][kratka_i] = 1
                                        if pokaz == l+1:
                                            cv2.putText(self.plansza, "-", (kratka_i * 50 + 20, kratka_j * 70 + 70), cv2.FONT_HERSHEY_COMPLEX, 2,(0, 0, 255), 3)
                        if j >= 6 and j <= 9:
                            if i >= 0 and i <= 2:
                                for kratka_j in range(6, 9):
                                    for kratka_i in range(0, 3):
                                        wykresl2[kratka_j][kratka_i] = 1
                                        if pokaz == l+1:
                                            cv2.putText(self.plansza, "-", (kratka_i * 50 + 20, kratka_j * 70 + 70), cv2.FONT_HERSHEY_COMPLEX, 2,(0, 0, 255), 3)
                            if i >= 3 and i <= 5:
                                for kratka_j in range(6, 9):
                                    for kratka_i in range(3, 6):
                                        wykresl2[kratka_j][kratka_i] = 1
                                        if pokaz == l+1:
                                            cv2.putText(self.plansza, "-", (kratka_i * 50 + 20, kratka_j * 70 + 70), cv2.FONT_HERSHEY_COMPLEX, 2,(0, 0, 255), 3)
                            if i >= 6 and i <= 8:
                                for kratka_j in range(6, 9):
                                    for kratka_i in range(6, 9):
                                        wykresl2[kratka_j][kratka_i] = 1
                                        if pokaz == l+1:
                                            cv2.putText(self.plansza, "-", (kratka_i * 50 + 20, kratka_j * 70 + 70), cv2.FONT_HERSHEY_COMPLEX, 2,(0, 0, 255), 3)


            #zapisać kratki z liczbami
            for j in range(9):
                for i in range(9):
                    if self.sudoku[j][i] != 0 :
                        wykresl2[j][i] = 1
                        if pokaz== l+1:
                            cv2.putText(self.plansza, "-", (i * 50 + 20, j * 70 + 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255),3)
            #sprawdzić kolumny i rzędyx i kratki
            for j in range(9):
                liczba = 0
                for i in range(9):
                    if wykresl2[j][i]==0:
                        liczba = liczba + 1
                        zap_i = i
                        zap_j = j
                if liczba == 1:
                    wynik = 0
                    self.sudoku[zap_j][zap_i] = l+1
                    #print("roz2",l+1,zap_j,zap_i)
                    if self.sudoku[zap_j][zap_i] != 0:
                        #print("roz2--", l+1, zap_j, zap_i)
                        cv2.putText(self.plansza, str(self.sudoku[zap_j][zap_i]), (zap_i * 50 + 20, zap_j * 70 + 70), cv2.FONT_HERSHEY_COMPLEX, 2,(255, 0, 0), 3)
            for i in range(9):
                liczba = 0
                for j in range(9):
                    if wykresl2[j][i]==0:
                        liczba = liczba + 1
                        zap_i = i
                        zap_j = j
                if liczba == 1:
                    wynik = 0
                    self.sudoku[zap_j][zap_i] = l+1
                    #print("roz2",l+1,zap_j,zap_i)
                    if self.sudoku[zap_j][zap_i] != 0:
                        #print("roz2--", l+1, zap_j, zap_i)
                        cv2.putText(self.plansza, str(self.sudoku[zap_j][zap_i]), (zap_i * 50 + 20, zap_j * 70 + 70), cv2.FONT_HERSHEY_COMPLEX, 2,(255, 0, 0), 3)
            for n in range(3):
                for m in range(3):
                    liczba = 0
                    for i in range(n * 3, n * 3 + 3):
                        for j in range(m * 3, m * 3 + 3):
                           if wykresl2[j][i] == 0:
                                liczba = liczba + 1
                                zap_i = i
                                zap_j = j
                                #print("roz2<>", m, n, ",", j, i, liczba)
                    if liczba == 1:
                        wynik = 0
                        self.sudoku[zap_j][zap_i] = l+1
                        if self.sudoku[zap_j][zap_i] != 0:
                            #print("roz2<>", l+1, zap_j, zap_i)
                            cv2.putText(self.plansza, str(self.sudoku[zap_j][zap_i]), (zap_i * 50 + 20, zap_j * 70 + 70), cv2.FONT_HERSHEY_COMPLEX, 2,(255, 0, 0), 3)
        return wynik

    def sprawdzenie(self):
        a=0
        while a == 0:
            flaga = roz1()
            print("pop:flaga", flaga)
            if flaga == 1:
                a = roz2()
                print("pop:a", a)
            if spr()==0:
                print("pop:błąd")
                return 0
            cv2.imshow("self.plansza", self.plansza)
        return 1


    #rozwiązanie poprzez założenie
    def roz3(self):
        #wyszukanie najmniejszyej liczby w kratkach albo rzędach lub kolumnach
        wynik_i = 10
        wynik_j = 10
        wynik_nm = 10
        for j in range(9):
            liczba = 0
            for i in range(9):
                if self.sudoku[j][i] == 0:
                    liczba = liczba + 1
            if liczba!=0:
                if liczba < wynik_j:
                    wynik_j=liczba
                    zap_j = j
                    print("roz3-", liczba ,zap_j)
        for i in range(9):
            liczba = 0
            for j in range(9):
                if self.sudoku[j][i] == 0:
                    liczba = liczba + 1
            if liczba != 0:
                if liczba < wynik_i:
                    wynik_i=liczba
                    zap_i = i
                    print("roz3|", liczba ,zap_i)
        for n in range(3):
            for m in range(3):
                liczba = 0
                for i in range(n * 3, n * 3 + 3):
                    for j in range(m * 3, m * 3 + 3):
                        if self.sudoku[j][i] == 0:
                            liczba = liczba + 1
                if liczba != 0:
                    if liczba < wynik_nm:
                        wynik_nm = liczba
                        zap_n = n
                        zap_m = m
                        print("roz3<>", liczba, zap_n,zap_m)
        #porównanie wyników i sprawdzenie jakich liczb nie ma
        wykresl = np.zeros((9), int)
        if wynik_i<wynik_j:
            if wynik_i < wynik_nm:
                print(wynik_i)
                for j in range(9):
                    if 0!=self.sudoku[j][zap_i]:
                        zap=self.sudoku[j][zap_i]-1
                        wykresl[zap]=1
                        print(wykresl)
                for j in range(9):
                    if 0==wykresl[j]:
                        zap=j
                for j in range(9):
                    if self.sudoku[j][zap_i]==0:
                        self.sudoku[j][zap_i]=zap
                        print("dodane",j,zap_i,zap)
                        self.sudoku[zap_j][i] = 0
                        sprawdzenie_wynik = sprawdzenie()
                        if sprawdzenie_wynik==1:
                            self.sudoku[j][zap_i] = zap
                            cv2.putText(self.plansza, str(self.sudoku[j][zap_i]), (zap_i * 50 + 20, j * 70 + 70),cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 3)
                            break
            else:
                print(wynik_nm)


        else:
            if wynik_j<wynik_nm:
                print(wynik_j)
                for i in range(9):
                    if 0!=self.sudoku[zap_j][i]:
                        zap = self.sudoku[zap_j][i]-1
                        wykresl[zap]=1
                        print(wykresl)
                for i in range(9):
                    if 0==wykresl[i]:
                        zap=i
                for i in range(9):
                    if self.sudoku[zap_j][i]==0:
                        self.sudoku[zap_j][i]=zap
                        print("dodane",zap_j,i,zap)
                        self.sudoku[zap_j][i]=0
                        sprawdzenie_wynik=sprawdzenie()
                        if sprawdzenie_wynik==1:
                            self.sudoku[zap_j][i] = zap
                            cv2.putText(self.plansza, str(self.sudoku[zap_j][i]), (i * 50 + 20, zap_j * 70 + 70),cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 3)
                            break
            else:
                print(wynik_nm)