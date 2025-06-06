from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import List
import logging
from models.data_models import Movie

logger = logging.getLogger(__name__)

class IMDBScraper:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def scrape_ranking(self) -> List[Movie]:
        # Iniciando scraping da pagina
        from config.settings import Settings
        
        try:
            logger.info("Loading IMDb top movies page")
            self.driver.get(Settings.IMDB_TOP_MOVIES_URL)
            
            movies = []
            movie_elements = self.driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")
            
            if not movie_elements:
                logger.warning("No movie elements found with the given selector")
                return movies
            
            logger.info(f"Found {len(movie_elements)} movies to process")
            
            for i, movie_element in enumerate(movie_elements, start=1):
                movie = self._extract_movie_data(movie_element, i)
                if movie:
                    movies.append(movie)
            
            return movies
            
        except Exception as e:
            logger.error(f"Error scraping IMDb: {e}")
            raise
    
    def _extract_movie_data(self, movie_element, index: int) -> Movie:
        #Individualizando cada elemento em um objeto
        try:
            title = self.clean_title(movie_element)
            year = self._get_element_text(movie_element, "div.cli-title-metadata span:nth-child(1)")
            duration = self._get_element_text(movie_element, "div.cli-title-metadata span:nth-child(2)")
            pg = self._get_element_text(movie_element, "div.cli-title-metadata span:nth-child(3)")
            
            logger.info(f"Processed movie {index}: {title}")
            
            return Movie(
                title=title,
                year=year,
                duration=duration,
                pg=pg
            )
        except Exception as e:
            logger.warning(f"Error processing movie {index}: {e}")
            return None
    
    def _get_element_text(self, parent, selector: str, default: str = 'N/A') -> str:
        # Metodo auxiliar de extração de dados
        try:
            element = parent.find_element(By.CSS_SELECTOR, selector)
            return element.text
        except Exception:
            return default
    
    def clean_title(self, movie_element):
        text_string =self._get_element_text(movie_element, "h3.ipc-title__text")
        period_index = text_string.find('.')
        title = text_string[period_index + 1:].strip()
        return title