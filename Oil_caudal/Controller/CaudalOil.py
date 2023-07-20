import xlwings as xw
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from Oil_caudal.Model.Función_caudal import caudalOil

HOJA = "Hoja1"
QMAX = "Qmax"
PWF = "Pwf"
PR = "Pr"
QO = "Qo"

def main():
    wb = xw.Book.caller()
    hoja = wb.sheets[0]

    qmax = hoja[QMAX]
    pr = hoja[PR]
    pwf = hoja[PWF].value

    hoja[QO].value = caudalOil(qmax,pwf,pr)


    # codigo para la gráfica

    fig, ax = plt.subplots()
    ax.plot(HOJA[PWF], HOJA[QO])
    hoja.pictures.add(fig, name="Pwf vs Qo", update=True, left=hoja.range("B16").left, pop=hoja.range("B16").pop)



if __name__ == "__main__":
    xw.Book("CaudalOil.xlsm").set_mock_caller()
    main()
