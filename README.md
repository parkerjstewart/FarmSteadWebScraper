# FarmSteadWebScraper

This project was created for Find-your-farmer.com. Find-your-farmer sources food from various vendors, including Double Star Farms (https://fs27.formsite.com/doublestarfarms/fd8esnpkyu/index.html)
Double Star changes their inventory weekly, and since they have hundreds of product on their site at once, it was very challenging for us at Find Your Farmer to keep track of the changes in their inventory.
To solve this problem, I created this webscraper. The scraper runs on an AWS server, keeps track of the previous offerings from Double Star Farms in a MYSQL database, and sends emails every Monday morning 
detailing which products were added to the site, which were taken off the site, which products went out of stock, and which products are back in stock. 

The script does this by first collecting all of the products on the MYSQL database. Those products signify the previous week's offerings from Double Star Farms. 
It then scrapes the html off of Double Star's website and compiles a list of the products they are offering this week. It then compares those lists to find their differences and sends an email detailing all of the changes. 

Table of contents: 
1. HTMLScraper.py -- as the title of this file suggests, this file scrapes the Double Star Farms website, collecting all of the products currently listed on their webstie and whether or not those products are in stock. 
2. DatabaseConnector.py -- this file contains the functions necessary for communicating and interacting with the MYSQL database
3. Differences.py -- this file is responsible for determining which products have been added/taken off the site and which products are now in stock/now out of stock. 
4. EmailNotifications.py -- this file contains the functions for formatting and sending the emails, which notify Find-Your-Farmer of the changes to the site.
5. __main__.py -- brings all of these files together into one useful script that spares us hours of analysing Double Star Farms' website every week. 
