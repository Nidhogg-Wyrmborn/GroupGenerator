import random, sys, easygui

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
    number_per_group = easygui.integerbox("number of students per group")
    generator = GroupSelector(studs, number_per_group)
    easygui.msgbox(generator.main())