def show_menu():
    print("- - - - - -  MENU - - - - - -")
    print("[1] Cek Saldo")
    print("[2] Top Up Saldo")
    print("[3] Pembelian")

    menu = input("PILIH MENU> ")

    if menu == "1":
        ceksaldo()
    if menu == "2":
        topup()
    if menu == "3":
        pmbln()

def ceksaldo():
    saldo = 1500000
    print("Cek saldo")
    print("Jumlah Saldo = Rp. ",saldo)
    tanya()

def topup():
    print("Top Up Saldo")
    q = int(input("Input : "))
    print(q)
    p = 1500000
    saldo = q + p
    print("saldo: ",saldo)
    tanya()
def pmbln():
    print("Pembelian")
    x = int(input("Check Out: "))
    print(x)
    saldo = 1500000
    saldo_akhir = saldo - x
    print("saldo_akhir: ",saldo_akhir)
    if saldo_akhir > x:
        print("Transaksi berhasil!")
    if saldo_akhir < x:
        print("Saldo anda tidak cukup!")
    tanya()

def tanya():
    print("\n1.Ke Menu\n2.Keluar")
    plh = input("\nPilih [1/2] = ")
    if plh == "1":
        show_menu()
    if plh == "2":
        print("Thank You ")


show_menu()

