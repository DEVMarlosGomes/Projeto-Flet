import flet as ft
import sqlite3
import os
import time

# Banco de dados
DB_FILE = "quiz_cyberpunk_pro.db"

# Perguntas organizadas por nível
perguntas = {
    "Fácil": [
        {"pergunta": "Qual a capital do Brasil?", "opcoes": ["São Paulo", "Brasília", "Rio de Janeiro"], "resposta": "Brasília"},
        {"pergunta": "Quanto é 2 + 2?", "opcoes": ["3", "4", "5"], "resposta": "4"}
    ],
    "Médio": [
        {"pergunta": "Qual linguagem estamos usando?", "opcoes": ["Java", "Python", "C++"], "resposta": "Python"},
        {"pergunta": "Em que ano foi lançado Cyberpunk 2077?", "opcoes": ["2020", "2019", "2021"], "resposta": "2020"}
    ],
    "Difícil": [
        {"pergunta": "Quem é o personagem icônico interpretado por Keanu Reeves?", "opcoes": ["Johnny Silverhand", "V", "Adam Smasher"], "resposta": "Johnny Silverhand"},
        {"pergunta": "Qual corporação domina Night City?", "opcoes": ["Militech", "Arasaka", "Kang Tao"], "resposta": "Arasaka"}
    ]
}

# Inicializa banco
def inicializar_banco():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS historico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            pontuacao INTEGER NOT NULL,
            nivel TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Salva pontuação
def salvar_pontuacao(nome, pontuacao, nivel):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO historico (nome, pontuacao, nivel) VALUES (?, ?, ?)", (nome, pontuacao, nivel))
    conn.commit()
    conn.close()

# Lê histórico
def ler_historico():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT nome, pontuacao, nivel FROM historico ORDER BY id DESC LIMIT 5")
    registros = c.fetchall()
    conn.close()
    return registros

# Função principal
def main(page: ft.Page):
    inicializar_banco()

    # Configurações visuais
    page.title = "Cyberpunk Quiz Pro"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0a0a0a"
    page.window_width = 500
    page.window_height = 750
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    neon = "#39ff14"
    pink = "#ff007f"
    blue = "#00eaff"
    font_title = ft.TextStyle(size=32, weight=ft.FontWeight.BOLD, color=neon)
    font_text = ft.TextStyle(size=18, weight=ft.FontWeight.BOLD, color=blue)

    nome_usuario = ft.TextField(label="Digite seu nome", border_color=pink)
    nivel_dropdown = ft.Dropdown(
        label="Escolha o nível",
        options=[ft.dropdown.Option(n) for n in perguntas.keys()],
        border_color=blue
    )
    pergunta_texto = ft.Text(style=font_text)
    opcoes_radios = ft.RadioGroup()
    resultado_texto = ft.Text(style=font_text)
    historico_texto = ft.Text(style=font_text)

    indice = {"valor": 0}
    pontuacao = {"valor": 0}
    nivel_atual = {"valor": "Fácil"}

    # Mostrar pergunta
    def mostrar_pergunta():
        quiz = perguntas[nivel_atual["valor"]]
        if indice["valor"] < len(quiz):
            p = quiz[indice["valor"]]
            pergunta_texto.value = p["pergunta"]
            opcoes_radios.content = [
                ft.Radio(value=op, label=op, active_color=neon) for op in p["opcoes"]
            ]
            page.update()
        else:
            resultado_texto.value = f"Parabéns, {nome_usuario.value}! Pontuação: {pontuacao['valor']}/{len(quiz)}"
            salvar_pontuacao(nome_usuario.value, pontuacao["valor"], nivel_atual["valor"])
            atualizar_historico()
            btn_responder.disabled = True
            btn_iniciar.disabled = False
            page.update()

    # Atualiza histórico
    def atualizar_historico():
        registros = ler_historico()
        texto = "Histórico:\n"
        for nome, pts, niv in registros:
            texto += f"{nome} ({niv}): {pts}\n"
        historico_texto.value = texto
        page.update()

    # Inicia quiz
    def iniciar_quiz(e):
        if nome_usuario.value.strip() == "" or not nivel_dropdown.value:
            resultado_texto.value = "Insira nome e escolha o nível!"
            page.update()
            return
        indice["valor"] = 0
        pontuacao["valor"] = 0
        nivel_atual["valor"] = nivel_dropdown.value
        btn_responder.disabled = False
        btn_iniciar.disabled = True
        resultado_texto.value = ""
        mostrar_pergunta()

    # Responde
    def responder(e):
        if not opcoes_radios.value:
            resultado_texto.value = "Selecione uma opção."
            page.update()
            return

        quiz = perguntas[nivel_atual["valor"]]
        resposta_correta = quiz[indice["valor"]]["resposta"]

        if opcoes_radios.value == resposta_correta:
            pontuacao["valor"] += 1
            resultado_texto.value = "Resposta correta! [++ Neon ++]"
        else:
            resultado_texto.value = f"Errado! Resposta: {resposta_correta}"

        indice["valor"] += 1
        page.update()
        time.sleep(0.8)
        mostrar_pergunta()

    # Botões com estilo cyberpunk
    btn_iniciar = ft.ElevatedButton("Iniciar Quiz", on_click=iniciar_quiz, style=ft.ButtonStyle(bgcolor=neon, color="#000"))
    btn_responder = ft.ElevatedButton("Responder", on_click=responder, disabled=True, style=ft.ButtonStyle(bgcolor=pink, color="#000"))

    # Cabeçalho com imagem
    img = ft.Image(
        src="https://i.imgur.com/z9dTtZb.jpg", 
        width=400, height=200, fit=ft.ImageFit.COVER
    )

    # Layout
    page.add(
        img,
        ft.Text("Cyberpunk Quiz", style=font_title),
        nome_usuario,
        nivel_dropdown,
        btn_iniciar,
        pergunta_texto,
        opcoes_radios,
        btn_responder,
        resultado_texto,
        historico_texto
    )

# Executa app
ft.app(target=main)
