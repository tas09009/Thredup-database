import requests, re
from bs4 import BeautifulSoup
from selenium import webdriver
from lxml import etree
import lxml.html
import urllib.request



url = 'https://www.thredup.com/petite?department_tags=petite&sizing_id=755%2C765%2C778%2C750%2C756%2C774%2C791%2C799&skip_equivalents=true'

# Parse HTML and pull all href links
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')





# ------------------------------------------------------------------------------------

def product_href(): # Could use url as a parameter...
    '''
    Listed products's url from a search result: 
    '''
    # Empty list to be used later for list_link
    product_list = []
    
    for page_number in range(1,2): # Everytime range increases, items increase by 50
        url_page = ((url) + str(page_number))

        # Parse HTML and pull all href links
        response = requests.get(url_page)
        soup = BeautifulSoup(response.text, 'html.parser')

        grid_products = soup.findAll('div', {'class': 'uiUj-TxKXzmIOHZu6poxM grid-item'})
        for i in grid_products:
            product = i.find('a', {'class': '_1di0il_2VkBBwWJz9eDxoJ'}).get('href')
            product_list.append(product)
    
    url_front = 'https://www.thredup.com'
    list_link = [url_front + a for a in product_list]
    return list_link 


# print(product_href())
print(type(product_href))



'''
['https://www.thredup.com/product/women-polyester-bonworth-blue-pullover-sweater/71513293?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-wool-american-eagle-outfitters-pink-cardigan/71160866?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-polyester-liz-claiborne-black-zip-up-hoodie/71325226?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-supima-cotton-jjill-red-long-sleeve-turtleneck/71601482?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-cotton-banana-republic-factory-store-blue-jacket/68887601?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-cotton-jjill-yellow-long-sleeve-blouse/68856138?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-nylon-zella-red-active-tank/72251660?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-cotton-talbots-outlet-white-34-sleeve-blouse/72292413?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-levis-purple-tank-top/72279600?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-polyester-coldwater-creek-teal-fleece/72153964?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-merino-wool-ann-taylor-loft-red-wool-cardigan/72143977?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-rayon-ann-taylor-loft-green-long-sleeve-blouse/72247483?sizing_id=755,765,778,750,756,774,791,799', 
'https://www.thredup.com/product/women-cotton-gap-green-khakis/75279998?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-polyester-c9-by-champion-black-active-pants/74891677?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-cotton-ann-taylor-loft-black-casual-skirt/74922020?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-polyester-ann-taylor-loft-black-casual-skirt/74931711?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-cotton-old-navy-black-cardigan/75544955?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-lambswool-talbots-black-wool-cardigan/67081710?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-rayon-old-navy-orange-casual-dress/71315483?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-silk-ann-taylor-black-sleeveless-silk-top/71392036?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-viscose-ann-taylor-gray-pullover-sweater/71354463?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-linen-ann-taylor-loft-brown-blazer/71908747?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-c9-by-champion-blue-active-pants/74828978?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-polyester-ann-taylor-tan-casual-dress/65618274?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-polyester-ann-taylor-loft-teal-long-sleeve-blouse/69663473?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-polyester-ann-taylor-loft-ivory-long-sleeve-blouse/70784171?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-polyester-aerie-black-active-pants/75441746?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-polyester-ann-taylor-factory-white-short-sleeve-blouse/75575421?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-cotton-ann-taylor-loft-green-cardigan/75569068?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-polyester-ann-taylor-loft-brown-dress-pants/75512905?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-polyester-athleta-blue-active-pants/75396595?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-polyester-banana-republic-gray-casual-dress/75553803?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-silk-ann-taylor-black-silk-skirt/70506579?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-cotton-ann-taylor-loft-gray-pullover-sweater/74269989?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-wool-linda-allard-ellen-tracy-teal-jacket/64487452?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-polyester-merona-white-casual-dress/72341464?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-polyester-como-blu-white-long-sleeve-blouse/72335561?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-cotton-banana-republic-purple-long-sleeve-button-down-shirt/72289060?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-polyester-mondetta-black-jacket/72463252?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-acrylic-assorted-brands-brown-vest/72281965?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-rayon-ann-taylor-loft-ivory-casual-skirt/70976370?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-nylon-ann-taylor-brown-short-sleeve-blouse/74345102?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-cotton-jcrew-ivory-long-sleeve-blouse/68952302?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-polyester-ann-taylor-loft-outlet-red-casual-dress/67007422?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-polyester-banana-republic-factory-store-black-jacket/68044342?sizing_id=755,765,778,750,756,774,791,799', 
'https://www.thredup.com/product/women-polyamide-assorted-brands-white-active-pants/73368240?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-triacetate-ann-taylor-black-blazer/73433929?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-cotton-express-blue-long-sleeve-button-down-shirt/73290011?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-viscose-american-eagle-outfitters-white-casual-dress/67776759?sizing_id=755,765,778,750,756,774,791,799', 'https://www.thredup.com/product/women-silk-banana-republic-green-casual-dress/67582737?sizing_id=755,765,778,750,756,774,791,799']
'''