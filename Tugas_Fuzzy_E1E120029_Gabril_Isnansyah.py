print("1. FUNGSI KEANGGOTAAN LINEAR")
print("2. FUNGSI KEANGGOTAAN SEGITIGA")
print("3. FUNGSI KEANGGOTAAN TRAPESIUM")

x = int(input("Pilih = " ))

if x == 1 : 
    print("FUNGSI KEANGGOTAAN LINEAR")

    a = int(input(" masukan nilai a = "))
    b = int(input(" masukan nilai b = "))

    nilai = int(input(" masukan nilai derajat keanggotaan = "))

    pilih =int(input("1. linear naik \n2. linear turun \npilih =  "))
    if pilih == 1:
        if nilai <= a:
            print(0)
        elif nilai >= b:
            print(1)
        else :
            hasil = ((nilai-a)/(b-a))
            print(hasil) 
    else : 
        if nilai <= a:
            print(1)
        elif nilai >= b:
            print(0)
        else :
            hasil = ((b - nilai)/(b-a))
            print("nilai = ",hasil) 
elif x == 2 :
    print("FUNGSI KEANGGOTAAN SEGITIGA")

    a = int(input(" masukan nilai a = "))
    b = int(input(" masukan nilai b = "))
    c = int(input(" masukan nilai c = "))

    nilai = int(input(" masukan nilai derajat keanggotaan = "))

    if nilai <= a or nilai >= c :   
        print("0")
    
    elif nilai  >= a or nilai <= b :
        hasil = ((nilai-a)/(b-a))
        print(hasil) 

    else :
        hasil = ((b-nilai)/(c-b))
        print(hasil) 


elif x == 3 :
    print("FUNGSI KEANGGOTAAN TRAPESIUM")

    a = int(input(" masukan nilai a = "))
    b = int(input(" masukan nilai b = "))
    c = int(input(" masukan nilai c = "))
    d = int(input(" masukan nilai d = "))

    nilai = int(input(" masukan nilai derajat keanggotaan = "))

    if nilai <= a or nilai >= d :   
        print(0)
        
    elif nilai  > a or nilai <= b :
        hasil = ((nilai-a)/(b-a))
        print(hasil) 
    if nilai <  b or nilai <= c :   
        print(1)
    else :
        hasil = ((d-nilai)/(d-c))
        print(hasil) 

else :
    print("error")
