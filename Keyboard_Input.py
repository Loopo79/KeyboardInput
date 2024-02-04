import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    def on_keyboard(e: ft.KeyboardEvent):
        key.content = ft.Text(e.key)
        key.visible = True
        shift.visible = e.shift
        control.visible = e.ctrl
        alt.visible = e.alt
        page.update()

    def createContainer(str):
        return ft.Container(
        content=ft.Text(str),
        padding=5,
        visible = False,
        bgcolor = ft.colors.RED_400,
        border_radius=5,
        alignment=ft.alignment.center,
    )
    
    page.on_keyboard_event = on_keyboard
    key = createContainer("")
    shift = createContainer("Shift")
    control = createContainer("Control")
    alt = createContainer("Alt")
    
    
    keyD = ft.Container(ft.Row(controls = [key, shift, control, alt],
                  alignment = ft.MainAxisAlignment.CENTER),)
    page.add( ft.Text("Press any key with a combination of CTRL, ALT and SHIFT keys..."),
              keyD)

ft.app(target=main)
