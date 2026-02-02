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

Execute o projeto:

```bash
python dev.py
```