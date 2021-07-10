
class BoardPage:

    def __init__(self, driver):
        self.driver = driver

    def click_addList_icon(self):
        self.driver.find_element_by_xpath("//span[text()='Add a list']").click()

    def click_addCard_icon(self):
        self.driver.find_element_by_xpath("//textarea[text()='Not Started']//parent::div//following-sibling::div/child::a/child::span[text()='Add a card']").click()

    def set_listTitle_input(self,listTitle):
        self.driver.find_element_by_xpath("//input[@placeholder='Enter list title…']").send_keys(listTitle)

    def set_cardTitle_input(self, cardTitle):
        self.driver.find_element_by_xpath("//textarea[@placeholder='Enter a title for this card…']").send_keys(cardTitle)

    def click_addList_button(self):
        self.driver.find_element_by_xpath("//input[@type='submit']").click()

    def click_addCard_button(self):
        self.driver.find_element_by_xpath("//input[@type='submit'][@value='Add card']").click()

    def dragndrop_card2_source(self):
        return self.driver.find_element_by_xpath("//span[text()='card 2']")

    def dragndrop_inProgress_target(self):
        return self.driver.find_element_by_xpath("//textarea[text()='In Progress']/parent::div/following-sibling::div/child::a/child::span[text()='Add a card']")

    def dragndrop_card3_source(self):
        return self.driver.find_element_by_xpath("//span[text()='card 3']")

    def dragndrop_qa_target(self):
        return self.driver.find_element_by_xpath("//textarea[text()='QA']/parent::div/following-sibling::div/child::a/child::span[text()='Add a card']")
