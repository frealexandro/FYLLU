import reflex as rx
import os

config = rx.Config(
    app_name="fronted",
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
        },
    
)