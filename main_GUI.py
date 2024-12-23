from datetime import datetime
from nicegui import ui
from fakedata_my import fakedata, namelist

name_obj = namelist()
names= name_obj.generate('names_MY.txt',1000)

ui.dark_mode().enable()
log = ui.log(max_lines=500).classes('w-full h-500')
#ui.button('Randomize Entity', on_click=lambda: log.push(datetime.now().strftime('%X.%f')[:-5]))
with ui.row():
    ui.button('Randomize Entity', on_click=lambda: log.push(fakedata(names)))
    ui.button('Clear', on_click=log.clear)

ui.run()