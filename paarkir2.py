nama_orang = input("nama : ")
apakah_membawa_STNK = input("apakah membawa STNK ? : ")

list1 = ('ya, iya, bawa, membawa')
list2 = ('tidak, tertinggal, lupa, hilang, tidak membawa')

if apakah_membawa_STNK in list1 :
    print("silahkan pergi")
if apakah_membawa_STNK in list2 :
    print("maaf tidak boleh pergi/dikenakan denda karena tidak membawa STNK")