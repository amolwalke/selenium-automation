import time
import os
import shutil



def copyfiles():
    path = "D:\documents"
    dir_list = os.listdir(path)
    
    # print the list
    a=len(dir_list)
    print(a) 
    i=int(a)+1

    source= 'D:\\fol1'
    destination = 'D:\\New_folder'
    # shutil.copy2(source,destination)
    shutil.copytree(source,destination)
    


copyfiles()
time.sleep(5)

def rename_file():

    
    path1="D:\\New_folder\\"
    dir_list1 = os.listdir(path1)
    row_count = len(dir_list1)
    print("no of rows",row_count)
    count=row_count+1

    for j in range(row_count):
        print(j)

        print(dir_list1[j])
        vv =path1 + str(dir_list1[j])
        eee=path1 + str(count)
        ext = vv.split('.')[-1]  
        print(ext)
        qwerty = eee +'.'+ ext  
        print(qwerty)
        print(vv,qwerty)
        
        os.rename(vv,qwerty)
        count += 1


        

        
rename_file()    
