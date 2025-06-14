🎮 Game Listings Scraper (Scrapy)
This is a Scrapy-based web scraping project that collects product information from a game store website and saves the results into a CSV file.

📁 Output Format (Games.csv)
The spider exports the following fields:

Title	Price	Status
Assassin's Creed	$59.99	In stock
Elden Ring	$69.99	In stock

🧩 Features
Scrapes game data from a paginated website

Extracts and cleans product title, price, and stock status

Saves data into a clean, structured CSV file

🔍 Extracted Fields
Each row in Games.csv includes:

Title: Game name

Price: Price of the game (e.g., $59.99)

Status: Availability (e.g., In stock, Out of stock)

🚀 Installation
Clone this repository

bash
Copy
Edit
git clone https://github.com/your-username/scrapy-games-spider.git
cd scrapy-games-spider
(Optional) Create a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install scrapy
🕷️ How to Run
Run the Scrapy spider and export results to Games.csv:

bash
Copy
Edit
scrapy crawl games -o Games.csv
games is the name of the spider (defined in games_spider.py)

🗂️ Project Structure
bash
Copy
Edit
scrapy-games-spider/
│
├── games/
│   ├── spiders/
│   │   └── games_spider.py       # The spider
│   ├── __init__.py
│   ├── items.py
│   ├── pipelines.py
│   └── settings.py
│
├── Games.csv                     # Output file
└── README.md
✅ Example Extraction Code
python
Copy
Edit
yield {
    'Title': product.css('h2.product-title::text').get(),
    'Price': product.css('span.price::text').get(),
    'Status': product.css('p.in-stock::text').get(default='').strip()
}
