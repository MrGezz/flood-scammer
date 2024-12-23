from datetime import datetime
from nicegui import ui

ui.dark_mode().enable()
log = ui.log(max_lines=50).classes('w-full h-500')
ui.button('Log time', on_click=lambda: log.push(datetime.now().strftime('%X.%f')[:-5]))

ui.run()