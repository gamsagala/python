print("Selamat Datang di ATM saya")
print("Pilih Option :")
print("1. Check Uang Saya")
print("2. Ambil Uang Saya")
print("3. Tabung Uang Saya")
option=int(input("Silahkan pilih option :"))
if option==1: 
    print("Uang Kamu Berjumlah rp.200.000")
    

elif option==2:
    print("uang kamu berjumlah rp.200.000 , mau ambil berapa ?")
    print("1. Rp.100.000")
    print("2. Rp.200.000")
    uang_kamu=200000
    option==int(input("option :"))
    if option==1:
        hasil=uang_kamu - 100000
        print("Uang Kamu Sekarang Berjumlah : ",hasil)
    elif option==2:
        hasil2=uang_kamu - 200000
        print("Uang Kamu Sekarang Berjumlah : ",hasil2)
    else :
        print("Keyword Anda Salah")
elif option==3:
    uang_kamu=200000
    print("Uang Berjumlah Rp.200.000 , Mau Nabung Berapa ?")
    option3=int(input("Mau Nabung Berapa :"))
    hasil3= uang_kamu+option3
    print("Jumlah Uang Kamu Sekarang :",hasil3)
else :
    print("Keyword Anda Salah, Mohon Coba Lagi!")

