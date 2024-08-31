import reflex as rx
from typing import List
from fronted.styles.styles import Size, Spacing
from fronted.styles.colors import Color, TextColor
from fronted.styles.fonts import Font, FontWeight

# Styles
styles = {
    "main_content": {
        "width": "100%",
        "max_width": "1200px",  # Increased max-width
        "margin": "0 auto",
        "padding": "6rem 1rem",
        "position": "relative",
        "z_index": "10",
    },
    "text_container": {
        "width": "100%",
        "max_width": "800px",  # Container for text content
        "margin": "0 auto",
    },
    "button": {
        "background_color": "#0099ff",
        "color": "black",
        "font_weight": "italic",
        "padding": "0.75rem 1.5rem",
        "size" : "3",
        "font_size": "1.125rem",
        "font_family":"Comic Sans MS",
        "transition": "background-color 300ms",
        "_hover": {
            "background_color": "#FF00FF",
        },
    },
}

# Components
def main_content():
    return rx.box(
        rx.vstack(
            rx.box(
                rx.heading("Tu suscripción de analytics", font_size="40px", margin_bottom="1rem", color="black",font_family="Comic Sans MS"),
                rx.heading("completa, flexible y accesible.", font_size="40px", margin_bottom="5rem", color="black",font_family="Comic Sans MS"),
                rx.text(
                    "Escala y delega todas las operaciones de analitycs de tu organización con un servicio de operación confiable y sin complicaciones.",
                    font_size="20px",
                    margin_bottom="2rem",
                    color="black",
                    font_family="Comic Sans MS"
                ),
                rx.text(
                    "Business Intelligence | Machine Learning | Dashboards | Flow Automation | Artificial Intelligence",
                    font_size="lg",
                    margin_bottom="2rem",
                    color="black",
                    font_family="Comic Sans MS"
                ),
                style=styles["text_container"],
                text_align="center",
            ),
            rx.button("Comenzar prueba gratis", style=styles["button"]),
            rx.text("Agenda una reunión y obtén 7 días gratis.", font_size="sm", margin_top="1rem", color="black",font_family="Comic Sans MS"),
            align_items="center",
            width="100%",
        ),
        style=styles["main_content"],
    )

