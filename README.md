# ScrapyRecipeScrape
![image](https://user-images.githubusercontent.com/76887982/233875246-de4d16f1-0e48-4055-846a-1e881d236b52.png)
1. Execute above commands. 
2. Retrieve url list for recipes starting with A. in recipes.py
```
import scrapy
import json
import re

class RecipesSpider(scrapy.Spider):
    name = 'recipes'
    allowed_domains = ['www.tarladalal.com']
    start_urls = ['https://www.tarladalal.com/RecipeAtoZ.aspx']
    def parse(self, response):
        #  for recipe in response.xpath("//span[@class='rcc_recipename']/a"):
        #     yield{
        #         'recipe':recipe.xpath("./@href").get(),
        #         'url': response.urljoin(recipe.xpath("./@href").get())
        #         # 'product': recipe.xpath(".//div[@class='p_box_price']/span[1]/text()").get(),
        #         # 'product': recipe.xpath(".//div[@class='p_box_price']/span[2]/text()").get()
        #     }
        #     next_page = response.urljoin(response.xpath("//a[@class='rescurrpg']/following-sibling::a[1]/@href").get())
        #     if next_page:
        #         yield scrapy.Request(url=next_page, callback=self.parse)
		```
3. Extract recipe urls into Aurls.txt file: in recipes.py
def parse(self, response):
        # f = open('recipes_A_Urls.json')
  
        # # returns JSON object as a dictionary
        # data = json.load(f)
        
        # # Iterating through the json
        # # list
        # for i in data['recipe_A']:
        #     url = i['url']  // yield
 4. Use url links in Aurls.txt and retrieve each recipe details going to each url in the txt file, using recipes.py file
