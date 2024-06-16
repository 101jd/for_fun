from PyQt6.QtWidgets import QMainWindow, QFileDialog, QApplication, QMenuBar, QTextEdit


class NoticeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Notes")
        self.setContentsMargins(0, 0, 0, 30)
        self.setMenuBar(self.menu_bar)
        
        self.save_opt.setCheckable(True)
        self.save_opt.triggered.connect(self.save_text)
        
        self.load_opt.setCheckable(True)
        self.load_opt.triggered.connect(self.load_file)
        
        self.new_opt.setCheckable(True)
        self.new_opt.triggered.connect(self.clear_field)
        
        self.exit_opt.setCheckable(True)
        self.exit_opt.triggered.connect(self.terminate)
        
        self.setCentralWidget(self.text_field)
        self.text_field.setReadOnly(False)
        
    def save_text(self):
        option = QFileDialog().options()
        path = self.save_as_dial.getSaveFileName(self.text_field, "Save file", "default.txt", "*.txt", options=option)[0]
        
        with open (f'{path}', 'w', encoding="utf-8") as file:
            file.write(self.text_field.toPlainText())
            
        self.save_opt.setChecked(False)
        
    def load_file(self):
        option = QFileDialog().options()
        path = self.save_as_dial.getOpenFileName(self.text_field, "Load File", "", "*.txt", options=option)[0]
        
        with open(f'{path}', 'r', encoding="utf-8") as file:
            self.text_field.setText(file.read())
            
        self.load_opt.setChecked(False)
            
    def clear_field(self):
        self.text_field.clear()
        self.new_opt.setChecked(False)
            
    def terminate(self):
        self.close()
   
    app = QApplication([])
        
    menu_bar = QMenuBar()
    file_opt = menu_bar.addMenu("File")
    new_opt = file_opt.addAction("New")
    load_opt = file_opt.addAction("Load")
    save_opt = file_opt.addAction("Save")
    exit_opt = file_opt.addAction("Exit")
    
    text_field = QTextEdit()
    
    save_as_dial = QFileDialog()
    
    
window = NoticeWindow()
window.show()


NoticeWindow.app.exec()