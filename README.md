# beeMôn:

Na beeMôn criamos muitos sistemas de raspagem de dados e buscamos todos os dias inovação na analise dos dados. Este desafio esta aberto para todos que quiserem abrir um fork e submeter suas ideias de tecnologia.

## Desafio:
Escolher uma dos sites abaixo para fazer o desafio

- [quotes.toscrape](https://quotes.toscrape.com/)
- [imdb.com](https://www.imdb.com/chart/top/?ref_=nv_mv_250)

### Minimo Entregável:

- Buscar dados de forma automatizada(script de linha de comando ou interface clicavel)
- Padronizar os retornos de forma estruturada (json/csv)
- Sistema de logs de para acompanhamento da execução
- Ter um prova da consulta (Screenshot)

### Pontos Extra para:

- Armazenamento dos resultados em um banco relacional ou não relacional
- Fazer um dataframe que possibilite visualizar os resultados via pandas
- Trazer resultados de forma dinamica sem fixar caminhos no `xpath`
- Dockerizar a aplicação
- Conseguir agendar uma execução para um dia e horario.

### Libs sugeridas:

 - Selenium 
 - Scrapy
 - Pandas
 - Requests
 - BeautifulSoup 


### O que iremos avaliar:

- Conhecimento em HTML
- Conhecimento em fluxo de request/response
- Conhecimento em extração de dados
- Conhecimento em base64
- Boas práticas de programação
- Utilização de bibliotecas de terceiros
- Documentação
- Criatividade
- Cobertura de testes
- Tempo de execução do código
- Versionamento do código




# Doc do projeto

O crawler desenvolvido foi feito em selenium, pois o site do imdb, implementa o conteudo da pagina via javascript. Não foram utilizados scrapy, beautifulsoup ou request. Pois o seu impacto na eficiencia do scraping desses dados seria infimo, porém num caso de maior escala, seria fortemente recomendavel o uso deles. 


### requesitos:

ter python e pip instalado na maquina.
## Instalação

verificar se o python e o pip estão disponiveis para uso

```bash
  python --version
  pip --version
```
    
caso não tenha obtido a versão dos dois itens, verifique o guia de instalação do python em:

- https://www.python.org/

Antes de rodar a aplicação é necessario criar um ambiente virtual do python. Navege até o diretorio do projeto dentro dele execute :

```bash
  /desafio crawler
  python -m venv venv
```
a estrutura do projeto deve ficar assim:

    /desafio crawler
        /webscraper
        /venv

agora para rodar o ambiente virtual, dentro do diretorio \desafio-crawler insira:

bash
```bash
  source venv/Scripts/activate
```
powershell
```bash
  venv/Scripts/activate
```

navegar até o diretorio webscraper:
```bash
  cd Web_scraper
```
rodar comando:
```bash
  pip install -r requirements.txt
```
e para rodar a aplicação basta navegar até o diretorio \scr e rodar:

```bash
  python main.py
```

## Funcionalidades

- Scraping dos 250 filmes do ranking do imdb
- exporta os dados dos filmes como json e csv
- mantém o log do Scraping do site

arquivos criados:


## Screenshots

![csv_screenshot](https://github.com/YtanSilva/desafio-crawler/blob/main/Web_Scraper/img/screen_csv.png)

![json_screenshot](https://github.com/YtanSilva/desafio-crawler/blob/main/Web_Scraper/img/screen_json.png)

![log_screenshot](https://github.com/YtanSilva/desafio-crawler/blob/main/Web_Scraper/img/screen_logs.png)




