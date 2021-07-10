

class LandingPage:

    def __init__(self, driver):
        self.driver = driver

    def click_createboard_icon(self):
        self.driver.find_element_by_xpath("//button[@aria-label='Create board or Workspace']").click()

    def click_createboard_option(self):
        self.driver.find_element_by_xpath("//span[text()='Create board']").click()

    def set_boardtitle_input(self,boardTitle):
        self.driver.find_element_by_xpath("//input[@placeholder='Add board title']").send_keys(boardTitle)

    def click_createboard_button(self):
        self.driver.find_element_by_xpath("//button[text()='Create board']").click()

    def click_available_board(self):
        self.driver.find_element_by_xpath("//h3[text()='YOUR WORKSPACES']//parent::div//child::div[text()='Trello Project']").click()


