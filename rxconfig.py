import reflex as rx

config = rx.Config(
    app_name="adogontour_service",
    api_url="https://api.adogontour.it",
    deploy_url="https://www.adogontour.it", # Add this line
    show_built_with_reflex=False,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(),
    ]
)