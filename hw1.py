#Pairut Dumkuengthanant ID: 64856070
#Marco Pinuelas ID: 27707619
from pathlib import Path
import shutil
def shorten(code):
    iname=code[2:]
    return iname
def search_name(name: str, file_path: Path)-> Path:
    try:
        nfile=(file_path.joinpath(Path(name)))
        if nfile.exists()==True:
            return 'True', nfile
        else:
            #print("ERROR")
            return 'False', 'False'
    except:
        return 'False', 'False'
def extension_name(extension: str, file_path: Path)->Path:
        try:
            ext='**/'+extension
            newpath=(sorted((file_path).glob(ext)))
            (newpath[0])
            (newpath[0].exists())
            return newpath
        except:
            return 'ERROR'
def compare_size(fsize: int, file_path: Path)->[Path]:
    anpath=sorted(file_path.glob('**/*.*'))
    ll=[]
    for i in range(len(anpath)):
        if anpath[i].stat().st_size>=int(fsize):
            ll.append(str(anpath[i]))
    return ll
def main():
    input1=input("")
    fname=Path(input1)
    while True:
        fname=Path(input1)
        if fname.exists():
            break
        else:
            print("ERROR")
            input1=input("")
    input2=input("")
    while True:
        if input2[0]=='N':
            namef=shorten(input2)
            bol,nname=search_name(namef,fname)
            if bol=='True':
                nfilepath=search_name(namef, fname)
                break
        if input2[0]=='E':
            ext=shorten(input2)
            if '.' in ext:
                extend1='*'+ext
                nfilepath=extension_name(extend1,fname)
                nname=nfilepath
                if nfilepath!='ERROR':
                    break  
            elif '.' not in ext:
                extend1='*.'+ext
                nfilepath=extension_name(extend1, fname)
                nname=nfilepath
                if nfilepath!='ERROR':
                    break
        if input2[0]=='S':
            sizen=shorten(input2)
            nname=compare_size(sizen, fname)
            #print(nname)
            break
        
        else:
            print("ERROR")
        input2=input("")
    input3=input("")
    while True:
        if input3=='P':
            if type(nname)==list:
                for i in range(len(nname)):
                    print(nname[i])
                break
            else:
                print(str(nname))
                break
        if input3=='F':
            if type(nname)==list:
                for i in range(len(nname)):
                    if '.txt' in str(nname[i]):
                        print(nname[i])
                        fle=open(str(nname[i]), 'r')
                        nfle=fle.readline()
                        print(nfle,'\n', end='')
                    elif '.py' in str(nname[i]):
                        print(nname[i])
                        fle=open(str(nname[i]), 'r')
                        nfle=fle.readline()
                        print(nfle,'\n', end='')
                fle.close()
                break
            else:
                fle=open(str(nname), 'r')
                nfle=fle.readline()
                print(str(nname))
                for i in nfle:
                    print(i, end='')
                fle.close()
                break
        if input3=='D':
            if type(nname)==list:
                for i in range(len(nname)):
                    newfle=str(nname[i])+'.dup'
                    shutil.copy(str(nname[i]), newfle)
                    print(newfle)
                break
            else:
                newfle=str(nname)+'.dup'
                shutil.copy(str(nname), newfle)
                print(newfle)
                break
        if input3=='T':
            if type(nname)==list:
                for i in range(len(nname)):
                    Path(nname[i]).touch()
                    print(str(nname[i]))
                break
            else:        
                Path(nname).touch()
                print(str(nname))
                break
        else:
            print("ERROR")
        input3=input("")
main()
