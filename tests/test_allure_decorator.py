import allure
from allure_commons.types import Severity
from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'elenarog')
@allure.feature('Allure')
@allure.story('Allure with decorator')
def test_using_allure_decorator_steps_github_issue_exists():
    open_main_page()
    find_repo('eroshenkoam/allure-example')
    open_repo_link('eroshenkoam/allure-example')
    open_issues_tab()
    check_issue_exists('issue_to_test_allure_report')


@allure.step('Открыть главную страницу')
def open_main_page():
    browser.open('/')


@allure.step('Найти репозиторий {repo}')
def find_repo(repo):
    s('.header-search-button').click()
    s('#query-builder-test').send_keys(repo).press_enter()


@allure.step('Перейти по ссылке репозитория {repo}')
def open_repo_link(repo):
    ss('.search-match').element_by(have.exact_text(repo)).click()


@allure.step('Открыть таб Issues')
def open_issues_tab():
    s('#issues-tab').click()


@allure.step('Проверить видимость Issue с текстом {issue_text}')
def check_issue_exists(issue_text):
    ss('[data-hovercard-type="issue"]').element_by(have.exact_text(issue_text)).should(be.visible)
