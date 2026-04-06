import flet as ft
import api_service as api  

def main(page: ft.Page):
    page.title = "O que toca?"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 500
    page.window_height = 800

    titulo = ft.Text("🎵 O que Toca?", size=30, weight="bold")
    descricao = ft.Text("Descubra o repertório do último show do seu artista favorito! Digite o nome da banda abaixo para ver a data, o local e as músicas que rolaram na apresentação mais recente.", color=ft.Colors.GREY_400)
    input_banda = ft.TextField(label="Nome da Banda", width=300)
    lista_resultados = ft.ListView(expand=True, spacing=10)
    progresso = ft.ProgressBar(visible=False, color="amber")

    def buscar_clique(e):
        if not input_banda.value: return
        
        progresso.visible = True
        lista_resultados.controls.clear()
        page.update()

    
        resposta = api.buscar_ultimo_setlist(input_banda.value)
        progresso.visible = False

        if isinstance(resposta, dict) and "erro" in resposta:
            lista_resultados.controls.append(ft.Text(resposta["erro"], color="red"))
        elif not resposta:
            lista_resultados.controls.append(ft.Text("Nada encontrado.", color="orange"))
        else:
            
            show = resposta[0]
            
            data = show.get('eventDate', '---')
            venue = show.get('venue', {}).get('name', 'Local desconhecido')
            
            lista_resultados.controls.append(
                ft.Container(
                    content=ft.Text(f"📅 {data} - {venue}", weight="bold"),
                    padding=10, bgcolor=ft.Colors.WHITE10, border_radius=5
                )
            )

            sets = show.get('sets', {}).get('set', [])
            if isinstance(sets, dict): sets = [sets]

            for s in sets:
                musicas = s.get('song', [])
                if isinstance(musicas, dict): musicas = [musicas]
                for m in musicas:
                    lista_resultados.controls.append(
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.MUSIC_NOTE, color="amber"),
                            title=ft.Text(m.get('name', 'Música'))
                        )
                    )
        page.update()

    btn = ft.ElevatedButton("Buscar", on_click=buscar_clique)
    page.add(titulo, descricao, ft.Row([input_banda, btn]), progresso, ft.Divider(height=20), lista_resultados)

ft.app(target=main)