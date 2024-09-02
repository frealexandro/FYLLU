import reflex as rx
from fronted.components.prices import icon_price


class FormState(rx.State):
    email: str = ""

    def handle_submit(self, form_data: dict):
        self.email = form_data.get("email", "")


def email_form():
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder="Ingresa tu correo",
                type="email",
                name="email",
                style={
        "background_color": "white",
        "color": "black",
        "font_size": "16px",
        "& input::placeholder": {"color": "black"},
    }
            ),
            rx.button("Enviar", type="submit", bg="#0099ff", color="black", 
                      font_family="Comic Sans MS",transition= "background-color 300ms",
                      _hover={"background_color": "#FF00FF"}),
        ),
        on_submit=FormState.handle_submit,
    )



def cta_card():
    return rx.box(
        rx.vstack(
            rx.heading("¡Únete a nuestra lista de espera!", 
                       font_size="25px", color ="black", 
                       font_family="Comic Sans MS"),
                       
            rx.text("Actualmente estamos en beta privada, pero puedes unirte a nuestra lista de espera para ser el primero en enterarte cuando abramos nuestras puertas.", 
                    mb="6", color="black", font_family="Comic Sans MS"),
            
            email_form(),            
            
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






def benefit_card(title: str, descriptions: list, icon_price_value: bool = False):
    if icon_price_value:
        content = rx.box(
            *[icon_price("check", desc) for desc in descriptions[:3]]
        )
    else:
        content = rx.text(descriptions[0], color="black", font_family="Comic Sans MS")
    
    return rx.card(
        rx.heading(title, size="lg", font_weight="semibold", mb="2", color="black", font_family="Comic Sans MS"),
        content,
        width="100%",
        height="auto",
        bg="white",
        style={
            "padding": "10px",
            "borderRadius": "5px",
            "transition": "background-color 300ms",
            "_hover": {
                "border": "2px solid #0099ff",
            }
        }
    )

def benefits():
    return rx.box(
        rx.vstack(
            rx.heading("¡Empecemos a lo", font_size="46px", text_align="center",
                       margin_bottom="8", color="black", font_family="Comic Sans MS"),

            rx.heading("grande! con tu", font_size="46px", text_align="center",
                        margin_bottom="8", color="black", font_family="Comic Sans MS"),
            
            rx.heading("primer proyecto!", font_size="46px", text_align="center",
                        margin_bottom="30px", color="black", font_family="Comic Sans MS"),
            
            rx.text("Agendemos una 30-min call para conocernos, darte la bienvenida y ponernos en marcha con un primer pedido.", font_family="Comic Sans MS",color="black"),
            
            rx.grid(
                benefit_card("¿Qué haremos en nuestra primera reunión?",
                            ["Una llamada de descubrimiento para conocer más sobre tu proyecto.",
                             "Conocer cómo RandIA puede ayudarte a expandir tu equipo de analytics.",
                             "Crear una propuesta de valor personalizada para tu proyecto."
                             ],
                            icon_price_value=True),
                
                benefit_card("Sin compromisos, ni tarifas ocultas", 
                             ["¡La mejor forma de conocernos es probándonos! durante el free trial realizaremos por ti tu primer pedido, 100% gratis para ti."]),
                #benefit_card("Revisiones ilimitadas", "¿Cambios en el proyecto? ¡No hay problema! Seguiremos trabajando hasta que estés 100% satisfecho."),
                #benefit_card("Todo en una misma aplicación", "Haz tus pedidos, da feedback y recibe tus diseños en una misma aplicación intuitiva y súper ágil."),
                columns="1",
                spacing="4",
                width="100%",
                margin_top = "5",
            ),
            max_width="container.xl",
            px="4",
            py="8",
        ),
        margin_top="2.3em"
    )