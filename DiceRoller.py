import random
import flet as ft

def main(page: ft.Page):

    def roll(e):
        numero = random.randint(1, 6)
        numberLabel.value = str(numero)

        match(numero):
            case 1:
                diceImage.src = "cara1.png"
            
            case 2:
                diceImage.src = "cara2.png"

            case 3:
                diceImage.src = "cara3.png"

            case 4:
                diceImage.src = "cara4.png"

            case 5:
                diceImage.src = "cara5.png"

            case 6:
                diceImage.src = "cara6.png"

        page.update()

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    diceImage = ft.Image(src="genericDice.png", width=300, height=300)
    numberLabel = ft.Text(value="No roll yet")
    rollButton = ft.ElevatedButton(text="Roll", on_click=roll)

    page.add(diceImage, numberLabel, rollButton)

ft.app(target=main)
