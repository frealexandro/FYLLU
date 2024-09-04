import reflex as rx
import fronted.constants as const
from fronted.components.link_button import link_button
from fronted.styles.colors import Color
from fronted.styles.styles import Spacing
from fronted.components.link_icon import link_icon
from fronted.styles.colors import Color, TextColor
from fronted.styles.styles import Size, Spacing





def social_media() -> rx.Component:
    return rx.chakra.box(
        rx.hstack(
        rx.avatar(
                    name="RandIA",
                    size="5",
                    src="/RandIA-negro-logo.png",
                    radius="full",
                    color=TextColor.BODY.value,
                    bg=Color.BACKGROUND.value,
                    padding="2px",
                    border=f"4px solid {Color.PRIMARY.value}",
                    #padding_top= "10px"
                ),
                position="relative"
            ),
            rx.vstack(
                rx.heading(
                    "RandIA",
                    size=Spacing.BIG.value,
                    font_family="Comic Sans MS",
                ),
                rx.text(
                    "@RandIA",
                    margin_top=Size.ZERO.value,
                    color="balck",
                ),
                rx.hstack(
                #    link_icon(
                #        "/icons/github.svg",
                #        const.GITHUB_URL,
                #        "GitHub"
                #    ),
                #    link_icon(
                #        "/icons/x.svg",
                #        const.TWITTER_X_URL,
                #        "Twitter/X"
                #    ),
                    link_icon(
                        "/icons/instagram.svg",
                        const.INSTAGRAM_URL,
                        "Instagram"
                    ),
                #    link_icon(
                #        "/icons/tiktok.svg",
                #        const.TIKTOK_URL,
                #        "TikTok"
                #    ),
                    link_icon(
                        "/icons/spotify.svg",
                        const.SPOTIFY_URL,
                        "Spotify"
                    ),
                    link_icon(
                        "/icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn"
                    ),
                    spacing=Spacing.LARGE.value,
                    padding_top=Size.SMALL.value
                ),
                spacing=Spacing.ZERO.value,
                align_items="start"
            ),
            align="end",
            spacing=Spacing.DEFAULT.value,
            padding_top=Size.BIG.value
        )

def com_newsletter() -> rx.Component:
    return rx.vstack(
        
        rx.heading("Suscríbete a", font_size="40px", weight="bold", mb="6",font_family="Comic Sans MS"),
        rx.heading("nuestro newsletter", font_size="40px", weight="bold", mb="6",font_family="Comic Sans MS"),
        rx.chakra.box(
            element="iframe",
            src="https://embeds.beehiiv.com/c9c3f7b7-7ed9-428a-a58f-cb53577fa352?slim=true",
            height="50px",
            width="100%",
        ),
    )