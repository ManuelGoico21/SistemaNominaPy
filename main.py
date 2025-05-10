import pandas as pd
from fpdf import FPDF
from fpdf.enums import XPos, YPos
import os
from datetime import datetime

# Ruta absoluta del logo
logo_path = os.path.abspath(os.path.join("logos", "logo.png"))
if not os.path.exists(logo_path):
    print("❌ No se encontró el logo en:", logo_path)
    exit()
print(f"✅ Logo encontrado en: {logo_path}")

class ReciboPDF(FPDF):
    def header(self):
        # Logo
        self.image(logo_path, x=10, y=8, w=30)
        # Título principal
        self.set_font("Helvetica", "B", 16)
        self.cell(
            0, 10,
            "ACADEMIA DE LENGUAS DE SANTO DOMINGO",
            align="C",
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT
        )
        # Subtítulo con comillas ASCII
        self.set_font("Helvetica", "", 10)
        self.cell(
            0, 5,
            '"The Power to Communicate"',
            align="C",
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT
        )
        self.ln(5)


def leer_datos_excel(archivo):
    return pd.read_excel(archivo)


def crear_recibo_pago(empleado, carpeta_salida):
    os.makedirs(carpeta_salida, exist_ok=True)
    fecha_str = datetime.now().strftime("%d/%m/%Y")
    nombre_pdf = f"{empleado['NombreEmpleado'].replace(' ', '_')}_{fecha_str.replace('/','')}.pdf"
    ruta_pdf = os.path.join(carpeta_salida, nombre_pdf)

    pdf = ReciboPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)
    pdf.set_font("Helvetica", "", 12)

    # Título de quincena
    pdf.cell(
        0, 8,
        "1ERA QUINCENA DE MAYO 2025",
        align="C",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT
    )
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(
        0, 5,
        "COMPROBANTE DE PAGO",
        align="C",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT
    )
    pdf.ln(5)

    # Nombre del empleado en franja roja
    pdf.set_fill_color(208, 0, 0)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(
        0, 8,
        f" Nombre del Empleado: {empleado['NombreEmpleado']}",
        fill=True,
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT
    )
    pdf.ln(2)

    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", "", 10)

    def dibujar_seccion(titulo, datos):
        # Cabecera de sección
        pdf.set_fill_color(208, 0, 0)
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(140, 8, titulo, border=1, fill=True, align="C")
        pdf.cell(50, 8, "", border=1, fill=True)
        pdf.ln()

        # Filas de detalle
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Helvetica", "", 10)
        for concepto, valor in datos[:-1]:
            pdf.cell(140, 8, concepto, border="LR")
            texto = f"{valor:,.2f}" if valor is not None else "-"
            pdf.cell(50, 8, texto, border="LR", align="R")
            pdf.ln()

        # Fila de total
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(140, 8, datos[-1][0], border=1)
        total = datos[-1][1]
        pdf.cell(50, 8, f"{total:,.2f}", border=1, align="R")
        pdf.ln(10)

    # Preparar datos
    ingresos = [
        ("SALARIO", empleado["Salario"]),
        ("BONO VACACIONAL", None),
        ("INCENTIVOS", None),
        ("HORAS EXTRAS", empleado["HorasExtras"]),
        ("OTROS", None),
        ("TOTAL INGRESOS", empleado["TotalIngresos"]),
    ]
    deducciones = [
        ("AFP", empleado["AFP"]),
        ("SFS", empleado["SFS"]),
        ("PERCAPITA ADICIONAL", None),
        ("SEGURO MEDICO", None),
        ("ISR", empleado["ISR"]),
        ("OTROS DESC", None),
        ("TOTAL DEDUCCIONES", empleado["TotalDeducciones"]),
    ]

    # Dibujar secciones
    dibujar_seccion("INGRESOS BRUTOS", ingresos)
    dibujar_seccion("DEDUCCIONES", deducciones)

    # Ingreso Neto
    pdf.set_fill_color(208, 0, 0)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(140, 8, "INGRESO NETO", border=1, fill=True)
    pdf.cell(50, 8, f"{empleado['IngresoNeto']:,.2f}", border=1, fill=True, align="R")

    pdf.output(ruta_pdf)
    print(f"📄 PDF creado: {ruta_pdf}")


def main():
    df = leer_datos_excel("empleados.xlsx")
    for _, fila in df.iterrows():
        crear_recibo_pago(fila, "recibos_generados")


if __name__ == "__main__":
    main()
