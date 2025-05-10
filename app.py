import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import threading
import os

# Importamos la función principal que genera los recibos
from main import crear_recibo_pago, leer_datos_excel

class NominaApp:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Nómina - Generador de Recibos")

        # Archivo Excel
        tk.Label(master, text="Archivo Excel:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.excel_path = tk.Entry(master, width=50)
        self.excel_path.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(master, text="Examinar…", command=self.browse_excel).grid(row=0, column=2, padx=5)

        # Carpeta de salida
        tk.Label(master, text="Carpeta de Salida:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.out_folder = tk.Entry(master, width=50)
        self.out_folder.grid(row=1, column=1, padx=5, pady=5)
        tk.Button(master, text="Seleccionar…", command=self.browse_folder).grid(row=1, column=2, padx=5)

        # Botón Generar
        self.btn_generate = tk.Button(master, text="Generar Recibos", command=self.start_generation, bg="#d90429", fg="white")
        self.btn_generate.grid(row=2, column=0, columnspan=3, pady=10)

        # Área de log
        self.log_area = scrolledtext.ScrolledText(master, width=80, height=20, state="disabled")
        self.log_area.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

    def log(self, mensaje):
        self.log_area.configure(state="normal")
        self.log_area.insert(tk.END, mensaje + "\n")
        self.log_area.see(tk.END)
        self.log_area.configure(state="disabled")

    def browse_excel(self):
        path = filedialog.askopenfilename(
            title="Selecciona el archivo Excel",
            filetypes=[("Excel Files", "*.xlsx *.xls")],
        )
        if path:
            self.excel_path.delete(0, tk.END)
            self.excel_path.insert(0, path)

    def browse_folder(self):
        path = filedialog.askdirectory(title="Selecciona carpeta de salida")
        if path:
            self.out_folder.delete(0, tk.END)
            self.out_folder.insert(0, path)

    def start_generation(self):
        excel = self.excel_path.get().strip()
        out_dir = self.out_folder.get().strip()

        if not excel or not os.path.isfile(excel):
            messagebox.showerror("Error", "Selecciona un archivo Excel válido.")
            return
        if not out_dir or not os.path.isdir(out_dir):
            messagebox.showerror("Error", "Selecciona una carpeta de salida válida.")
            return

        # Deshabilitar botón para evitar dobles clicks
        self.btn_generate.config(state="disabled")
        threading.Thread(target=self.generate, args=(excel, out_dir), daemon=True).start()

    def generate(self, excel, out_dir):
        try:
            df = leer_datos_excel(excel)
            total = len(df)
            self.log(f"Iniciando generación de {total} recibos…")
            for i, row in df.iterrows():
                nombre = row["NombreEmpleado"]
                self.log(f"  • Generando recibo para: {nombre}")
                crear_recibo_pago(row, out_dir)
            self.log("✅ ¡Todos los recibos fueron generados con éxito!")
            messagebox.showinfo("Finalizado", "Se generaron todos los recibos correctamente.")
        except Exception as e:
            self.log(f"❌ Error: {e}")
            messagebox.showerror("Error al generar recibos", str(e))
        finally:
            self.btn_generate.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = NominaApp(root)
    root.mainloop()
