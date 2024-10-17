from nicegui import ui
from dice import *

ui.page_title("Libello")
ui.label('Initial Button Testing')
with ui.button(on_click=lambda: ui.notify(f"Result: {d20()}")):
    ui.label("D20")
    ui.image("https://cdn-icons-png.flaticon.com/512/6729/6729800.png")

ui.run()