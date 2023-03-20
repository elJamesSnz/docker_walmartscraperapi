from time import sleep
from random import randint
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def scrape_walmart():       
   
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')    
    driver = WebDriver(options=options)
    driver.minimize_window()
    
    url = 'https://super.walmart.com.mx/all-departments'
    # get al sitio
    driver.get(url)
    sleep(randint(2,3))

    try:    
        # verificación click & hold
        element = driver.find_element(By.XPATH, "//div[@id='px-captcha']")
        action = ActionChains(driver)
        action.move_to_element_with_offset(element, 0, 0).click_and_hold().perform()
        sleep(10)
        action.release(element)
        action.perform()
        sleep(0.2)
        action.release(element)
        # verificación click & hold
        sleep(1)
        print('Click & hold verificado')
        sleep(5)
    except:
        # no hay hold&click
        print('no hay click and hold')

    categorias = []
    for categoria_div in driver.find_elements(By.CSS_SELECTOR, 'div[class="w_C9 w_D8 w_DL w_DR w_Db tl mt4"]'):
        categoria_nombre = categoria_div.find_element(By.CSS_SELECTOR, 'h2[class="ma0"]').text    
        categoria_a = categoria_div.find_element(By.CSS_SELECTOR, "a")
        categoria_enlace = categoria_a.get_attribute("href")
        subcategorias_ul = categoria_div.find_element(By.CSS_SELECTOR, 'ul[class="pt2 pl0 list"]')

        subcategorias = []
        for subcategoria_li in subcategorias_ul.find_elements(By.CSS_SELECTOR, 'li[class="pv1 pv0-m"]'):
            subcategoria_a = subcategorias_ul.find_element(By.LINK_TEXT, subcategoria_li.text)
            subcategoria_enlace = subcategoria_a.get_attribute("href")      
            subcategoria_info = {
                'name': subcategoria_li.text,
                'url': subcategoria_enlace,        
            }
            subcategorias.append(subcategoria_info)
            
        categoria_info = {
            'name': categoria_nombre,
            'url': categoria_enlace,
            'subcategorias': subcategorias
            
        }
        categorias.append(categoria_info)

    categoriasJSON = {
        'departament': 'Despensa',
        'url': url,
        'categories' : categorias
    }

    return categoriasJSON
