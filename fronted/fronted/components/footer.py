import reflex as rx

def AccordionItem(title: str, content: str):
    return rx.box(
        rx.box(
            rx.text(title, class_name="text-lg hover:no-underline cursor-pointer", on_click="toggleAccordion"),
            class_name="border-b border-gray-700 py-2 bg-black w-full",
        ),
        rx.box(
            rx.text(content, class_name="text-gray-300 py-2 bg-black w-full"),
            class_name="hidden accordion-content",
        ),
    )


def FAQAccordion():
    return rx.box(
        rx.heading("Preguntas Frecuentes", font_size="40px", weight="bold", mb="6",font_family="Comic Sans MS",padding_top="100px"),
        rx.heading("General", font_size="4xl", font_weight="bold", mb="6",padding_top="50px", font_family="Comic Sans MS"),
        rx.accordion.root(
            rx.accordion.item(
                header="¿Qué servicios de analítica están incluidos?",
                content="Nuestro servicio incluye una amplia gama de soluciones de analítica, desde pipelines de datos y modelos de machine learning hasta dashboards interactivos y automatización de flujos de trabajo. Todos los servicios son personalizables según las necesidades específicas de su negocio y los desafíos de datos que enfrente.",
            ),
            rx.accordion.item(
                header="¿Para cuantos pedidos alcanza mi suscripción?",
                content="Su suscripción le permite realizar pedidos ilimitados. Sin embargo, trabajamos en los pedidos de forma secuencial, por lo que el tiempo de entrega puede variar según la cantidad de pedidos en cola.",
            ),
            rx.accordion.item(
                header="¿En 48 a 72 horas? wow!",
                content="Sí, nos esforzamos por ofrecer un servicio rápido y eficiente. La mayoría de los diseños se completan en un plazo de 24 a 72 horas, dependiendo de la complejidad del proyecto y la carga de trabajo actual.",
            ),
            width="100%",
            type="multiple",
            color_scheme="blue",
        ),
        rx.heading("Nuestro equipo", font_size="4xl", font_weight="bold", mb="6",padding_top="50px", font_family="Comic Sans MS"),
        rx.accordion.root(
            rx.accordion.item(
                header="¿Quiénes son los data developers de RandIA?",
                content="Nuestro equipo de data developers está compuesto por profesionales altamente capacitados y con experiencia en una amplia gama de disciplinas, incluyendo ciencia de datos, ingeniería de software y análisis de negocios. Todos los miembros de nuestro equipo son seleccionados a través de un riguroso proceso de selección y entrenamiento para garantizar la más alta calidad en nuestros servicios.",
            ),
            rx.accordion.item(
                header="¿Cómo se asignan los proyectos a los data developers?",
                content="Los proyectos se asignan a los data developers en función de su experiencia y habilidades específicas. Trabajamos en estrecha colaboración con nuestros clientes para garantizar que los proyectos se asignen al miembro más adecuado de nuestro equipo.",
            ),
            rx.accordion.item(
                header="¿Qué sucede si no estoy satisfecho con el resultado final?",
                content="Nuestro objetivo es garantizar la satisfacción del cliente en todo momento. Si no está satisfecho con el resultado final, trabajaremos con usted para realizar las revisiones necesarias hasta que esté 100% satisfecho con el resultado.",
            ),
            width="100%",
            type="multiple",
            color_scheme="blue",
        ),
        background="black",
        color="white",
        p="6",
        width="100%",
        max_width="2xl",
        mx="auto",
        padding_bottom="100px",
        padding_left="50px",
        
        ),
        #rx.heading("Precios", font_size="4xl", font_weight="bold", mb="6",padding_top="50px", font_family="Comic Sans MS"),

# JavaScript to toggle accordion content visibility
toggleAccordionScript = """
document.querySelectorAll('.accordion-item').forEach(item => {
    item.querySelector('.text-lg').addEventListener('click', () => {
        const content = item.querySelector('.accordion-content');
        content.classList.toggle('hidden');
    });
});
"""

# Add the script to your HTML
rx.script(toggleAccordionScript)