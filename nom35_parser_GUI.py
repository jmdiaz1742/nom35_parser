#!/usr/bin/env python3

# NOM-35 Parser
# Consume un archivo .csv con respuestas del cuestionario
# Produce un reporte con resultados y graficas

from guizero import App, Box, PushButton, Text, TextBox
from csv_manager import CsvManager
from graph_manager import *

#### Constants ###
SCRIPT_NAME: str = "Generador de reporte para NOM-35"
VERSION_MAIN: int = 0
VERSION_MINOR: int = 1
VERSION_PATCH: int = 0
SCRIPT_VERSION_STR: str = f"{VERSION_MAIN}.{VERSION_MINOR}.{VERSION_PATCH}"
# File stuff
EXT_CSV: str = ".csv"

### Global variables ###
csv_manager: CsvManager


### Functions ###


def pick_file():
    """Pick a csv file"""
    global csv_manager
    global generate_report_button
    file_name: str = app.select_file(
        filetypes=[["Archivo CSV", f"*{EXT_CSV}"]]
    )
    file_name_text.value = f"Archivo:\n{file_name}"
    csv_manager = CsvManager(file_name)
    if csv_manager.valid:
        generate_report_button.enable()
        print(f"Archivo {csv_manager.get_file()} seleccionado")
    else:
        generate_report_button.disable()
        print(f"Archivo erroneo")


def generate_report():
    """Generate Report"""
    global csv_manager
    global generate_report_button
    global generate_graphs_button
    if csv_manager.generate_report():
        report: str = csv_manager.get_report()
        with open("report.txt", "w") as report_file:
            report_file.write(report)
        generate_graphs_button.enable()
        app.info(f"{SCRIPT_NAME}", "Reporte listo")
    else:
        app.error(f"{SCRIPT_NAME}", "Error al generar report")


def generate_graphs():
    """Generate Graphs"""
    global csv_manager
    # if csv_manager.data_ready():
    if create_histogram(csv_manager.get_answers_list(0)):
        app.info(f"{SCRIPT_NAME}", "Gráficas creadas")
    else:
        app.error(f"{SCRIPT_NAME}", "Error al generar gráficas")


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
    text=f"Archivo:\n",
)

generate_report_button: PushButton = PushButton(
    app,
    grid=[0, 1],
    align="left",
    command=generate_report,
    text="Generar Reporte",
    enabled=False,
)

generate_graphs_button: PushButton = PushButton(
    app,
    grid=[0, 2],
    align="left",
    command=generate_graphs,
    text="Generar Gráficas",
    enabled=False,
)


### Main ###
if __name__ == "__main__":
    print(f"{SCRIPT_NAME} v{SCRIPT_VERSION_STR}")

    app.display()
