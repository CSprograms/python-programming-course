"""
NCERT Supplementary Program - Unit 5: Lists

Choice

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
myList = [22, 4, 16, 38, 13]
while True:
    print('\n1.Append 2.Insert 3.Modify 4.Del-pos '
          '5.Del-val 6.Sort-A 7.Sort-D 8.Display 9.Exit')
    ch = int(input('Choice: '))
    if   ch==1: myList.append(int(input('Element: ')))
    elif ch==2: myList.insert(int(input('Position: ')),
                              int(input('Element: ')))
    elif ch==3:
        p = int(input('Position: '))
        if p < len(myList):
            myList[p] = int(input('New element: '))
    elif ch==4:
        p = int(input('Position: '))
        if p < len(myList): myList.pop(p)
    elif ch==5:
        e = int(input('Value: '))
        if e in myList: myList.remove(e)
    elif ch==6: myList.sort()
    elif ch==7: myList.sort(reverse=True)
    elif ch==8: print('List:', myList)
    elif ch==9: break
