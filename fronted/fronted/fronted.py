"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import reflex as rx
from fronted.pages.index import index
from fronted.pages.funnel_ventas import funnel_ventas
import fronted.styles.styles as styles
#from fronted.api.api import featured
#from fronted.api import api



# Create app instance and add index page.
# Create app instance and add index page.
app = rx.App()
app.add_page(index)
app.add_page(funnel_ventas)


#app.api.add_api_route("/featured", featured)