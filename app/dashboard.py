from shiny import App, render, ui
from parser import load_all_files
from analyzer import summary_stats


data = load_all_files()

app_ui = ui.page_fluid(
    ui.h2("Dashboard Débitos Diretos"),
    ui.hr(),
    ui.output_text("total"),
    ui.output_text("ops"),
)

def server(input, output, session):

    stats = summary_stats(data)

    @output
    @render.text
    def total():
        return f"Total Processado: {stats['total']} €"

    @output
    @render.text
    def ops():
        return f"Número de Operações: {stats['operations']}"

app = App(app_ui, server)
