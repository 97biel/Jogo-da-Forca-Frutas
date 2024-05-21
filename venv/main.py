import flet as ft
import string
import random

def adivinhar(letter):
    return ft.Container(
        width=50,
        height=50,
        bgcolor=ft.colors.AMBER_500,
        border_radius=ft.border_radius.all(5),
        content=ft.Text(
            value=letter,
            color=ft.colors.WHITE,
            size=30,
            text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.BOLD,
        )
    )

def main(page: ft.Page):
    page.title = "Jogo da Forca - FRUTAS"
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = ft.colors.AMBER_100

    def escolher_nova_palavra():
        nonlocal choiced
        choiced = random.choice(lista).upper()
        victim.data = 0
        victim.src = 'images/forca_0.png'
        word.controls = [adivinhar('_') for _ in choiced]
        for control in keyboard_controls:
            control.disabled = False
            control.gradient = ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[ft.colors.AMBER, ft.colors.DEEP_ORANGE]
            )
            control.update()
        word.update()
        victim.update()
        page.update()

    lista = ['Goiaba', 'Maca', 'Manga', 'Maracujá', 'Uva', 'Tangerina', 'Beterraba', 'Abacaxi']
    choiced = random.choice(lista).upper()

    def validar(e):
        acerto = False
        for pos, letter in enumerate(choiced):
            if e.control.content.value == letter:
                word.controls[pos] = adivinhar(letter=letter)
                acerto = True
        word.update()

        if not acerto:
            victim.data += 1

            if victim.data > 6:
                page.dialog = ft.AlertDialog(
                    title=ft.Text(value="Você perdeu. :("),
                    on_dismiss=lambda e: escolher_nova_palavra(),
                    open=True
                )
                page.update()
                return

            erros = victim.data
            victim.src = f'images/forca_{erros}.png'
            victim.update()

        e.control.disabled = True
        e.control.gradient = ft.LinearGradient(colors=[ft.colors.RED])
        e.control.update()
        
        if all(c.content.value != '_' for c in word.controls):
            page.dialog = ft.AlertDialog(
                title=ft.Text(value='Você ganhou! :)'), 
                on_dismiss=lambda e: escolher_nova_palavra(), 
                open=True
            )
            page.update()

    scene = ft.Image(src='images/top1.png', width=200)
    
    victim = ft.Image(
        data=0,
        src='images/forca_0.png',
        repeat=ft.ImageRepeat.NO_REPEAT,
        height=300,
    )

    word = ft.Row(
        col={'xs': 12, 'lg': 6},
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            adivinhar('_') for _ in choiced
        ]
    )

    game = ft.Container(
        col={'xs': 12, 'lg': 6},
        width=400,
        height=400,
        border_radius=20,
        bgcolor=ft.colors.YELLOW,
        shadow=[ft.BoxShadow(
            spread_radius=10,
            blur_radius=0,
            color=ft.colors.DEEP_ORANGE,
            offset=ft.Offset(x=-50, y=-20)
        ),
        ft.BoxShadow(
            spread_radius=0,
            blur_radius=60,
            color=ft.colors.DEEP_ORANGE,
            offset=ft.Offset(x=-50, y=-20)
        )],
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                victim,
                word,
            ]
        )
    )

    keyboard_controls = [
        ft.Container(
            height=50,
            width=50,
            padding=5,
            border_radius=ft.border_radius.all(5),
            content=ft.Text(
                value=letter,
                color=ft.colors.WHITE,
                size=20,
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.BOLD
            ),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[ft.colors.AMBER, ft.colors.DEEP_ORANGE]
            ), 
            on_click=validar
        ) for letter in string.ascii_uppercase
    ]
    
    keyboard = ft.Container(
        col={'xs': 12, 'lg': 6},
        width=250,
        height=250,
        border_radius=20,
        padding=30,
        bgcolor=ft.colors.GREEN,
        content=ft.Row(
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=keyboard_controls
        ),
        shadow=[ft.BoxShadow(
            spread_radius=10,
            blur_radius=0,
            color=ft.colors.DEEP_ORANGE,
            offset=ft.Offset(x=50, y=20),
        ),
        ft.BoxShadow(
            spread_radius=0,
            blur_radius=60,
            color=ft.colors.DEEP_ORANGE,
            offset=ft.Offset(x=50, y=20)
        )]
    )

    game_keyboard_row = ft.ResponsiveRow(
        controls=[
            game,
            keyboard
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )

    layout = ft.Column(
        controls=[
            scene,
            game_keyboard_row,
            scene
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(layout)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, assets_dir='assets')
