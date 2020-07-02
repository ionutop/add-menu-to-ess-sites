from actions import *

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testadmin.ecom.essentracomponents.com/admin/login")

login(driver)

create_main_menu(driver)

create_meta_category(driver, "Protection", "/Caps")

create_meta_category(driver, "Point of Sale", "/Tapes")

create_meta_category(driver, "Hardware", "/feet-castors-glides")

create_meta_category(driver, "Electronics", "/cable-management")

add_meta_to_main_menu(driver)