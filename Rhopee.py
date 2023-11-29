import os, json

barangbelanja = []
hargabarang = []
totalharga = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def bacaJson():
    try:
        with open("hasilbselanja.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        with open("hasilbelanja.json", "w") as file:
            kosong = []
            json.dump(kosong, file, indent=2)
            return kosong

def tulis_ulangJson(baru):
    with open("hasilbelanja.json", "w") as file:
        json.dump(baru, file, indent=2)

def elektronik() :
            clear_screen()
            print('Beberapa Produk teratas :\n 1. Apple Iphone 13 Pro Max ($1300)\n 2. Powebank Delcell Blast 9000mAh ($21)\n 3. Apple Iphone 12 Pro Max ($1042)\n 4. Samsung Galaxy Z Flip3 5G ($1040)\n 5. Oppo Reno6 ($371)\n 6. Xiomi Mi TV 4 32 inch HD LED ($296)\n 7. Xiaomi 11T Pro ($499)\n 8. Lenovo IdeaPad Slim 1 11IGL05 ($571)\n 9. Macbook Pro A1502 EMC 2835 ($750)\n 10. Apple iPad Pro 2020 ($789)')
            elektronik1 = ["Apple Iphone 13 Pro Max", 1300]
            elektronik2 = ["Powebank Delcell Blast 9000mAh", 21]
            elektronik3 = ["Apple Iphone 12 Pro Max", 1042]
            elektronik4 = ["Samsung Galaxy Z Flip3 5G", 1040]
            elektronik5 = ["Oppo Reno6", 371]
            elektronik6 = ["Xiomi Mi TV 4 32 inch HD LED", 296]
            elektronik7 = ['Xiaomi 11T Pro', 499]
            elektronik8 = ['Lenovo IdeaPad Slim 1 11IGL05', 571]
            elektronik9 = ['Macbook Pro A1502 EMC 2835', 750]
            elektronik10 = ['Apple iPad Pro 2020', 789]
            new_1 = int(input("\nMasukkan barang yang ingin dibeli:"))
            if new_1 == 1 :
                barangbelanja.append(elektronik1[0])
                hargabarang.append(elektronik1[1])
            elif new_1 == 2 :
                barangbelanja.append(elektronik2[0])
                hargabarang.append(elektronik2[1])
            elif new_1 == 3 :
                barangbelanja.append(elektronik3[0])
                hargabarang.append(elektronik3[1])
            elif new_1 == 4 :
                barangbelanja.append(elektronik4[0])
                hargabarang.append(elektronik4[1])
            elif new_1 == 5 :
                barangbelanja.append(elektronik5[0])
                hargabarang.append(elektronik5[1])
            elif new_1 == 6 :
                barangbelanja.append(elektronik6[0])
                hargabarang.append(elektronik6[1])
            elif new_1 == 7 :
                barangbelanja.append(elektronik7[0])
                hargabarang.append(elektronik7[1])
            elif new_1 == 8 :
                barangbelanja.append(elektronik8[0])
                hargabarang.append(elektronik8[1])
            elif new_1 == 9 :
                barangbelanja.append(elektronik9[0])
                hargabarang.append(elektronik9[1])
            elif new_1 == 10 :
                barangbelanja.append(elektronik10[0])
                hargabarang.append(elektronik10[1])
            else :
                print("\nMasukkan Angka yang benar")   

def fashion():
        clear_screen()
        print ('Beberapa Produk teratas dari kami :')
        print (' 1. Cucchi Horsebit 1955 mini bag ($98)\n 2. Cucchi black backpack ($120)\n 3. Cucchi Bestiary bag with bees ($113)\n 4. Erigoes sweatshirt slim ($38)\n 5. Erigoes Windbreaker Dark Blue ($20)\n 6. Erigoes Sweatshirt Kazuo Black ($10)\n 7. Pradam Wool and Cashmere knit vest ($51)\n 8. Pradam Brique brushed leather bag ($70)\n 9. Pradam technical fabric hoodie ($66)\n 10. Pradam Studded Re-Nylon baseball cap ($25)')
        barang1 = ['Cucchi Horsebit 1955 mini bag', 98]
        barang2 = ['Cucchi black backpack', 120]
        barang3 = ['Cucchi Bestiary bag with bees', 113]
        barang4 = ['Erigoes sweatshirt slim', 38]
        barang5 = ['Erigoes Windbreaker Dark Blue', 20]
        barang6 = ['Erigoes Sweatshirt Kazuo Black', 10]
        barang7 = ['Pradam Wool and Cashmere knit vest', 51]
        barang8 = ['Pradam Brique brushed leather bag', 70]
        barang9 = ['Pradam technical fabric hoodie', 66]
        barang10 = ['Pradam Studded Re-Nylon baseball cap', 25]
        new_2 = int(input('\nMasukkan barang yang ingin dibeli:'))
        if new_2 == 1 :
            barangbelanja.append(barang1[0])
            hargabarang.append(barang1[1])
        elif new_2 == 2 :
            barangbelanja.append(barang2[0])
            hargabarang.append(barang2[1])
        elif new_2 == 3 :
            barangbelanja.append(barang3[0])
            hargabarang.append(barang3[1])
        elif new_2 == 4 :
            barangbelanja.append(barang4[0])
            hargabarang.append(barang4[1])
        elif new_2 == 5 :
            barangbelanja.append(barang5[0])
            hargabarang.append(barang5[1])
        elif new_2 == 6 :
            barangbelanja.append(barang6[0])
            hargabarang.append(barang7[1])
        elif new_2 == 7 :
            barangbelanja.append(barang7[0])
            hargabarang.append(barang7[1])
        elif new_2 == 8 :
            barangbelanja.append(barang9[0])
            hargabarang.append(barang8[1])
        elif new_2 == 9 :
            barangbelanja.append(barang9[0])
            hargabarang.append(barang9[1])
        elif new_2 == 10 :
            barangbelanja.append(barang10[0])
            hargabarang.append(barang10[1])
        else : 
            print ('\nMasukkan databaru yang sesuai ')

def furniture():
    clear_screen()
    print ('Beberapa Produk teratas dari kami :')
    print (' 1. Gunnared chair gray medium ($214)\n 2. Chaise longue Orrsta merah ($300)\n 3. Folding shopping cart ($114)\n 4. Kitchenware metal wire rack ($39)\n 5. Sofa Bench Rotan Seater Natural ($20)\n 6. Table Rectangular Metal Furniture ($41)\n 7. Smart bedside table modern minimalist ($89)\n 8. Metal rack shoe rack display modern ($5)\n 9. Large Tall Bookcase 4 Tiers Industrial Metal ($32)\n 10. Bed Twin frame bedroom ($33)')
    purnitur1 = ['Gunnared chair gray medium', 214]
    purnitur2 = ['Chaise longue Orrsta merah', 300]
    purnitur3 = ['Folding shopping cart', 114]
    purnitur4 = ['Kitchenware metal wire rack', 39]
    purnitur5 = ['Sofa Bench Rotan Seater Natural', 20]
    purnitur6 = ['Table Rectangular Metal Furniture', 41]
    purnitur7 = ['Smart bedside table modern minimalist', 801]
    purnitur8 = ['Metal rack shoe rack display modern', 5]
    purnitur9 = ['Tall Bookcase 4 Tiers Industrial Metal', 32]
    purnitur10 = ['Bed Twin frame bedroom', 33]
    new_3 = int(input('\nMasukkan barang yang ingin dibeli:'))
    if new_3 == 1 :
        barangbelanja.append(purnitur1[0])
        hargabarang.append(purnitur1[1])
    elif new_3 == 2 :
        barangbelanja.append(purnitur2[0])
        hargabarang.append(purnitur2[1])
    elif new_3 == 3 :
        barangbelanja.append(purnitur3[0])
        hargabarang.append(purnitur3[1])
    elif new_3 == 4 :
        barangbelanja.append(purnitur4[0])
        hargabarang.append(purnitur4[1])
    elif new_3 == 5 :
        barangbelanja.append(purnitur5[0])
        hargabarang.append(purnitur5[1])
    elif new_3 == 6 :
        barangbelanja.append(purnitur6[0])
        hargabarang.append(purnitur7[1])
    elif new_3 == 7 :
        barangbelanja.append(purnitur7[0])
        hargabarang.append(purnitur7[1])
    elif new_3 == 8 :
        barangbelanja.append(purnitur9[0])
        hargabarang.append(purnitur8[1])
    elif new_3 == 9 :
        barangbelanja.append(purnitur9[0])
        hargabarang.append(purnitur9[1])
    elif new_3 == 10 :
        barangbelanja.append(purnitur10[0])
        hargabarang.append(purnitur10[1])
    else : 
        print ('\nMasukkan databaru yang sesuai ')
            

def keranjangsaya() :
    clear_screen()
    ket = ['NO', 'Nama', 'Harga']
    print(f'{ket[0]:<5}{ket[1]:<39}{ket[2]:<18}')
    print('='*60)
    for j in range(len(barangbelanja)):
            print(f'{j+1:<5}{barangbelanja[j]:<38}','$'+ f'{hargabarang[j]:<18}')
    print('='*60)
    total = sum(hargabarang)
    print('Total Harga :' + ' $' + str(total))
    print('='*60)


def ubahkeranjang() :
    clear_screen()
    ket = ['No', 'Nama', 'Harga']
    print(f'{ket[0]:<5}{ket[1]:<38}{ket[2]:<18}')
    print('='*60)
    total = sum(hargabarang)
    for j in range(len(barangbelanja)):
            print(f'{j+1:<5}{barangbelanja[j]:<38}','$'+ f'{hargabarang[j]:<18}')
    print('='*60)

    print('1. Ganti Barang\n2. Hapus Barang\n3. Kembali  ')
    ubah = int(input('inputkan angka yang diiginkan:'))
    if ubah == 1 :
        hapus = int(input('Masukkan nomor berapa yang ingin diubah:'))
        hapus = hapus - 1
        data = barangbelanja[hapus]
        barangbelanja.pop(hapus)
        hargabarang.pop(hapus)
        clear_screen()
        print('Apa Yang Ingin Anda Beli?')
        print("Kategori:\n 1. Elektronik \n 2. Fashion \n3. Furniture")
        choose = int(input('Masukkan kode 1-3 untuk memilih kategori yang diinginkan:'))
        if choose == 1:
            clear_screen()
            print('Beberapa Produk teratas :\n 1. Apple Iphone 13 Pro Max ($1300)\n 2. Powebank Delcell Blast 9000mAh ($21)\n 3. Apple Iphone 12 Pro Max ($1042)\n 4. Samsung Galaxy Z Flip3 5G ($1040)\n 5. Oppo Reno6 ($371)\n 6. Xiomi Mi TV 4 32 inch HD LED ($296)\n 7. Xiaomi 11T Pro ($499)\n 8. Lenovo IdeaPad Slim 1 11IGL05 ($571)\n 9. Macbook Pro A1502 EMC 2835 ($750)\n 10. Apple iPad Pro 2020 ($789)')
            elektronik1 = ["Apple Iphone 13 Pro Max", 1300]
            elektronik2 = ["Powebank Delcell Blast 9000mAh", 21]
            elektronik3 = ["Apple Iphone 12 Pro Max", 1042]
            elektronik4 = ["Samsung Galaxy Z Flip3 5G", 1040]
            elektronik5 = ["Oppo Reno6", 371]
            elektronik6 = ["Xiomi Mi TV 4 32 inch HD LED", 296]
            elektronik7 = ['Xiaomi 11T Pro', 499]
            elektronik8 = ['Lenovo IdeaPad Slim 1 11IGL05', 571]
            elektronik9 = ['Macbook Pro A1502 EMC 2835', 750]
            elektronik10 = ['Apple iPad Pro 2020', 789]
            new_1 = int(input("\nMasukkan barang yang ingin dibeli:"))
            if new_1 == 1 :
                barangbelanja.insert(hapus, elektronik1[0])
                hargabarang.insert(hapus, elektronik1[1])
            elif new_1 == 2 :
                barangbelanja.insert(hapus, elektronik2[0])
                hargabarang.insert(hapus, elektronik2[1])
            elif new_1 == 3 :
                barangbelanja.insert(hapus, elektronik3[0])
                hargabarang.insert(hapus, elektronik3[1])
            elif new_1 == 4 :
                barangbelanja.insert(hapus, elektronik4[0])
                hargabarang.insert(hapus, elektronik4[1])
            elif new_1 == 5 :
                barangbelanja.insert(hapus, elektronik5[0])
                hargabarang.insert(hapus, elektronik5[1])
            elif new_1 == 6 :
                barangbelanja.insert(hapus,elektronik6[0])
                hargabarang.insert(hapus, elektronik6[1])
            elif new_1 == 7 :
                barangbelanja.insert(hapus, elektronik7[0])
                hargabarang.insert(hapus, elektronik7[1])
            elif new_1 == 8 :
                barangbelanja.insert(hapus, elektronik8[0])
                hargabarang.insert(hapus, elektronik8[1])
            elif new_1 == 9 :
                barangbelanja.insert(hapus, elektronik9[0])
                hargabarang.insert(hapus, elektronik9[1])
            elif new_1 == 10 :
                barangbelanja.insert(hapus, elektronik10[0])
                hargabarang.insert(hapus, elektronik10[1])
            else :
                print("\nMasukkan Angka yang benar")
        elif choose == 2 :
            clear_screen()
            print ('Beberapa Produk teratas dari kami :')
            print (' 1. Cucchi Horsebit 1955 mini bag ($98)\n 2. Cucchi black backpack ($120)\n 3. Cucchi Bestiary bag with bees ($113)\n 4. Erigoes sweatshirt slim ($38)\n 5. Erigoes Windbreaker Dark Blue ($20)\n 6. Erigoes Sweatshirt Kazuo Black ($10)\n 7. Pradam Wool and Cashmere knit vest ($51)\n 8. Pradam Brique brushed leather bag ($70)\n 9. Pradam technical fabric hoodie ($66)\n 10. Pradam Studded Re-Nylon baseball cap ($25)')
            barang1 = ['Cucchi Horsebit 1955 mini bag', 98]
            barang2 = ['Cucchi black backpack', 120]
            barang3 = ['Cucchi Bestiary bag with bees', 113]
            barang4 = ['Erigoes sweatshirt slim', 38]
            barang5 = ['Erigoes Windbreaker Dark Blue', 20]
            barang6 = ['Erigoes Sweatshirt Kazuo Black', 10]
            barang7 = ['Pradam Wool and Cashmere knit vest', 51]
            barang8 = ['Pradam Brique brushed leather bag', 70]
            barang9 = ['Pradam technical fabric hoodie', 66]
            barang10 = ['Pradam Studded Re-Nylon baseball cap', 25]
            new_2 = int(input('\nMasukkan barang yang ingin dibeli:'))
            if new_2 == 1 :
                barangbelanja.insert(hapus, barang1[0])
                hargabarang.insert(hapus, barang1[1])
            elif new_2 == 2 :
                barangbelanja.insert(hapus, barang2[0])
                hargabarang.insert(hapus, barang2[1])
            elif new_2 == 3 :
                barangbelanja.insert(hapus, barang3[0])
                hargabarang.insert(hapus, barang3[1])
            elif new_2 == 4 :
                barangbelanja.insert(hapus, barang4[0])
                hargabarang.insert(hapus, barang4[1])
            elif new_2 == 5 :
                barangbelanja.insert(hapus, barang5[0])
                hargabarang.insert(hapus, barang5[1])
            elif new_2 == 6 :
                barangbelanja.insert(hapus, barang6[0])
                hargabarang.insert(hapus, barang7[1])
            elif new_2 == 7 :
                barangbelanja.insert(hapus, barang7[0])
                hargabarang.insert(hapus, barang7[1])
            elif new_2 == 8 :
                barangbelanja.insert(hapus, barang9[0])
                hargabarang.insert(hapus, barang8[1])
            elif new_2 == 9 :
                barangbelanja.insert(hapus, barang9[0])
                hargabarang.insert(hapus, barang9[1])
            elif new_2 == 10 :
                barangbelanja.insert(hapus, barang10[0])
                hargabarang.insert(hapus, barang10[1])
            else : 
                print ('\nMasukkan databaru yang sesuai ')

        elif choose == 3:
            clear_screen()
            print ('Beberapa Produk teratas dari kami :')
            print (' 1. Gunnared chair gray medium ($214)\n 2. Chaise longue Orrsta merah ($300)\n 3. Folding shopping cart ($114)\n 4. Kitchenware metal wire rack ($39)\n 5. Sofa Bench Rotan Seater Natural ($20)\n 6. Table Rectangular Metal Furniture ($41)\n 7. Smart bedside table modern minimalist ($89)\n 8. Metal rack shoe rack display modern ($5)\n 9. Large Tall Bookcase 4 Tiers Industrial Metal ($32)\n 10. Bed Twin frame bedroom ($33)')
            purnitur1 = ['Gunnared chair gray medium', 214]
            purnitur2 = ['Chaise longue Orrsta merah', 300]
            purnitur3 = ['Folding shopping cart', 114]
            purnitur4 = ['Kitchenware metal wire rack', 39]
            purnitur5 = ['Sofa Bench Rotan Seater Natural', 20]
            purnitur6 = ['Table Rectangular Metal Furniture', 41]
            purnitur7 = ['Smart bedside table modern minimalist', 801]
            purnitur8 = ['Metal rack shoe rack display modern', 5]
            purnitur9 = ['Tall Bookcase 4 Tiers Industrial Metal', 32]
            purnitur10 = ['Bed Twin frame bedroom', 33]
            new_3 = int(input('\nMasukkan barang yang ingin dibeli:'))
            if new_3 == 1 :
                barangbelanja.insert(hapus, purnitur1[0])
                hargabarang.insert(hapus, purnitur1[1])
            elif new_3 == 2 :
                barangbelanja.insert(hapus, purnitur2[0])
                hargabarang.insert(hapus, purnitur2[1])
            elif new_3 == 3 :
                barangbelanja.insert(hapus, purnitur3[0])
                hargabarang.insert(hapus, purnitur3[1])
            elif new_3 == 4 :
                barangbelanja.insert(hapus, purnitur4[0])
                hargabarang.insert(hapus, purnitur4[1])
            elif new_3 == 5 :
                barangbelanja.insert(hapus, purnitur5[0])
                hargabarang.insert(hapus, purnitur5[1])
            elif new_3 == 6 :
                barangbelanja.insert(hapus, purnitur6[0])
                hargabarang.insert(hapus, purnitur7[1])
            elif new_3 == 7 :
                barangbelanja.insert(hapus, purnitur7[0])
                hargabarang.insert(hapus, purnitur7[1])
            elif new_3 == 8 :
                barangbelanja.insert(hapus, purnitur9[0])
                hargabarang.insert(hapus, purnitur8[1])
            elif new_3 == 9 :
                barangbelanja.insert(hapus, purnitur9[0])
                hargabarang.insert(hapus, purnitur9[1])
            elif new_3 == 10 :
                barangbelanja.insert(hapus, purnitur10[0])
                hargabarang.insert(hapus, purnitur10[1])
            else : 
                print ('\nMasukkan databaru yang sesuai ')
            
            intimenu()
    if ubah == 2 :
        hapus = int(input('Masukkan nomor yang ingin dihapus'))
        hapus = hapus - 1
        data = barangbelanja[hapus]
        barangbelanja.pop(hapus)
        hargabarang.pop(hapus)
        clear_screen()
        print(data, 'telah dihapus dari data')
        clear_screen()
    if ubah == 3 :
        intimenu()
        

def checkout() :
    clear_screen()
    bacaJson()
    print('List barang yang akan anda beli: \n')
    ket = ['No', 'Nama', 'Harga']
    print(f'{ket[0]:<5}{ket[1]:<38}{ket[2]:<18}')
    print('='*60)
    totalharga = sum(hargabarang)
    for j in range(len(barangbelanja)):
            print(f'{j+1:<5}{barangbelanja[j]:<38}','$'+ f'{hargabarang[j]:<18}')
    print('='*60)
    total = sum(hargabarang)
    print('Total Harga :' + ' $' + str(total))
    print('='*60)
    print('Apakah Anda Yakin ? \n 1. Ya\n 2. Tidak, Kembali ke Menu Awal  ')
    user = int(input('Inputkan angka yang anda inginkan :'))
    if user == 1 :
        total = sum(hargabarang)
        total = int(total)
        if 100<= total <=499  :
            diskon = int(total * 0.1)
            totalharga = total - diskon
            print("Anda Telah Mendapatkan Diskon Sebesar 10% karena telah berbelanja lebih dari $100")
        elif 500<= total <=999 :
            diskon = int(total * 0.15)
            totalharga = total - diskon
            print("Anda Telah Mendapatkan Diskon Sebesar 15% karena telah berbelanja lebih dari $500")
        elif 1000<= total <=9999 :
            diskon = int(total * 0.2)
            totalharga = total - diskon
            print("Anda Telah Mendapatkan Diskon Sebesar 20% karena telah berbelanja lebih dari $1000")
        elif total >= 10000 :
            diskon = int(total * 0.35)
            totalharga = total - diskon
            print("Anda Telah Mendapatkan Diskon Sebesar 35% karena telah berbelanja lebih dari $10000")
        print("Anda Mendapat Potongan : $" + str(diskon))
        print("Total Belanja Anda Sementara : $" + str(totalharga))
        lanjut = int(input("inputkan angka 1 untuk melanjutkan :"))
        if lanjut == 1 :
            clear_screen()
        print("Jasa Pengiriman:")
        print('\n1. JNE : $20. Akan diterima sekitar 7 hari setelah pembayaran ')
        print("2. JNT : $35. Akan diterima sekitar 5 hari setelah pembayaran")
        print('3. Sicepat : $25. Akan diterima sekitar 8 hari setelah pembayaran')
        user = int(input("\nSilakan inputkan 1-3 untuk memilih jasa pengiriman:"))
        if user == 1 :
            ongkir = 20
            totalharga = totalharga + ongkir
        elif user == 2 :
            ongkir = 35
            totalharga = totalharga + ongkir
        elif user == 3 :
            ongkir = 25
            totalharga = totalharga + ongkir
        lanjut1 = int(input("inputkan angka 1 untuk melanjutkan :"))
        if lanjut1 == 1 :
            clear_screen()
        ket = ['No', 'Nama', 'Harga']
        print(f'{ket[0]:<5}{ket[1]:<38}{ket[2]:<18}')
        print('='*60)
        totalharga = sum(hargabarang)
        for j in range(len(barangbelanja)):
            print(f'{j+1:<5}{barangbelanja[j]:<38}','$'+ f'{hargabarang[j]:<18}')
        print('='*60)
        total = sum(hargabarang)
        totalharga = totalharga - diskon + ongkir
        print('Total Harga Belanja :' + ' $' + str(total))
        print('Potongan Diskon :' + ' $' + str(diskon))
        print('Ongkir :' + ' $' + str(ongkir))
        print("Total Akhir :" + ' $' + str(totalharga))
        print('='*60)
        Program = {'barang' : barangbelanja}
        program1 = {'harga' : hargabarang}
        program2 = {'diskon' : diskon}
        program3 = {'ongkir' : ongkir}
        program4 = {'total' : totalharga}
        
        
        hitungan = bacaJson()
        hitungan.append(Program)
        hitungan.append(program1)
        hitungan.append(program2)
        hitungan.append(program3)
        hitungan.append(program4)
        tulis_ulangJson(hitungan)
    else :
        intimenu()    


def intimenu():
 while True :
    bacaJson()
    print("\nhalo", nama)
    print(" 1.Lanjut Berbelanja\n 2.Keranjang saya \n 3.Edit Keranjang Saya\n 4.Checkout")
    user = int(input("Masukkan Angka 1-5 yang anda inginkan:"))
    if user == 1 :
        clear_screen()
        print('Apa Yang Ingin Anda Beli?')
        print("Kategori:\n 1. Elektronik \n 2. Fashion \n 3. Furniture")
        pilihan = int(input('Masukkan kode 1-3 untuk memilih kategori yang diinginkan:'))
        if pilihan == 1:
            elektronik()
        elif pilihan == 2 :
            fashion()
        elif pilihan == 3:
            furniture()
    elif user == 2 :
        keranjangsaya()
    elif user == 3 :
        ubahkeranjang()
    elif user == 4 :
        checkout()
        
        # Program = {'barang' : barangbelanja}
        # program1 = {'harga' : hargabarang}
        # program2 = {'total' : totalharga}
        
        
        # hitungan = bacaJson()
        # hitungan.append(Program)
        # hitungan.append(program1)
        # hitungan.append(program2)
        # tulis_ulangJson(hitungan)
        print('Terima Kasih telah berbelanja di Rhopee')  
        break

  
print('~'*50)
print('Selamat Datang Di Belanja Online " Rhopee "')
print('~'*50)
nama = input("Silakan Masukkan Nama Anda:")
email = input("Silakan Masukkan Email Anda:")
print('~'*50)
print('Selamat Datang', nama)
print('Apa Yang Ingin Anda Beli?')
while True :
    print("Kategori:\n 1. Elektronik \n 2. Fashion \n 3. Furniture")
    pilihan = int(input('Masukkan kode 1-3 untuk memilih kategori yang diinginkan:'))
    print('~'*50)
    if pilihan == 1 :
        elektronik()
        break
    elif pilihan == 2 :
        fashion()
        break
    elif pilihan == 3 :
        furniture()
        break
    else :
        print ('Masukkan inputan sesuai nomer yang tersedia')
intimenu()
