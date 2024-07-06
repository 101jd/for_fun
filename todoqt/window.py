from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMenuBar, QLineEdit, QFileDialog, QLabel, QListWidget, QListWidgetItem, QListView, QPushButton, QSpinBox, QMainWindow
from PyQt6.QtGui import QAction

from todolist import TodoLost
from completedlist import CompletedList
from TaskBuilder import TaskBuilder
from Task import Task
from rwer import ReadWriter

##TODO 

##DONE
# Option NEW 
# FIX Index bug
# FIX Empty edit
# Set selected text in field
# List Completed

class TODOWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TODO')
        self.setCentralWidget(self.widget)
        self.todolist = TodoLost([])
        self.tb = TaskBuilder(0)
        self.cl = CompletedList()
        print('init', type(self.cl))
        
        self.add_task_butt.clicked.connect(self.add_button_clicked)
        self.complete_butt.clicked.connect(self.complete_butt_clicked)
        self.edit_butt.clicked.connect(self.edit_butt_clicked)
        self.sort_num_butt.clicked.connect(self.sort_num_butt_clicked)
        self.sort_prior_butt.clicked.connect(self.sort_prior_butt_clicked)
        self.delete_butt.clicked.connect(self.delete_task)
        
        self.new_opt.setCheckable(True)
        self.new_opt.triggered.connect(self.new_list)
        self.save_opt.setCheckable(True)
        self.save_opt.triggered.connect(self.save_list)
        self.load_opt.setCheckable(True)
        self.load_opt.triggered.connect(self.load_list)
        self.output.itemClicked.connect(self.item_selected)
        
        
    app = QApplication([])
    
    # WIDGETS & LAYOUTS:
    vbox = QVBoxLayout() # ОБЩАЯ ВЕРТИКАЛЬ
    widget = QWidget() # ОСНОВНОЙ ВИДЖЕТ
    text_todo = QLabel()
    text_todo.setText('TODO:')
    text_completed = QLabel()
    text_completed.setText('Completed')
    output = QListWidget()
    completed = QListWidget()
    completed.setFixedHeight(100)
    text_field = QLineEdit()
    menu = QMenuBar()
    
    vhwidget_1 = QWidget()
    vhwidget_2 = QWidget()
    
    file_opt = menu.addMenu('File')
    new_opt = file_opt.addAction('New')
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
    delete_butt = QPushButton()
    delete_butt.setText('Delete')
    
    hbox_1.addWidget(set_prior)
    hbox_1.addWidget(add_task_butt)
    
    hbox_2.addWidget(sort_num_butt)
    hbox_2.addWidget(sort_prior_butt)
    hbox_2.addWidget(edit_butt)
    hbox_2.addWidget(complete_butt)
    hbox_2.addWidget(delete_butt)
    
    vhwidget_1.setLayout(hbox_1)

    output.setAutoScroll(True)
    
    vbox.addWidget(menu)
    vbox.addWidget(text_todo)
    vbox.addWidget(output)
    vbox.addWidget(text_completed)
    vbox.addWidget(completed)
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
            task = self.todolist.complete_task(self.output.currentRow())
            self.output.takeItem(self.output.currentRow())
            self.cl.add_task(task)
            print('complete', type(self.cl))
            self.completed.addItem(task.to_string())
            
    def delete_task(self):
        if not self.todolist.is_empty():
            self.todolist.complete_task(self.output.currentRow())
            self.output.takeItem(self.output.currentRow())
        
    def edit_butt_clicked(self):
        if self.output.currentRow() > -1:
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
        
    def new_list(self):
        self.todolist = TodoLost([])
        self.cl.clear()
        # print('new', type(self.cl))
        self.tb = TaskBuilder(0)
        self.output.clear()
        self.completed.clear()
        self.new_opt.setChecked(False)
        
    def save_list(self):
        rw = ReadWriter()
        option = QFileDialog().options()
        path = self.save_as_dial.getSaveFileName(self.text_field, "Save file", "default.pickle", "*.pickle", options=option)[0]
        if path != "":
            print('save', type(self.cl))
            rw.write(self.todolist, self.cl, path)
        self.save_opt.setChecked(False)
            
    def load_list(self):
        rw = ReadWriter()
        option = QFileDialog().options()
        path = self.save_as_dial.getOpenFileName(self.text_field, "Load File", "", "*.pickle", options=option)[0]
        if path != "":
            self.todolist = rw.read(path)[0]
            print('read', type(self.cl))
            self.cl = rw.read(path)[1]
        self.output.clear()
        self.output.addItems([el.to_string() for el in self.todolist.get_todo_list()])
        self.completed.addItems([el.to_string() for el in self.cl.get_list()])
        self.tb = TaskBuilder(self.todolist.get_last_number() + 1)
        self.load_opt.setChecked(False)
        
    def item_selected(self):
        text = self.todolist.get_task(self.output.currentRow()).get_description()
        self.text_field.setText(text)
                
    def size(self):
        return self.todolist.size()
    
window = TODOWindow()
window.show()

TODOWindow.app.exec()