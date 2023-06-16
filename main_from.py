import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo

# Inisialisasi
window = tkinter.Tk()
window.configure(bg="yellow")
window.geometry("300x300")
window.resizable(False,False)
window.title("Pendaftaran Mukbang")

# variable dan function
NAMA_LENGKAP = tkinter.StringVar()
ALAMAT_RUMAH = tkinter.StringVar()
MAKANAN_FAVORIT = tkinter.StringVar()
MINUMAN_FAVORIT = tkinter.StringVar()
OLAHRAGA_FAVORIT = tkinter.StringVar()

# Fungsi Tombol
def Tombol_click():
 if not NAMA_LENGKAP.get() or not ALAMAT_RUMAH.get() or not MAKANAN_FAFORIT.get() or not MINUMAN_FAFORIT.get() or not OLAHRAGA_FAFORIT.get():
    showinfo(title="error!",message="mohon lengkapi semua from!")
 else:
    pesan = f"Hallo {NAMA_LENGKAP.get()} Kamu Sudah Terdaftar!"
    showinfo(title="Selamat",message=pesan)

# frame input
style = ttk.Style()
style.configure("Custom.TEntry", fieldbackground="green")
input_frame = ttk.Frame(window)

# penempatan grid, pack, place
input_frame.pack(padx=10,pady=10,fill="x", expand=True)

# komponen nama lengkap
nama_depan_label = ttk.Label(input_frame, text="Nama Lengkap:")
nama_depan_label.pack(padx=10,fill="x",expand=True)
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_LENGKAP, style="Custom.TEntry")
nama_depan_entry.pack(padx=10,fill="x",expand=True)
# komponen alamat rumah
alamat_rumah_label = ttk.Label(input_frame, text="ALAMAT :")
alamat_rumah_label.pack(padx=10,fill="x",expand=True)
alamat_rumah_entry = ttk.Entry(input_frame,textvariable=ALAMAT_RUMAH)
alamat_rumah_entry.pack(padx=10,fill="x",expand=True)
# komponen makanan faforit
makanan_favorit_label = ttk.Label(input_frame, text="MAKANAN FAVORIT :")
makanan_favorit_label.pack(padx=10,fill="x",expand=True)
makanan_favorit_entry = ttk.Entry(input_frame,textvariable=MAKANAN_FAVORIT)
makanan_favorit_entry.pack(padx=10,fill="x",expand=True)
# komponen minuman faforit
minuman_favorit_label = ttk.Label(input_frame, text="MINUMAN FAVORIT :")
minuman_favorit_label.pack(padx=10,fill="x",expand=True)
minuman_favorit_entry = ttk.Entry(input_frame,textvariable=MINUMAN_FAVORIT)
minuman_favorit_entry.pack(padx=10,fill="x",expand=True)
# komponen  faforit
olahraga_favorit_label = ttk.Label(input_frame, text="OLAHRAGA FAVORIT :")
olahraga_favorit_label.pack(padx=10,fill="x",expand=True)
olahraga_favorit_entry = ttk.Entry(input_frame,textvariable=OLAHRAGA_FAVORIT)
olahraga_favorit_entry.pack(padx=10,fill="x",expand=True)
                    
# tombol
tombol_daftar = ttk.Button(input_frame,text="Daftar",command=Tombol_click)
tombol_daftar.pack(fill="x",expand=True, padx=10,pady=10)

window.mainloop()
