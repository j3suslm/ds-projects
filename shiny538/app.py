from shiny import App, render, ui
from shinywidgets import output_widget, render_widget
import plotly.graph_objects as go
import polars as pl
from pathlib import Path

# 1. Custom Plotly Stylist
def economist_layout(fig, title, subtitle=""):
    fig.update_layout(
        title=f"<b>{title}</b><br><span style='font-size:14px; color:#666'>{subtitle}</span>",
        font_family="Arial, sans-serif",
        paper_bgcolor="#f5f4f0",
        plot_bgcolor="#f5f4f0",
        margin=dict(t=80, l=10, r=10, b=40),
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
        hovermode="x unified",
        xaxis=dict(showgrid=False, linecolor="#000000", linewidth=1),
        yaxis=dict(showgrid=True, gridcolor="#d7d7d7", gridwidth=0.5, zeroline=False)
    )
    return fig

# 2. UI Definition
css_path = Path(__file__).parent / "styles.scss"

app_ui = ui.page_navbar(
    ui.nav_panel(
        "Economic Dashboard",
        ui.layout_column_wrap(
            ui.card(
                ui.card_header("Output Analysis"),
                output_widget("main_plot"),
                ui.card_footer("Source: Internal Data Pipeline", style="font-style: italic; font-size: 0.8rem;")
            ),
            width=1
        ),
    ),
    title="Intelligence Unit",
    theme=ui.Theme("shiny"), # This compiles your SCSS automatically
)

# 3. Server Logic
def server(input, output, session):
    @render_widget
    def main_plot():
        # Mock data using Polars
        df = pl.DataFrame({
            "year": [2020, 2021, 2022, 2023, 2024, 2025],
            "value": [100, 105, 102, 110, 115, 118],
            "forecast": [None, None, None, None, 116, 120]
        })

        fig = go.Figure()
        
        # Actual Data
        fig.add_trace(go.Scatter(
            x=df["year"], y=df["value"],
            mode='lines+markers',
            name='Actual',
            line=dict(color='#e3120b', width=3)
        ))
        
        # Forecast Data (dashed)
        fig.add_trace(go.Scatter(
            x=df["year"], y=df["forecast"],
            mode='lines',
            name='Forecast',
            line=dict(color='#006ba2', width=2, dash='dot')
        ))

        return economist_layout(fig, "Portfolio Performance", "Index 2020 = 100")

app = App(app_ui, server)
