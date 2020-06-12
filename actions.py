from menu_auto import *


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testadmin.ecom.essentracomponents.com/admin/login")

login(driver)

# CREATE MAIN MENU
go_to_menu_page(driver)
add_main_menu(driver)
save(driver)
promote(driver)
time.sleep(3)
approve(driver)

# CREATE PROTECTION META CATEGORY
go_to_menu_page(driver)
add_meta_category(driver, "Protection", "/Caps")
time.sleep(3)
save(driver)
time.sleep(3)
promote(driver)
time.sleep(3)
approve(driver)

# CREATE POINT OF SALE META CATEGORY
go_to_menu_page(driver)
add_meta_category(driver, "Point of Sale", "/Tapes")
time.sleep(5)
save(driver)
time.sleep(3)
promote(driver)
time.sleep(3)
approve(driver)

# CREATE HARDWARE META CATEGORY
go_to_menu_page(driver)
add_meta_category(driver, "Hardware", "/feet-castors-glides")
time.sleep(3)
save(driver)
time.sleep(3)
promote(driver)
time.sleep(3)
approve(driver)

# CREATE ELECTRONICS META CATEGORY
go_to_menu_page(driver)
add_meta_category(driver, "Electronics", "/cable-management")
time.sleep(3)
save(driver)
time.sleep(3)
promote(driver)
time.sleep(3)
approve(driver)

#driver.close()
