import reflex as rx
import fronted.styles.styles as styles
from fronted.styles.styles import Size
from fronted.styles.colors import Color , TextColor









styles = {
    "button": {
        "background_color": "#0099ff",
        "color": "black",
        "font_weight": "italic",
        "padding": "1.2rem 0.6rem",
        "size" : "3",
        "font_size": "1.125rem",
        "font_family":"Comic Sans MS",
        "transition": "background-color 300ms",
        "_hover": {
            "background_color": "#FF00FF",
        },},}






def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium",color=Color.PRIMARY.value,font_family="Comic Sans MS"), href=url
    )

def service_item(icon: str, title: str, description: str) -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.text(icon, font_size="2em", margin_right="0.5em",font_family="Comic Sans MS"),
            rx.heading(title, size="xs",font_family="Comic Sans MS"),
            margin_bottom="0.5em",
        ),
        rx.text(description, font_size="xs", color="black",font_family="Comic Sans MS"),
        direction="column",
    )



def navbar_dropdown() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/RandIA-negro-logo.png",
                        width="3em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "RandIA", size="7", weight="bold" , color=Color.PRIMARY.value, font_family="Comic Sans MS"
                        
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
                                    font_family="Comic Sans MS",
                                ),
                                rx.icon("chevron-down"),
                                weight="medium",
                                variant="ghost",
                                size="3",
                                color=Color.PRIMARY.value,
                                

                            ),
                        ),
                        rx.menu.content(
                        rx.heading("Servicios", size="x0.5", margin_bottom="1em",bg = "#FFFFFF", color="black", font_family="Comic Sans MS"),
                        rx.grid(
                            service_item("📊", "Dashboards Interactivos", "Visualizaciones de datos personalizadas y en tiempo real para una toma de decisiones ágil"),
                            service_item("🔍", "Análisis Predictivo", "Modelos de machine learning para prever tendencias y comportamientos futuros"),
                            service_item("🔄", "Automatización de Procesos", "Flujos de trabajo automatizados para optimizar operaciones y reducir errores"),
                            service_item("📈", "Análisis de Rendimiento", "Métricas clave y KPIs personalizados para evaluar y mejorar el desempeño del negocio"),
                            service_item("🕸️", "Web Scraping Avanzado", "Recolección y procesamiento de datos web para obtener insights del mercado"),
                            service_item("🧠", "Integración GEN-AI", "Implementación de IA generativa para análisis avanzado de datos y automatización inteligente de flujos de trabajo"),
                            service_item("📱", "Analítica Móvil", "Seguimiento y análisis de comportamiento de usuarios en aplicaciones móviles"),
                            service_item("🔗", "Integración de Datos", "Unificación de fuentes de datos dispares para una visión holística del negocio"),
                            service_item("🛒", "Análisis de Conversión", "Optimización del embudo de ventas mediante análisis detallado del comportamiento del cliente"),
                            columns="3",
                            spacing="3",
                            color = "black",
                            bg = "#FFFFFF",
                            border_style="solid",
                            border_color="#FAD6A5",
                        ),
                        width="800px",
                        padding="1.5em",
                        color=Color.PRIMARY.value,
                        bg = "#FFFFFF",
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
                        font_family="Comic Sans MS"
                    ),
                    rx.button("Comenzar prueba gratis", style=styles["button"]),
                    spacing="6",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        bg= "#FFBE76",
        padding="1em",
        width="100%",
        ),)



