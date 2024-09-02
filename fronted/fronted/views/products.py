def create_link(hover_style, text_color, link_text):
    """Create a hyperlink with custom hover and color styles."""
    return rx.el.a(
        link_text,
        href="#",
        _hover=hover_style,
        color=text_color,
    )


def create_list_item(hover_style, text_color, item_text):
    """Create a list item with a hyperlink inside."""
    return rx.el.li(
        create_link(
            hover_style=hover_style,
            text_color=text_color,
            link_text=item_text,
        )
    )


def create_styled_heading(
    heading_level, font_size, margin_bottom, heading_text
):
    """Create a styled heading with custom font size and margin."""
    return rx.heading(
        heading_text,
        font_weight="600",
        margin_bottom=margin_bottom,
        font_size=font_size,
        line_height="1.75rem",
        as_=heading_level,
    )


def create_search_input(placeholder_text):
    """Create a styled search input field with custom placeholder."""
    return rx.el.input(
        type="text",
        placeholder=placeholder_text,
        class_name="focus:ring-[#FF6B35]",
        border_width="1px",
        border_color="#D1D5DB",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
        },
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_top_left_radius="0.5rem",
        border_bottom_left_radius="0.5rem",
        width="100%",
    )


def create_icon(
    alt_text, icon_height, icon_name, icon_width
):
    """Create an icon with specified dimensions and alt text."""
    return rx.icon(
        alt=alt_text,
        tag=icon_name,
        height=icon_height,
        width=icon_width,
    )


def create_search_button():
    """Create a styled search button with a search icon."""
    return rx.el.button(
        create_icon(
            alt_text="Search",
            icon_height="1.25rem",
            icon_name="search",
            icon_width="1.25rem",
        ),
        class_name="bg-[#FF6B35] hover:bg-[#FF8C61]",
        transition_duration="300ms",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_top_right_radius="0.5rem",
        border_bottom_right_radius="0.5rem",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_search_bar(input_placeholder):
    """Create a search bar with input field and search button."""
    return rx.flex(
        create_search_input(
            placeholder_text=input_placeholder
        ),
        create_search_button(),
        display="flex",
        align_items="center",
    )


def create_search_section(
    section_title, search_placeholder
):
    """Create a search section with title and search bar."""
    return rx.box(
        create_styled_heading(
            heading_level="h2",
            font_size="1.25rem",
            margin_bottom="1rem",
            heading_text=section_title,
        ),
        create_search_bar(
            input_placeholder=search_placeholder
        ),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_section_heading(heading_text):
    """Create a styled section heading."""
    return rx.heading(
        heading_text,
        font_weight="700",
        margin_bottom="1.5rem",
        font_size="1.5rem",
        line_height="2rem",
        color="#1F2937",
        as_="h2",
    )


def create_card_image(alt_text, image_src):
    """Create an image for a card with specified source and alt text."""
    return rx.image(
        src=image_src,
        alt=alt_text,
        height="12rem",
        object_fit="cover",
        width="100%",
    )


def create_card_description(description_text):
    """Create a styled description text for a card."""
    return rx.text(
        description_text,
        margin_bottom="1rem",
        color="#4B5563",
    )


def create_learn_more_link():
    """Create a 'Learn More' link with custom styling."""
    return rx.el.a(
        "Learn More",
        href="#",
        class_name="text-[#FF6B35]",
        font_weight="600",
        _hover={"text-decoration": "underline"},
    )


def create_card_content(card_title, card_description):
    """Create the content section of a card with title and description."""
    return rx.box(
        create_styled_heading(
            heading_level="h3",
            font_size="1.25rem",
            margin_bottom="0.5rem",
            heading_text=card_title,
        ),
        create_card_description(
            description_text=card_description
        ),
        create_learn_more_link(),
        padding="1rem",
    )


def create_feature_card(
    image_alt, image_src, card_title, card_description
):
    """Create a feature card with image, title, and description."""
    return rx.box(
        create_card_image(
            alt_text=image_alt, image_src=image_src
        ),
        create_card_content(
            card_title=card_title,
            card_description=card_description,
        ),
        background_color="#ffffff",
        overflow="hidden",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_feature_icon(alt_text, icon_name):
    """Create a feature icon with specified alt text and icon name."""
    return rx.icon(
        alt=alt_text,
        tag=icon_name,
        height="3rem",
        margin_bottom="1rem",
        margin_left="auto",
        margin_right="auto",
        width="3rem",
    )


def create_colored_text(text_color, text_content):
    """Create text with a specified color."""
    return rx.text(text_content, color=text_color)


def create_feature_box(
    icon_alt, icon_name, feature_title, feature_description
):
    """Create a feature box with icon, title, and description."""
    return rx.box(
        create_feature_icon(
            alt_text=icon_alt, icon_name=icon_name
        ),
        create_styled_heading(
            heading_level="h3",
            font_size="1.25rem",
            margin_bottom="0.5rem",
            heading_text=feature_title,
        ),
        create_colored_text(
            text_color="#4B5563",
            text_content=feature_description,
        ),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        text_align="center",
    )


def create_social_link(icon_alt, icon_name):
    """Create a social media link with icon."""
    return rx.el.a(
        create_icon(
            alt_text=icon_alt,
            icon_height="1.5rem",
            icon_name=icon_name,
            icon_width="1.5rem",
        ),
        href="#",
        _hover={"color": "#ffffff"},
        color="#9CA3AF",
    )


def create_header():
    """Create the header section with logo and navigation links."""
    return rx.flex(
        rx.box(
            "RandIA",
            font_weight="700",
            font_size="1.5rem",
            line_height="2rem",
            color="#ffffff",
        ),
        rx.list(
            create_list_item(
                hover_style={"color": "#E5E7EB"},
                text_color="#ffffff",
                item_text="Home",
            ),
            create_list_item(
                hover_style={"color": "#E5E7EB"},
                text_color="#ffffff",
                item_text="Services",
            ),
            create_list_item(
                hover_style={"color": "#E5E7EB"},
                text_color="#ffffff",
                item_text="About",
            ),
            create_list_item(
                hover_style={"color": "#E5E7EB"},
                text_color="#ffffff",
                item_text="Contact",
            ),
            display="flex",
            column_gap="1.5rem",
        ),
        display="flex",
        align_items="center",
        justify_content="space-between",
    )


def create_header_container():
    """Create a container for the header with styling."""
    return rx.box(
        rx.box(
            create_header(),
            width="100%",
            style=rx.breakpoints(
                {
                    "640px": {"max-width": "640px"},
                    "768px": {"max-width": "768px"},
                    "1024px": {"max-width": "1024px"},
                    "1280px": {"max-width": "1280px"},
                    "1536px": {"max-width": "1536px"},
                }
            ),
            margin_left="auto",
            margin_right="auto",
            padding_left="1rem",
            padding_right="1rem",
        ),
        class_name="bg-[#FF6B35]",
        padding_top="1rem",
        padding_bottom="1rem",
    )


def create_main_content():
    """Create the main content section of the page."""
    return rx.box(
        rx.heading(
            "Find the Perfect Analytics Solution",
            font_weight="700",
            margin_bottom="2rem",
            font_size="2.25rem",
            line_height="2.5rem",
            text_align="center",
            color="#1F2937",
            as_="h1",
        ),
        rx.box(
            create_search_section(
                section_title="Search Analytics Services",
                search_placeholder="Search for analytics services...",
            ),
            create_search_section(
                section_title="Search by Data Solution Categories",
                search_placeholder="Search categories (e.g., Machine Learning)...",
            ),
            gap="1.5rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
                }
            ),
            margin_bottom="3rem",
        ),
        rx.box(
            create_section_heading(
                heading_text="Featured Analytics Services"
            ),
            rx.box(
                create_feature_card(
                    image_alt="Data Visualization Dashboard",
                    image_src="https://replicate.delivery/yhqm/J17lVUak2bpmCpxNcS5Vvh6d5oPXu6XJQG5RHKDCwzyYOM2E/out-0.webp",
                    card_title="Data Visualization Dashboard",
                    card_description="Create stunning interactive dashboards for your data.",
                ),
                create_feature_card(
                    image_alt="Predictive Analytics Engine",
                    image_src="https://replicate.delivery/yhqm/fdtO4hKjyw0MbKQUFmXn7S5fs2nIxT9IoMHCbT8n1zlk5wYTA/out-0.webp",
                    card_title="Predictive Analytics Engine",
                    card_description="Forecast trends and make data-driven decisions.",
                ),
                create_feature_card(
                    image_alt="Real-time Data Processing",
                    image_src="https://replicate.delivery/yhqm/wbb98v0rdS5mA9FJaeZy3wMpxTZpei4gMhCsJfsFveNNmDjNB/out-0.webp",
                    card_title="Real-time Data Processing",
                    card_description="Process and analyze data streams in real-time.",
                ),
                gap="1.5rem",
                display="grid",
                grid_template_columns=rx.breakpoints(
                    {
                        "0px": "repeat(1, minmax(0, 1fr))",
                        "768px": "repeat(3, minmax(0, 1fr))",
                    }
                ),
            ),
            margin_bottom="3rem",
        ),
        rx.box(
            create_section_heading(
                heading_text="Why Choose RandIA?"
            ),
            rx.box(
                create_feature_box(
                    icon_alt="Fast",
                    icon_name="zap",
                    feature_title="Lightning Fast",
                    feature_description="Get results quickly with our optimized algorithms.",
                ),
                create_feature_box(
                    icon_alt="Secure",
                    icon_name="shield",
                    feature_title="Secure & Reliable",
                    feature_description="Your data is protected with enterprise-grade security.",
                ),
                create_feature_box(
                    icon_alt="Collaborative",
                    icon_name="users",
                    feature_title="Collaborative",
                    feature_description="Work seamlessly with your team on analytics projects.",
                ),
                create_feature_box(
                    icon_alt="Scalable",
                    icon_name="trending-up",
                    feature_title="Scalable",
                    feature_description="Grow your analytics capabilities as your needs evolve.",
                ),
                gap="1.5rem",
                display="grid",
                grid_template_columns=rx.breakpoints(
                    {
                        "0px": "repeat(1, minmax(0, 1fr))",
                        "768px": "repeat(2, minmax(0, 1fr))",
                        "1024px": "repeat(4, minmax(0, 1fr))",
                    }
                ),
            ),
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="2rem",
        padding_bottom="2rem",
    )


def create_footer_content():
    """Create the content for the footer section."""
    return rx.box(
        rx.box(
            create_styled_heading(
                heading_level="h3",
                font_size="1.25rem",
                margin_bottom="1rem",
                heading_text="RandIA",
            ),
            create_colored_text(
                text_color="#9CA3AF",
                text_content="Your one-stop marketplace for analytics solutions.",
            ),
        ),
        rx.box(
            create_styled_heading(
                heading_level="h4",
                font_size="1.125rem",
                margin_bottom="1rem",
                heading_text="Quick Links",
            ),
            rx.list(
                create_list_item(
                    hover_style={"color": "#ffffff"},
                    text_color="#9CA3AF",
                    item_text="Home",
                ),
                create_list_item(
                    hover_style={"color": "#ffffff"},
                    text_color="#9CA3AF",
                    item_text="Services",
                ),
                create_list_item(
                    hover_style={"color": "#ffffff"},
                    text_color="#9CA3AF",
                    item_text="About Us",
                ),
                create_list_item(
                    hover_style={"color": "#ffffff"},
                    text_color="#9CA3AF",
                    item_text="Contact",
                ),
                display="flex",
                flex_direction="column",
                gap="0.5rem",
            ),
        ),
        rx.box(
            create_styled_heading(
                heading_level="h4",
                font_size="1.125rem",
                margin_bottom="1rem",
                heading_text="Legal",
            ),
            rx.list(
                create_list_item(
                    hover_style={"color": "#ffffff"},
                    text_color="#9CA3AF",
                    item_text="Terms of Service",
                ),
                create_list_item(
                    hover_style={"color": "#ffffff"},
                    text_color="#9CA3AF",
                    item_text="Privacy Policy",
                ),
                create_list_item(
                    hover_style={"color": "#ffffff"},
                    text_color="#9CA3AF",
                    item_text="Cookie Policy",
                ),
                display="flex",
                flex_direction="column",
                gap="0.5rem",
            ),
        ),
        rx.box(
            create_styled_heading(
                heading_level="h4",
                font_size="1.125rem",
                margin_bottom="1rem",
                heading_text="Connect With Us",
            ),
            rx.flex(
                create_social_link(
                    icon_alt="Facebook",
                    icon_name="facebook",
                ),
                create_social_link(
                    icon_alt="Twitter", icon_name="twitter"
                ),
                create_social_link(
                    icon_alt="LinkedIn",
                    icon_name="linkedin",
                ),
                display="flex",
                column_gap="1rem",
            ),
        ),
        gap="2rem",
        display="grid",
        grid_template_columns=rx.breakpoints(
            {
                "0px": "repeat(1, minmax(0, 1fr))",
                "768px": "repeat(4, minmax(0, 1fr))",
            }
        ),
    )


def create_footer():
    """Create the footer section with content and copyright notice."""
    return rx.box(
        create_footer_content(),
        rx.box(
            rx.text("© 2023 RandIA. All rights reserved."),
            border_color="#374151",
            border_top_width="1px",
            margin_top="2rem",
            padding_top="2rem",
            text_align="center",
            color="#9CA3AF",
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1rem",
        padding_right="1rem",
    )


def create_page_layout():
    """Create the overall page layout including header, main content, and footer."""
    return rx.box(
        create_header_container(),
        create_main_content(),
        rx.box(
            create_footer(),
            background_color="#1F2937",
            padding_top="2rem",
            padding_bottom="2rem",
            color="#ffffff",
        ),
        background_color="#F3F4F6",
        font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
    )


def create_app():
    """Create the main application with necessary styles and layout."""
    return rx.fragment(
        rx.el.link(
            href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
            rel="stylesheet",
        ),
        rx.el.style(
            """
        @font-face {
            font-family: 'LucideIcons';
            src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
        }
    """
        ),
        create_page_layout(),
    )