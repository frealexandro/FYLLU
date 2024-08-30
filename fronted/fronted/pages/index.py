import reflex as rx
import fronted.utils as utils
import fronted.styles.styles as styles
from fronted.components.navbar import navbar_dropdown

#from link_bio.components.footer import footer

from fronted.views.header import header
from fronted.views.content import content
from fronted.views.prices import prices

#from link_bio.views.index_links import index_links
#from link_bio.views.sponsors import sponsors
from fronted.styles.styles import Size


@rx.page(
    title=utils.index_title,
    description=utils.index_description,
)

def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar_dropdown(),
        rx.center(
            rx.vstack(
                header(),
                content(),
                prices(),

                style={
                    "flex": "1",  # Permite que el vstack ocupe el espacio disponible
                    "display": "flex",
                    "flexDirection": "column",
                    "justifyContent": "center",  # Centrar verticalmente
                    "alignItems": "center",  # Centrar horizontalmente
                    "width": "100%",  # Asegura que el contenedor ocupe todo el ancho de la ventana
                }
            ),
            style={
                "width": "100%",
                "bg": "#FAFAFA"  # Asegura que el contenedor ocupe todo el ancho de la ventana
            }
        )
    )