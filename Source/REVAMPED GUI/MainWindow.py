# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#
# NOTE: THIS FILE IS EDITED SEPARATE, NEW FILE IS CREATED WHEN GUI IS UPDATED
# AND MERGED INTO THIS PROGRAM


from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
import easygui, random, requests, os, sys, time, shutil

# define working version (str)
WorkingVersion = "1.1.0"

class Ui_MainWindow(object):
    # setup the widgets in the ui
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.centralwidget.hide()
        self.ProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.ProgressBar.setEnabled(True)
        self.ProgressBar.setGeometry(QtCore.QRect(70, 490, 661, 21))
        self.ProgressBar.setProperty("value", 0)
        self.ProgressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.ProgressBar.setTextVisible(True)
        self.ProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.ProgressBar.setObjectName("ProgressBar")
        self.progressText = QtWidgets.QLabel(self.centralwidget)
        self.progressText.setGeometry(QtCore.QRect(144, 470, 511, 20))
        self.progressText.setAlignment(QtCore.Qt.AlignCenter)
        self.progressText.setObjectName("progressText")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.GroupGenerator = QtWidgets.QMenu(self.menubar)
        self.GroupGenerator.setObjectName("GroupGenerator")
        self.menuStart_Module = QtWidgets.QMenu(self.GroupGenerator)
        self.menuStart_Module.setObjectName("menuStart_Module")
        #self.GroupGenerator.aboutToShow.connect(self.GroupGeneratorWidget)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_File = QtWidgets.QAction(MainWindow)
        self.actionLoad_File.setObjectName("actionLoad_File")
        self.actionCheck_for_Update = QtWidgets.QAction(MainWindow)
        self.actionCheck_for_Update.triggered.connect(self.checkForUpdate)
        self.actionCheck_for_Update.setObjectName("actionCheck_for_Update")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionGroup_Generator = QtWidgets.QAction(MainWindow)
        self.actionGroup_Generator.triggered.connect(self.GroupGeneratorWidget)
        self.actionGroup_Generator.setObjectName("actionGroup_Generator")
        self.menuStart_Module.addAction(self.actionGroup_Generator)
        #self.actionStart_Module = QtWidgets.QAction(MainWindow)
        #self.actionStart_Module.triggered.connect(self.GroupGeneratorWidget)
        #self.actionStart_Module.setObjectName("actionStart_Module")
        self.GroupGenerator.addAction(self.actionCheck_for_Update)
        self.GroupGenerator.addSeparator()
        self.GroupGenerator.addAction(self.menuStart_Module.menuAction())
        self.menubar.addAction(self.GroupGenerator.menuAction())

        self.studentfile = ''
        self.MainWindow = MainWindow
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.checkForUpdate(True)

    # define the update function
    def Update(self, version_number):
        print("updating")
        # set central widget to the progress bar
        self.MainWindow.setCentralWidget(self.centralwidget)

        # define target
        target = f"https://raw.githubusercontent.com/Nidhogg-Wyrmborn/GroupGenerator/main/Dist/{version_number}/GroupGenerator.exe"

        # get the filesize for downloading
        filesize = requests.get(target, stream=True, verify=False).headers['content-length']
        print(filesize)

        # make tmp directory
        os.mkdir("./tmp")

        # begin downloading
        with requests.get(target, stream=True, verify=False) as r:
            # get status of remote host
            r.raise_for_status()
            prev = 0
            with open("./tmp/GroupGenerator.exe", "wb") as f:
                # create counter
                num = 0

                # for each chunk in stream, write chunk
                for chunk in r.iter_content(chunk_size=8192):
                    # iterate chunks (8192 Bytes, 8 KB)
                    f.write(chunk)
                    num += 1

                    # calculate percentage done
                    percentage = prev + (len(chunk)/int(filesize))*100
                    prev = percentage

                    # update progress bar
                    self.ProgressBar.setValue(int(round(percentage,0)))
                    #print(self.ProgressBar.value()) # DEBUG

        # create restart thread
        Thread(target=self.restart, daemon=False).start()
        sys.exit(1)

    # define the restart function (class function)
    def restart(self):
        print("restarting")
        time.sleep(3)
        shutil.move("./tmp/GroupGenerator.exe", "./GroupGenerator.exe")
        shutil.rmtree("./tmp")
        os.system("start ./GroupGenerator.exe")

    # get version number and compare the working version
    def version(self, version1, version2):
        print("checking versions")
        # split into individual digits
        version1 = version1.split(".")
        version2 = version2.split(".")

        # check if the version numbers are compatible
        if len(version1) != len(version2):
            easygui.msgbox("Version Numbers not save format, please report on github")
            return False

        # create matrix of version numbers
        numbers = []

        # add version digits to numbers matrix
        for num in range(len(version1)):
            # add each digit to matrix as list e.g. [[1,1],[0,0],[0,1]]
            numbers.append([version1[num], version2[num]])

        # test if dev version number equal, lesser, or greater than working
        for i in range(len(numbers)):
            # if greater then update available
            if numbers[i][0] > numbers[i][1]:
                return True
                break

            # if equal continue
            if numbers[i][0] == numbers[i][1]:
                continue

            # else (lesser) then notify and ask if downgrade
            else:
                c = easygui.buttonbox("You are ahead of Development, Downgrade?", choices=["yes", "no"])
                # if yes, "update" available
                if c == "yes":
                    return True

                # otherwise leave be
                else:
                    return False

    # check for updates
    def checkUpdate(self):
        print("getting version")
        # set _translate for displaying progresstext
        _translate = QtCore.QCoreApplication.translate

        # try to get version numbers, if fail, no internet, continue
        try:
            content = requests.get("https://raw.githubusercontent.com/Nidhogg-Wyrmborn/GroupGenerator/main/version.v", verify=False)
        except:
            print("error")
            return None

        # if update available
        if self.version(content.content.decode(), WorkingVersion):
            print("update available")
            # display text above progress bar
            self.progressText.setText(_translate("MainWindow", "Update Available"))
            return [True, content.content.decode()]
        # otherwise return [false, none]
        else:
            return [False, None]

    # when button clicked to check for update, run this
    def checkForUpdate(self, isSelf=False):
        if not isSelf:
            self.setupUi(self.MainWindow)
        print("check for update")
        c = self.checkUpdate()
        if c == None:
            easygui.msgbox("unable to check for updates")
        else:
            if c[0]:
                self.Update(c[1])

    # define the function to switch layouts
    def GroupGeneratorWidget(self):
        #self.centralwidget.show()
        GGWidget = GroupGeneratorWidget()
        self.MainWindow.setCentralWidget(GGWidget)

    # define the text for each widget
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.progressText.setText(_translate("MainWindow", " "))
        self.GroupGenerator.setTitle(_translate("MainWindow", "Main"))
        self.menuStart_Module.setTitle(_translate("MainWindow", "Start Module"))
        self.actionLoad_File.setText(_translate("MainWindow", "Load File"))
        self.actionCheck_for_Update.setText(_translate("MainWindow", "Check for Update"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionGroup_Generator.setText(_translate("MainWindow", "Group Generator"))

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


# if run as main, execute code below
if __name__ == "__main__":
    # create the app
    app = QtWidgets.QApplication(sys.argv)

    # create the main window
    MainWindow = QtWidgets.QMainWindow()

    # create the ui from the class
    ui = Ui_MainWindow()

    # setup the widgets
    ui.setupUi(MainWindow)

    # show the window
    MainWindow.show()

    # exit on app exit (press the x)
    sys.exit(app.exec_())