import reflex as rx

config = rx.Config(
    app_name="Adogontour Service",
    favicon="/favicon.ico",  # Percorso relativo alla cartella assets
)


def mobile_nav_link(label: str, href: str):
    return rx.link(
        label,
        href=href,
        width="100%",
        padding="0.75rem",
        text_align="left",
        color_scheme="gray",
        class_name="mobile-menu-link",
    )

def header_section():
    return rx.box(
        rx.box(
            rx.hstack(
                # Blocco di sinistra
                rx.hstack(
                    rx.link("Servizi", href="/servizi", color_scheme="gray"),
                    rx.link("Chi Siamo", href="/chi-siamo", color_scheme="gray"),
                    spacing="5",
                    justify="end",
                    flex="1",
                ),

                # Logo Centrale
                rx.center(
                    rx.link(
                        rx.image(src="/logo.png", height="60px", width="auto"),
                        href="/",
                    ),
                    padding_x="2rem",
                ),

                # Blocco di destra
                rx.hstack(
                    # Link adiacenti al logo
                    rx.hstack(
                        rx.link("Noleggio", href="/noleggio", color_scheme="gray"),
                        rx.link("Contatti", href="/contatti", color_scheme="gray"),
                        spacing="5",
                    ),

                    # La "molla" che spinge il tasto successivo tutto a destra
                    rx.spacer(),

                    # Tasto Area Riservata
                    rx.link(
                        rx.button(
                            "Area Riservata",
                            variant="surface",
                            radius="full",
                            color_scheme="gray",
                            on_click=rx.redirect("https://adogontour-service.streamlit.app", is_external=True),
                        ),
                    ),
                    align_items="center",
                    flex="1",
                ),
                width="100%",
                align_items="center",
            ),
            display=rx.breakpoints(initial="none", md="block"),
            width="100%",
        ),
        rx.box(
            rx.hstack(
                rx.link(
                    rx.image(
                        src="/logo.png",
                        height=rx.breakpoints(initial="48px", sm="56px"),
                        width="auto",
                    ),
                    href="/",
                    aria_label="Adogontour Service - Home",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.button(
                            "Menu",
                            variant="ghost",
                            radius="full",
                            aria_label="Apri o chiudi menu",
                            class_name="mobile-menu-trigger",
                        )
                    ),
                    rx.menu.content(
                        rx.vstack(
                            mobile_nav_link("Servizi", "/servizi"),
                            mobile_nav_link("Chi Siamo", "/chi-siamo"),
                            mobile_nav_link("Noleggio", "/noleggio"),
                            mobile_nav_link("Contatti", "/contatti"),
                            rx.link(
                                "Area Riservata",
                                href="https://adogontour-service.streamlit.app",
                                is_external=True,
                                width="100%",
                                padding="0.75rem",
                                text_align="center",
                                color_scheme="gray",
                                background_color="var(--accent-3)",
                                border_radius="0.75rem",
                            ),
                            spacing="1",
                            align_items="stretch",
                            width="100%",
                        ),
                        padding="0.75rem",
                        background_color="rgba(0, 0, 0, 0.96)",
                        border="1px solid var(--gray-5)",
                        border_radius="1rem",
                        box_shadow="0 12px 30px rgba(0, 0, 0, 0.35)",
                        side="bottom",
                        align="end",
                        side_offset=8,
                        width="min(calc(100vw - 2rem), 24rem)",
                        class_name="mobile-menu-panel",
                    ),
                    modal=False,
                ),
                width="100%",
                align_items="center",
                justify="between",
            ),
            display=rx.breakpoints(initial="block", md="none"),
            width="100%",
        ),
        width="100%",
        padding=rx.breakpoints(initial="0.75rem 1rem", md="1rem 2rem"),
        background_color="rgba(0, 0, 0, 0.8)",
        backdrop_filter="blur(10px)",
        position="sticky",
        height=rx.breakpoints(initial="auto", md="10vh"),
        top="0",
        z_index="100",
        border_bottom="1px solid var(--gray-5)",
    )

def info_card(title: str, description: str, icon: str, link: str):
    return rx.card(
        rx.vstack(
            rx.icon(icon, size=40, color="var(--accent-9)"),
            rx.heading(title, size="5"),
            rx.text(description, color_scheme="gray"),
            spacing="3",
            align_items="start",
        ),
        #_hover={"transform": "translateY(-20px)","box_shadow": "0 20px 15px rgba(0,0,0,0.3)","background_color": "#000000",},
        #on_click=rx.redirect(link),
        width="100%",
        max_width="350px",
        class_name="hero-card",
        transition="transform 0.25s ease, box-shadow 0.25s ease",
        _hover={"transform": "translateY(-5px)", "box_shadow": "0 16px 36px rgba(0,0,0,0.28)"},
    )

def hero_section():
    return rx.box(
        rx.vstack(
            # Puoi valutare di rimuovere o rimpicciolire questa immagine se preferisci averla solo nell'header
            rx.heading(
                "Adogontour Service",
                size=rx.breakpoints(initial="7", md="9"),
                weight="bold",
                class_name="hero-title",
            ),
            rx.text(
                "Audio • Luci • Multimedia - Live • Conferenze • Corporate",
                size=rx.breakpoints(initial="3", md="5"),
                color_scheme="gray",
                class_name="hero-subtitle",
            ),
            rx.button(
                "Scopri di più",
                size=rx.breakpoints(initial="3", md="4"),
                radius="full",
                on_click=rx.redirect("/chi-siamo"),
            ),
            rx.spacer("\n\n"),
            rx.markdown("___"),
            rx.flex(
                info_card(
                    "Service Audio & Luci", 
                    "Fornitura, allestimento e gestione di impianti audio e luci per concerti, festival ed eventi dal vivo.", 
                    "speaker",
                    "/servizi"
                ),
                info_card(
                    "Progettazione e Rendering", 
                    ("Progettiamo tutti i sistemi necessari, creando disegni tecnici e rendering 3D (in collaborazione con ", rx.link("Scenic Vision Studio", href="http://scenicvisionstudio.it", is_external=True), ")."), 
                    "ruler",
                    "/servizi"
                ),
                info_card(
                    "Noleggio", 
                    "Noleggio di attrezzature audio e luci professionali per i tuoi eventi. ", 
                    "warehouse",
                    "servizi"
                ),
                spacing="5",
                flex_wrap="wrap",
                justify_content="center",
                width="100%",
            ),
            rx.button(
                "I nostri servizi",
                size=rx.breakpoints(initial="3", md="4"),
                radius="full",
                on_click=rx.redirect("/servizi"),
            ),
            spacing="5",
            align_items="center",
        ),
        padding=rx.breakpoints(initial="4rem 1rem 3rem", md="8rem 2rem"),
        # A sleek dark gradient background for the hero
        background_image="linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('/hero-bg.jpeg')",
        background_size="cover",
        background_position="center",
        background_repeat="no-repeat",
        width="100%",
        height=rx.breakpoints(initial="auto", md="90vh"),
        text_align="center",
    )

def service_detail_block(title: str, description: rx.Component | str, icon: str, reverse: bool = False):
    # La parte di testo
    content = rx.vstack(
        rx.heading(
            title,
            size=rx.breakpoints(initial="5", md="7"),
            color="var(--accent-11)",
        ),
        rx.text(
            description,
            size=rx.breakpoints(initial="3", md="5"),
            color_scheme="gray",
            line_height="1.6",
        ),
        spacing="4",
        align_items="start",
        flex="1",
    )
    
    # La parte visiva (un box con l'icona)
    visual = rx.center(
        rx.icon(icon, size=100, color="var(--accent-9)"),
        background="var(--gray-3)",
        border_radius="1rem",
        padding=rx.breakpoints(initial="2rem", md="3rem"),
        flex="1",
        min_width=rx.breakpoints(initial="0", md="250px"),
        width="100%",
        box_shadow="0 10px 30px rgba(0,0,0,0.3)",
    )
    
    # Layout responsivo usando il dizionario per i breakpoints
    desktop_direction = "row" if not reverse else "row-reverse"
    
    return rx.flex(
        content,
        visual,
        direction={
            "initial": "column",    # Su smartphone (schermi piccoli): impila verticalmente
            "md": desktop_direction # Su tablet/desktop (schermi medi/grandi): affianca
        },
        spacing="7",
        align_items="center",
        width="100%",
        padding_y=rx.breakpoints(initial="3rem", md="4rem"),
        border_bottom="1px solid var(--gray-4)",
        class_name="content-enter",
    )

@rx.page(title="Adogontour Service - Home")
def index():
    return rx.vstack(
        header_section(), # <-- Header inserito in cima
        hero_section(),
        spacing="0",
        width="100%",
    )

@rx.page(route="/contatti", title="Adogontour Service - Contatti")
def contatti():
    return rx.vstack(
        header_section(),
        
        # Hero section per Contatti
        rx.box(
            rx.vstack(
                rx.heading(
                    "Contatti",
                    size=rx.breakpoints(initial="7", md="9"),
                    weight="bold",
                    class_name="hero-title",
                ),
                rx.text(
                    "Siamo a disposizione per informazioni, preventivi e supporto tecnico.", 
                    size=rx.breakpoints(initial="4", md="6"),
                    color_scheme="gray", 
                    text_align="center", 
                    max_width="700px",
                    class_name="hero-subtitle",
                ),
                align_items="center",
                spacing="4",
            ),
            padding_y=rx.breakpoints(initial="3.5rem", md="6rem"),
            width="100%",
            background_image="linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url('/fari-magazzino.jpeg')",
            background_position="50% 30%",
            background_size="cover",
            border_bottom="1px solid var(--gray-5)",
            class_name="page-hero",
        ),
        
        # Contenitore principale delle informazioni di contatto
        rx.box(
            rx.flex(
                # Email Card
                rx.card(
                    rx.vstack(
                        rx.icon("mail", size=50, color="var(--accent-9)"),
                        rx.heading("Email", size=rx.breakpoints(initial="5", md="6")),
                        rx.text("Scrivici per richiedere un preventivo o per dettagli sui nostri servizi.", color_scheme="gray", text_align="center"),
                        rx.link(
                            "service@adogontour.it", 
                            href="mailto:service@adogontour.it", 
                            color="var(--accent-11)", 
                            weight="bold", 
                            size=rx.breakpoints(initial="4", md="5")
                        ),
                        align_items="center",
                        spacing="4",
                        padding=rx.breakpoints(initial="1.5rem", md="2rem"),
                    ),
                    width="100%",
                    max_width="400px",
                    box_shadow="0 10px 30px rgba(0,0,0,0.2)",
                    _hover={"transform": "translateY(-5px)", "transition": "transform 0.3s ease"},
                ),
                
                # Telefono Card
                rx.card(
                    rx.vstack(
                        rx.icon("phone", size=50, color="var(--accent-9)"),
                        rx.heading("Telefono", size=rx.breakpoints(initial="5", md="6")),
                        rx.text("Chiamaci per urgenze o per parlare direttamente con un nostro responsabile.", color_scheme="gray", text_align="center"),
                        rx.link(
                            "+39 366 817 1000",  # Inserisci qui il numero reale
                            href="tel:+393668171000", 
                            color="var(--accent-11)", 
                            weight="bold", 
                            size=rx.breakpoints(initial="4", md="5")
                        ),
                        align_items="center",
                        spacing="4",
                        padding=rx.breakpoints(initial="1.5rem", md="2rem"),
                    ),
                    width="100%",
                    max_width="400px",
                    box_shadow="0 10px 30px rgba(0,0,0,0.2)",
                    _hover={"transform": "translateY(-5px)", "transition": "transform 0.3s ease"},
                ),
                
                direction=rx.breakpoints(initial="column", md="row"),
                spacing=rx.breakpoints(initial="5", md="8"),
                justify="center",
                align_items="center",
                width="100%",
                padding_y=rx.breakpoints(initial="3rem", md="5rem"),
            ),
            width="100%",
            max_width="1000px",
            margin="0 auto",
            padding_x=rx.breakpoints(initial="1.25rem", sm="2rem", md="0"),
        ),

        spacing="0",
        width="100%",
        min_height="100vh",
    )

@rx.page(route="/chi-siamo", title="Adogontour Service - Chi Siamo")
def chi_siamo():
    return rx.vstack(
        header_section(),
        
        # Hero section per Chi Siamo
        rx.box(
            rx.vstack(
                rx.heading(
                    "Chi Siamo",
                    size=rx.breakpoints(initial="7", md="9"),
                    weight="bold",
                    class_name="hero-title",
                ),
                rx.text(
                    "Venti anni nel settore degli eventi live, scopri chi siamo.", 
                    size=rx.breakpoints(initial="4", md="6"),
                    color_scheme="gray", 
                    text_align="center", 
                    max_width="700px",
                    class_name="hero-subtitle",
                ),
                align_items="center",
                spacing="4",
            ),
            padding_y=rx.breakpoints(initial="3.5rem", md="6rem"),
            width="100%",
            background_image="linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url('/about-bg.jpeg')",
            background_position="50% 30%",
            background_size="cover",
            border_bottom="1px solid var(--gray-5)",
            class_name="page-hero",
        ),

        # Contenitore principale dei contenuti
        rx.box(
            rx.vstack(
                # Blocco 1: Le Radici e gli Eventi
                rx.flex(
                    rx.vstack(
                        rx.heading("Le Nostre Radici", size=rx.breakpoints(initial="5", md="7"), color="var(--accent-11)"),
                        rx.text("Adogontour Service nasce nel 2007 a Cuneo. Nel corso degli anni si afferma come punto di riferimento per la fornitura tecnica nella provincia e non solo.", size=rx.breakpoints(initial="3", md="5"), color_scheme="gray", line_height="1.6"),
                        rx.text("Dai numerosi eventi sul territorio, fino al supporto di rassegne come Ted X Cuneo, la nostra esperienza sul campo ci permette di affrontare e risolvere ogni tipo di sfida tecnica.", size=rx.breakpoints(initial="3", md="5"), color_scheme="gray", line_height="1.6"),
                        spacing="4",
                        align_items="start",
                        flex="1",
                    ),
                    rx.center(
                        rx.icon("history", size=100, color="var(--accent-9)"),
                        background="var(--gray-3)",
                        border_radius="1rem",
                        padding=rx.breakpoints(initial="2rem", md="3rem"),
                        flex="1",
                        min_width=rx.breakpoints(initial="0", md="250px"),
                        width="100%",
                        box_shadow="0 10px 30px rgba(0,0,0,0.3)",
                    ),
                    direction=rx.breakpoints(initial="column", md="row"),
                    spacing="7",
                    align_items="center",
                    width="100%",
                    padding_y=rx.breakpoints(initial="3rem", md="4rem"),
                    border_bottom="1px solid var(--gray-4)",
                ),

                # Blocco 2: L'Evoluzione Logistica e Tecnica (Il tuo apporto)
                rx.flex(
                    rx.center(
                        rx.icon("rocket", size=100, color="var(--accent-9)"),
                        background="var(--gray-3)",
                        border_radius="1rem",
                        padding=rx.breakpoints(initial="2rem", md="3rem"),
                        flex="1",
                        min_width=rx.breakpoints(initial="0", md="250px"),
                        width="100%",
                        box_shadow="0 10px 30px rgba(0,0,0,0.3)",
                    ),
                    rx.vstack(
                        rx.heading("Evoluzione e Innovazione", size=rx.breakpoints(initial="5", md="7"), color="var(--accent-11)"),
                        rx.text("Oggi, pur mantenendo le proprie radici, Adogontour è un service che punta alla massima efficienza attraverso la tecnologia e un approccio analitico ai flussi di lavoro.", size=rx.breakpoints(initial="3", md="5"), color_scheme="gray", line_height="1.6"),
                        rx.text("Gestiamo l'intera catena logistica con strumenti digitali proprietari per ottimizzare l'inventario e la gestione del magazzino.", size=rx.breakpoints(initial="3", md="5"), color_scheme="gray", line_height="1.6"),
                        rx.text("Lavoriamo con standard industriali e console digitali di altissimo livello (DiGiCo, Chamsys, HK Audio) per garantire sempre stabilità e scalabilità in ogni produzione.", size=rx.breakpoints(initial="3", md="5"), color_scheme="gray", line_height="1.6"),
                        spacing="4",
                        align_items="start",
                        flex="1",
                    ),
                    direction=rx.breakpoints(initial="column", md="row-reverse"),
                    spacing="7",
                    align_items="center",
                    width="100%",
                    padding_y=rx.breakpoints(initial="3rem", md="4rem"),
                ),

                width="100%",
                max_width="1100px",
                margin="0 auto",
                padding_x=rx.breakpoints(initial="1.25rem", sm="2rem", md="0"),
            ),
            width="100%",
        ),

        # Call to Action finale
        rx.box(
            rx.vstack(
                rx.heading("Affidati alla nostra esperienza", size=rx.breakpoints(initial="5", md="7")),
                rx.text("Decenni di storia uniti alle tecnologie più avanzate per il tuo evento.", size=rx.breakpoints(initial="3", md="5"), color_scheme="gray"),
                rx.button("Richiedi disponibilità", size=rx.breakpoints(initial="3", md="4"), radius="full", margin_top="1rem", on_click=rx.redirect("/contatti")),
                align_items="center",
                spacing="4"
            ),
            padding_y=rx.breakpoints(initial="3.5rem", md="6rem"),
            width="100%",
            text_align="center",
            background="var(--gray-2)", 
        ),
        
        spacing="0",
        width="100%",
        min_height="100vh",
    )

@rx.page(route="/servizi", title="Servizi - Adogontour")
def servizi():
    return rx.vstack(
        header_section(),
        
        # Hero section specifica per i servizi
        rx.box(
            rx.vstack(
                rx.heading(
                    "I Nostri Servizi",
                    size=rx.breakpoints(initial="7", md="9"),
                    weight="bold",
                    class_name="hero-title",
                ),
                rx.text(
                    "Soluzioni tecniche complete per eventi dal vivo, dalla pre-produzione alla realizzazione in loco.", 
                    size=rx.breakpoints(initial="4", md="6"),
                    color_scheme="gray", 
                    text_align="center", 
                    max_width="700px",
                    class_name="hero-subtitle",
                ),
                align_items="center",
                spacing="4",
            ),
            padding_y=rx.breakpoints(initial="3.5rem", md="6rem"),
            width="100%",
            background_image="linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url('/services-bg.jpeg')",
            background_position="50% 70%",
            background_size="cover",
            border_bottom="1px solid var(--gray-5)",
            class_name="page-hero",
        ),

        # Contenitore principale dei servizi
        rx.box(
            rx.vstack(
                service_detail_block(
                    title="Service Audio & Luci",
                    description="Offriamo servizi completi di fornitura, allestimento e gestione di impianti audio e luci. Che si tratti di un concerto live, di un festival o di un evento corporate, garantiamo la massima qualità sonora e un impatto visivo straordinario grazie a personale qualificato e attrezzature professionali.",
                    icon="speaker",
                    reverse=False
                ),
                service_detail_block(
                    title="Progettazione e Rendering",
                    description=rx.fragment(
                        "La fase preparatoria è fondamentale. Progettiamo nel dettaglio tutti i sistemi necessari, realizzando disegni tecnici accurati e rendering 3D per previsualizzare il palco e ottimizzare le risorse. Operiamo in stretta collaborazione con ",
                        rx.link("Scenic Vision Studio", href="http://scenicvisionstudio.it", is_external=True, color="var(--accent-9)", weight="bold", underline="always"),
                        "."
                    ),
                    icon="ruler",
                    reverse=True
                ),
                service_detail_block(
                    title="Noleggio Attrezzature",
                    description="Mettiamo a disposizione i nostri materiali per il noleggio a breve e lungo termine. Disponiamo di tecnologie audio e luci revisionate e pronte all'uso, ideali per supportare professionisti del settore, band e organizzatori che necessitano di materiale affidabile.",
                    icon="warehouse",
                    reverse=False
                ),
                width="100%",
                max_width="1100px", # Mantiene i contenuti ben centrati e leggibili
                margin="0 auto",
                padding_x=rx.breakpoints(initial="1.25rem", sm="2rem", md="0"),
            ),
            width="100%",
        ),

        # Call to Action finale
        rx.box(
            rx.vstack(
                rx.heading("Hai un progetto in mente?", size=rx.breakpoints(initial="5", md="7")),
                rx.text("Contattaci per discutere le tue necessità tecniche e richiedere un preventivo.", size=rx.breakpoints(initial="3", md="5"), color_scheme="gray"),
                rx.button("Richiedi un Preventivo", size=rx.breakpoints(initial="3", md="4"), radius="full", margin_top="1rem", on_click=rx.redirect("/contatti")),
                align_items="center",
                spacing="4"
            ),
            padding_y=rx.breakpoints(initial="3.5rem", md="6rem"),
            width="100%",
            text_align="center",
            background="var(--gray-2)", # Sfondo leggermente staccato dal nero puro
        ),
        
        spacing="0",
        width="100%",
        min_height="100vh",
    )

@rx.page(route="/noleggio", title="Adogontour Service - Noleggio")
def noleggio():
    return rx.vstack(
        header_section(),
        rx.text("Pagina in costruzione")
    )

@rx.page(route="/404", title="404 - Pagina Non Trovata")
def custom_404():
    return rx.vstack(
        header_section(),
        
        # 404 Content
        rx.box(
            rx.vstack(
                rx.image("/logo.png", height=rx.breakpoints(initial="180px", md="250px")),
                rx.heading("404", size=rx.breakpoints(initial="8", md="9"), weight="bold", color="var(--accent-11)"),
                rx.heading("Pagina Non Trovata", size=rx.breakpoints(initial="5", md="7")),
                rx.text(
                    "La pagina che stai cercando non esiste o è stata spostata.",
                    size=rx.breakpoints(initial="4", md="5"),
                    color_scheme="gray",
                    text_align="center"
                ),
                rx.button(
                    "Torna alla Home",
                    size=rx.breakpoints(initial="3", md="4"),
                    radius="full",
                    margin_top="1rem",
                    on_click=rx.redirect("/")
                ),
                align_items="center",
                spacing="4",
            ),
            width="100%",
            padding_y=rx.breakpoints(initial="6rem", md="10rem"),
            display="flex",
            justify_content="center",
            align_items="center",
            flex="1", # Pushes the content to fill the remaining vertical space
        ),
        
        spacing="0",
        width="100%",
        min_height="100vh",
    )

# The theme definition handles all the global styling
app = rx.App(
    stylesheets=["/styles.css"],
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        accent_color="purple",
        radius="large",
    )
)
