"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import reflex as rx
from fronted.pages.index import index
from fronted.pages.funnel_ventas import funnel_ventas
import fronted.styles.styles as styles
from fronted.api import api



class State(rx.State):
    """define the state of the app"""


# Create app instance and add index page.
app = rx.App()


app.api