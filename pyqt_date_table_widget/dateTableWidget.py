from PyQt5.QtCore import QDate
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QAbstractItemView, QTableWidget


class DateTableWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.verticalHeader().setVisible(True)
        self.setEditTriggers(QAbstractItemView.AllEditTriggers)

        date = QDate.currentDate()
        for i in range(100):
            date_str = date.toString('yyyy-MM-dd')
            item = QTableWidgetItem(date_str)
            if date.dayOfWeek() == 6:
                item.setForeground(QColor('#0000FF'))
            elif date.dayOfWeek() == 7:
                item.setForeground(QColor('#FF0000'))
            self.setRowCount(self.rowCount()+1)
            self.setVerticalHeaderItem(i, item)
            date = date.addDays(1)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    dateTableWidget = DateTableWidget()
    dateTableWidget.show()
    app.exec_()