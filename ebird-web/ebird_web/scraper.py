import requests
from bs4 import BeautifulSoup

# TO DO: probably move stuff like this to an env file
ID_LABELS = ['Size & Shape', 'Color Pattern', 'Behavior', 'Habitat']
ALL_ABOUT_BIRDS_URL = "https://www.allaboutbirds.org/guide/"

# TO DO: this will need to be more robust to handle things like lower case letters, characters etc. Right now assumes the input `species` is given in Title Case.
# TO DO: exception handling
def _build_url(species: str) -> str:
    """
    A function to build the URL for querying ID information about a specific bird.
    All About Birds takes a species name and maps spaces to underscores in its URL.
    """
    parsed_species = species.replace(" ", "_")
    return f"{ALL_ABOUT_BIRDS_URL}{parsed_species}/id"

# TO DO: Some of the ID headings have sub-headings - will need to separate them out and return a nested dict.
# TO DO: exception handling
def get_bird_id(species: str) -> dict:
    """
    A function to scrape the All About Birds website for a given species.
    Returns a dictionary with: 
        keys: 4 standard ID attributes 
        values: text displayed under these ID headings 
    """
    r = requests.get(url = _build_url(species))
    soup = BeautifulSoup(r.content, "html.parser")
    
    output = {}
    for label in ID_LABELS:
        output[label] = soup.find('article', {'aria-label':f'{label}'}).get_text()
    return output