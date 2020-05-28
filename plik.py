#changes
import numpy as np
import cv2
from sudokuclass import sudokuC




sudokuCob=sudokuC()
sudokuCob.sudoku[0][0]=4
sudokuCob.sudoku[0][3]=8
sudokuCob.sudoku[0][5]=1

sudokuCob.sudoku[1][2]=6
sudokuCob.sudoku[1][3]=3
sudokuCob.sudoku[1][4]=4
sudokuCob.sudoku[1][6]=8

sudokuCob.sudoku[2][0]=9
sudokuCob.sudoku[2][1]=8
sudokuCob.sudoku[2][2]=1
sudokuCob.sudoku[2][3]=2
sudokuCob.sudoku[2][7]=3

sudokuCob.sudoku[3][0]=7
sudokuCob.sudoku[3][1]=4
sudokuCob.sudoku[3][3]=1
sudokuCob.sudoku[3][5]=2
sudokuCob.sudoku[3][7]=5
sudokuCob.sudoku[3][8]=8

sudokuCob.sudoku[4][2]=2
sudokuCob.sudoku[4][4]=9
sudokuCob.sudoku[4][7]=4
sudokuCob.sudoku[4][8]=3

sudokuCob.sudoku[5][0]=3
sudokuCob.sudoku[5][2]=8
sudokuCob.sudoku[5][3]=7
sudokuCob.sudoku[5][5]=4
sudokuCob.sudoku[5][6]=2
sudokuCob.sudoku[5][8]=1

sudokuCob.sudoku[6][0]=1
sudokuCob.sudoku[6][2]=3
sudokuCob.sudoku[6][3]=4
sudokuCob.sudoku[6][6]=5

sudokuCob.sudoku[7][0]=8
sudokuCob.sudoku[7][1]=6
sudokuCob.sudoku[7][5]=5
sudokuCob.sudoku[7][8]=4

sudokuCob.sudoku[8][0]=5
sudokuCob.sudoku[8][4]=8

#sudoku[1][0]=3
#sudoku[1][2]=2
sudokuCob.wypisanie()

flaga=1
a=0

while cv2.waitKey(0)!=ord('q') and flaga==1:
    flaga=sudokuCob.roz1()

    if flaga==1:
        a=sudokuCob.roz2()
        print("a",a)
        if a==1:
            sudokuCob.roz3()
            a=0
    cv2.imshow("plansza",sudokuCob.plansza)
while cv2.waitKey(0)!=ord('q'):
    if sudokuCob.spr()==1:
        cv2.circle(sudokuCob.plansza,(240,330),100,(0,255,0),-1)
    else:
        cv2.circle(sudokuCob.plansza, (240, 330), 100, (0, 0, 255), -1)
    cv2.imshow("plansza", sudokuCob.plansza)
cv2.destroyAllWindows()
