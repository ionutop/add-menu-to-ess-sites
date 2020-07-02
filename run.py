from actions import *
from test_data import locale

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testadmin.ecom.essentracomponents.com/admin/login")

login(driver)

create_main_menu(driver)

if locale != "us" and locale != "ca":
    print(type(locale))
    create_meta_category(driver, "Protection", "/Caps")
else:
    pass

create_meta_category(driver, "Point of Sale", "/Tapes")

create_meta_category(driver, "Hardware", "/feet-castors-glides")

create_meta_category(driver, "Electronics", "/cable-management")

add_meta_to_main_menu(driver)