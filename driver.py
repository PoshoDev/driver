import os, subprocess

mat = "601341p"

def main():
    print("Loading programs for "+mat+"...")
    i = 1
    fname = mat + str(i) + ".py"
    while os.path.exists(fname):
        DrawBorder(fname)
        j = 1
        while os.path.exists(Inp(i, j)):
            RunCode(mat, i, j)
            # Loading Outputs
            a, la = GetList("correct"+Ext(i, j))
            b, lb = GetList(Out(i, j))            
            DrawHeader(la, lb, j)
            errors = 0
            total = len(a)
            for k in range(total):
                check = '=' if a[k]==b[k] else 'X'
                DrawInner(a[k], b[k], la, lb, check)
                if (a[k] != b[k]): errors += 1
            DrawBottom(la, lb, errors, total)
            j += 1
        i += 1
        fname = mat + str(i) + ".py"
        
def DrawHeader(la, lb, j):
    print('┌' + '─'*(la+lb+9) + '┐')
    print("│ " + Spaces("Case #"+str(j), la+lb+7) + " │")
    print('├──' + '─'*la + "┬───┬" + '─'*lb + '──┤')
    
def DrawInner(inpa, inpb, la, lb, check):
    print("│ " + Spaces(inpa, la) + " │ " +check+" │ "+ Spaces(inpb, lb) + " │")
    
def DrawBottom(la, lb, errors, total):
    print('├──' + '─'*la + "┴───┴" + '─'*lb + '──┤')
    print("│ " + Spaces("SCORE:", la+lb+7) + " │")
    print("│ " + Spaces(str(total-errors)+" / "+str(total), la+lb+7) + " │")
    print('└' + '─'*(la+lb+9) + '┘')
    
def DrawBorder(text):
    print("")
    print('╔══' + '═'*(len(text)) + '══╗')
    print("║  " + text + "  ║")
    print('╚══' + '═'*(len(text)) + '══╝')

def Ext(i, j):
    return "_"+str(i)+"_"+str(j)+".txt"

def Inp(i, j):
    return "input" + Ext(i, j)
    
def Out(i, j):
    return "output" + Ext(i, j)
    
def GetList(fname):
    l = []
    biggest = 0
    with open(fname) as f:
        l.append(f.read().splitlines())
        for i in range(len(l[0])):
            if len(l[0][i]) > biggest:
                biggest = len(l[0][i])
    return l[0], biggest
    
def Spaces(res, size):
    for i in range(size-len(res)):
        res += ' '
    return res
    
def RunPython(fname, i, j):
    os.system("python "+fname+".py < "+Inp(i, j)+" > "+Out(i, j))

def RunCpp(fname):
    return

def RunJava(fname):
    return

def LookFor(name, ext):
    if os.path.exists(name + ext):
        return True
    return False

def RunCode(mat, i, j):
    name = mat + str(i)
    if LookFor(mat, ".py"):
        RunPython(name, i, j)
        return True
    elif LookFor(mat, ".cpp"):
        RunCpp(name, i, j)
        return True
    elif LookFor(mat, ".java"):
        RunJava(name, i, j)
        return True
    return False
        
if __name__ == "__main__":
    main()