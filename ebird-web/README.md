# ebird-web
A Python library to scrape the [All About Birds](https://www.allaboutbirds.org) site for distinguishing features and characteristics of bird species.

# Install
`python -m pip install .`

# To Do
<input type="checkbox"> Basic web scraper with `beautifulsoup`:

* <input type="checkbox"> Output data format?
* <input type="checkbox"> Standard fields/characteristics to scrape?
* <input type="checkbox"> Key words for bird biology/anatomy?
* <input type="checkbox"> Do we need our own db?

<input type="checkbox"> Unit tests

<input type="checkbox"> Integration with [LangChain](https://python.langchain.com/docs/introduction/) ?

# Done 

<input type="checkbox" checked> Get API key: https://ebird.org/api/keygen

* API key being stored locally with Liz

<input type="checkbox" checked> Check out [ebird-api](https://github.com/ProjectBabbler/ebird-api) Python library (might not need to write our own API wrapper?)

* Could be generally useful but we probably won't require it
* We'll be scraping the [All About Birds ID](https://www.allaboutbirds.org/guide/Baltimore_Oriole/id) page which only requires the **common name**, which will be displayed to the user

    * Unfortunately currently limited to only North American birds 