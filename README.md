Utiliza-se (Random, Flet e String)
Se pode fazer os itens responsive caso use imagens no keyboard e game, mas preferi as columns no top e bottom e responsive no gamer e keyboard. Para rodar telas menores, pode aplicar o wrap em gamer e keyboard


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
        page.update()  -> Função com o fim de atualizar uma nova palavra no game

    lista = ['Goiaba', 'Maca', 'Manga', 'Maracujá', 'Uva', 'Tangerina', 'Beterraba', 'Abacaxi']
    choiced = random.choice(lista).upper()

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
    ] -> A bibliota string foi usada para trazer os caracters alfa para o teclado 
