import reflex as rx

config = rx.Config(
    app_name="Adogontour-Service",
    api_url="https://api.adogontour.it",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(),
    ]
)