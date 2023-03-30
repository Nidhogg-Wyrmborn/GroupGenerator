from PyQt5 import QtCore, QtGui, QtWidgets

class GroupGeneratorWidget(QtWidgets.QWidget):
    # define the initialization function
    def __init__(self, parent=None):
        # initialize parent
        super(GroupGeneratorWidget, self).__init__(parent)

        # create command button (load file)
        self.Command = QtWidgets.QPushButton(self)
        self.Command.setGeometry(QtCore.QRect(350, 10, 93, 28))
        self.Command.clicked.connect(self.notify)
        self.Command.setObjectName("Command")

        # create output label (groups generated)
        self.Output = QtWidgets.QLabel(self)
        self.Output.setGeometry(QtCore.QRect(170, 140, 451, 321))
        self.Output.setAutoFillBackground(True)
        self.Output.setFrameShape(QtWidgets.QFrame.Box)
        self.Output.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Output.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignTop)
        self.Output.setObjectName("Output")

        # create parameter line edit (no. students per group)
        self.Parameters = QtWidgets.QLineEdit(self)
        self.Parameters.setGeometry(QtCore.QRect(340, 50, 113, 22))
        self.Parameters.setObjectName("Parameters")

        # create process button (calculate groups)
        self.Process = QtWidgets.QPushButton(self)
        self.Process.setGeometry(QtCore.QRect(350, 100, 93, 28))
        self.Process.clicked.connect(self.getParam)
        self.Process.setObjectName("Process")

        # set text for each widget
        self.retranslateUi(self)

    # set text for each widget
    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        self.Command.setText(_translate("GroupGeneratorWidget", "Load File"))
        self.Output.setText(_translate("GroupGeneratorWidget", " "))
        self.Parameters.setPlaceholderText(_translate("GroupGeneratorWidget", "Number of students per Group"))
        self.Process.setText(_translate("GroupGeneratorWidget", "Process"))

    # use existing file, pre-set file, or create new file
    def notify(self, filename=None):
        if filename:
            #print("load pre-existing file")
            with open(filename, 'r') as f:
                self.students = f.readlines()
            for student in range(len(self.students)):
                self.students[student] = self.students[student].replace("\n", "")
        else:
            #print("get user input")
            c = easygui.buttonbox("Use old list?", choices=["yes", "no"])
            if c == "yes":
                #print("open file")
                self.studentfile = easygui.fileopenbox("select studentfile", default="*.lst", filetypes=["*.lst"])
                try:
                    with open(self.studentfile, 'r') as f:
                        self.students = f.readlines()
                    for student in range(len(self.students)):
                        self.students[student] = self.students[student].replace("\n", "")
                except FileNotFoundError:
                    easygui.msgbox("Error, file does not exist!")
                except:
                    pass
            if c == "no":
                #print("save file")
                tutorial = tutorial = "to create a list of students, write in the names of each student (first name, lastname, middlename, which ever suits you)\n" \
                "on each line, each line will be read by the program and interpreted as a single student, once the program is open it will ask for\n" \
                "the number of students per group, i will work on making a program that can take a number of groups and figure that out"
                studentfile = easygui.filesavebox("select studentfile", default="*.lst", filetypes=["*.lst"])
                try:
                    with open(studentfile, 'w') as f:
                        f.write(tutorial)
                    os.system("start "+studentfile)
                except:
                    pass

    # test if list has duplicate items
    def dup(self, lst):
        if type(lst) != list:
            raise Exception("Not List")
        if len(lst) != len(set(lst)):
            return True
        else:
            return False

    # create 1 group of students
    def add_students(self, student_list, number_per_group):
        out = []
        for i in range(number_per_group):
            out.append(random.choice(student_list))
        if self.dup(out):
            out = list(set(out))
            count = 0
            while self.dup(out) or len(out)<number_per_group:
                count += 1
                if count > 100:
                    break
                out.append(random.choice(student_list))
                out = list(set(out))
        return out

    # create groups of students until no students left to add
    def GenerateGroups(self, student_list, number_per_group):
        groups = []
        while True:
            if student_list == []:
                break
            candidate = self.add_students(student_list, int(number_per_group))
            if self.dup(candidate):
                continue
            else:
                for c in candidate:
                    if c == '':
                        break
                    student_list.pop(student_list.index(c))
            groups.append(candidate)

        op = ''
        #print(repr(groups))
        for group in range(len(groups)):
            op+= (f"group {group+1}:\t{groups[group]}")+"\n"
        op += f"number of groups:\t{len(groups)}"+"\n"
        op += f"last group has {len(groups[-1:][0])} members"

        return op

    # reset the student list (it is emptied after generating groups)
    def resetStudentList(self):
        self.notify(self.studentfile)

    # get the parameters and calculate groups
    def getParam(self):
        if not self.studentfile:
            #print("warn")
            easygui.msgbox("No File Selected!")
            return
        # sort students into groups
        _translate = QtCore.QCoreApplication.translate

        #print("generate groups")
        # generate groups, notify on error
        try:
            output = self.GenerateGroups(self.students, int(self.Parameters.text()))
        except Exception as e:
            easygui.msgbox("Error\n"+str(e))

        #print("reset")
        # reset the studentlist
        self.resetStudentList()

        #print("set output")
        # set output label to the output variable
        self.Output.setText(_translate("MainWindow", f"{output}"))
