
def tapis(n):    
    for i in range(n):
        diag = ""
        for j in range(n-i): 
            diag += "#" 
        diag += " " 
        for j in range(i): diag += "#" 
        print("|" + diag + "|")

tapis(5)