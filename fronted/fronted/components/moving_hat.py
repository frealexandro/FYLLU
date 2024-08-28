import reflex as rx
from typing import List

styles = {
    "moving_hat": lambda top, left, size, offset: {
        "position": "absolute",
        "top": top,
        "left": left,
        "width": "100%",
        "opacity": "2",
        "animation": "moveHat 60s linear infinite",
        "transition": "transform 0.3s ease",
        "_hover": {
            "transform": "translateY(-10px) rotate(5deg)",
        },
        "img": {
            "width": size,
            "height": "auto",
            "margin-left": offset,
        },
    }
}

def moving_hat(top: str, left: str, size: str, offset: str = "0px"):
    return rx.box(
        rx.image(src="/hat one piece.png", alt="Moving Hat"),
        style=styles["moving_hat"](top, left, size, offset),
    )
