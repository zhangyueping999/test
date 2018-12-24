import allure


class TestLogin:
    def test_a(self):
        print("\n111")
        assert 1

    @allure.step('我是测试登录步骤')
    def test_b(self):
        allure.attach('描述', '我是测试步骤001的描述～～～')
        print("\n222")
        assert 0