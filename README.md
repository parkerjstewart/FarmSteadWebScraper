# FarmSteadWebScraper

This project was created for Find-your-farmer.com. Find-your-farmer sources food from various vendors, including Double Star Farms (https://fs27.formsite.com/doublestarfarms/fd8esnpkyu/index.html)
Double Star changes their inventory weekly, and since they have hundreds of product on their site at once, it was very challenging for us at Find Your Farmer to keep track of the changes in their inventory.
To solve this problem, I created this webscraper. The scraper runs on an AWS server, keeps track of the previous offerings from Double Star Farms in a MYSQL database, and sends emails every Monday morning 
detailing which products were added to the site, which were taken off the site, which products went out of stock, and which products are back in stock. 

The script does this by first collecting all of the products on the MYSQL database. Those products signify the previous week's offerings from Double Star Farms. 
It then scrapes the html off of Double Star's website and compiles a list of the products they are offering this week. It then compares those lists to find their differences and sends an email detailing all of the changes. 

