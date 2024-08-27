import reflex as rx
import fronted.styles.styles as styles

#from fornted.routes import Route

from fronted.styles.styles import Size
from fronted.styles.colors import Color



def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium",color=Color.PRIMARY.value,), href=url
    )

def service_item(icon: str, title: str, description: str) -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.text(icon, font_size="2em", margin_right="0.5em"),
            rx.heading(title, size="sm"),
            margin_bottom="0.5em",
        ),
        rx.text(description, font_size="sm", color="gray"),
        direction="column",
    )


def navbar_dropdown() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/fylluicon.png",
                        width="3em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "FYLLU", size="7", weight="bold"
                        
                    ),
                    align_items="center",
                    spacing="3",
                    margin_left="5em"

                    
                ),
                rx.hstack(
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.button(
                                rx.text(
                                    "Servicios",
                                    size="4",
                                    weight="medium",
                                    color=Color.PRIMARY.value,
                                ),
                                rx.icon("chevron-down"),
                                weight="medium",
                                variant="ghost",
                                size="3",
                                color=Color.PRIMARY.value,
                                

                            ),
                        ),
                        rx.menu.content(
                        rx.heading("Servicios", size="xl", margin_bottom="1em",bg = "#FAD6A5"),
                        rx.grid(
                            service_item("🖼️", "Diseño para redes sociales", "Contenido para Instagram, Meta, LinkedIn o TikTok"),
                            service_item("🎨", "Diseño de marca", "Manuales de marca, logotipos, key visuals y activos de marca"),
                            service_item("📊", "Diseño para anuncios digitales", "Anuncios de paid marketing para Google, Meta, X o TikTok"),
                            service_item("✏️", "Diseño de ilustración", "Assets digitales, iconos, personajes y material de marketing ilustrado"),
                            service_item("📑", "Diseño de presentaciones", "Decks, ebooks, one pagers y presentaciones comerciales"),
                            service_item("📧", "Diseño de email", "Plantillas para email marketing, firmas y diseño para email"),
                            service_item("🎬", "Edición de video", "Tutoriales, demos de productos, podcast o videos informativos"),
                            service_item("🎭", "Animación 2D/3D", "Motion graphics, videos animados, demos de producto y animación 2D/3D"),
                            service_item("🌐", "Diseño web", "Landing pages, sitios webs completos y plantillas de email marketing"),
                            columns="3",
                            spacing="5",
                            color = Color.PRIMARY.value,
                            bg = "#FAD6A5",
                            border_style="solid",
                            border_color="#FAD6A5",
                        ),
                        width="800px",
                        padding="1.5em",
                        color=Color.PRIMARY.value,
                        bg = "#FAD6A5",
                    )
                    
                    
                    ),
                    navbar_link("Portafolio", "/#"),
                    navbar_link("Precios", "/#"),
                    navbar_link("Preguntas frecuentes", "/#"),
                    navbar_link("Clips", "/#"),
                    spacing="6",
                    
                ),
                rx.hstack(
                    rx.button(
                        "Iniciar sesión",
                        size="3",
                        variant="outline",
                        color=Color.PRIMARY.value,
                    ),
                    rx.button("Comenzar prueba gratis", size="3", color=Color.PRIMARY.value),
                    spacing="6",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        bg= Color.CONTENT.value,
        padding="1em",
        width="100%",
        ),)







#*ejemplo mouredev
#def navbar() -> rx.Component:
#    return rx.hstack(
#        rx.link(
    #         rx.box(
    #             rx.text("moure", as_="span", color=Color.PRIMARY.value),
    #             rx.text("dev", as_="span", color=Color.SECONDARY.value),
    #             style=styles.navbar_title_style
    #         ),
    #         href=Route.INDEX.value
    #     ),
    #     position="sticky",
    #     bg=Color.CONTENT.value,
    #     padding_x=Size.BIG.value,
    #     padding_y=Size.DEFAULT.value,
    #     z_index="999",
    #     top="0"
    # )

            # rx.mobile_and_tablet(
        #     rx.hstack(
        #         rx.hstack(
        #             rx.image(
        #                 src="/fylluicon.png",
        #                 width="2em",
        #                 height="auto",
        #                 border_radius="25%",
        #             ),
        #             rx.heading(
        #                 "Reflex", size="6", weight="bold"
        #             ),
        #             align_items="center",
        #         ),
        #         rx.menu.root(
        #             rx.menu.trigger(
        #                 rx.icon("menu", size=30)
        #             ),
        #             rx.menu.content(
        #                 rx.menu.item("Servicios"),
        #                 rx.menu.item("Portafolio"),
        #                 rx.menu.item("Precios"),
        #                 rx.menu.item("Preguntas frecuentes"),
        #                 rx.menu.separator("Clips"),
        #                 rx.menu.separator(),
        #                 rx.menu.item("Iniciar sesión"),
        #                 rx.menu.item("Comenzar prueba gratis"),
        #             ),
        #             justify="end",
        #         ),
        #         justify="between",
        #         align_items="center",
        #     ),
        # ),
        
    #)