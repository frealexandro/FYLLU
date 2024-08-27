"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import reflex as rx
from fronted.pages.index import index
import fronted.styles.styles as styles



# Create app instance and add index page.
app = rx.App()
app.add_page(index)
