import reflex as rx
import datetime
import fronted.constants as const
#from fronted.components.moving_hat import moving_hat
from fronted.components.prices import pricing_final
#from fronted.styles.styles import Size, Spacing
#from fronted.styles.colors import Color, TextColor

#from fronted.components.link_icon import link_icon
#from link_bio.components.info_text import info_text
#from link_bio.components.link_button import link_button
#from link_bio.state.PageState import PageState




# Main App
def prices():
    return rx.box(
        #moving_hat("2rem", "2", "8rem"),
        #moving_hat("20rem", "0", "8rem", "10rem"),
        #moving_hat("10rem", "0", "8rem", "70rem"),
        pricing_final(),
        style={
            "min_height": ["50vh", "60vh", "70vh"],
            "width": "100%",
            "background": "radial-gradient(at 50% 40%, #FFBE76 100px, #FFBE76 30%, #FAFAFA 70%)",
            "overflow": "hidden",
            "position": "relative",
        },
    )