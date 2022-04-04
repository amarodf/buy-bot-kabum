from os import system
from selenium import webdriver
from time import sleep
from twocaptcha import TwoCaptcha

solver = TwoCaptcha('API_KEY')


CHROME_DRIVER_PATH = 'C:\Program Files (x86)\chomedriver.exe'
driver = webdriver.Chrome(CHROME_DRIVER_PATH)

# url do que comprar 
PRO_URL= 'https://www.kabum.com.br/produto/166104/placa-de-video-zotac-nvidia-geforce-rtx-3060-ti-twin-edge-lhr-8gb-14-0-gbps-gddr6-dlss-ray-tracing-zt-a30610e-10mlhr'

MAX_PRICE = 10

#login info 

EMAIL = 'xxxxxxx@gmail.com'
PASSWORD = 'xxxx'

driver.get(PRO_URL)
add_to_cart_button = driver.find_element_by_xpath('//*[@id="blocoValores"]/div[2]/button')
add_to_cart_button.click()

skip_to_cart =  driver.find_element_by_xpath('//*[@id="__next"]/div[1]/section/div/div[3]/button[2]')
skip_to_cart.click()

skip_to_checkout = driver.find_element_by_xpath('//*[@id="__next"]/section/section/section/div[6]/button')
skip_to_checkout.click()

open_login = driver.find_element_by_xpath('//*[@id="opcao-2"]')
open_login.click()

user = driver.find_element_by_xpath('//*[@id="lemail"]')
user.send_keys(EMAIL)

password = driver.find_element_by_xpath('//*[@id="lsenha"]')
password.send_keys(PASSWORD)

login = driver.find_element_by_xpath('//*[@id="form-login"]/div/button')
login.click()

shipping_option = driver.find_element_by_xpath('//*[@id="__next"]/section/section/section/div[3]/div/div[2]/div[2]/label[3]/div[2]')
shipping_option.click()

go_to_payment_option = driver.find_element_by_xpath('//*[@id="__next"]/section/section/section/div[6]/button')
go_to_payment_option.click()

credit_card_option = driver.find_element_by_xpath('//*[@id="payment-form"]/details[3]/summary/div')
credit_card_option.click()

card_name = driver.find_element_by_xpath('')
card_name.send_keys("1111111111")

card_number = driver.find_element_by_xpath('')
card_number.send_keys("1111111111")

good_thru = driver.find_element_by_xpath('')
good_thru.send_keys("1111111111")

cvv = driver.find_element_by_xpath('')
cvv.send_keys("1111111111")

cpf = driver.find_element_by_xpath('')
cpf.send_keys("1111111111")

birthday = driver.find_element_by_xpath('')
birthday.send_keys("1111111111")

buy = driver.find_element_by_xpath('//*[@id="__next"]/section/section/section/div[6]/button')
buy.click()

privacy_policy = driver.find_element_by_xpath('//*[@id="__next"]/section/section/section/form/div[12]/label/span')
privacy_policy.click()

try:
    result = solver.recaptcha(
        sitekey='6LfDxboZAAAAAD6GHukjvUy6lszoeG3H4nQW57b6',
        url='https://2captcha.com/demo/recaptcha-v2-invisible?level=low')

except Exception as e:
    system.exit(e)

else:
    system.exit('result: ' + str(result))

confirm_buy = driver.find_element_by_xpath('//*[@id="__next"]/section/section/section/form/div[13]/button')
confirm_buy.click()

print("Pedido realizado com sucesso")