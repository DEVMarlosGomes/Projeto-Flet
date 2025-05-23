# **Cyberpunk Quiz Pro**

![Cyberpunk Banner](https://i.imgur.com/z9dTtZb.jpg)

Um quiz interativo com visual e estética inspirados no universo **Cyberpunk 2077**! Desenvolvido com **Python**, **Flet** e **SQLite** para armazenar o histórico dos jogadores.

---

## **Recursos do Projeto**

* **Interface futurista** com cores neon.
* **Três níveis de dificuldade**: Fácil, Médio e Difícil.
* **Histórico de partidas** salvo em banco de dados.
* **Feedback visual** após cada resposta.
* **Banco de dados SQLite** para persistência de dados.

---

## **Tecnologias Utilizadas**

* **Python 3.8+**
* **Flet** - Framework para criação de interfaces gráficas.
* **SQLite3** - Banco de dados leve embutido.
* **Estilo Cyberpunk** - Neon, preto e elementos vibrantes.

---

## **Instalação**

1. **Clone o repositório**:

```bash
git clone https://github.com/seuusuario/cyberpunk-quiz-pro.git
cd cyberpunk-quiz-pro
```

2. **Crie um ambiente virtual (opcional mas recomendado):**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. **Instale as dependências:**

```bash
pip install flet
```

---

## **Como Rodar o Projeto**

```bash
python quiz_cyberpunk_pro.py
```

O aplicativo abrirá automaticamente uma janela com o quiz.

---

## **Como Jogar**

1. **Digite seu nome**.
2. **Escolha um nível** de dificuldade.
3. Clique em **"Iniciar Quiz"**.
4. Leia a pergunta e **selecione a resposta**.
5. Clique em **"Responder"**.
6. No final, veja sua pontuação e o **histórico das últimas partidas**.

---

## **Demonstração Visual**

| Tela Inicial                             | Seleção de Nível                          | Resultado                                     |
| ---------------------------------------- | ----------------------------------------- | --------------------------------------------- |
| ![tela](https://i.imgur.com/z9dTtZb.jpg) | ![nível](https://i.imgur.com/z9dTtZb.jpg) | ![resultado](https://i.imgur.com/z9dTtZb.jpg) |

*(Imagens ilustrativas, substitua por capturas reais do app se desejar.)*

---

## **Banco de Dados**

* O banco **`quiz_cyberpunk_pro.db`** é criado automaticamente.
* Armazena:

  * Nome do jogador
  * Pontuação
  * Nível escolhido
* Exibe as **últimas 5 partidas** no histórico.

---

## **Estrutura do Código**

* `inicializar_banco()` → Cria a tabela no banco, se não existir.
* `salvar_pontuacao()` → Insere o resultado do usuário.
* `ler_historico()` → Consulta e exibe o histórico.
* `main()` → Monta toda a interface e lógica de interação.

---

## **Estilo Cyberpunk**

* **Neon verde** (`#39ff14`), **rosa vibrante** (`#ff007f`) e **azul elétrico** (`#00eaff`).
* Fundo preto total (`#0a0a0a`).
* Tipografia **bold e estilizada**.
* Botões com efeito neon e imagem temática no topo.

---

## **Exemplo de Uso**

```plaintext
> Digite seu nome: V
> Escolha o nível: Difícil
> Pergunta: Quem é o personagem icônico interpretado por Keanu Reeves?
> Opções: Johnny Silverhand, V, Adam Smasher
> Sua resposta: Johnny Silverhand
> Resposta correta! [++ Neon ++]
```

---

## **Possíveis Melhorias**

* Adicionar **cronômetro** para respostas.
* Mais níveis e perguntas.
* Sons e animações cyberpunk.
* Exportação de **ranking global**.

---

## **Autor**

Desenvolvido por **\Marlos Gomes/**
Inspirado pelo universo de **Cyberpunk 2077**

---

## **Licença**
