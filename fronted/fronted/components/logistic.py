import reflex as rx



def icon_section(icon: str, title: str, description: str, bg_color: str, icon_color: str):
    return rx.vstack(
        rx.box(
            rx.icon(icon, size=48),
            bg=bg_color,
            p="4",
            border_radius="full",
            mb="4",
        ),
        rx.heading(title, size="xl", font_weight="bold", mb="2", font_family="Comic Sans MS"),
        rx.text(description, color="gray.600", font_family="Comic Sans MS"),
        align_items="center",
        text_align="center",
        max_width="sm",
        style={
            "border": "2px solid #0099ff",  # Borde azul
            "background_color" : "white",
            "padding": "10px",
            "borderRadius": "5px",
            "transition": "background-color 300ms",
        "_hover": {
            "border": "2px solid #FF00FF",
        },
        }
    )

def proces_product():
    return rx.box(
        rx.flex(
            rx.box(
                icon_section(
                    "alarm_clock_check",
                    "Crea un pedido",
                    "Completa un breve formulario con todos los detalles que tengas en mente para tu proyecto de analytics. ¡No te tomará más de 2 minutos!",
                    "purple.100",
                    "purple.600",
                ),
                margin="10px", 
            ),
            rx.box(
                icon_section(
                    "alarm_clock_check",
                    "Lo asignamos a nuestro equipo",
                    "Nuestro equipo seleccionará al mejor grupo de especialistas para tu proyecto, con un data director y un equipo dedicado.",
                    "green.100",
                    "green.600",
                ),
                margin="10px", 
            ),
            rx.box(
                icon_section(
                    "alarm_clock_check",
                    "Entregamos tus diseños",
                    "Recibe las primeras iteraciones de tus pedidos en tiempo récord, en un plazo aproximado de 24 a 72 horas dependiendo de la complejidad de cada pedido.",
                    "yellow.100",
                    "yellow.600",
                ),
                margin="10px", 
            ),
            justify="center",  # Centrar horizontalmente
            #align="center",  # Centrar verticalmente
            width="100%",  #
        ),
        bg="#FAFAFA",
        color="black",
        px="4",
        py="8",
        max_width="container.xl",
        mx="auto",
    )

