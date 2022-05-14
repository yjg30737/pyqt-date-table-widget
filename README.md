# pyqt-date-table-widget
PyQt table widget for showing date

## Requirements
PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-date-table-widget`

## Feature
* Available to set date range to show (100 as default)
* Available to set start date (current date as default)
* Show different color for weekend

## Example
Code Example
```python
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication
from pyqt_date_table_widget import DateTableWidget

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    afterFifteenDaysFromToday = QDate.currentDate().addDays(15)
    dateTableWidget = DateTableWidget(start_date=afterFifteenDaysFromToday, date_range=1000)
    dateTableWidget.setColumnCount(2)
    dateTableWidget.setHorizontalHeaderLabels(['Literature', 'Mathematics'])
    dateTableWidget.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/144793727-55338cb4-2a88-44f4-afc0-c2a184c95f85.png)



