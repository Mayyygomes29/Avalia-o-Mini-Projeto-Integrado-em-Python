# Projeto de Estatísticas com FastAPI e Streamlit

Sistema em Python para gerar estatísticas a partir de arquivos CSV, disponibilizá-las via API REST com FastAPI e visualizar com Streamlit.

## Documentação da API

```http
  GET /health
```
```RETORNA O STATUS DA API {'status': 'ok'} ```

```http
  GET /stats
```
```RETORNA A ANÁLISE ESTATÍSTICA ```
```http
 POST /sum
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `x`    | `int` | **Obrigatório**. Parcela 1 (Número que você quer somar) |
| `y`     | `int` | **Obrigatório**. Parcela 2 (Número que você quer somar) |

```RETORNA A SOMA ENTRE X E Y ```


## Funcionalidades

- Leitura de arquivos CSV (vendas.csv)

- Geração de estatísticas em stats.json

- API FastAPI com endpoints:

    /health -> retorna status da API

   /stats -> retorna estatísticas em JSON

  /sum -> retorna a soma entre x e y

- Visualização interativa via Streamlit (ui/app.py)

- Implementação funcional usando map, filter e reduce

## Tecnologias

**Backend**: FastAPI, Python 3.12+

**Visualização**: Streamlit

**Dependências**: pandas, numpy, matplotlib (via requirements.txt)


## 🗂️ Estrutura do Projeto

```bash
project/
│
├── data/
│   └── vendas.csv              # Dados de entrada
│
├── src/
│   ├── core/
│   │   └── metrics.py          # Funções de análise funcional
│   ├── make_stats.py           # Script para gerar stats.json
│   └── main.py                 # Aplicação FastAPI
│
├── ui/
│   └── app.py                  # Interface de visualização com Streamlit
│
├── stats.json                  # Saída gerada pelo processamento
├── requirements.txt            # Dependências do projeto
└── README.md                   # Documentação do projeto
```
  
## Referência

 - [Streamlit documentation](https://docs.streamlit.io/)
 - [matplotlib](https://matplotlib.org/)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

## Autor
<p> Mayara Gomes Silva </p> 
<p> maya.gomessilva29@gmail.com </p>
<p>https://www.linkedin.com/in/mayara-gomes-desenvolvedora-backend/ </p>
