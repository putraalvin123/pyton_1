import tkinter
from tkinter import ttk

# Inisialisasi
window = tkinter.Tk()
window.configure(bg="white")
window.geometry("400*200")
window.resizable(false,false)
window.title("Pendaftaran Mukbang")

# variable dan function
Nama_Depan = tkinter.StringVar()
ALAMAT_RUMAH = tkinter.StringVar()
MAKANAN_FAFORIT = tkinter.StringVar()
MINUMAN_FAFORIT = tkinter.StringVar()
HOBI_FAFORIT = tkinter.StringVar()

# Fungsi Tombol
def tombol_click():
    pesan = f"hallo {NAMA_DEPAN.get()}, kamu sudah terdaftar!"
    showinfo(title="Selamat",message=pesan)


# frame input
input_frame = ttk.frame(window)

# penempatan grid, pack, place
input_frame.pack(padx=10,pady=10,fill="x", expand=True)

# komponen nama lengkap
nama_lengkap_label = ttk.Label(input_frame, text="Nama Depan :")
nama_depan_label.pack(padx=10,fill="x",expand=True)
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)
# komponen alamat rumah
alamat_rumah_label = ttk.Label(input_frame, text="ALAMAT :")
alamat_rumah_label.pack(padx=10,fill="x",expand=True)
alamat_rumah_entry = ttk.Entry(input_frame,textvariable=ALAMAT_RUMAH)
alamat_rumah_entry.pack(padx=10,fill="x",expand=True)
# komponen makanan faforit
makanan_faforit_label = ttk.Label(input_frame, text="ALAMAT :")
makanan_faforit_label.pack(padx=10,fill="x",expand=True)
makanan_faforit_entry = ttk.Entry(input_frame,textvariable=ALAMAT_RUMAH)
makanan_faforit_entry.pack(padx=10,fill="x",expand=True)
                    
# tombol
tombol_daftar = ttk.Button(input_frame,text="DAFTAR",command=tombol)
tombol_daftar.pack(fill="x",expand=True, padx=10,pady=10)

window.mainloop()
