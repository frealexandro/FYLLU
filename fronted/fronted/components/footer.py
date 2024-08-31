import reflex as rx

def AccordionItem(title: str, content: str):
    return rx.box(
        rx.box(
            rx.text(title, class_name="text-lg hover:no-underline cursor-pointer", on_click="toggleAccordion"),
            class_name="border-b border-gray-700 py-2"
        ),
        rx.box(
            rx.text(content, class_name="text-gray-300"),
            class_name="hidden accordion-content"
        ),
        class_name="accordion-item"
    )


def FAQAccordion():
    return rx.box(
        rx.heading("General", font_size="4xl", font_weight="bold", mb="6"),
        rx.accordion.root(
            rx.accordion.item(
                header="¿Qué diseños están incluidos?",
                content="Nuestro servicio incluye una amplia gama de diseños, desde logotipos y tarjetas de presentación hasta diseños web y materiales de marketing. Todos los diseños son personalizables según sus necesidades específicas.",
            ),
            rx.accordion.item(
                header="¿Para cuantos pedidos alcanza mi suscripción?",
                content="Su suscripción le permite realizar pedidos ilimitados. Sin embargo, trabajamos en los pedidos de forma secuencial, por lo que el tiempo de entrega puede variar según la cantidad de pedidos en cola.",
            ),
            rx.accordion.item(
                header="¿En 24 a 72 horas? wow!",
                content="Sí, nos esforzamos por ofrecer un servicio rápido y eficiente. La mayoría de los diseños se completan en un plazo de 24 a 72 horas, dependiendo de la complejidad del proyecto y la carga de trabajo actual.",
            ),
            width="100%",
            type="multiple",
        ),
        bg="#0f0f0f",
        color="white",
        p="6",
        max_width="2xl",
        mx="auto",
    )

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