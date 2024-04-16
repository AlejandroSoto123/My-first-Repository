import flet as ft

def main(page: ft.Page):
    def add1(e):
        numero = int(numberLabel.value)
        numero += 1
        numberLabel.value = str(numero)

    def minus1(e):
        numero = int(numberLabel.value)
        numero -= 1
        numberLabel.value = str(numero)

    page.horizontal_alignment = "CENTER"  
    page.vertical_alignment = "CENTER"  
    titleText = ft.Text(value="Counter App")  
    numberLabel = ft.Text(value="0")
    plusButton = ft.IconButton(icon="add") 
    minusButton = ft.IconButton(icon="remove")  

    plusButton.on_click = add1  
    minusButton.on_click = minus1  

    picture = ft.Image(src="https://images.pexels.com/photos/1011630/pexels-photo-1011630.jpeg?cs=srgb&dl=animal-white-young-1011630.jpg&fm=jpg")
    rowButtons = ft.Row(controls=[minusButton, plusButton])
    page.add(titleText, numberLabel, rowButtons, picture) 

ft.app(target=main)
