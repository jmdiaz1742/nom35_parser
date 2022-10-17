# NOM-35 Parser
# Consume un archivo .csv con respuestas del cuestionario
# Produce un reporte con resultados y graficas

from guizero import App, Box, PushButton, Text, TextBox

#### Constants ###
SCRIPT_NAME: str = "Generador de reporte para NOM-35"
VERSION_MAIN: int = 0
VERSION_MINOR: int = 1
VERSION_PATCH: int = 0
SCRIPT_VERSION_STR: str = f"{VERSION_MAIN}.{VERSION_MINOR}.{VERSION_PATCH}"
# File stuff
EXT_CSV: str = ".csv"

### Global variables ###
csv_file: str = ""


### Functions ###


def generate_report():
    """Generate Report"""
    print("Reporte listo!")


def pick_file():
    """Pick a csv file"""
    csv_file = app.select_file(
        filetypes=[["Archivo CSV", f"*{EXT_CSV}"]]
    )
    file_name_text.value = f"Archivo:\n{csv_file}"
    print(f"Archivo {csv_file} seleccionado")


### GUI Elements ###
app: App = App(
    title=f"{SCRIPT_NAME} v{SCRIPT_VERSION_STR}",
    layout="grid",
    width=1000,
    height=300,
)

file_box: Box = Box(
    app,
    grid=[0, 0],
)
pick_file_button: PushButton = PushButton(
    file_box,
    align="left",
    command=pick_file,
    text="Seleccionar archivo",
)
file_name_text: Text = Text(
    file_box,
    align="left",
    text=f"Archivo: {csv_file}",
)

generate_report_button: PushButton = PushButton(
    app,
    grid=[0, 1],
    align="left",
    command=generate_report,
    text="Generar Reporte",
)


### Main ###
if __name__ == "__main__":
    print(f"{SCRIPT_NAME} v{SCRIPT_VERSION_STR}")

    app.display()
