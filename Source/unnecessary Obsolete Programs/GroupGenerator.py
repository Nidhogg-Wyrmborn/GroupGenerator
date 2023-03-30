import random, sys, os, easygui, threading, requests, shutil, time
import tkPBar as tkPB

WorkingVersion = "1.0.4"

def restart():
    time.sleep(1)
    shutil.move("./tmp/GroupGenerator.exe", "./GroupGenerator.exe")
    shutil.rmtree("./tmp")
    os.system("start ./GroupGenerator.exe")

def Update(version_number, pbar):
    # update to given version

    target = f"https://raw.githubusercontent.com/Nidhogg-Wyrmborn/GroupGenerator/main/Dist/{version_number}/GroupGenerator.exe"

    filesize = requests.get(target, stream=True, verify=False).headers['content-length']
    print(filesize)
    #sys.exit()

    os.mkdir("./tmp")
    # display progress bar
    pbar.root.destroy()
    pbar = tkPB.tkProgressbar(int(filesize), Determinate=True)
    with requests.get(target, stream=True, verify=False) as r:
        r.raise_for_status()
        prev = 0
        with open("./tmp/GroupGenerator.exe", 'wb') as f:
            # create counter
            num = 0
            for chunk in r.iter_content(chunk_size=8192):
                # iterate chunks
                f.write(chunk)
                num += 1
                pbar.update(len(chunk))
                current = prev + (len(chunk)/int(filesize))*100
                prev = current
                pbar.description(Desc=f"%{round(current,1)}")
    pbar.root.destroy()
    threading.Thread(target=restart, daemon=False).start()
    sys.exit(1)

def version(version1, version2):
    # check versions if version1 greater that version2 True
    version1 = version1.split(".")
    version2 = version2.split('.')

    if len(version1)!=len(version2):
        easygui.msgbox("Version Numbers not same format, please report on github:\n https://github.com/Nidhogg-Wyrmborn/GroupGenerator")
        sys.exit(1)

    numbers = []

    for num in range(len(version1)):
        numbers.append([version1[num], version2[num]])

    print(numbers)

    for i in range(len(numbers)):
        index = i
        if numbers[index][0] > numbers[index][1]:
            print("greater")
            easygui.msgbox("update available")
            return True
            break
        if numbers[index][0] == numbers[index][1]:
            print("equal")
            continue
        else:
            print("lesser")
            c = easygui.buttonbox("You are ahead of Development, Downgrade?", choices=["yes", "no"])
            if c == "yes":
                return True
            else:
                return False
    return False

def checkUpdate():
    # check for update
    c = tkPB.tkProgressbar(10000,Determinate=False)
    c.description("Check for updates")
    try:
        content = requests.get("https://raw.githubusercontent.com/Nidhogg-Wyrmborn/GroupGenerator/main/version.v", verify=False)
    except:
        return None
    print(content.content.decode())
    if version(content.content.decode(), WorkingVersion):
        c.description("update found")
        # if update
        return [True, content.content.decode(), c]
    else:
        c.description("no update found")
        c.root.destroy()
        # if no update
        return [False, None, None]

class GroupSelector:
    def __init__(self, student_list, number_per_group):
        self.student_list = student_list
        self.number_per_group = number_per_group
        self.groups = []
        self.c = []

    def dup(self, lst):
        if type(lst) != list:
            raise Exception("Not List")
        if len(lst) != len(set(lst)):
            return True
        else:
            return False

    def add_students(self, student_list, number_per_group):
        out = []
        for i in range(number_per_group):
            #print(i)
            out.append(random.choice(student_list))
        if self.dup(out):
            out = list(set(out))
            count = 0
            while self.dup(out) or len(out)<number_per_group:
                count+=1
                if count > 100:
                    break
                #print(out)
                out.append(random.choice(student_list))
                out = list(set(out))
        return out

    def main(self):
        self.groups = []
        while True:
            # is adding students to list
            if self.student_list == []:
                break
            candidate = self.add_students(self.student_list, self.number_per_group)
            if self.dup(candidate):
                #print(candidate, end="\r")
                continue
            else:
                for c in candidate:
                    if c == '':
                        break
                    self.student_list.pop(self.student_list.index(c))
            
            self.groups.append(candidate)

        op = ''
        #print(self.groups)

        for group in range(len(self.groups)):
            op+=(f"group {group+1}:\t{self.groups[group]}")+"\n"
        op+=(f"number of groups:\t{len(self.groups)}")+"\n"
        op+=(f"last group has {len(self.groups[-1:][0])} members")

        return op

def Initialize():
    c = checkUpdate()
    if c == None:
        easygui.msgbox("unable to check for updates")
    else:
        if c[0]:
            print(c)
            #sys.exit()
            Update(c[1], c[2])

if __name__ == '__main__':
    Initialize()

    new = easygui.buttonbox("create new list?", choices=['yes', 'no'])
    if new == "yes":
        studentfile = easygui.filesavebox("select studentfile", default="*.lst", filetypes=["*.lst"])
    if new == 'no':
        studentfile = easygui.fileopenbox("select studentfile", default="*.lst", filetypes=["*.lst"])

    try:
        with open(studentfile, 'r') as f:
            studentlist = f.readlines()
    except:
        tutorial = "to create a list of students, write in the names of each student (first name, lastname, middlename, which ever suits you)\n" \
        "on each line, each line will be read by the program and interpreted as a single student, once the program is open it will ask for\n" \
        "the number of students per group, i will work on making a program that can take a number of groups and figure that out"
        try:
            with open(studentfile, 'w') as f:
                f.write(tutorial)
            sys.exit(1)
        except:
            print("NoneType")
            sys.exit(1)

    studs = []

    for student in studentlist:
        studs.append(student.replace("\n", ""))

    running = True

    while running:
        try:
            number_per_group = easygui.integerbox("number of students per group")
            if number_per_group == None:
                running = False
            generator = GroupSelector(studs, number_per_group)
            easygui.msgbox(generator.main())
            studs = []
            for student in studentlist:
                studs.append(student.replace("\n", ""))
            del generator
        except:
            running = False
            continue