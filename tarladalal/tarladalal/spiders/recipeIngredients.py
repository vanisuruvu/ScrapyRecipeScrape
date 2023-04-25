import scrapy
import json
import re

class RecipesSpider(scrapy.Spider):
    name = 'recipes'
    allowed_domains = ['www.tarladalal.com']
    # start_urls = ['https://www.tarladalal.com/RecipeAtoZ.aspx']
    # start_urls = ['https://www.tarladalal.com/maharashtrian-kothimbir-vadi-recipe-deep--fried-42069r']
    # with open("C:/VANI/ScrapyProjects/tarladalal/tarladalal/spiders/recipeUrls.txt", "rt") as f:
    #     start_urls = [url.strip() for url in f.readlines()]
        

    def parse(self, response):
        # f = open('AllRecipeIngredients.json')
  
        # # # # returns JSON object as a dictionary
        # data = json.load(f)
        
        # # # # Iterating through the json
        # # # # list
       
        # for i in data['recipe_ingredients']:
        #     yield ( i['ingredients'])
        
        # f.close()
        # nutrition=""
        # for row in response.xpath("//table[@id='rcpnutrients']"):
        #      nutrition = {
        #         # 'nutrient' : row.xpath('td[1]//text()').extract_first(),
        #         # 'value': row.xpath('td[2]/span//text()').extract_first() if row.xpath('td[2]/span//text()').extract_first()
        #         #     else row.xpath('td[2]//text()').extract_first() ,
        #     }
        ingredient = response.xpath("//div[@id='rcpinglist']/div/descendant-or-self::text()").extract()
        ingredient = [x for x in ingredient if x != " " and x!="\n"]
        yield{
        
           'recipeID': re.findall(r'\d+',response.request.url)[0],
            # 'recipeName': response.xpath("//*[@id='ctl00_cntrightpanel_lblRecipeName']/text()").get(),
           'ingredients': ingredient,
            # 'preparationTime': (response.xpath("//time[@itemprop='prepTime']/text()").get()) if response.xpath("//time[@itemprop='prepTime']/text()").get() 
            #             else response.xpath("//div[@id='ctl00_cntrightpanel_pnlRecipeScale']//p[2]/text()").get(),
            # 'cookingTime': (response.xpath("//time[@itemprop='cookTime']/text()").get()) if response.xpath("//time[@itemprop='cookTime']/text()").get() 
            #             else response.xpath("//div[@id='ctl00_cntrightpanel_pnlRecipeScale']//p[2]/text()").get(),
            # 'preparationMethod': response.xpath("//div[@id='recipe_small_steps']//li[@itemprop = 'itemListElement']/span/descendant-or-self::*/text()").extract(),
            # 'nutritionInfo': nutrition,
            #         #  if response.xpath("td[1]/descendant-or-self::*/text()").extract(),
            #             # else response.xpath("td[1]/descendant-or-self::*/text()").extract() +" "+ ''.join( response.xpath("td[2]/descendant-or-self::*/text()").extract()),
           'recipeURL': response.request.url,

            # 'product': recipe.xpath(".//div[@class='p_box_price']/span[1]/text()").get(),
            # 'product': recipe.xpath(".//div[@class='p_box_price']/span[2]/text()").get()
        }
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
