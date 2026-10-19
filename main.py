import tkinter as tk

def prediksi_prodi():
    label_hasil.config(text="Prodi Pilihan: Teknologi Informasi")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x500")

label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Times New Roman", 14, "bold"))
label_judul.pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

mata_pelajaran = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Fisika",
    "Kimia",
    "Biologi",
    "Ekonomi",
    "Sosiologi",
    "Geografi",
    "Informatika"
]

entries = []

for i, mapel in enumerate(mata_pelajaran):
    lbl = tk.Label(frame_input, text=f"Nilai {mapel}:")
    lbl.grid(row=i, column=0, sticky="w", pady=2, padx=5)
    
    entry = tk.Entry(frame_input)
    entry.grid(row=i, column=1, pady=2, padx=5)
    entries.append(entry)

btn_prediksi = tk.Button(root, text="Hasil Prediksi", command=prediksi_prodi)
btn_prediksi.pack(pady=15)

label_hasil = tk.Label(root, text="Prodi Pilihan: -", font=("Times New Roman", 10))
label_hasil.pack(pady=5)

root.mainloop()