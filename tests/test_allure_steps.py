import allure
from allure_commons.types import Severity
from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'elenarog')
@allure.feature('Allure')
@allure.story('Allure with steps')
def test_using_allure_dynamic_steps_github_issue_exists():
    with allure.step('Открыть главную страницу'):
        browser.open('/')

    with (allure.step('Найти репозиторий')):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()

    with allure.step('Перейти по ссылке репозитория'):
        ss('.search-match').element_by(have.exact_text('eroshenkoam/allure-example')).click()

    with allure.step('Открыть таб Issues'):
        s('#issues-tab').click()

    with allure.step('Проверить видимость Issue с текстом «С Новым Годом (2022)»'):
        ss('[data-hovercard-type="issue"]').element_by(have.exact_text('issue_to_test_allure_report')).should(
            be.visible)
