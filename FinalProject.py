import flet as ft
import os

class estudiante(ft.UserControl):
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def build(self):
        info = ft.Text(value=f"{self.name}: {self.points} points remaining")
        return info

def main(page: ft.Page):
    names = ['Manuel Jesus', 'AleJandro', 'Reilly', 'Hans', 'Manuel Liriano', 'Jeudry', 'Yury',
             'Daniela Cabrera', 'Daniela Sofia', 'Nicolas', 'Roxi', 'Fabrianny', 'Felix', 'Marcos',
             'Joaquin', 'Juan', 'Jadeline', 'Chrismerlis', 'Camila', 'Shelsie' , 'Emmanuel', 'Paolo',
             'Brittney']
    
    scores = {}

    
    if not os.path.exists("puntos_restantes.txt"):
        scores = {name: 100 for name in names}
    else:
        
        with open("puntos_restantes.txt", "r") as f:
            for line in f:
                name, points = line.strip().split(": ")
                
                points = ''.join(filter(str.isdigit, points))
                scores[name] = int(points)

    def textbox_changed(e):
        input_text = e.control.value
        for name in names:
            if name == input_text:
                scores[name] -= 5
                pointscolumn.controls.append(ft.Text(f"{name}: {scores[name]} points remaining"))
                
                with open('puntos_restantes.txt', 'w') as f:
                    for name, points in scores.items():
                        f.write(f"{name}: {points} points remaining\n")
                break
        page.update()

    tb = ft.TextField(
        label="Enter a name:",
        on_change=textbox_changed,
    )
    namescolum = ft.Column(controls=[])
    pointscolumn = ft.Column(controls=[])

    for name in names:
        namescolum.controls.append(ft.Text(value=name))

    namesrow = ft.Row(controls=[namescolum, pointscolumn])
    maincolum = ft.Column(controls=[tb, namesrow])

    page.add(maincolum)

ft.app(target=main)