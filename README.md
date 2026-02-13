# 🤖 Fortuna Bot

## Pré-requisitos

- Python **3.10+**
- pip
- Token de bot do Telegram (via @BotFather)

---

## Clonar o repositório

```bash
git clone <url-do-repositorio>
cd fortuna
```

---

## Criar o arquivo de variáveis de ambiente

Copie o arquivo de exemplo:

```bash 
cp .env.example .env
```

Edite o .env e informe o token do bot:

```env
TOKEN_TELEGRAM=SEU_TOKEN_AQUI
```

---

## Instalar as dependências

```bash
pip install -r requirements.txt
```

---
## Executar o projeto

Execute, na pasta raiz do projeto, o comando:

```bash
python dev.py
```

---

## Página do Projeto (GitHub Pages)

Este projeto possui uma landing page configurada na pasta `docs/`. Para ativá-la:

1. Vá até as **Configurações (Settings)** do repositório no GitHub.
2. Clique na seção **Pages** no menu lateral esquerdo.
3. Em **Build and deployment** > **Source**, selecione **Deploy from a branch**.
4. Em **Branch**, selecione a branch `main` (ou `master`) e a pasta `/docs`.
5. Clique em **Save**.

Sua página estará acessível em `https://<seu-usuario>.github.io/<nome-do-repositorio>/`.