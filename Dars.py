"""
12-01-2022y

"""

# ism = "Abrorbek"
# Familiya = "Isaev"
# print("Mening isim familiyam:" + " " + ism + " " + Familiya)
# ism_familiya = f"Mening ismim {ism}"
# print(ism_familiya)
# print(f"Mening ismim>> {ism}")

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    # 06-dars:
# >>......................................
# STRING METODLAR

# gap = "mening ismim Abrorbek"
# isim = "abrorbek"
# print(isim.upper())
# print(isim.lower())
# print(gap.title())
# print(gap.capitalize())
# meva = "   olma   "
# print("MEn", meva.lstrip(), "ni yaxshi koraman")
# print("Men", meva.rstrip(), "ni yaxshi ko'raman")
# print("Men", meva.strip(), "ni yaxshi ko'raman")
# print("Men ", meva, "ni yaxshi ko'raman")
# ......................................<<


# >>......................................
# INPUT

# sorov = input( "Ismiingizni kiritingn\n>>>")
# print("Sizning ismingiz rostan ham" + sorov.title()+ " tog'rimi")
# ha_yoq = input("Ha yoki Yo'q\n>>>")
# if ha_yoq == "ha":
#     print("salom", sorov.title(), "kirishingiz mumkin".title())
# else:
#         print("Xayir", sorov.title(), "sizda kirish uchun ruxsat yo'q")


# mashenalr = ["nexia", 'matiz', 'bmv', 'mers']
# for avto in mashenalr:
#     if avto == "bmv":
#         print(avto.upper())
#     else:
#         print(avto.title())
# ......................................<<
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    

 
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    # 7-dars: 
# >>......................................
# LISTLAR BILAN ISHLASH

# mevalar = ["olma", 'anor', 'anjir', 'shaftoli', "o'rik"]
# narxlar = [123, 12000, 23000, 234.500, 32000]
# aralash = ["nexia", 12000, "ikki", 36.500]
# print(mevalar[0])
# print(mevalar[3].title())
# print(narxlar[0] + narxlar[2])
# print(narxlar[1] + 12)
# print(narxlar[3] + 1000)
# mevalar[1] = "keve"
# print(mevalar)
# ......................................<<


# >>......................................
# .uppend()

# aralash.append("banan")
# aralash.append("anor")
# aralash.append("gilos")
# aralash.append("girdli")
# aralash.append("shoptoli")
# aralash.append("pamedor")
# aralash.append("rarvuz")
# aralash.append("guruch")
# aralash.append("kartishka")
# print(aralash)
# ......................................<<
    
# >>......................................
# .insert()

# aralash.insert(0, "nexia")
# aralash.insert(1, "nexia3")
# aralash.insert(2, "nexia2")
# aralash.insert(3, "malibu")
# aralash.insert(4, "laseti")
# aralash.insert(5, "treker")
# aralash.insert(6, "traktir")
# aralash.insert(7, "damas")
# aralash.insert(8,"mapiz")
# ......................................<<


# >>......................................
# del el,nom[index]

# aralash.append('olma')
# aralash.append("karbanat")
# aralash.insert(1, "azot")
# aralash.insert(0, "qo'rg'oshin")
# aralash.insert(2, "vodorod")
# del aralash[1]
# del aralash[3]
# del aralash[4]
# del aralash[6]
# del aralash[2]
# del aralash[7]
# print(aralash)
# ......................................<<


# >>......................................
# .remove["index"]

# aralash.append("shikob")
# aralash.insert(1, "stol")
# aralash.append("stul")
# aralash.insert(1, "devan")
# aralash.remove("stul")
# aralash.remove("guruch")
# ......................................<<


# >>......................................
# .pop()
# list.1 = list.2.pop(index) ## list.1ga = list.2dan.sug'rib olib otqaz(elementni)

# aralash.append("go'sht")
# aralash.append("un")
# aralash.append("guruch")
# aralash.append("shirinlik")
# olingan_mahsulotlar = aralash.pop(1)
# olingan_mahsulotlar = aralash.pop(5)
# olingan_mahsulotlar = aralash.pop(8)
# olingan_mahsulotlar = aralash.pop(10)
# ......................................<<


# >>......................................
# AMALIYOT

# dostlar = []
# dostlar.append("Elbek")
# dostlar.append("Asat")
# dostlar.append("Hasan")
# dostlar.append('Husan')
# print(dostlar[0], "qalesan yaxshimisan bugun litseyga boramizmi?")
# print(dostlar[1], "qalesan yaxshimisan bugun kurashga borasanmi. E yana bir gap", dostlar[1], "bugun kochada ishlemizmi?")
# print("nima gap ", dostlar[2], "maktab qale o'tvotti bolla qale")
# print("nima qivosan", dostlar[3], "ishlar yaxshimi ketvottimi")

# sonlar = [120000, 32000, 5600, 10000, -121, 12,5]
# print(sonlar[0] + sonlar[1] - sonlar[2])
# javoblar = sonlar[3] + sonlar[4]
# print(javoblar)
# sonlar[-2] = -5
# sonlar[1] = 46000
# t_shaxslar = ["AL-Buxoriy", "Ibin-sino"]
# z_shaxslar = ["JEms Bond", "Usmon Nosir"]
# print("Men tarixiy shaxlardan", t_shaxslar[0], "bilan, Zamonaviy shaxslardan esa", z_shaxslar[1], "bilan ko'rishishni hohlardim")
# friends = []
# friends.append("Axror")
# friends.append("Atxam")
# friends.append("Sobir")
# friends.append("Elbek")
# friends.append("Javoh")
# friends.append("Hasan")
# friends.remove("Hasan")
# friends.remove("Sobir")
# friends.insert(1, "Jobir")
# friends.insert(6, "Yusuf")
# ......................................<<

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    
    
    

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#   08-dars
# >>......................................
# .sort(), .sort(reverse=True)

# avtolar = ["bmv", "aude", "mersedes", "nexia", "volva", "treker"]
# avtolar.sort()
# print(avtolar)

# avtolar.sort(reverse=True)
# print(avtolar)
# ......................................<<


# >>......................................
# sorted(), sorted(list, reverse=True)

# avtolar.append("tufli")
# avtolar.append("koylak")
# avtolar.append("shim")
# avtolar.append("sumka")
# avtolar.append("kurtka")
# print(sorted(avtolar))
# sonlar = [13, 313, -3, 233, 666, 232, 0, -34, -4]
# print(sorted(sonlar))

# avtolar.append("achka")
# avtolar.append("soat")
# avtolar.append("quti")
# avtolar.append("kompyuter")
# avtolar.append("korpa")
# print(sorted(avtolar, reverse=True))
# print(sorted(sonlar, reverse=True))
# avtolar.append("ruchka")
# avtolar.append("qalam")
# print(len(avtolar))
# ......................................<<


# >>......................................
# range(), max(), min(), sum()

# sonlar = list(range(0, 20))
# sonlar = list(range(0, 21))
# toq_sonlar = list(range(1, 10, 2))
# juft_sonlar = list(range(10, 23, 2))

# print(sonlar)
# print(toq_sonlar)
# print(juft_sonlar)
# print(max(sonlar))

# print(min(sonlar))

# print(sum(sonlar))
# ......................................<<


# >>......................................
# list[index:index]

# print(avtolar[0:12])
# print(avtolar[6:14])
# ......................................<<


# >>......................................
# 1>> r'oyxatga ikkita nom berish:  2>> royxatda nusxa olish
# 1>>
# my_avto = []
# my_avto = avtolar
# print(my_avto)
# avtolar.append("sim")
# /1>>

# 2>>
# my_cars = []
# my_cars = avtolar[:]
# my_cars.remove("nexia")
# print(my_cars)
# print(avtolar)
# /2>>
# ......................................<<


# >>......................................
#1>> TUPLE uzgarmas royxatlar: 1>> TUPLE <-> LISTGA

# 1>>
# toys = ("shrek", "car", "bus")
# toys.append("teddy")
# print(toys)
# type(toys)

# 2>>
# toys = list(toys)
# type(toys)
# toys.append('teddy')
# toys = tuple(toys)
# type(toys)
# ......................................<<


# >>......................................

# davlatlar = ["ameka", "frabsiya" "angliya", "germaniya", "malaziya", "butan"]
# print(davlatlar)
# ......................................<<
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # 9-dars
# >>......................................
# for sikli

# mehmonlar = ["Ali", "Vali", "Ebek", "Shaxzod"]
# for mehmon in mehmonlar:
    # print(f"hurmatli {mehmon} sizning hisoningizda mablag' yetarli emas shu sababli telefon qila olmaysiz")
    # print("Hurmat bilan MCHS")
#     print("salom", mehmon)
#     print("hayir", mehmon)

# raqamlar = list(range(1,21))
# for raqam in raqamlar:
#     print(f"{raqam} ning kvadrati {raqam**2} ga teng")

# raqamlar_kvadrati = []
# for raqam in raqamlar:
#     raqamlar_kvadrati.append(raqam**2)
# print(raqamlar)
# print(raqamlar_kvadrati)

# dostlar = []
# print("3 ta eng yaqin dostingizi ismii kiriting")
# for dost in range(4):
    # dostlar.append(input(f"{dost+1}do'stingizi ismini kiriting\n>>>"))
# print(dostlar)
# ......................................<<


# >>......................................
# AMALIYOT

# ismlar = ["Abror", "Ali", "Vali", "Hasan", "Husan"]
# for ism in ismlar:
#     print("Salom", ism)
# print("Amal 5 marta takrorlandi")

# sonlar = list(range(11, 100, 2))
# print(sonlar)
# for son in sonlar:
#     print(son**3)

# kinolar = []
# print("sizga eng sevimli bolgan 5 ta kino nomini kiriting")
# for kino in range(5):
#     kinolar.append(input(f"sizga sevimli bo'lgan {kino+1}-kino\n>>>"))
# print(kinolar)
# n_people = int(input("bugun nechi kishi bilan suhbaatlashdingiz\n>>>"))
# suhbatlashgan_odamlar = []
# for suhbatlashgan_odam in range(n_people):
#     suhbatlashgan_odamlar.append(input(f"Bugun siz suhbatlashgan {suhbatlashgan_odam + 1} odam kim edi\n>>>"))
# print(suhbatlashgan_odamlar)
# ......................................<<
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # 10-dars
# >>......................................
# if else operstorlari

# buyumlar = ["olma", "mishka", "kitob", "taroq", "bmw"]
# for buyum in buyumlar:
#     if buyum == "bmw":
#         print(buyum.upper())
#     else:
#         print(buyum.title())

# ism = input("ismingizni kiriting\n>>>")
# if ism.lower() == "ali":
#     print("salom Ali")
# else:
#     print("Uzur siz Ali emassiz")

# javob = float(input("12x6 nechiga teng\n..."))
# if javob != 72:
#     print('javob hato')
# else:
#     print("Tabriklaymiz javob tog'ri")

# yosh = float(input("yoshingiz nechida\n>>"))
# if yosh >= 18:
#     print("kirish mumkin")
# else:
#     print('sizga kirish mumkin emas')


# yil = int(input("tug'ilgan yilingizni kiriting:..."))
# if 2022-yil<=18:
#     print(f"Sizning yoshingiz {2022-yil} da")
#     print("sizga kirish mumkin emas")
# else:
#     print("sizga kirish mumkin")
# ......................................<<


# >>......................................
# AMALIYOT

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == "gm":
#         print(car.upper())
#     else:
#         print(car.title())
#         if car != "gm":
#             print(car.upper())
#         else:
#             print(car.title())
            
# login = input("login kiriting: ")
# if login.lower() == 'admin':
#     print("Salom Admin. foydalanuvchilar Ruyhatini ko'rishni hoxlaysizmi?")
# else:
#     print(f"salom {login.title()} hush kelibsiz")

# print("ikkita son kiriting")
# son = float(input("birrinchi sonni kiritig:  "))
# i_son = float(input("ikkinchi sonni kiriting:  "))
# if son > i_son:
#     print(f"{son} katta {i_son} dan")
# if son == i_son:
#     print("ikkalasi teng")
# else:
#     print(f"{i_son} katta {son} dan")

# istalgan_son = float(input("Hohlagan son kiriting\n .."))
# if istalgan_son < 0:
#     print("manfiy son")
# else:
#     print("musbat son")

# ildiz_son = int(input("istalgan son kiriting\n .."))
# if ildiz_son > 0:
#     print("qalesan")
# else:
#     print("musbat son kiriting")
# ......................................<<
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # 11-dars
# >>......................................
# if elif operatorlar

# son = 50
# if son < 0:
#     print("manfiy son")
# else:
#     print("musbat son")

# kirish = int(input("yoshingiz nechida:..."))
# if kirish <= 4:
#     print("sizga kirish tekin")
# elif kirish <= 12:
#     print("sizga kirish 5000 so'm")
# elif kirish <= 18:
#     print("sizga kirish 8000 so'm")
# else:
#     print("sizga kirish 10000 so'm")
    
# # YOKI

# if kirish <= 4:
#     narx = 0
# elif kirish <= 12:
#     narx = 5000
# elif kirish <= 18:
#     narx = 8000
# else:
#     narx = 10000
    
# print(f"sizga kirish {narx} so'm")

# kun = input("bugun nima kun:>>")
# harorat = float(input("havo harorati qanday:>>"))
# # if kun.lower() == "shanba" or kun.lower() == "yakshanba":
# #     print("bugun dam olish kuni")
# # else:
# #     print("bugun ish kuni"

# if kun.lower() == "yakshanba" and harorat>=30:
#     print("qani cho'milgani ketdik")
# elif kun.lower() == "yakshanba" and harorat < 30:
#     print("bugun uyda dam olamiz")
# else:
#     print("bugun ishlash kerak")

# narx = 10000
# choy = 1
# salat = 0

# if choy and salat:
#     narx = narx + 10000
# elif choy or salat:
#     narx = narx +5000

# print(f"Jami narx {narx} so'm boldi")


# non = 1
# kampot = 0
# assorti = 1

# if salat:
#     print("Mijoz salat oldi")
#     narx = narx + 3000
# if choy:
#     print("Mijoz choy oldi")
#     narx = narx + 2000
# if non:
#     print("Mijoz non oldi")
#     narx = narx + 4000
# if kampot:
#     print("Mijoz kampot oldi")
#     narx = narx + 10000
# if assorti:
#     print("Mijoz assorti oldi")
#     narx = narx + 5000
    
# print(F"Jami narx {narx} so'm boldi")

# menu_ov = ["somsa", "osh", "shashlik", "norin"]
# menu_salat = ["aliviya", 'fentuza', 'karam', 'chimchi'] 
# buyurtma = []
# taom = input("Nima ovqatlar yeysiz:>>>")
# birinchi = input("yana nima yeysiz")
# ikkinsi = input("desertga nima yeysiz:>>>")
# for taom in menu_ov:
#     if taom.lower() and birinchi in menu_ov:
#             print(f"Menuda {taom} bor")
#     else:
#             print(f"Menuda {taom} yo'q")
# ......................................<<


# >>......................................
    # Amaliyot

juft_son = int(input('juft son kiriting\n??'))
# son = list(range(0, 100, 2))
if juft_son%2:
    print('Juft son kiriting')
else:
    print('Rahmat')

# ......................................<<
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
    

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # 14-dars
# >>......................................
# lug'at bilan ishlash

# car_0 = {"madel":"ferrari", "rang":"qora"}
# print(car_0["madel"])
# print(car_0["rang"])

# ing_uz = {"apple":"olma", "car":"moshena", "frukt":"meva"}
# print(ing_uz["apple"])

# mevalar = {"olma":10000, "orik":20000, "shaftoli":12000}
# print(f"olma nari {mevalar['olma']}so'm")

# talaba_0 = {"ism":"Abrorbek Isaev", "yosh":16, "yili":2006}
# print(f"{talaba_0['ism']} {talaba_0['yili']} yilda tug'ilan {talaba_0['yosh']} da")
# ......................................<<



# >>......................................
    # Ro'yxatga element qo'shish

# talaba_0['kurs'] = 1
# talaba_0['fakultit'] = 'IIV'

# talaba_0['ism'] = 'Asror'
# ......................................<<



# >>......................................
    # Bosh Ro'yxat va Ro'yxatdan element o'chirish

# talaba_1 = {}
# talaba_1["ism"] = 'Abrorbek'
# talaba_1["Familiya"] = 'Isaev'
# talaba_1['kurs'] = 1
# # print(talaba_1)
# print(f"Talaba {talaba_1['ism']} {talaba_1['Familiya']} {talaba_1['kurs']}-kurs")

# del talaba_0['yili']
# ......................................<<


# >>......................................
# telefonlar = {
#     'Abrorbek':'iphone13 pro',
#     'Asrorbek':'Redmi not8',
#     'Ebek':'Samsung',
#     'Javoh':'Huave P30 lite'
#     }
# print(telefonlar)
# ......................................<<


# >>......................................
    # get() metodi

# phone = telefonlar.get('quvonch', 'Bunday ism mavjud emas')
# print(phone)


# ......................................<<
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\