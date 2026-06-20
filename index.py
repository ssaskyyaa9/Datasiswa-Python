import  pandas as pd
import matplotlib.pyplot as plt

def nilaiSiswa():
    # 1. menampilkan/membaca file excel
    data =  pd.read_excel('nilaiSiswa.xlsx')
    print(data)

    # 2. Menghitung rata-rata tiap siswa
    data["Rata_rata"] = data[["Matematika", "Bahasa Indonesia", "Informatika"]].mean(axis=1)
    print("\nData dengan Rata-rata:")
    print(data)

    # 3. Menentukan siswa dengan nilai rata-rata tertinggi
    tertinggi = data.loc[data["Rata_rata"].idxmax()]
    print("\nSiswa dengan nilai tertinggi:", tertinggi["Nama"], "-", tertinggi["Rata_rata"])

    # 4. Visualisasi nilai Matematika
    plt.bar(data["Nama"], data["Matematika"], color="pink")
    plt.title("Grafik Nilai Matematika Siswa")
    plt.xlabel("Nama Siswa")
    plt.ylabel("Nilai")
    plt.show()

    # 5. Visualisasi nilai Bahasa Indonesia
    plt.bar(data["Nama"], data["Bahasa Indonesia"], color="pink")
    plt.title("Grafik Nilai Bahasa Indonesia Siswa")
    plt.xlabel("Nama Siswa")
    plt.ylabel("Nilai")
    plt.show()

    # 6. Visualisasi nilai Informatika
    plt.bar(data["Nama"], data["Informatika"], color="pink")
    plt.title("Grafik Nilai Informatika Siswa")
    plt.xlabel("Nama Siswa")
    plt.ylabel("Nilai")
    plt.show()

    # 8.buat grafik untuk menampilkan nilai rata-rata tertinggi
    data["Nilai_Tertinggi"] = data[["Matematika", "Bahasa Indonesia", "Informatika"]].max(axis=1) 

    # 7.Visualisasi data nilai tertinggi
    plt.bar(data["Nama"], data["Nilai_Tertinggi"], color="pink")
    plt.title("Grafik Nilai rata-rata tertinggi")
    plt.xlabel("Nama Siswa")
    plt.ylabel("Nilai")
    plt.show()

nilaiSiswa()