from core.driver_manager import DriverManager
from scrapers.imdb_ranking_scraper import IMDBScraper
import time

def main():

    driver = None
    try:
        driver = DriverManager.get_driver()
        scraper = IMDBScraper(driver)
        
        movies = scraper.scrape_ranking()
        print(f"Successfully scraped {len(movies)} movies")
        
        # Here you could add code to save the movies to a file/database
        # using functions from utils.storage
        
    except Exception as e:
        print(f"Application error: {e}")
    finally:
        if driver:
            time.sleep(2)  # Final pause for visualization
            driver.quit()
            print("Browser closed")

if __name__ == "__main__":
    main()