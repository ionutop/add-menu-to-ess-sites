from actions import *
from test_data import admin, all_locales


for loc in all_locales:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(admin + "/login")

    login(driver, loc)

    create_main_menu(driver)

    if loc != "us" and loc != "ca":
        create_meta_category(driver, "Protection", "/Caps", loc)
    else:
        pass

    create_meta_category(driver, "Point of Sale", "/Tapes", loc)

    create_meta_category(driver, "Hardware", "/feet-castors-glides", loc)

    create_meta_category(driver, "Electronics", "/cable-management", loc)

    add_meta_to_main_menu(driver, loc)

    time.sleep(2)
    driver.close()
