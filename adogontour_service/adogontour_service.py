import reflex as rx

config = rx.Config(
    app_name="Adogontour Service",
    favicon="/favicon.ico",  # Percorso relativo alla cartella assets
)

def header_section():
    return rx.box(
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
                        variant="surface", # Usa uno stile diverso per farlo risaltare
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
        width="100%",
        padding="1rem 2rem",
        background_color="rgba(0, 0, 0, 0.8)", 
        backdrop_filter="blur(10px)",
        position="sticky",
        height="10vh",
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
    )

def hero_section():
    return rx.box(
        rx.vstack(
            # Puoi valutare di rimuovere o rimpicciolire questa immagine se preferisci averla solo nell'header
            rx.heading("Adogontour Service", size="9", weight="bold"),
            rx.text(
                "Audio • Luci • Multimedia - Live • Conferenze • Corporate",
                size="5",
                color_scheme="gray",
            ),
            rx.button("Scopri di più", size="4", radius="full", on_click=rx.redirect("/chi-siamo")),
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
            rx.button("I nostri servizi", size="4", radius="full", on_click=rx.redirect("/servizi")),
            spacing="5",
            align_items="center",
        ),
        padding="8rem 2rem",
        # A sleek dark gradient background for the hero
        background_image="linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('/hero-bg.jpeg')",
        background_size="cover",
        background_position="center",
        background_repeat="no-repeat",
        width="100%",
        height="90vh",
        text_align="center",
    )

def service_detail_block(title: str, description: rx.Component | str, icon: str, reverse: bool = False):
    # La parte di testo
    content = rx.vstack(
        rx.heading(title, size="7", color="var(--accent-11)"),
        rx.text(description, size="5", color_scheme="gray", line_height="1.6"),
        spacing="4",
        align_items="start",
        flex="1",
    )
    
    # La parte visiva (un box con l'icona)
    visual = rx.center(
        rx.icon(icon, size=100, color="var(--accent-9)"),
        background="var(--gray-3)",
        border_radius="1rem",
        padding="3rem",
        flex="1",
        min_width="250px",
        width="100%",
        box_shadow="0 10px 30px rgba(0,0,0,0.3)",
    )
    
    # Layout responsivo usando il dizionario per i breakpoints
    desktop_direction = "row" if not reverse else "row-reverse"
    
    return rx.flex(
        content,
        visual,
        direction={
            "base": "column",       # Su smartphone (schermi piccoli): impila verticalmente
            "md": desktop_direction # Su tablet/desktop (schermi medi/grandi): affianca
        },
        spacing="7",
        align_items="center",
        width="100%",
        padding_y="4rem",
        border_bottom="1px solid var(--gray-4)",
    )

def index():
    return rx.vstack(
        header_section(), # <-- Header inserito in cima
        hero_section(),
        spacing="0",
        width="100%",
    )

def contatti():
    return rx.vstack(
        header_section(), # Richiama l'header che hai già creato
        rx.box(
            rx.heading("Contattaci", size="8", margin_bottom="1rem"),
            rx.text("Scrivici per un preventivo sui servizi audio e luci.", size="5"),
            # Qui puoi aggiungere form, email, numeri di telefono, ecc.
            padding="4rem 2rem",
            align_items="center",
        ),
        spacing="0",
        width="100%",
        min_height="100vh",
    )

def chi_siamo():
    return rx.vstack(
        header_section(),
        
        # Hero section per Chi Siamo
        rx.box(
            rx.vstack(
                rx.heading("Chi Siamo", size="9", weight="bold"),
                rx.text(
                    "Una storia proiettata nel futuro tecnico dello spettacolo.", 
                    size="6", 
                    color_scheme="gray", 
                    text_align="center", 
                    max_width="700px"
                ),
                align_items="center",
                spacing="4",
            ),
            padding_y="6rem",
            width="100%",
            background_image="linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url('/about-bg.jpeg')",
            background_position="center",
            background_size="cover",
            border_bottom="1px solid var(--gray-5)",
        ),

        # Contenitore principale dei contenuti
        rx.box(
            rx.vstack(
                # Blocco 1: Le Radici e gli Eventi
                rx.flex(
                    rx.vstack(
                        rx.heading("Le Nostre Radici", size="7", color="var(--accent-11)"),
                        rx.text("Adogontour Service nasce da Pier Francesco Leardi nel 2007. Nel corso degli anni si afferma come punto di riferimento per la fornitura tecnica nella provincia di Cuneo e non solo.", size="5", color_scheme="gray", line_height="1.6"),
                        rx.text("Abbiamo curato la direzione tecnica e la fornitura per innumerevoli manifestazioni pubbliche. Dai numerosi eventi estivi sul territorio, fino al supporto di rassegne come Ted X Cuneo, la nostra esperienza sul campo ci permette di affrontare e risolvere ogni tipo di sfida tecnica.", size="5", color_scheme="gray", line_height="1.6"),
                        spacing="4",
                        align_items="start",
                        flex="1",
                    ),
                    rx.center(
                        rx.icon("history", size=100, color="var(--accent-9)"),
                        background="var(--gray-3)",
                        border_radius="1rem",
                        padding="3rem",
                        flex="1",
                        min_width="250px",
                        width="100%",
                        box_shadow="0 10px 30px rgba(0,0,0,0.3)",
                    ),
                    direction={"base": "column", "md": "row"},
                    spacing="7",
                    align_items="center",
                    width="100%",
                    padding_y="4rem",
                    border_bottom="1px solid var(--gray-4)",
                ),

                # Blocco 2: L'Evoluzione Logistica e Tecnica (Il tuo apporto)
                rx.flex(
                    rx.center(
                        rx.icon("rocket", size=100, color="var(--accent-9)"),
                        background="var(--gray-3)",
                        border_radius="1rem",
                        padding="3rem",
                        flex="1",
                        min_width="250px",
                        width="100%",
                        box_shadow="0 10px 30px rgba(0,0,0,0.3)",
                    ),
                    rx.vstack(
                        rx.heading("Evoluzione e Innovazione", size="7", color="var(--accent-11)"),
                        rx.text("Oggi, pur mantenendo le nostre radici, Adogontour è un service che punta alla massima efficienza attraverso la tecnologia e un approccio analitico ai flussi di lavoro.", size="5", color_scheme="gray", line_height="1.6"),
                        rx.text("Gestiamo l'intera catena logistica con strumenti digitali proprietari per ottimizzare l'inventario e la gestione del magazzino.", size="5", color_scheme="gray", line_height="1.6"),
                        rx.text("Lavoriamo con standard industriali e console digitali di altissimo livello (DiGiCo, Chamsys, HK Audio) per garantire sempre stabilità e scalabilità in ogni produzione.", size="5", color_scheme="gray", line_height="1.6"),
                        spacing="4",
                        align_items="start",
                        flex="1",
                    ),
                    direction={"base": "column", "md": "row-reverse"},
                    spacing="7",
                    align_items="center",
                    width="100%",
                    padding_y="4rem",
                ),

                width="100%",
                max_width="1100px",
                margin="0 auto",
                padding_x=["2rem", "2rem", "0"],
            ),
            width="100%",
        ),

        # Call to Action finale
        rx.box(
            rx.vstack(
                rx.heading("Affidati alla nostra esperienza", size="7"),
                rx.text("Decenni di storia uniti alle tecnologie più avanzate per il tuo evento.", size="5", color_scheme="gray"),
                rx.button("Richiedi disponibilità", size="4", radius="full", margin_top="1rem", on_click=rx.redirect("/contatti")),
                align_items="center",
                spacing="4"
            ),
            padding_y="6rem",
            width="100%",
            text_align="center",
            background="var(--gray-2)", 
        ),
        
        spacing="0",
        width="100%",
        min_height="100vh",
    )

def servizi():
    return rx.vstack(
        header_section(),
        
        # Hero section specifica per i servizi
        rx.box(
            rx.vstack(
                rx.heading("I Nostri Servizi", size="9", weight="bold"),
                rx.text(
                    "Soluzioni tecniche complete per eventi dal vivo, dalla pre-produzione alla realizzazione in loco.", 
                    size="6", 
                    color_scheme="gray", 
                    text_align="center", 
                    max_width="700px"
                ),
                align_items="center",
                spacing="4",
            ),
            padding_y="6rem",
            width="100%",
            background_image="linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url('/services-bg.jpeg')",
            background_position="50% 70%",
            background_size="cover",
            border_bottom="1px solid var(--gray-5)",
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
                    description=rx.text(
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
                padding_x=["2rem", "2rem", "0"],
            ),
            width="100%",
        ),

        # Call to Action finale
        rx.box(
            rx.vstack(
                rx.heading("Hai un progetto in mente?", size="7"),
                rx.text("Contattaci per discutere le tue necessità tecniche e richiedere un preventivo.", size="5", color_scheme="gray"),
                rx.button("Richiedi un Preventivo", size="4", radius="full", margin_top="1rem", on_click=rx.redirect("/contatti")),
                align_items="center",
                spacing="4"
            ),
            padding_y="6rem",
            width="100%",
            text_align="center",
            background="var(--gray-2)", # Sfondo leggermente staccato dal nero puro
        ),
        
        spacing="0",
        width="100%",
        min_height="100vh",
    )

def pagina_in_costruzione():
    return rx.vstack(
        header_section(),
        rx.card(
            rx.vstack(
                rx.icon("hammer"),
                rx.heading("Pagina in costruzione", size="7"),
                align="center"
            )
        ),
        align="center"
    )

# The theme definition handles all the global styling
app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        accent_color="purple",
        radius="large",
    )
)
app.add_page(index, title="Adogontour Service")
app.add_page(pagina_in_costruzione, route="/contatti", title="Contatti - Adogontour")
app.add_page(chi_siamo, route="/chi-siamo", title="Chi Siamo - Adogontour")
app.add_page(servizi, route="/servizi", title="Servizi - Adogontour")
app.add_page(pagina_in_costruzione, route="/noleggio", title="Noleggio - Adogontour")