import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('sample_table_and_styles_demo.py')
        self.setGeometry(300, 200, 500, 300)
        self.create_table_ui()
        self.createTableAction()

        # Main layout
        self.main_layout = qtw.QVBoxLayout(self)
        self.title = qtw.QLabel('Just a Simple Table and Styles Demo')
        self.title.setAlignment(qtc.Qt.AlignCenter)
        self.title.setFont(qtg.QFont('Times', 10, weight=qtg.QFont.Bold))
        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.table)

        # Set Style
        self.setStyleSheet(self.style_sheets())

        self.show()

    def create_table_ui(self):
        rows = 5
        cols = 3

        # init table
        self.table = qtw.QTableWidget(self)
        self.table.setRowCount(rows)
        self.table.setColumnCount(cols)
        self.table.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3'])
        self.table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)

        # set table values
        for row in range(rows):
            for col in range(cols):
                self.table.setItem(row, col, qtw.QTableWidgetItem(f'Cell {row + 1},{col + 1}'))

        self.table.show()

    def createTableAction(self):
        #  create our custom QActions
        self.add_above_action = qtw.QAction("Add row above", self)
        self.add_above_action.triggered.connect(lambda: self.table.insertRow(self.table.currentRow()))
        self.add_below_action = qtw.QAction("Add row below", self)
        self.add_below_action.triggered.connect(lambda: self.table.insertRow(self.table.currentRow() + 1))

    def contextMenuEvent(self, event):
        context_menu = qtw.QMenu(self)
        context_menu.addAction(self.add_above_action)
        context_menu.addAction(self.add_below_action)

        # By passing the event's position as argument we ensure that the context menu appears at the expected position.
        context_menu.exec_(event.globalPos())

    def style_sheets(self):
        style = '''
            QTableWidget {
                border: 10px solid #3beefa
            }
            QHeaderView::section {
                background-color:grey
            }
            QTableWidget::item {
                border: 1px dotted #3beefa
            }
        '''

        return style


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec_())
