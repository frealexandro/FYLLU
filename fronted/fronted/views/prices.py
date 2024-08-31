import reflex as rx
import datetime
import fronted.constants as const
#from fronted.components.moving_hat import moving_hat
from fronted.components.prices import pricing_final , title_prices
#from fronted.styles.styles import Size, Spacing
#from fronted.styles.colors import Color, TextColor

#from fronted.components.link_icon import link_icon
#from link_bio.components.info_text import info_text
#from link_bio.components.link_button import link_button
#from link_bio.state.PageState import PageState




# Main App
def prices():
    return rx.box(
        title_prices(),
        pricing_final(),
        style={
            "min_height": ["120vh", "140vh", "160vh"],
            "width": "100%",
            "background": "linear-gradient(#FAFAFA  0.1%, #B87333 90%)",
            #"width":"20%",
            #"height":"100%",
            "overflow": "hidden",
            "position": "relative",
            "margin_top":"10em",
        },
    )