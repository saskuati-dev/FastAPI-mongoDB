# FastAPI com MongoDB

Este é um projeto simples que demonstra como usar o FastAPI com MongoDB.

## Descrição

Este projeto fornece um exemplo básico de como criar uma API RESTful usando FastAPI e MongoDB. Ele inclui operações CRUD (Criar, Ler, Atualizar, Excluir) para gerenciar dados em um banco de dados MongoDB.

## Pré-requisitos

*   Python 3.7+
*   MongoDB instalado e em execução

## Instalação

1.  Clone o repositório:

    ```bash
    git clone https://github.com/saskuati-dev/FastAPI-mongoDB.git
    cd FastAPI-mongoDB
    ```

2.  Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv .venv
    source .venv/bin/activate   # No Linux/macOS
    .venv\Scripts\activate  # No Windows
    ```

3.  Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Configuração

1.  Configure a conexão com o MongoDB no arquivo de configuração (se necessário).

2.  Certifique-se de que o MongoDB está em execução.

## Execução

1.  Execute a aplicação FastAPI:

    ```bash
    uvicorn main:app --reload
    ```

    Isso iniciará o servidor FastAPI.

2.  Acesse a API em seu navegador ou com um cliente HTTP em `http://localhost:8000`.

## Endpoints

*   `GET /`: Endpoint raiz (pode retornar uma mensagem de boas-vindas).
*   `POST /`: Cria um novo item.
*   `PUT /{item_id}`: Atualiza um item existente.
*   `DELETE /{item_id}`: Exclui um item.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.


