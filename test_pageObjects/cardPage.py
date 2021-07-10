class CardPage:

    def __init__(self, driver):
        self.driver = driver

    def click_card(self):
        self.driver.find_element_by_xpath("//span[text()='card 1']").click()

    def click_addMember(self):
        self.driver.find_element_by_xpath("//span[text()='Members']").click()

    def select_member(self):
        self.driver.find_element_by_xpath("//span[text()='Avinash Kannan ']").click()

    def close_addMember(self):
        self.driver.find_element_by_xpath("(//span[text()='Members'])[2]/following-sibling::a").click()

    def set_comments_input(self,comments):
        self.driver.find_element_by_xpath("//textarea[@placeholder='Write a comment…']").send_keys(comments)

    def click_saveCard_button(self):
        self.driver.find_element_by_xpath("//input[@type='submit'][@value='Save']").click()

    def click_closecrad_button(self):
        self.driver.find_element_by_xpath("//h2[text()='card 1']//parent::div/parent::div//parent::div/parent::div/child::a").click()
