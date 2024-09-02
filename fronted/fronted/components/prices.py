import reflex as rx
from fronted.routes import Route



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




def price_component(price:str):
    return rx.box(
        rx.box(
            rx.text("USD", class_name="absolute -top-3 right-40 text-2xl font-sans"),
            rx.text(price, class_name="relative text-SM font-sans"),
            class_name="relative",
        ),
        rx.text("/mes", class_name="text-2xl font-normal ml-20 font-sans"),
        class_name="font-bold text-5xl tracking-tighter font-sans",
    )



def icon_price(icon: str, text: str):
    return rx.flex(
        rx.icon(icon, size=25, color="#0099ff"),
        rx.text(text, font_family="Comic Sans MS",color="black"),
        direction="row",
        gap="1",
        aling="center",
    )



def content_card(title: str, credits_text: str, price: str , condition_1: str, 
                 condition_2: str, condition_3: str, professional_1: str , professional_2: str, type_sopport: str):
    return rx.vstack(
        rx.heading(title, size="10", font_family="Comic Sans MS", mb="2", text_align="center", color="#0099ff"),
        price_component(price=price),
        rx.heading("QUÉ ESTÁ INCLUIDO" , font_family="Comic Sans MS", text_align="center" ,mb="2",size="2", color="#0099ff"),
        icon_price("circle_check_big", credits_text),
        icon_price("dot", condition_1),
        icon_price("dot", condition_2),
        icon_price("dot", condition_3),
        rx.heading("UN EQUIPO COMPUESTO POR" , font_family="Comic Sans MS", text_align="center" ,mb="2",size="2", color="#0099ff"),
        rx.text (professional_1, font_family="Comic Sans MS"),
        rx.text (professional_2, font_family="Comic Sans MS"),
        rx.text(type_sopport, font_family="Comic Sans MS"),
        rx.button("Comenzar prueba gratis", style=styles["button"],on_click=rx.redirect(Route.FUNNEL.value),
                    external=True,),
                    

        
        
        
        align_items="center",
        text_align="center",
        max_width="sm",
        style={
            "width": "300px",  # Establece un ancho fijo para el contenedor
            "max_width": "300px",
            #establece un alto fijo para el contenedor
            "height": "580px",
            "border": "2px solid #0099ff",  # Borde azul
            "background_color": "white",
            "padding": "10px",
            "borderRadius": "5px",
            # "transition": "background-color 300ms",
            # "_hover": {
            #     "border": "2px solid #FF00FF",
            # },
        }
    )

def pricing_final():
    return rx.box(
        rx.flex(
            rx.box(
                content_card(
                    "Básico",
                    "50 créditos por mes",
                    "550",
                    "1 Proyecto activo a la vez",
                    "Flujos de automatización básicos",
                    "Dashboards interactivos predefinidos",
                    "1 Project Manager",
                    "1 Data Director",
                    "Equipo de data dedicado"



                ),
                margin_left="200px",
                
            ),
            rx.box(
                content_card(
                    "Profesional",
                    "70 créditos por mes",
                    "$750",
                    "2 Proyecto activo a la vez",
                    "Modelos de IA predefinidos",
                    "Flujos de automatización avanzados",
                    "1 Project Manager",
                    "1 Data Director",
                    "Equipo de data dedicado"
                ),
                margin="1px", 
            ),
            rx.box(
                content_card(
                    "Empresarial",
                    "100 créditos por mes",
                    "$1090",
                    "3 Proyecto activo a la vez",
                    "Modelos de IA personalizados",
                    "Arquitectura de datos personalizada",
                    "1 Project Manager",
                    "1 Data Director",
                    "Equipo de data dedicado"
                ),
                margin_right="200px", 

            ),
            justify="center",  # Centrar horizontalmente
            #align="center",  # Centrar verticalmente
            width="100%",  #
        ),
        
        color="black",
        px="4",
        py="8",
        max_width="container.xl",
        mx="auto",
        margin_top="100px",
    )


def title_prices():
    return rx.box(
        rx.heading(
            "Un equipo de datadevelopers a tu disposición",
            font_size="40px",
            margin_bottom="1rem",
            color="black",
            font_family="Comic Sans MS",
            text_align="center",  # Center the text
        ),
        rx.heading(
            "por una fracción de costo",
            font_size="40px",
            margin_bottom="5rem",
            color="black",
            font_family="Comic Sans MS",
            text_align="center"  # Center the text
        ),
        rx.text.strong(
            "Selecciona la cantidad de créditos mensuales según las necesidades analyticas de tu",
            font_size="20px",
            color="black",
            font_family="Comic Sans MS",
            text_align="center"  # Center the text
        ),
        rx.text.strong(
            "equipo. ¡No te preocupes! los créditos no utilizados se acumulan para que no se",
            font_size="20px",
            color="black",
            font_family="Comic Sans MS",
            text_align="center"  # Center the text
        ),
        rx.text.strong(
            "desperdicie ningún dólar.",
            font_size="20px",
            color="black",
            font_family="Comic Sans MS",
            text_align="center"  # Center the text
        ),
        justify="center",
        align_items="center",  # Center the items vertically
        text_align="center",  # Center the text horizontally
        style={
            "display": "flex",
            "flex_direction": "column",
            "width": "100%",  # Ensure the box takes the full width
        }
    )