import reflex as rx
import os

config = rx.Config(
    app_name="fronted",
    api_url="http://localhost:8000",
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
        },
    
)