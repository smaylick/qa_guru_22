import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_onboarding_screen(context):
    if context == 'bs':
        pytest.skip()

    with step('Проверка первого экрана'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.text('Свободная энциклопедия'))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

    with step('Проверка второго экрана'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.text('Новые способы исследований'))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

    with step('Проверка третьего экрана'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.text('Списки для чтения с синхронизацией'))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

    with step('Проверка четвёртого экрана'):
        browser.element((AppiumBy.CSS_SELECTOR, "android.widget.TextView")).should(have.text('Data'))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")).click()

    with step('Проверка главного экрана'):
        browser.element((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.text('Поиск по Википедии'))


def test_android_search_wiki_Appium_bstack(context):

    if context == 'local':
        pytest.skip()

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))