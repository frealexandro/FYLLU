import reflex as rx
from fronted.components.footer import FAQAccordion

def footer():
    return rx.container(
        FAQAccordion(),
    )