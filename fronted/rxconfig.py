import reflex as rx

config = rx.Config(
    app_name="fronted",
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
        },
)