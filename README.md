# Flipkart Review Scraper

This is a Flask-based web application for scraping product reviews from Flipkart. It allows users to search for products, fetch reviews, and display them on a web page.

## Table of Contents
- [Demo](#demo)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Demo
You can view the Demo LinkedIn post by following this [link](https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7052045923731857408).

## Features
- Search for a product on Flipkart.
- Scrape and display product reviews.
- Show product name, price, and images.
- Write reviews to a CSV file.
- Error handling and logging for robustness.

## Installation
Provide instructions on how to install and set up the project locally. Include any prerequisites.

```bash
# Clone the repository
git clone https://github.com/yourusername/flipkart-review-scraper.git
cd flipkart-review-scraper
```

# Install dependencies
pip install -r requirements.txt

## Usage
Explain how to use the application:

1. Start the Flask application using [`python app.py`.](app.py)

Replace here "username" and "password" with their actual MongoDB credentials. Here's a code snippet with comments to guide the user:

```python
# Replace 'username' and 'password' with your MongoDB database credentials
# Example: 'my_actual_username' and 'my_actual_password'

client = pymongo.MongoClient("mongodb+srv://my_actual_username:my_actual_password@cluster0.ln0bt5m.mongodb.net/?retryWrites=true&w=majority")
db = client['scrapper']
coll = db['scraper_coll']
coll.insert_many(reviews
```

In the code snippet you provided, the lines `db = client['scrapper']` and `coll = db['scraper_coll']` are used to interact with a specific database and collection within a MongoDB database.

1.1 `db = client['scrapper']`:
   - `client` is an instance of the `pymongo.MongoClient` class, which is used to connect to a MongoDB server.
   - MongoDB databases are organized into collections, and each collection can contain documents (i.e., data records).
   - In this line, the code creates a variable `db` and associates it with a specific database named 'scrapper' within the MongoDB server. You can replace 'scrapper' with the actual name of the database you want to interact with.

1.2 `coll = db['scraper_coll']`:
   - Once you have a reference to the database, you can further specify the collection you want to work with.
   - In this line, the code creates a variable `coll` and associates it with a specific collection named 'scraper_coll' within the 'scrapper' database. You should replace 'scraper_coll' with the actual name of the collection you want to use.

After these two lines, you can use the `coll` variable to interact with the 'scraper_coll' collection, which may include operations like inserting, updating, querying, or deleting documents in that collection. Similarly, you can use the `db` variable to perform database-level operations within the 'scrapper' database.

   
3. Access the application in a web browser at [http://localhost:5000](http://localhost:5000).
4. Enter the product name in the search box and click the search button.
5. View the scraped reviews, product details, and images.

## Dependencies

List the major dependencies used in your project. You can also include the version numbers.

- Flask
- Flask-CORS
- BeautifulSoup
- Requests
- pymongo (commented out)

## Contributing

We welcome contributions to our project. If you'd like to contribute, please follow these guidelines:

1. **Fork the project:** Click the "Fork" button on the top right of the project's GitHub page. This will create a copy of the project in your own GitHub account.

2. **Create a new branch:** Before you start making changes, create a new branch in your forked repository. This branch should have a descriptive name related to the feature or bug you're working on.

3. **Make your changes:** Make your desired changes in the code. Be sure to follow any coding standards or style guidelines that the project may have.

4. **Test your changes:** Ensure that your changes work as expected and do not introduce new issues. If the project has tests, run them to confirm that your changes don't break existing functionality.

5. **Create a pull request (PR):** When you're ready to contribute your changes, create a pull request from your branch to the original project. Provide a clear and concise description of your changes, along with any relevant details. The project maintainers will review your PR, and if it's approved, it will be merged into the project.


I appreciate your contributions and thank you for helping make our project better!


## License

This project is licensed under the [GNU General Public License v3.0](LICENSE). See the [LICENSE](LICENSE) file for more details.

**Note**: Provide links to any related documents or additional information, and make sure to keep your README up-to-date as your project evolves.
