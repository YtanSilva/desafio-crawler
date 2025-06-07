from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import List
import logging
import os
from models.data_models import Movie

logger = logging.getLogger(__name__)

class IMDBScraper:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.selectors = {
            'movie_list': "li.ipc-metadata-list-summary-item",
            'title': "h3.ipc-title__text",
            'metadata': "div.cli-title-metadata span",
            'rating': "span.ipc-rating-star--rating",
            'url': "div.cli-children a.ipc-title-link-wrapper"
        }
    
    def scrape_ranking(self) -> List[Movie]:
        # Iniciando scraping da pagina
        from config.settings import Settings
        
        try:
            logger.info("Loading IMDb top movies page")
            self.driver.get(Settings.IMDB_TOP_MOVIES_URL)
            
            movie_elements = self.driver.find_elements(By.CSS_SELECTOR, self.selectors['movie_list'])
            
            if not movie_elements:
                logger.warning("No movie elements found with the given selector")
                return []
            
            logger.info(f"Found {len(movie_elements)} movies to process")
            
            with ThreadPoolExecutor(max_workers=min(32, os.cpu_count() + 4)) as executor:
                results = list(executor.map(
                    lambda x: self._extract_movie_data(x[1], x[0]),
                    enumerate(movie_elements, start=1)
                ))
            
            return [movie for movie in results if movie]
            
        except Exception as e:
            logger.error(f"Error scraping IMDb: {e}")
            raise
    
    def _extract_movie_data(self, movie_element, index: int) -> Movie:
        #Individualizando cada elemento em um objeto
        try:
            title = self._get_clean_title(movie_element)
            metadata = movie_element.find_elements(
                By.CSS_SELECTOR, self.selectors['metadata']
            )
            year = metadata[0].text if len(metadata) > 0 else 'N/A'
            duration = metadata[1].text if len(metadata) > 1 else 'N/A'
            pg = metadata[2].text if len(metadata) > 2 else 'N/A'
            rating = movie_element.find_element(
                By.CSS_SELECTOR, self.selectors['rating']
            )
            rating = rating.text if rating else 'N/A'
            url = movie_element.find_element(
                By.CSS_SELECTOR, self.selectors['url']
            )
            url = url.get_attribute('href') if url else 'N/A'
            
            if logger.isEnabledFor(logging.INFO):
                logger.info(f"Processed movie {index}: {title}")
            
            return Movie(
                title=title,
                year=year,
                duration=duration,
                pg=pg,
                rating=rating,
                url=url
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
    
    def _get_clean_title(self, movie_element) -> str:
        text_string =self._get_element_text(movie_element, self.selectors['title'])
        period_index = text_string.find('.')
        return text_string[period_index + 1:].strip() if period_index != -1 else text_string
    
    def _get_element_url(self, parent, selector: str, default: str= "N/A") -> str:
        try:
            element = parent.find_element(By.CSS_SELECTOR, selector)
            return element.get_attribute("href")
        except Exception:
            return default