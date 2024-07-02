from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMenuBar, QLineEdit, QFileDialog, QLabel, QListWidget, QListWidgetItem, QListView, QPushButton, QSpinBox, QMainWindow
from PyQt6.QtGui import QAction

from todolist import TodoLost
from TaskBuilder import TaskBuilder
from Task import Task
from rwer import ReadWriter

class TODOWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TODO')
        self.setCentralWidget(self.widget)
        self.todolist = TodoLost([])
        self.tb = TaskBuilder()
        
        self.add_task_butt.clicked.connect(self.add_button_clicked)
        self.complete_butt.clicked.connect(self.complete_butt_clicked)
        self.edit_butt.clicked.connect(self.edit_butt_clicked)
        self.sort_num_butt.clicked.connect(self.sort_num_butt_clicked)
        self.sort_prior_butt.clicked.connect(self.sort_prior_butt_clicked)
        
        self.save_opt.setCheckable(True)
        self.save_opt.triggered.connect(self.save_list)
        self.load_opt.setCheckable(True)
        self.load_opt.triggered.connect(self.load_list)
        
    app = QApplication([])
    
    
    # WIDGETS & LAYOUTS:
    vbox = QVBoxLayout() # ОБЩАЯ ВЕРТИКАЛЬ
    widget = QWidget() # ОСНОВНОЙ ВИДЖЕТ
    output = QListWidget()
    text_field = QLineEdit()
    menu = QMenuBar()
    
    vhwidget_1 = QWidget()
    vhwidget_2 = QWidget()
    
    file_opt = menu.addMenu('File')
    save_opt = file_opt.addAction('Save')
    load_opt = file_opt.addAction('Load')
    
    
    hbox_1 = QHBoxLayout() # ВЕРХНЯЯ ГОРИЗОНТАЛЬ ПРИОРИТЕТ И КНОПКА ДОБАВИТЬ
    set_prior = QSpinBox()
    set_prior.setMaximumSize(50, 20)
    add_task_butt = QPushButton()
    add_task_butt.setText("Add task")
    
    hbox_2 = QHBoxLayout() # НИЖНЯЯ ГОРИЗОНТАЛЬ С КНОПКАМИ УПРАВЛЕНИЯ
    sort_num_butt = QPushButton()
    sort_num_butt.setText("Sort by num")
    sort_prior_butt = QPushButton()
    sort_prior_butt.setText('Sort by priority')
    edit_butt = QPushButton()
    edit_butt.setText('Edit')
    complete_butt = QPushButton()
    complete_butt.setText('Complete')
    
    hbox_1.addWidget(set_prior)
    hbox_1.addWidget(add_task_butt)
    
    hbox_2.addWidget(sort_num_butt)
    hbox_2.addWidget(sort_prior_butt)
    hbox_2.addWidget(edit_butt)
    hbox_2.addWidget(complete_butt)
    
    vhwidget_1.setLayout(hbox_1)

    output.setAutoScroll(True)
    # for i in range(50):
    #     output.addItem('Hello')
    #     output.addItem('World!')
    
    
    vbox.addWidget(menu)
    vbox.addWidget(output)
    vbox.addWidget(text_field)
    
    
    vhwidget_1.setLayout(hbox_1)
    vhwidget_2.setLayout(hbox_2)
    vbox.addWidget(vhwidget_1)
    vbox.addWidget(vhwidget_2)
    widget.setLayout(vbox)
    # END OF WIDGETS & LAYOUTS
    
    save_as_dial = QFileDialog()
    
    ## SLOTS
    
    def add_button_clicked(self):
        task = self.tb.new_task(self.set_prior.value(), self.text_field.displayText())
        self.todolist.add_task(task)
        item = QListWidgetItem(task.to_string())
        self.output.addItem(item)
        self.text_field.clear()
        
    def complete_butt_clicked(self):
        if not self.todolist.is_empty():
            self.todolist.complete_task(self.output.currentRow())
            self.output.takeItem(self.output.currentRow())
        
    def edit_butt_clicked(self):
        if self.output.currentRow() >= -1:
            task:Task = self.todolist.get_task(self.output.currentRow())
            task.edit(self.set_prior.value(), self.text_field.displayText())
            self.output.clear()
            self.output.addItems([el.to_string() for el in self.todolist.get_todo_list()])
            self.text_field.clear()
        
    def sort_num_butt_clicked(self):
        self.output.clear()
        self.output.addItems([el.to_string() for el in self.todolist.sort_by_num()])
        
    def sort_prior_butt_clicked(self):
        self.output.clear()
        self.output.addItems([el.to_string() for el in self.todolist.sort_by_priority()])
        
    def save_list(self):
        rw = ReadWriter()
        option = QFileDialog().options()
        path = self.save_as_dial.getSaveFileName(self.text_field, "Save file", "default.pickle", "*.pickle", options=option)[0]
        if path != "":
            rw.write(self.todolist, path)
        self.save_opt.setChecked(False)
            
    def load_list(self):
        rw = ReadWriter()
        option = QFileDialog().options()
        path = self.save_as_dial.getOpenFileName(self.text_field, "Load File", "", "*.pickle", options=option)[0]
        if path != "":
            self.todolist = rw.read(path)
        self.output.clear()
        self.output.addItems([el.to_string() for el in self.todolist.get_todo_list()])
        self.load_opt.setChecked(False)
        
            
    
window = TODOWindow()
window.show()

TODOWindow.app.exec()