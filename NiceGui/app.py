from nicegui import ui

# for text 
ui.label("Welcome to the Nicegui tutorial!")



#markdown 
ui.markdown("## This is a markdown section")

# HTML 
ui.html("<p>This is a paragraph in HTML</p>")

# mermaid 
ui.mermaid("""
           graph TD;
           A --> B;
           A --> C;
           B --> D;
           C --> D;""")

# Widgets: 

# Input field
ui.input(label="Firstname", placeholder="Type something...", on_change = lambda e: fname.set_text(e.value))
fname = ui.label()

# text area 

ui.textarea(label = " message", on_change =lambda e: msg.set_text(e.value))
msg = ui.label()


# Number input
ui.number(label = " age", max= 100, min = 1)

# date input
ui.date(value = "2025-05-25")

# time input
ui.time(value= "12:00")

#color input
ui.color_input()
ui.color_picker()

# button 
ui.button("click me !",on_click = lambda e: ui.notify("You have click me !"))




ui.run(host= "127.0.0.1",port = 8000)