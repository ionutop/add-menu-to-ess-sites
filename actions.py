from menu_auto import *
from test_data import *


# CREATE MAIN MENU
def create_main_menu(d):
    go_to_menu_page(d)
    add_main_menu(d)
    save(d)
    promote(d)
    time.sleep(3)
    approve(d)


# CREATE PROTECTION META CATEGORY
def create_meta_category(d, name, link):
    go_to_menu_page(d)
    add_meta_category(d, name, link)
    time.sleep(3)
    save(d)
    time.sleep(3)
    promote(d)
    time.sleep(3)
    approve(d)


# ADD META TO MENU
def add_meta_to_main_menu(d):
    go_to_menu_page(d)
    add_meta_to_menu(d, "Point of Sale")
    time.sleep(2)
    if locale != "us" and locale != "ca":
        go_to_menu_page(d)
        add_meta_to_menu(d, "Protection")
        time.sleep(2)
    else:
        pass
    go_to_menu_page(d)
    add_meta_to_menu(d, "Hardware")
    time.sleep(2)
    go_to_menu_page(d)
    add_meta_to_menu(d, "Electronics")
    time.sleep(2)
    promote(d)
    time.sleep(2)
    approve(d)
    time.sleep(2)
    d.close()
