from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import dbConfig

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/caminho/para/pasta/de/perfil")

browser = webdriver.Chrome(options=options)
wait = WebDriverWait(browser, 10)
browser.get("https://web.whatsapp.com/")
print("Waiting for you scan your QRcode")
  

def openUnread():
    unreadMessage = wait.until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div[3]/div/div[2]/button[2]'))
    )
    unreadMessage.click()

def menu():
    input_message = wait.until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'))
    )

    messages = [
        "Options:",
        "",
        "1 - SEE ALL PRODUCTS",
        "2 - SEE ALL CATEGORIES",
        "3 - SEE ALL BRANDS",
        "4 - EXIT",
        "",
        "Type the number of the option you want to choose:"
    ]

    for message in messages:
        input_message.send_keys(message)
        input_message.send_keys(Keys.SHIFT, Keys.ENTER)

    #input_message.send_keys(Keys.ENTER)

def readMessage():
    clientChat = browser.find_elements(By.CLASS_NAME, "_akbu")
    #_amk6 << class que engloba o horario da mensagem.
    if clientChat:
        return clientChat[-1].text

def seeAllProducts():
    products = dbConfig.selectAllProduts()
    input_message = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p')
    for product in products:
        message = f"Product: {product[1]} - Price: {product[2]}"
        input_message.send_keys(message)
        input_message.send_keys(Keys.SHIFT, Keys.ENTER)
    
    input_message.send_keys(Keys.ENTER)

def seeAllCategories():
    categories = dbConfig.selectAllCategories()
    input_message = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p')
    for category in categories:
        message = f"Category: {category[1]}"
        input_message.send_keys(message)
        input_message.send_keys(Keys.SHIFT, Keys.ENTER)
    
    input_message.send_keys(Keys.ENTER)

def seeAllBrands():
    brands = dbConfig.selectAllBrands()
    input_message = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p')
    for brand in brands:
        message = f"Brand: {brand[1]}"
        input_message.send_keys(message)
        input_message.send_keys(Keys.SHIFT, Keys.ENTER)
    
    input_message.send_keys(Keys.ENTER)


def main():
    message = True
    c = True
    while c:
        try:
            openUnread()
            c = False
        except Exception as e:
            print(f"error {e}, trying again")
            openUnread()
    i = 0
    while True:
        sleep(1)
        while message:
            sleep(2)
            try:
                bubbleNotifications = browser.find_elements(By.CLASS_NAME, "_ahlk")
                for i in range(len(bubbleNotifications)):
                    notification = bubbleNotifications[i]
                    notification.click()
                    lastMessage = readMessage()
                    print(lastMessage)

                    if lastMessage == "1":
                        print("the chosen option is 1")
                    elif lastMessage == "2":
                        print("the chosen option is 2")
                    elif lastMessage == "3":
                        print("the chosen option is 3")
                    elif lastMessage == "4":
                        print("the chosen option is 4")
                    else:
                        print("invalid option")
                        print("menu") # << this print is for represent the menu function
                        continue
                    print("menu") # << this print is for represent the menu function
                    message = False
                sleep(2)
            except Exception as e:
                print(f"error {e}")
        
        
        message = True

main()