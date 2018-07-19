import os
import subprocess

def main():
    list = []
    changedFilesinFolder = []
    filesDictionary = {}
    fname = 'C:/RadOnc/PoC/GITTest/filelist.txt'
    list = getlastcommits(fname)
    getdiffincommit(1, fname, list)
    fname = 'C:/RadOnc/PoC/GITTest/Test'
    list = getlastcommits(fname)
    changedFilesinFolder = getdiffincommit(2, fname, list)
    list = []
    print(len(changedFilesinFolder))
    for change in changedFilesinFolder:
        change = 'C:/RadOnc/PoC/GITTest'+change
        print('Passing', change)
        list = getlastcommits(change)
        print(len(list))
        filesDictionary[change] = list[0]
        print('Helloo',list[0])
    print(filesDictionary)



def getlastcommits(fname):
    list = []
    cwd = os.getcwd()
    output = 'C:/RadOnc/PoC/GITTest/commit.txt'
    cmd = 'git log '+fname+ '>> ' + output
    print(cmd)
    val = os.system(cmd)
    file = open(output, 'r')
    for line in file:
        if line.startswith('commit'):
            if len(list) <= 2:
                data = line.split('commit')
                list.append(data[1][1:7])
    file.close()
    os.remove(output)
    return list


def getdiffincommit(option, fname, list):
    changed = []
    cwd = os.getcwd()
    output = 'C:/RadOnc/PoC/GITTest/filediff.txt'
    commnd = 'git diff  ' + list[0] + ' ' + list[1] + ' '+fname+ '>> ' + output
    print(commnd)
    cmd = 'git diff  ' + list[0] + ' ' + list[1] + ' '+fname+ ' >> ' + output
    val = os.system(cmd)
    file = open(output, 'r')
    for line in file:
        if option == 1:
            if line.startswith('+'):
                if line.startswith('+++') != True:
                    print(line)
        if option == 2:
            if line.startswith('+++'):
                changed.append(line[5:len(line)-1])
                print(line[5:len(line)])
    file.close()
    print(changed)
    os.remove(output)
    return changed

main()