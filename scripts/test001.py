import allure, pytest

TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'

class Test01:
    @allure.step('第一个测试步骤')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase(TEST_CASE_LINK, '测试用例')
    def test_001(self):
        allure.attach('第一个描述', '第一个标题')
        assert 0

    @allure.step('第二个测试步骤')
    @allure.severity(allure.severity_level.MINOR)
    @allure.issue('140', 'Pytest-flaky test retries shows like test steps')
    def test_002(self):
        allure.attach('第二个描述', '第二个标题')
        assert 1


if __name__ == '__main__':
    pytest.main('-s --alluredir report test001.py')
