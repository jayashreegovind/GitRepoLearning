import os
import subprocess

list = []
cwd = os.getcwd()
cmd = 'git log C:\RadOnc\PoC\GITTest\\filelist.txt >> commit.txt'
val = os.system(cmd)
file = open('commit.txt', 'r')
for line in file:
    if line.startswith('commit'):
         data = line.split('commit')
         list.append(data[1][1:7])
file.close();
os.remove('commit.txt')
cwd = os.getcwd()
commnd = 'git diff  '+list[0]+' ' +list[1]+' C:\RadOnc\PoC\GITTest\\filelist.txt'+' >>C:\RadOnc\PoC\GITTest\\filediff.txt'
print(commnd)
cmd = 'git diff  '+list[0]+' ' +list[1]+' C:\RadOnc\PoC\GITTest\\filelist.txt'+' >>C:\RadOnc\PoC\GITTest\\filediff.txt'
val = os.system(cmd)
file1 = open('filediff.txt', 'r')
for line in file1:
    if line.startswith('+'):
        if line.startswith('+++') != True:
            print(line)
file1.close();
os.remove('filediff.txt')
cwd = os.getcwd()
cmd = 'git log C:\RadOnc\PoC\GITTest\Test >> folderdiff.txt'
val = os.system(cmd)
list = []
file2 = open('folderdiff.txt', 'r')
for line in file2:
    if line.startswith('commit'):
         if len(list) <= 2:
             data = line.split('commit')
             list.append(data[1][1:7])
         if len(list) > 2:
             break;
print(list[0]+'-'+list[1])
file2.close();
os.remove('folderdiff.txt')
cwd = os.getcwd()
commnd = 'git diff  '+list[0]+' ' +list[1]+' C:\RadOnc\PoC\GITTest\Test'+' >>C:\RadOnc\PoC\GITTest\\filediff.txt'
print(commnd)
cmd = 'git diff  '+list[0]+' ' +list[1]+' C:\RadOnc\PoC\GITTest\Test'+' >>C:\RadOnc\PoC\GITTest\\filediff.txt'
val = os.system(cmd)
file3 = open('filediff.txt', 'r')
for line in file3:
    if line.startswith('+++'):
        print(line[5:len(line)])
file3.close();
os.remove('filediff.txt')