# pyqt-date-table-widget
PyQt Date Table Widget

## Requirements
PyQt5 >= 5.8

## Setup
``` pip3 install git+https://github.com/yjg30737/pyqt-date-table-widget.git --upgrade```

## Example
Code Example
```python
from PyQt5.QtWidgets import QApplication
from pyqt_date_table_widget import DateTableWidget

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    dateTableWidget = DateTableWidget()
    dateTableWidget.setColumnCount(2)
    dateTableWidget.setHorizontalHeaderLabels(['Literature', 'Mathematics'])
    dateTableWidget.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/144792395-fcfec9e4-e5fc-448b-aef0-33f8073dfa5a.png)


