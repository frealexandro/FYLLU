import reflex as rx
from fronted.components.footer import FAQAccordion
from fronted.components.newsletter import com_newsletter , social_media


def footer():
    return rx.box(  # Cambiado de rx.container a rx.box para tener más control
        rx.flex(
            rx.box(
                FAQAccordion(),
                width="40%",  # Ajustado para ocupar la mitad del ancho
                padding_right="40",
            ),
            rx.box(
                com_newsletter(),
                social_media(),
                width="50%",  # Ajustado para ocupar la mitad del ancho
                padding_top="100px",
                padding_left="300px",
                color="white",
            ),
            width="100%",
            justify="space-between",  # Distribuye el espacio entre los elementos
            align_items="flex-start",  # Alinea los elementos en la parte superior
        ),
        width="100%",
        background="black",
        padding="4",  # Añade un poco de padding alrededor del footer
    )

