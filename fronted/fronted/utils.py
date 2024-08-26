import reflex as rx


def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")