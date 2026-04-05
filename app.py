import flet as ft

def main(page: ft.Page):
    
    page.title = "O Que Toca? - Setlist.fm"
    page.theme_mode = ft.ThemeMode.DARK 
    page.padding = 30
    page.window_width = 500
    page.window_height = 700

    titulo = ft.Text("🎵 O Que Toca ?", size=30, weight=ft.FontWeight.BOLD)
    subtitulo = ft.Text("Descubra o setlist do último show da sua banda.", color=ft.Colors.GREY_400)
    
    input_banda = ft.TextField(label="Nome da Banda (ex: Djavan)", width=300)
    btn_buscar = ft.ElevatedButton(text="Procurar", icon=ft.Icons.SEARCH)
    lista_musicas = ft.ListView(expand=True, spacing=10, padding=20)

    def ao_clicar(e):
        lista_musicas.controls.clear()
        if not input_banda.value:
            lista_musicas.controls.append(ft.Text("⚠️ Digite o nome de uma banda/artista!", color=ft.Colors.RED_400))
        else:
            lista_musicas.controls.append(
                ft.Text(f"A procurar por: {input_banda.value}...", color=ft.Colors.AMBER)
            )
        page.update()

    btn_buscar.on_click = ao_clicar

    page.add(
        titulo,
        subtitulo,
        ft.Row([input_banda, btn_buscar]),
        ft.Divider(height=20, color=ft.Colors.WHITE24),
        lista_musicas
    )

ft.app(target=main)