# Conversor de Moedas com FastAPI

## Visão Geral
Este projeto é uma API assíncrona baseada em FastAPI para conversão de moedas em tempo real. Ele fornece uma interface simples e eficiente para os usuários converterem valores de moeda usando taxas de câmbio obtidas de uma API externa, como a Alpha Vantage.

## Funcionalidades
- Processamento assíncrono para melhorar o desempenho e a escalabilidade.
- Framework FastAPI para desenvolvimento rápido e documentação interativa automática.
- Tratamento de erros para garantir robustez e confiabilidade.
- Geração automática de documentação da API.

## Requisitos
- Python 3.7+
- FastAPI
- aiohttp

## Rotas da API
- **GET /async/v2/{from_currency}**: Converte moeda de forma assíncrona.
  - **Parâmetros**:
    - `from_currency` (path): Código da moeda de origem (por exemplo, USD).
    - `to_currencies` (query): Lista de códigos de moeda de destino separados por vírgula (por exemplo, EUR,GBP).
    - `price` (query): Valor do dinheiro a ser convertido.
  - **Resposta**: Objeto JSON contendo os valores convertidos para cada moeda de destino.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar solicitações de pull para melhorar o projeto.
