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

class progressWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(progressWidget, self).__init__(parent)

        # craete progressbar
        self.ProgressBar = QtWidgets.QProgressBar(self.centralwidget)

        # enable the progressbar
        self.ProgressBar.setEnabled(True)

        # set it's size(661x21) and location (70, 490)
        self.ProgressBar.setGeometry(QtCore.QRect(70, 490, 661, 21))

        # set the progress bar value to 0
        self.ProgressBar.setProperty("value", 0)

        # set the progress bar's text to center
        self.ProgressBar.setAlignment(QtCore.Qt.AlignCenter)

        # make the text visible
        self.ProgressBar.setTextVisible(True)

        # set the progressbar to horizontal
        self.ProgressBar.setOrientation(QtCore.Qt.Horizontal)

        # set the progressbar objectname
        self.ProgressBar.setObjectName("ProgressBar")

        # create the download details label
        self.progressText = QtWidgets.QLabel(self.centralwidget)

        # set the size (511x20) and location (144, 470)
        self.progressText.setGeometry(QtCore.QRect(144, 470, 511, 20))

        # set the alignment (center)
        self.progressText.setAlignment(QtCore.Qt.AlignCenter)

        # set the download details object name
        self.progressText.setObjectName("progressText")

        # set central widget (DUPLICATE, DONE TOWARDS END OF SETUP)
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.progressText.setText(_translate("MainWindow", " "))

class Ui_MainWindow(object):
    # setup the widgets in the ui
    def setupUi(self, MainWindow, nth=False):
        # setup the Main window

        # set the main window object name
        MainWindow.setObjectName("MainWindow")

        # enable the mainwindow (enable interaction)
        MainWindow.setEnabled(True)

        # size the window to 800x600 (800 px height, 600 px Width)
        MainWindow.resize(800, 600)

        # create central widget (progressbar and download details)
        self.centralwidget = QtWidgets.QStackedWidget(MainWindow)

        # set the central widget object name
        self.centralwidget.setObjectName("centralwidget")

        # hide the centralwidget (OBSOLETE)
        #self.centralwidget.hide()

        # create menubar
        self.menubar = QtWidgets.QMenuBar(MainWindow)

        # set location (0,0) and size (800x26)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))

        # set menubar object name
        self.menubar.setObjectName("menubar")

        # create menu for menubar (start module)
        self.GroupGenerator = QtWidgets.QMenu(self.menubar)

        # set object name
        self.GroupGenerator.setObjectName("GroupGenerator")

        # create submenu under GroupGenerator
        self.menuStart_Module = QtWidgets.QMenu(self.GroupGenerator)

        # set object name
        self.menuStart_Module.setObjectName("menuStart_Module")

        # open Group Generator widget on click (OBSOLETE)
        #self.GroupGenerator.aboutToShow.connect(self.GroupGeneratorWidget)

        # set main window's menubar to menubar
        MainWindow.setMenuBar(self.menubar)

        # create status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        # set object name
        self.statusbar.setObjectName("statusbar")

        # set main window's statusbar to statusbar
        MainWindow.setStatusBar(self.statusbar)

        # create action for menubar (UNUSED)
        self.actionLoad_File = QtWidgets.QAction(MainWindow)

        # set object name
        self.actionLoad_File.setObjectName("actionLoad_File")

        # create action for menubar (Check for update)
        self.actionCheck_for_Update = QtWidgets.QAction(MainWindow)

        # run function when clicked
        self.actionCheck_for_Update.triggered.connect(self.checkForUpdate)

        # set object name
        self.actionCheck_for_Update.setObjectName("actionCheck_for_Update")

        # create action for menubar (UNUSED)
        self.actionLoad = QtWidgets.QAction(MainWindow)

        # set object name
        self.actionLoad.setObjectName("actionLoad")

        # create action for submenu (Group Generator)
        self.actionGroup_Generator = QtWidgets.QAction(MainWindow)

        # run functino when clicked
        self.actionGroup_Generator.triggered.connect(self.GroupGeneratorWidget)

        # set object name
        self.actionGroup_Generator.setObjectName("actionGroup_Generator")

        self.actionModule_store = QtWidgets.QAction(MainWindow)
        self.actionModule_store.triggered.connect(self.loadModules)
        self.actionModule_store.setObjectName("actionModule_store")

        # add group generator action to submenu
        self.menuStart_Module.addAction(self.actionGroup_Generator)

        # create action for menu (OBSOLETE, CONFLICTORY)
        #self.actionStart_Module = QtWidgets.QAction(MainWindow)
        #self.actionStart_Module.triggered.connect(self.GroupGeneratorWidget)
        #self.actionStart_Module.setObjectName("actionStart_Module")

        # add check for update action to menu
        self.GroupGenerator.addAction(self.actionCheck_for_Update)

        # add separator to menubar
        self.GroupGenerator.addSeparator()

        # add start module submenu to menu
        self.GroupGenerator.addAction(self.menuStart_Module.menuAction())

        self.GroupGenerator.addAction(self.actionModule_store)

        # add menu to menubar
        self.menubar.addAction(self.GroupGenerator.menuAction())

        # declare studentfile variable (empty string)
        self.studentfile = ''

        # set MainWindow to a shared variable
        self.MainWindow = MainWindow

        # set central widget to Progressbar and download details
        self.MainWindow.setCentralWidget(self.centralwidget)

        # generate text for main window
        self.retranslateUi(MainWindow)

        self.Modules = []
        self.modList = []

        # setup all functions and connections (links between widgets)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        if nth:
            self.checkForUpdate()

    def loadModules(self):
        # load available modules from module list (in github)
        mods = self.checkResource("https://raw.githubusercontent.com/Nidhogg-Wyrmborn/GroupGenerator/main/ModuleList.MLst")

        # add available mods to self.modlist
        mods = mods.split("\n")

        for mod in range(len(mods)):
            mods[mod] = mods[mod].split("==")

        modDict = {}

        for mod in mods:
            modDict[mod[0]] = {}
            modDict[mod[0]]["version"] = mod[1]

        for mod in mods:
            self.modList.append(mod)

        print(modDict)
        print(self.modList)

    def checkResource(self, link):
        return requests.get(link, verify=False).content.decode()

    # define the update function
    def Update(self, version_number):
        print("updating") # DEBUG
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

        # exit out of program so restart is possible
        print("QtCore.QCoreApplication.instance().quit()")
        QtCore.QCoreApplication.instance().quit()

    # define the restart function (class function)
    def restart(self):
        print("restarting") # DEBUG

        # pause for 3 seconds to allow time for the main program to close
        time.sleep(3)

        # move the downloaded file to the current directory
        shutil.move("./tmp/GroupGenerator.exe", "./GroupGenerator.exe")

        # remove the temp directory
        shutil.rmtree("./tmp")

        # start the updated program
        os.system("start ./GroupGenerator.exe")

    # get version number and compare the working version
    def version(self, version1, version2):
        print("checking versions") # DEBUG

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
        print("getting version") # DEBUG

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
    def checkForUpdate(self):
        # try to update, if not possible, then change layout
        try:
            print("check for update") # DEBUG

            # set _translate for testing layout
            _translate = QtCore.QCoreApplication.translate

            self.progressText.setText(_translate("MainWindow", " "))

            # check for updates (request user intervention if downgrade recommended)
            c = self.checkUpdate()

            # if can't check (no internet or website blocked)
            if c == None:
                easygui.msgbox("unable to check for updates")
            # otherwise
            else:
                # if there is an update, update
                if c[0]:
                    self.Update(c[1])
        except:
            # set main widget to progressbar and download details
            self.setupUi(self.MainWindow)

    # define the function to switch layouts
    def GroupGeneratorWidget(self):
        #self.centralwidget.show() # OBSOLETE

        # create group generator widget
        GGWidget = GroupGeneratorWidget()

        # set main widget to ggwidget
        self.MainWindow.setCentralWidget(GGWidget)

    # define the text for each widget
    def retranslateUi(self, MainWindow):
        # create local translate function from library
        _translate = QtCore.QCoreApplication.translate

        # setup text for each widget
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GroupGenerator.setTitle(_translate("MainWindow", "Main"))
        self.menuStart_Module.setTitle(_translate("MainWindow", "Start Module"))
        self.actionLoad_File.setText(_translate("MainWindow", "Load File"))
        self.actionCheck_for_Update.setText(_translate("MainWindow", "Check for Update"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionGroup_Generator.setText(_translate("MainWindow", "Group Generator"))
        self.actionModule_store.setText(_translate("MainWindow", "Module Store"))

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