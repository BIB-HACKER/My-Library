'''INPUT =
   TAKE THE NUMBER OF POSSIBLE CODEWORD AS INTEGER 'N'.
   EACH 'N' LINES CONTAINS SINGLE WORDS,ITS LENGTH BEING AN ODD NUMBER GREATER THAN 2 AND LESS THAN 14. ALL CHRACTERS ARE LOWER CASE OF ENGLISH ALPHABET.
   
   OUTPUT =
   THE FIRST AND ONLY LINE OF OUTPUT MUST CONTAIN THE LENGTH OF THE CORRECT CODEWORD AND IT'S MIDDLE CHARACTER.
'''
print("INPUT: ")
line=[]
N=int(input("enter number -> "))
for i in range(N):
    line.append(input("enter word line = "))
print("OUTPUT: ")
for i in line:
    if i[::-1] in line:
        print(len(i),i[len(i)//2])
        break
