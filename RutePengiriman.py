import heapq
import random

# =====================================
# GRAPH RUTE PENGIRIMAN
# =====================================

graph = {
    "Tangerang": {
        "Jakarta": 20,
        "Serang": 30
    },
    "Jakarta": {
        "Tangerang": 20,
        "Bekasi": 15,
        "Depok": 18
    },
    "Bekasi": {
        "Jakarta": 15,
        "Cikarang": 20
    },
    "Depok": {
        "Jakarta": 18,
        "Bandung": 40
    },
    "Serang": {
        "Tangerang": 30,
        "Bandung": 35
    },
    "Bandung": {
        "Serang": 35,
        "Depok": 40,
        "Cikarang": 10
    },
    "Cikarang": {
        "Bekasi": 20,
        "Bandung": 10
    }
}

data_pengiriman = []

# =====================================
# ALGORITMA DIJKSTRA
# =====================================

def dijkstra(graph, start, end):

    queue = [(0, start, [])]
    visited = set()

    while queue:

        jarak, kota, path = heapq.heappop(queue)

        if kota in visited:
            continue

        visited.add(kota)
        path = path + [kota]

        if kota == end:
            return jarak, path

        for tetangga, bobot in graph[kota].items():

            if tetangga not in visited:
                heapq.heappush(
                    queue,
                    (jarak + bobot, tetangga, path)
                )

    return None

# =====================================
# MENU PROGRAM
# =====================================

while True:

    print("\n" + "=" * 60)
    print("     SISTEM RUTE PENGIRIMAN BARANG")
    print("=" * 60)
    print("1. Input Pengiriman")
    print("2. Lihat Riwayat Pengiriman")
    print("3. Cari Paket")
    print("4. Update Status")
    print("5. Keluar")

    menu = input("Pilih Menu : ")

    # =====================================
    # INPUT PENGIRIMAN
    # =====================================

    if menu == "1":

        print("\nDaftar Kota:")
        for kota in graph:
            print("-", kota)

        pengirim = input("\nNama Pengirim : ")
        penerima = input("Nama Penerima : ")

        asal = input("Kota Asal : ")
        tujuan = input("Kota Tujuan : ")

        berat = float(input("Berat Barang (Kg) : "))

        hasil = dijkstra(graph, asal, tujuan)

        if hasil is None:
            print("Rute tidak ditemukan!")
            continue

        jarak = hasil[0]
        rute = hasil[1]

        biaya = (jarak * 2500) + (berat * 5000)

        resi = "RESI" + str(random.randint(1000, 9999))

        data = {
            "resi": resi,
            "pengirim": pengirim,
            "penerima": penerima,
            "asal": asal,
            "tujuan": tujuan,
            "berat": berat,
            "jarak": jarak,
            "biaya": biaya,
            "rute": rute,
            "status": "Diproses"
        }

        data_pengiriman.append(data)

        print("\n" + "=" * 60)
        print("DATA BERHASIL DITAMBAHKAN")
        print("=" * 60)
        print("Nomor Resi :", resi)
        print("Rute       :", " -> ".join(rute))
        print("Jarak      :", jarak, "KM")
        print("Biaya      : Rp{:,.0f}".format(biaya))

    # =====================================
    # RIWAYAT
    # =====================================

    elif menu == "2":

        if len(data_pengiriman) == 0:
            print("\nBelum ada data pengiriman.")
        else:

            print("\n" + "=" * 80)

            for item in data_pengiriman:

                print("Resi       :", item["resi"])
                print("Pengirim   :", item["pengirim"])
                print("Penerima   :", item["penerima"])
                print("Asal       :", item["asal"])
                print("Tujuan     :", item["tujuan"])
                print("Rute       :", " -> ".join(item["rute"]))
                print("Jarak      :", item["jarak"], "KM")
                print("Biaya      : Rp{:,.0f}".format(item["biaya"]))
                print("Status     :", item["status"])
                print("-" * 80)

    # =====================================
    # CARI RESI
    # =====================================

    elif menu == "3":

        cari = input("Masukkan Nomor Resi : ")

        ditemukan = False

        for item in data_pengiriman:

            if item["resi"] == cari:

                print("\nDATA DITEMUKAN")
                print("Pengirim :", item["pengirim"])
                print("Penerima :", item["penerima"])
                print("Status   :", item["status"])
                print("Rute     :", " -> ".join(item["rute"]))

                ditemukan = True

        if not ditemukan:
            print("Data tidak ditemukan.")

    # =====================================
    # UPDATE STATUS
    # =====================================

    elif menu == "4":

        cari = input("Masukkan Nomor Resi : ")

        for item in data_pengiriman:

            if item["resi"] == cari:

                print("\n1. Diproses")
                print("2. Dikirim")
                print("3. Sampai")

                pilih = input("Pilih Status : ")

                if pilih == "1":
                    item["status"] = "Diproses"

                elif pilih == "2":
                    item["status"] = "Dikirim"

                elif pilih == "3":
                    item["status"] = "Sampai"

                print("Status berhasil diperbarui!")

    # =====================================
    # KELUAR
    # =====================================

    elif menu == "5":

        print("\nTerima kasih telah menggunakan aplikasi.")
        break

    else:
        print("Menu tidak tersedia!")