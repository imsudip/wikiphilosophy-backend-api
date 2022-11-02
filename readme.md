# Wikiphilosopy-Backend-API

This is the backend API for the [Wikiphilosopy project](https://github.com/imsudip/wikiphilosophy).
It is a REST API built using Flask in Python. It uses BeautifulSoup to scrape the data from Wikipedia.

> #### Read more about the project [here](https://imsudip.github.io/wikiphilosophy/).

### Check out the Web App [here](https://imsudip.github.io/wikiphilosophy/).

### Don't forget to :star: the repo

[![GitHub stars](https://img.shields.io/github/stars/imsudip/wikiphilosophy-backend-api.svg?style=for-the-badge&label=Star)](https://github.com/imsudip/wikiphilosophy-backend-api) ![GitHub forks](https://img.shields.io/github/forks/imsudip/wikiphilosophy-backend-api.svg?style=for-the-badge&label=Forks)

## How to run

1. You need to have Python 3 installed on your system. You can download it from [here](https://www.python.org/downloads/).
2. Fetch latest source code from main branch.
   ```
    git clone https://github.com/imsudip/wikiphilosophy-backend-api.git
    cd wikiphilosophy-backend-api
   ```
3. Install dependencies.
   ```
    pip install -r requirements.txt
   ```
4. Run the server.
   ```
    python main.py
   ```
5. The server will be running on port 5000. You can access it at [http://localhost:5000](http://localhost:5000).

This Project is deployed on [Deta.sh](https://deta.sh/).
You can deploy it on your own Deta.sh account by clicking on the button below.

[![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy?repo=https://github.com/imsudip/wikiphilosophy-backend-api)

## API Endpoints

### GET /wikisearch

PARAMS: `q` - The search query to be searched on Wikipedia.
Performs a Wikipedia search and returns the results.

```
curl -X GET "http://localhost:5000/wikisearch?q=philosophy" -H "accept: application/json"
```

### GET /wiki

PARAMS: `link` - The link of the Wikipedia page to be scraped.
Scrapes the Wikipedia page and returns the data.

```
curl -X GET "http://localhost:5000/wiki?link=https://en.wikipedia.org/wiki/Philosophy" -H "accept: application/json"
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE.MD) file for details.

## Contribute

Contributions are welcome. Please read our [contributing guidelines](https://github.com/imsudip/wikiphilosophy-backend-api/blob/master/CONTRIBUTING.md) before contributing.
