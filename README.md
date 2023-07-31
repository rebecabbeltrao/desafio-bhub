
# Desafio Bhub 

## Descrição

Desafio de criação de API simples para gerenciar os clientes da Bhub.

## Índice

- [Requisitos](#requisitos)
- [Documentação da API](#api-documentation)
- [Contributing](#como-executar)


## Requisitos 

- Instalar o [Python 3](https://www.python.org/downloads/) na sua máquina (caso não possua)
- Instalar e configurar o [MongoDB](https://www.mongodb.com) na sua máquina (caso não possua)
- (Não obrigatório) Instalar o [Robo3t](https://robomongo.org) para gerenciar o Mongodb
- Criar um arquivo `.env` no projeto usando como base o `env.example` e substituir pelas informações do seu banco de dados. 

## Documentação da API

A documentação da API está disponível no [Swagger Hub](https://app.swaggerhub.com/apis/rebeca.mbeltrao/desafio-bhub/1.0.0)

## Como executar 
- Crie um ambiente virtual usando o comando `python3 -m venv venv` no diretório raiz do repositório
- Depois, ative o ambiente usando o comando `source venv/bin/activate` (Linux ou macOS) ou `venv/Scripts/Activate` (Windows)
- Instale as bibliotecas com o comando: `pip install -r requirements.txt`
- Vá para a pasta `api` do projeto e execute seguinte comando: `flask --app app.py run`
- Caso deseje parar a execução, digite `Ctrl+C`
