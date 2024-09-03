import reflex as rx

config = rx.Config(
    app_name="fronted",
    cors_allowed_origins = [
        "http://localhost:3000",
        "https://www.randia.io",
    ],
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
        },
    
)