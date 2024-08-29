# content.py
import reflex as rx
from fronted.components.logistic import proces_product
from fronted.components.benefits_card import benefits , cta_card

def content():
    return rx.container(
        proces_product(),
        rx.flex(
            rx.box(
                benefits(),
                width=["100%", "100%", "50%"],
                padding_right=["0", "0", "1em"],
            ),
            rx.box(
                cta_card(),
                width=["100%", "100%", "50%"],
                padding_left=["20", "60", "1em"],
                padding_top=["20", "60", "5em"],
            ),
            width="100%",
            flex_direction=["column", "column", "row"],
        ),
        style={
            "display": "flex",
            "justifyContent": "center",  # Centrar horizontalmente
            "backgroundColor": "#FAFAFA",
            "width": "100vw",  # Asegura que el contenedor ocupe todo el ancho de la ventana
            "maxWidth": "100%",
        }
    )