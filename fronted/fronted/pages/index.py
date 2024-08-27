import reflex as rx
import fronted.utils as utils
import fronted.styles.styles as styles
from fronted.components.navbar import navbar_dropdown

#from link_bio.components.footer import footer

from fronted.views.header import header

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
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        bg = styles.Color.BACKGROUND.value,
        height="100vh",  # Asegura que el contenedor ocupe toda la altura de la ventana
        width="100%",
        #footer()
    )