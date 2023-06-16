import tkinter

window = tkinter.Tk()

Labelnama = tkinter.Label(window, text="Hello Nama Saya Alvin")
Labelkampus = tkinter.Label(window, text="berkuliah di STIMIK TUNAS BANGSA")
Labelsemester = tkinter.Label(window, text="Semester IV")
Labelprodi = tkinter.Label(window, text="Informatika A")


Labelnama.grid(row=1, column=1)
Labelkampus.grid(row=2, column=2)
Labelsemester.grid(row=3, column=1)
Labelprodi.grid(row=4, column=2)

window.mainloop()
