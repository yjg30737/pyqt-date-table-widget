from PyQt5.QtCore import QDate
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QTableWidget


class DateTableWidget(QTableWidget):
    def __init__(self, start_date: QDate = QDate.currentDate(), date_range: int = 100):
        super().__init__()
        self.__start_date = start_date
        self.__date_range = date_range
        self.__initUi()

    def __initUi(self):
        self.verticalHeader().setVisible(True)
        self.setEditTriggers(QAbstractItemView.AllEditTriggers)

        self.__setDateRows()

    def __setDateRows(self):
        date = self.__start_date
        for i in range(self.__date_range):
            date_str = date.toString('yyyy-MM-dd')
            item = QTableWidgetItem(date_str)
            if date.dayOfWeek() == 6:
                item.setForeground(QColor('#0000FF'))
            elif date.dayOfWeek() == 7:
                item.setForeground(QColor('#FF0000'))
            self.setRowCount(self.rowCount()+1)
            self.setVerticalHeaderItem(i, item)
            date = date.addDays(1)

    def setDateRange(self, date_range: int):
        self.__date_range = date_range

