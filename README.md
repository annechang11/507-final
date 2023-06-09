# Anne Chang's SI 507 Final Project

Project name: Tomato Recommender

Description:
This project uses a tree data structure to build an interactive recommendation system. The system asks the user what color and size of tomatoes they like, and recommends a corresponding tomato variety to the user. Information provided includes the variety's name, shape, days to maturity, and a link to an image of the tomato. The user can ask for recommendations again and again until they quit the system.

Package requirement:
Selenium (for scraping, but you can just load the data from the pre-processed json file.)

Files:
1) scrape.py: the program used to scrape tomato data from wikipedia
2) tomato_data.json: the scraped tomato data, saved in json format
3) tree.py: the program used to clean and process scraped data into a tree format
4) tomato_recommender.py: the program that interacts with the user and recommends tomatoes based on user input
5) images folder: images of the tomato varieties (optional; extra info of tomatoes provided to user)

How to use: 
Download the repository and run the "tomato_recommender.py" file, and you can start interact with the tomato recommender!

Thanks!

*Created by Anne Chang in April 2023. No use outside of SI 507 is permitted.*
