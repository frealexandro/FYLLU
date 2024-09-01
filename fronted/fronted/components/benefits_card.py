import reflex as rx


#font_family="Comic Sans MS"

def cta_card():
    return rx.box(
        rx.vstack(
            rx.heading("¡Desbloquea tu operación de analitycs ahora!", size="2xl", font_weight="bold", mb="4", color ="black", font_family="Comic Sans MS"),
            rx.text("Descubre cómo RandIA puede integrarse perfectamente en tus procesos, potenciando tu creatividad y aliviando tu carga de trabajo.", mb="6", color="black", font_family="Comic Sans MS"),
            
            rx.button("Ver planes", bg="#0099ff", color="black",  transition = "background-color 300ms",_hover={"bg": "#FF00FF"}),
            align_items="start",
            z_index="10",
            
        ),

        #mascot
        #rx.image(src="/placeholder.svg?height=200&width=200", alt="Grayola mascot", position="absolute", bottom="0", right="0", w="50%", h="50%", object_fit="contain"),
        bg="#FFBE76",
        p="6",
        border_radius="5px",
        position="relative",
        overflow="hidden",
        padding="115px",
        transition= "background-color 300ms",
        _hover={"border": "2px solid #0099ff"},
        font_family="Comic Sans MS",
    )

def benefit_card(title: str, description: str):
    return rx.card(
        rx.heading(title, size="lg", font_weight="semibold", mb="2", color="black", font_family="Comic Sans MS"),
        rx.text(description, color="black", font_family="Comic Sans MS"),
        width="100%",
        height="auto",
        p="4",
        bg="white",
        style={
             # Borde transparente
            "padding": "10px",
            "borderRadius": "5px",
             "transition": "background-color 300ms",
        "_hover": {
            "border": "2px solid #0099ff",}}
    )

def benefits():
    return rx.box(
        rx.vstack(
            rx.heading("BENEFICIOS DE USAR RANDIA", size="4xl", text_align="center", mb="8", color="black", font_family="Comic Sans MS"),
            rx.grid(
                benefit_card("Desarrollo de ultra alta calidad", "Contratamos a los mejores data developers de latinoamérica para trabajar en tus proyectos."),
                benefit_card("Entregas ultrarrápidas", "Entregamos tus diseños en tiempo récord y con tu feedback iteramos lo más rápido posible."),
                benefit_card("Revisiones ilimitadas", "¿Cambios en el proyecto? ¡No hay problema! Seguiremos trabajando hasta que estés 100% satisfecho."),
                benefit_card("Todo en una misma aplicación", "Haz tus pedidos, da feedback y recibe tus diseños en una misma aplicación intuitiva y súper ágil."),
                columns="2",
                spacing="4",
                width="100%",
            ),
            max_width="container.xl",
            mx="auto",
            px="4",
            py="8",
        ),
        margin_top="5em"
    )