import requests
from bs4 import BeautifulSoup
import json
import openai

# OpenAI API key
openai.api_key = 'your_openai_api_key_here'

# Function to find a page with the word "cat"
def find_cat_page():
    search_url = "https://icanhas.cheezburger.com/search/cat"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the first link to a cat-related page
    cat_page_link = None
    for a_tag in soup.find_all('a', href=True):
        if 'cat' in a_tag.text.lower():
            cat_page_link = a_tag['href']
            break

    if cat_page_link:
        return cat_page_link
    else:
        return "https://icanhas.cheezburger.com/"  # Default to homepage if no link is found

# Scraper function to fetch memes from a given page
def fetch_memes():
    cat_page_url = find_cat_page()
    response = requests.get(cat_page_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    memes = []
    for img_tag in soup.find_all('img', class_='resp-media'):
        img_url = img_tag['src']
        if img_url.endswith(('.jpg', '.png')):
            memes.append(img_url)
    
    return memes

# AI function to generate captions for memes
def generate_caption():
    prompt = "Generate a funny caption for a cat meme."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=30
    )
    return response.choices[0].text.strip()

# Save memes and captions to a JSON file
def save_memes_to_file(meme_data):
    with open('memes.json', 'w') as f:
        json.dump(meme_data, f)

# Main function to scrape memes and save them to a file
def scrape_and_save_memes():
    memes = fetch_memes()

    meme_data = []
    for meme_url in memes[:10]:  # Fetch top 10 memes for now
        caption = generate_caption()
        meme_data.append({'url': meme_url, 'caption': caption})

    save_memes_to_file(meme_data)

if __name__ == "__main__":
    scrape_and_save_memes()
