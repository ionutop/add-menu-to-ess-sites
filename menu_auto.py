from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import test_data
import time


def element_id(d, selector):
    x = WebDriverWait(d, 10).until(
        EC.presence_of_element_located((By.ID, selector)))
    return x


def element_selector(d, selector):
    x = WebDriverWait(d, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    return x


def element_xpath(d, selector):
    x = WebDriverWait(d, 10).until(
        EC.presence_of_element_located((By.XPATH, selector)))
    return x


def login(d):
    username = element_id(d, "username")
    username.clear()
    username.send_keys(test_data.user)

    password = element_id(d, "password")
    password.clear()
    password.send_keys(test_data.def_password)

    login_button = element_selector(d, '#js-visible > form > div.account-actions > input')
    login_button.click()


def save(d):
    save_button = element_selector(d, "body > div.app-content > div.content > div.section-content.sandboxed > div.main-content > div.sticky-container.sticky-fixed > div > div.button-group > button.button.primary.large.submit-button.primary")
    save_button.click()


def promote(d):
    promote_button_top = element_selector(d, "#sandbox-ribbon > div > div.col4.sandbox-actions-wrapper > div > div > button.button.workflow-entity-action")
    promote_button_top.click()

    promote_button_popup = element_selector(d, "body > div.modal.in > div.modal-footer > div > button")
    promote_button_popup.click()


def approve(d):
    promote_button_top = element_selector(d, "#sandbox-ribbon > div > div.col4.sandbox-actions-wrapper > div > div > button.button.workflow-entity-action")
    promote_button_top.click()

    promote_button_popup = element_selector(d, "body > div.modal.in > div.modal-footer > div > button")
    promote_button_popup.click()


def go_to_menu_page(d):
    d.get('https://testadmin.ecom.essentracomponents.com/admin/menu')


def add_main_menu(d):
    add_menu_button = element_selector(d,"body > div.app-content > div.content > div.section-content.sandboxed > div.main-content > div.sticky-container > div > button")
    add_menu_button.click()

    name_field = element_id(d, "fields'name'.value")
    name_field.send_keys('Main Menu')

    essentra_main_menu_checkbox = element_selector(d, "#field-menuType > div > div:nth-child(2) > label")
    essentra_main_menu_checkbox.click()


def add_meta_category(d, metaname, catname):
    add_menu_button = element_selector(d, "body > div.app-content > div.content > div.section-content.sandboxed > div.main-content > div.sticky-container > div > button")
    add_menu_button.click()

    name_field = element_id(d, "fields'name'.value")
    name_field.send_keys(metaname)

    meta_category_menu_checkbox = element_selector(d, "#field-menuType > div > div:nth-child(4) > label")
    meta_category_menu_checkbox.click()

    add_submenu_button = element_xpath(d, '//*[@id="menuItems"]/div[1]/div[2]/div[1]/button')
    add_submenu_button.click()

    menu_type_field = element_selector(d, "#field-type > div > div > input[type=text]")
    menu_type_field.send_keys('Essentra Category')
    actions = ActionChains(d)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(2)

    search_category = element_selector(d, "#field-essentraCategory > div > div > div > span > button.to-one-lookup-ess.secondary.button")
    search_category.click()

    select_meta_category_option = element_selector(d, "#tree-listgrid-search")
    select_meta_category_option.send_keys(catname)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(3)

    jump_to_context_button = element_selector(d, "#listGrid-tree")
    jump_to_context_button.click()

    select_sub_cat_button = element_selector(d, "body > div.modal.in.xl > div.modal-footer > div > button")
    select_sub_cat_button.click()
    time.sleep(3)

    save_popup_button = element_selector(d, "body > div.modal.in > div.modal-footer > div > button")
    save_popup_button.click()
    time.sleep(3)
    print()

    if metaname == "Electronics":
        name_field.clear()
        time.sleep(2)
        name_field.send_keys(metaname)
        time.sleep(2)
        add_submenu_button = element_selector(d, "#menuItems > div.fieldgroup-listgrid-wrapper-header.titlebar > div.listgrid-toolbar > div.listgrid-toolbar-actions > button")
        add_submenu_button.click()

        menu_type_field = element_selector(d, "#field-type > div > div > input[type=text]")
        menu_type_field.send_keys('Essentra Category')
        actions = ActionChains(d)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(2)

        search_category = element_selector(d, "#field-essentraCategory > div > div > div > span > button.to-one-lookup-ess.secondary.button")
        search_category.click()

        select_meta_category_option = element_selector(d, "#tree-listgrid-search")
        select_meta_category_option.send_keys("/fibre-management")
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(3)

        jump_to_context_button = element_selector(d, "#listGrid-tree")
        jump_to_context_button.click()

        select_sub_cat_button = element_selector(d, "body > div.modal.in.xl > div.modal-footer > div > button")
        select_sub_cat_button.click()
        time.sleep(3)

        save_popup_button = element_selector(d, "body > div.modal.in > div.modal-footer > div > button")
        save_popup_button.click()

        time.sleep(5)

        add_submenu_button = element_selector(d, "#menuItems > div.fieldgroup-listgrid-wrapper-header.titlebar > div.listgrid-toolbar > div.listgrid-toolbar-actions > button")
        add_submenu_button.click()

        menu_type_field = element_selector(d, "#field-type > div > div > input[type=text]")
        menu_type_field.send_keys('Essentra Category')
        actions = ActionChains(d)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(2)

        search_category = element_selector(d, "#field-essentraCategory > div > div > div > span > button.to-one-lookup-ess.secondary.button")
        search_category.click()

        select_meta_category_option = element_selector(d, "#tree-listgrid-search")
        select_meta_category_option.send_keys("/cable-ties-clips")
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(3)

        jump_to_context_button = element_selector(d, "#listGrid-tree")
        jump_to_context_button.click()

        select_sub_cat_button = element_selector(d, "body > div.modal.in.xl > div.modal-footer > div > button")
        select_sub_cat_button.click()
        time.sleep(3)

        save_popup_button = element_selector(d, "body > div.modal.in > div.modal-footer > div > button")
        save_popup_button.click()

        print("metacategory " + metaname + " has been added")
    else:
        print("metacategory " + metaname + " has been added")