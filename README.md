# animeRecommendationAI
**Anime Recommendation AI**

This Python script utilizes web scraping techniques to provide anime recommendations based on a given anime title. It leverages the MyAnimeList website to fetch information about the input anime and then suggests similar anime titles based on genre, rating, and episode count.

### How It Works:

1. **Searching for Anime URL:**
   - The script starts by searching for the given anime title on MyAnimeList to find its URL.
   - If the anime is found, the script proceeds to scrape its information.

2. **Scraping Anime Information:**
   - The script scrapes the anime's name, genres, rating, and episode count from its MyAnimeList page.
   - It simulates a user agent to access the website and extract the necessary data.

3. **Finding Similar Anime:**
   - Using the genres of the input anime, the script searches for other anime titles with similar genres on MyAnimeList.
   - It then retrieves information about these similar anime, including name, genres, rating, and episode count.

4. **Displaying Recommendations:**
   - The script displays the information about the input anime and a list of similar anime recommendations.
   - Recommendations are sorted based on genre similarity, rating, and episode count.

### How to Use:

- **Requirements:**
  - Python 3.x
  - `requests` library
  - `beautifulsoup4` library

- **Instructions:**
  1. Ensure you have Python installed on your system.
  2. Install the required libraries using the following commands:
     ```
     pip install requests
     pip install beautifulsoup4
     ```
  3. Run the script and input the desired anime title when prompted.
  4. The script will output the information of the input anime and provide a list of similar anime recommendations.

Feel free to explore and modify the script to enhance its functionality or integrate it into other applications. For any issues or queries, please contact the developer.

**Note:** This script relies on web scraping, and changes in the structure of the MyAnimeList website may affect its functionality.
