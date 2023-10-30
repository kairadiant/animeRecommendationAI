import requests
from bs4 import BeautifulSoup


# Function to search for anime URL using anime name
def search_anime_url(anime_name):
    search_url = f"https://myanimelist.net/search/all?q={anime_name}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_='information')
    for result in results:
        link = result.find('a', class_='hoverinfo_trigger fw-b fl-l').get('href')
        return link
    return None


# Function to scrape anime information
def scrape_anime_info(anime_url):
    anime_data = {}
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(anime_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting anime name
        name_element = soup.find('h1', class_='title-name')
        anime_data['Name'] = name_element.text.strip() if name_element else None

        # Extracting anime genres
        genres = []
        genres_elements = soup.find_all('span', itemprop='genre')
        for genre_element in genres_elements:
            genres.append(genre_element.text.strip())
        anime_data['Genres'] = genres

        # Extracting anime rating
        rating_element = soup.find('span', itemprop='ratingValue')
        anime_data['Rating'] = float(rating_element.text.strip()) if rating_element else None

        # Extracting episode count
        information_elements = soup.find_all('div', class_='spaceit_pad')
        for item in information_elements:
            if item.find('span', class_='dark_text').text.strip() == 'Episodes:':
                anime_data['EpisodeCount'] = item.contents[-1].strip()
                break
        else:
            anime_data['EpisodeCount'] = None

        return anime_data
    except Exception as e:
        print(f"Error scraping anime data: {e}")
        return None


# Function to get similar anime recommendations
def get_similar_anime_recommendations(anime_info):
    search_url = f"https://myanimelist.net/anime.php?c[]=a&c[]=b&c[]=c&c[]=d&c[]=e&c[]=f&c[]=g&c[]=h&c[]=i&c[]=j&c[]=k&c[]=l&c[]=m&c[]=n&c[]=o&q=&show={'+'.join(anime_info['Genres'])}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_='seasonal-anime js-seasonal-anime')
    recommendations = []
    for result in results:  
        title = result.find('a', class_='link-title')
        if title:
            anime_url = f"https://myanimelist.net{title.get('href')}"
            anime_info = scrape_anime_info(anime_url)
            if anime_info['Name'] != anime_info['Name']:
                recommendations.append(anime_info)
    recommendations.sort(key=lambda x: (x['Genres'] == anime_info['Genres'], x['Rating'], x['EpisodeCount']))
    return recommendations[:5]


# Input anime name from the user
anime_name = "Shingeki no Kyojin"

# Search for the anime URL
anime_url = search_anime_url(anime_name)

if anime_url:
    # Scrape anime information using the obtained URL
    anime_info = scrape_anime_info(anime_url)

    if anime_info:
        print("Anime Information:")
        print(f"URL: {anime_url}")
        print(f"Name: {anime_info['Name']}")
        print(f"Genres: {', '.join(anime_info['Genres'])}")
        print(f"Rating: {anime_info['Rating']}")
        print(f"Episode Count: {anime_info['EpisodeCount']}")

        # Get similar anime recommendations
        recommendations = get_similar_anime_recommendations(anime_info)
        print("\nSimilar Anime Recommendations:")
        for idx, recommendation in enumerate(recommendations, start=1):
            print(f"{idx}. Name: {recommendation['Name']}")
            print(f"   Genres: {', '.join(recommendation['Genres'])}")
            print(f"   Rating: {recommendation['Rating']}")
            print(f"   Episode Count: {recommendation['EpisodeCount']}")
            print()


    else:
        print("Failed to retrieve anime information.")
else:
    print("Anime not found.")
