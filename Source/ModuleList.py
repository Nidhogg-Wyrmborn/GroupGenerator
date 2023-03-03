import requests

def loadModules():
    # load available modules from module list (in github)
    mods = checkResource("https://raw.githubusercontent.com/Nidhogg-Wyrmborn/GroupGenerator/main/ModuleList.MLst")

    # add available mods to self.modlist
    mods = mods.split("\n")

    for mod in range(len(mods)):
        mods[mod] = mods[mod].split("==")

    for mod in range(len(mods)):
        mods[mod][1] = mods[mod][1].split(";")

    modDict = {}

    for mod in mods:
        print(mod)
        modDict[mod[0]] = {}
        modDict[mod[0]]["Name"] = mod[0]
        modDict[mod[0]]["version"] = mod[1][0]
        modDict[mod[0]]["Title"] = mod[1][1]
        modDict[mod[0]]["Desc"] = mod[1][2]
        modDict[mod[0]]["Details"] = mod[1][3]

    modList = []
    for mod in mods:
        modList.append(mod)

    print(modDict)
    print(modList)
    return modList, modDict

def checkResource(link):
    return requests.get(link, verify=False).content.decode()