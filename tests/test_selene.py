import allure
from allure_commons.types import Severity
from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'elenarog')
@allure.feature('Allure')
@allure.story('Only Selene')
def test_using_selene_github_issue_exists():
    browser.open('/')
    s('.header-search-button').click()
    s('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()
    ss('.search-match').element_by(have.exact_text('eroshenkoam/allure-example')).click()
    s('#issues-tab').click()
    ss('[data-hovercard-type="issue"]').element_by(have.exact_text('issue_to_test_allure_report')).should(be.visible)
