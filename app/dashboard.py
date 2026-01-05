from shiny import App, render, ui
import matplotlib.pyplot as plt
from parser import load_all_files
from analyzer import summary_stats, build_dataframe, totals_by_client


# -------- LOAD DATA --------
data = load_all_files()
df = build_dataframe(data)
stats = summary_stats(data)


# -------- UI --------
app_ui = ui.page_fluid(

    ui.h2("📊 Dashboard Débitos Diretos PS2"),
    ui.hr(),

    ui.row(
        ui.column(3, ui.card(ui.h4("Total (€)"), ui.h3(f"{stats['total']} €"))),
        ui.column(3, ui.card(ui.h4("Operações"), ui.h3(stats["operations"]))),
        ui.column(2, ui.card(ui.h4("Máximo (€)"), ui.h3(stats["max"]))),
        ui.column(2, ui.card(ui.h4("Mínimo (€)"), ui.h3(stats["min"]))),
        ui.column(2, ui.card(ui.h4("Média (€)"), ui.h3(stats["avg"]))),
    ),

    ui.hr(),
    ui.h3("📋 Tabela de Operações"),
    ui.output_table("table"),

    ui.hr(),
    ui.h3("📈 Total por Cliente"),
    ui.output_plot("grafico")
)


# -------- SERVER --------
def server(input, output, session):

    @output
    @render.table
    def table():
        return df

    @output
    @render.plot
    def grafico():
        client_totals = totals_by_client(data)
        plt.figure()
        plt.bar(client_totals["client"], client_totals["amount"])
        plt.title("Total recebido por cliente")
        plt.xlabel("Cliente")
        plt.ylabel("Valor (€)")
        plt.xticks(rotation=45)


app = App(app_ui, server)
