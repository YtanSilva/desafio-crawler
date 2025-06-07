from core.driver_manager import DriverManager
from scrapers.imdb_ranking_scraper import IMDBScraper
from config.logging.logger import setup_logging
from utils.file_exporter import export_movies_to_file
import time
import logging

def main():
    setup_logging(
        app_name='scraper',
        log_level='INFO'
     )
    logger = logging.getLogger(__name__)

    driver = None
    try:
        driver = DriverManager.get_driver()
        scraper = IMDBScraper(driver)
        
        movies = scraper.scrape_ranking()
        logger.info(f"Successfully scraped {len(movies)} movies")
        
        export_movies_to_file(movies, 'data', file_format='both')
    except Exception as e:
        logger.error(f"Application error: {e}")
    finally:
        if driver:
            time.sleep(2)
            driver.quit()
            logger.info("Browser closed")

if __name__ == "__main__":
    main()