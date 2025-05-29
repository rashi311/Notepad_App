from PyQt6.QtWidgets import QInputDialog,QFileDialog,QMenu,QMenuBar,QMainWindow,QVBoxLayout,QStackedLayout,QPushButton,QTextEdit,QComboBox,QApplication,QWidget,QLabel,QLineEdit,QFormLayout
import sys
from PyQt6.QtGui import QAction,QIcon,QTextCursor,QColor
from PyQt6.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Notepad")
        self.setGeometry(100,100,400,400)

        self.current_file=None

        self.edit_field=QTextEdit(self)
        self.setCentralWidget(self.edit_field)

        #create a menubar
        menubar=QMenuBar(self)
        self.setMenuBar(menubar)

        #create file menu
        file_menu=QMenu("File",self)
        menubar.addMenu(file_menu)

        #create action
        new_action=QAction("New",self)
        file_menu.addAction(new_action)
        new_action.triggered.connect(self.new_file)

        open_action=QAction("Open",self)
        file_menu.addAction(open_action)
        open_action.triggered.connect(self.open_file)

        save_action=QAction("Save",self)
        file_menu.addAction(save_action)
        save_action.triggered.connect(self.save_file)
        
        saveas_action=QAction("Save as",self)
        file_menu.addAction(saveas_action)
        saveas_action.triggered.connect(self.save_file_as)


        #creating edit menu
        edit_menu=QMenu("Edit",self)
        menubar.addMenu(edit_menu)

        #creating edit action
        undo_action=QAction("Undo",self)
        edit_menu.addAction(undo_action)
        undo_action.triggered.connect(self.edit_field.undo)

        redo_action=QAction("Redo",self)
        edit_menu.addAction(redo_action)
        redo_action.triggered.connect(self.edit_field.redo)
        
        cut_action=QAction("Cut",self)
        edit_menu.addAction(cut_action)
        cut_action.triggered.connect(self.edit_field.cut)

        copy_action=QAction("Copy",self)
        edit_menu.addAction(copy_action)
        copy_action.triggered.connect(self.edit_field.copy)

        paste_action=QAction("Paste",self)
        edit_menu.addAction(paste_action)
        paste_action.triggered.connect(self.edit_field.paste)

        find_action=QAction("Find",self)
        edit_menu.addAction(find_action)
        find_action.triggered.connect(self.find_text)
        
    def new_file(self):
        print("creating new file") 
        self.edit_field.clear()
        self.current_file=None

    def open_file(self):
        print("opening a file")    
        file_path,_=QFileDialog.getOpenFileName(self,"Open file","","All files(*);; Python File(*.py)") 
        with open(file_path,"r") as  file:
            text=file.read()
            self.edit_field.setText(text)

    def save_file_as(self):
        print("saving the file") 
        file_path,_= QFileDialog.getSaveFileName(self,"Save file","","All files(*);; Python File(*.py)")
        if file_path:
            with open(file_path,"w") as file:
                file.write(self.edit_field.toPlainText())

            self.current_file=file_path    

    def save_file(self):
        print("saving the file ")
        if self.current_file:  
            with open(self.current_file,"w") as file:
                file.write(self.edit_field.toPlainText()) 
        else:
            self.save_file_as()   

    def find_text(self):
        print("finding text")
        search_text,ok=QInputDialog.getText(self,"Find Text","Search for") 
        if ok:
            all_words=[]
            self.edit_field.moveCursor(QTextCursor.MoveOperation.Start)  
            highlight_color=QColor(Qt.GlobalColor.yellow)    

            while(self.edit_field.find(search_text)): 
                selection=QTextEdit.ExtraSelection()
                selection.format.setBackground(highlight_color) 

                selection.cursor=self.edit_field.textCursor()
                all_words.append(selection)

            self.edit_field.setExtraSelections(all_words)    



app=QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec())        
