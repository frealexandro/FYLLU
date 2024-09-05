import reflex as rx

config = rx.Config(
    app_name="fronted",
    cors_allowed_origins = [
        "http://localhost:3000",
        "https://randia.io",
        "https://rand-7x2s0oi2l-santiagos-projects-14c51bdf.vercel.app",
        
    ],
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
        },
    
)