import random, sys, easygui

WorkingVersion = 1.0.0

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
    with open(studentfile, 'w') as f:
        f.write(tutorial)
    sys.exit(1)

studs = []

for student in studentlist:
    studs.append(student.replace("\n", ""))

def update(version):
    # update to given version

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

    for i in range(len(numbers)):
        index = len(numbers)-i
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
            easygui.msgbox("HOW ON EARTH DID YOU GET AHEAD OF DEV????")
            sys.exit(1)
    return False

def checkUpdate():
    # check for update
    content = requests.get("https://raw.githubusercontent.com/Nidhogg-Wyrmborn/GroupGenerator/main/version.v", verify=False)
    print(content)
    if version(content, WorkingVersion):
        # if update
        return [True, content]
    else:
        # if no update
        return [False, None]

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

        for group in range(len(self.groups)):
            op+=(f"group {group+1}:\t{self.groups[group]}")+"\n"
        op+=(f"number of groups:\t{len(self.groups)}")+"\n"
        op+=(f"last group has {len(self.groups[-1:][0])} members")

        return op

if __name__ == '__main__':
    c = checkUpdate()
    if c[0]:
        Update(c[1])
    number_per_group = easygui.integerbox("number of students per group")
    generator = GroupSelector(studs, number_per_group)
    easygui.msgbox(generator.main())