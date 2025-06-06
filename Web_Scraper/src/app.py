from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time 

#search for some local webdriver if exists use it otherwise install
service = Service(ChromeDriverManager().install())

#webdriver options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36')
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(service=service, options=options)

url = 'https://www.imdb.com/chart/top/'

driver.get(url)
print("Página do IMDb carregada.")


time.sleep(2)

try:
    movies_list = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")

    if movies_list:
        print(f"Encontrados {len(movies_list)} elementos de filme.")
        for i, movie in enumerate(movies_list):
            try:
                print(f"\n--- Filme {i+1} ---")
                # print(movie.text)

                movie_title = movie.find_element(By.CSS_SELECTOR, "h3.ipc-title__text")
                movie_ano = movie.find_element(By.CSS_SELECTOR, "div.cli-title-metadata span:nth-child(1)")
                movie_runtime = movie.find_element(By.CSS_SELECTOR, "div.cli-title-metadata span:nth-child(2)")
                movie_pg = movie.find_element(By.CSS_SELECTOR, "div.cli-title-metadata span:nth-child(3)")
                print(f"Título: {movie_title.text if movie_title else 'N/A'}")
                print(f"Ano: {movie_ano.text if movie_ano else 'N/A'}")
                print(f"duração: {movie_runtime.text if movie_runtime else 'N/A'}")
                print(f"classificação: {movie_pg.text if movie_pg else 'N/A'}")

            except Exception as e_inner:
                print(f"Erro ao processar o elemento do filme {i+1}: {e_inner}")
                print(f"Texto bruto do elemento que causou erro: {movie.text}")
    else:
        print("Nenhum elemento de filme encontrado com o seletor CSS 'li.ipc-metadata-list-summary-item'.")
        print("Por favor, verifique o HTML da página do IMDb para a classe correta dos itens da lista.")

except Exception as e:
    print(f"Ocorreu um erro geral ao tentar encontrar os elementos: {e}")

time.sleep(2) # Pausa final para visualização

driver.quit()
print("Navegador fechado.")