import reflex as rx
import fronted.utils as utils
import fronted.styles.styles as styles
from fronted.components.navbar import navbar_dropdown


from fronted.views.header import header
from fronted.views.content import content
from fronted.views.prices import prices
from fronted.views.footer import footer
from fronted.routes import Route


from fronted.styles.styles import Size




@rx.page(
    
    route = Route.INDEX.value,
    title=utils.index_title,
    description=utils.index_description,
    
)

def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar_dropdown(),
        rx.vstack(
            rx.vstack(
                header(),
                content(),
                prices(),
                width="100%",
                background_color="#FAFAFA",
                
            ),
        ),
        footer(),  # Movido dentro del vstack principal
        width="100%",
        align_items="stretch",
       )