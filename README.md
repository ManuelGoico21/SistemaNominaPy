# Sistema de Nómina - Generador de Recibos 📄

Una aplicación para automatizar la generación y envío de recibos de nómina para empleados, diseñada para facilitar el trabajo del departamento de Recursos Humanos. Desarrollada en Python usando Tkinter para la interfaz gráfica y FPDF para la creación de PDFs.

## 🚀 Características

- **Generación Automática de Recibos:** Genera recibos en formato PDF a partir de una plantilla HTML.
- **Envío Masivo de Correos:** Envía automáticamente los recibos a cada empleado utilizando su dirección de correo electrónico registrada.
- **Interfaz Gráfica Intuitiva:** Diseño sencillo y fácil de usar para seleccionar archivos y carpetas.
- **Personalización Corporativa:** Incluye logo, colores y formato de recibo personalizable.
- **Registro de Actividad:** Muestra un log detallado del proceso para fácil monitoreo.

---

## 📁 Estructura del Proyecto

SistemaNomina/
│
├── app.py # Interfaz gráfica de usuario
├── main.py # Lógica principal para generación de recibos
├── empleados.xlsx # Archivo Excel con datos de empleados
├── plantilla_recibo.html # Plantilla HTML para los recibos
├── firma.html # Plantilla para las firmas del correo
├── logos/
│ └── logo.png # Logo corporativo
├── recibos/ # Carpeta para almacenar los recibos generados
├── setup.iss # Script de Inno Setup para el instalador
└── README.md # Archivo de documentación (este archivo)

---

## 🛠️ Requisitos

- Python 3.10 o superior
- Librerías requeridas:
  - `pandas`
  - `fpdf2`
  - `tkinter`
  - `openpyxl`

## Instálalas con:

- `pip install pandas fpdf2 openpyxl`

  
---

📦 Cómo Compilar a .exe
Si quieres distribuir tu aplicación como un ejecutable, sigue estos pasos:

1. Instala PyInstaller:

- `pip install pyinstaller`

2. Genera el ejecutable:

- `pyinstaller --name "SistemaNomina" --onedir --windowed \
  --add-data "logos;logos" \
  --add-data "recibos;recibos" \
  app.py`
---
3. Crea el instalador (opcional):

-Usa setup.iss con Inno Setup para crear un instalador profesional.
---
✉️ Configuración de Correo
Para que los correos se envíen correctamente, debes usar una contraseña de aplicación:

Activa la autenticación en dos pasos en tu cuenta de Gmail.

Genera una App Password en tu configuración de seguridad.

Ingresa esta contraseña en el campo Password App de la aplicación.
---

🚀 Cómo Usar la Aplicación

1- Abre SistemaNomina.exe.

2- Selecciona tu archivo empleados.xlsx.

3- Elige la carpeta donde se guardarán los PDFs.

4- Ingresa tu correo de Gmail y App Password.

5- Haz clic en Generar Recibos.

6- ¡Listo! Los recibos serán creados y enviados automáticamente.
---

🤝 Contribuciones
Si tienes ideas para mejorar esta aplicación o encuentras algún error, ¡siente libre de hacer un fork y enviar un pull request!

📄 Licencia
Este proyecto es de uso libre. Si lo mejoras, ¡me encantaría saber cómo! 😊
---
Creado por Manuel A. Otto Goico



