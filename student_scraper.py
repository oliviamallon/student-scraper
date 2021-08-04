#Selenium Tutorial #1
#https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
#This imports keys from a keyboard so the program can interact with the webpage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui as pa


def searchUniDays(brand_to_search):
   global output_text
   driver.get("https://www.myunidays.com")

   search = driver.find_element_by_id("search-focus")
   search.click()
   time.sleep(2)

   strUrl = driver.current_url

   search.send_keys(brand_to_search)

   time.sleep(3)
   search.send_keys(Keys.RETURN)

   # compares to see if there are search results for that shop
   # if the url hasn't changed then there are no search results
   strUrl1 = driver.current_url
   time.sleep(2)

   if (strUrl == strUrl1):
      output_text+= "\n" + ("Not Found on Unidays")
   else:
      benefitholder = driver.find_elements_by_class_name("partner-offers")[0]

      try:
         benefits = benefitholder.find_elements_by_css_selector("article.benefit:not(.benefit-filler)")
      except:
         benefits = []

      # benefits = driver.find_elements_by_css_selector("article.benefit:not(.benefit-filler)")
      num_offers = len(benefits)
      output_text+= "\n" + ("UNIDAYS OFFERS: ")
      count = 1
      if (num_offers != 0):
         for x in benefits:
            output_text+= "\n" + (str(count) + ". " + (x.find_elements_by_class_name("benefit-body")[0]).text)
            count += 1

      #print("Number of offers currently: " + str(num_offers))

   time.sleep(4)


def searchStudentBeans(brand_to_search):
   global output_text
   driver.get("https://www.studentbeans.com")
   #gets the search bar
   search = driver.find_element_by_xpath("/html/body/div[3]/div/nav/div[1]/div[1]/div/div[3]/button")
   search.click()

   time.sleep(2)
   searchbox = driver.find_elements_by_class_name("_1g5dvk1")[0]
   searchbox.send_keys(brand_to_search)
   time.sleep(2)

   #offers (discounts,related to and stocked by)
   # stored in 3 divs under this div
   offers = driver.find_elements_by_class_name("_1bazady")[0]

   try:
      #gets the div containing the actual discounts
      discountDiv = offers.find_elements_by_class_name("_i24b1r")[0]
      #gets each individual discount
      discounts_found = discountDiv.find_elements_by_tag_name("a")
   except:
      discountDiv = 0

   all_titles=""
   discounts=[]

   for x in discounts_found:
      discount_title=""
      try:
         #gets the brand of the discount
         discount_title = ((x.find_elements_by_class_name("_63p46ei")[0]).text)
         #lower makes them lowercase and strip removes whitespace at the front and end of the string
         discount_title = discount_title.lower().strip()
         brand_to_search = brand_to_search.lower().strip()

         if(discount_title == brand_to_search):
            discounts.append(x)

      except:
         discount_title = "error"

   output_text +="\n"+ ("\nSTUDENT BEANS OFFERS: ")
   if(len(discounts)!=0):
      count =1
      for x in discounts:
         #gets the actual discount for that brand
         discount_value = x.find_elements_by_class_name("_14bnlhzi")[0]
         output_text+= "\n" + (str(count) + ". " + (discount_value).text)
         count +=1
   else:
      output_text +="\n"+ ("There are no discounts found here.")


#MAIN FUNCTION

brand_to_search = pa.prompt(text='What brand would you like to search? ', title='', default='')

PATH = r"C:\Users\a1077121\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

output_text = "The brand you have searched is: " + brand_to_search+ "\nThe discounts are:\n"
searchUniDays(brand_to_search)

searchStudentBeans(brand_to_search)

pa.alert(text=output_text, title='', button='OK')
driver.close()




