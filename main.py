import pandas as pd
import xlwt
from Classes.calendar import Calendar

def assign():
    data = pd.read_csv('./input.csv', header=None)
    return [(data[0][i], data[1][i]) for i in range(len(data))]

def showInExcel(calendar):
    book = xlwt.Workbook(encoding="utf-8")

    sheet1 = book.add_sheet("Sheet 1")

    sheet1.write(0, 1, "MONDAY")
    sheet1.write(0, 2, "TUESDAY")
    sheet1.write(0, 3, "WENESDAY")
    sheet1.write(0, 4, "THURSDAY")
    sheet1.write(0, 5, "FRIDAY")
    sheet1.write(0, 6, "SARTUDAY")

    for i in range(1, 5):
        sheet1.write(i, 0, i)

    for i in range(len(calendar.getWeek())):
        for j in range(len(calendar.getWeek()[i].getShifts())):
            if calendar.getWeek()[i].getShifts()[j].getShiftStatus() and calendar.getWeek()[i].getShifts()[j].getSub() != '':
                value = calendar.getWeek()[i].getShifts()[j].getSub() +' | Room:'+ calendar.getWeek()[i].getShifts()[j].getRequiredClass()
                sheet1.write(j+1, i+1, value)
            elif calendar.getWeek()[i].getShifts()[j].getShiftStatus() == False:
                sheet1.write(j+1, i+1, 'X')

    book.save("Calendar.xls")

def main():
    values = assign()
    
    calendar = Calendar()
    calendar.setCal(values)
    calendar.showCal()

    showInExcel(calendar)
    

main()