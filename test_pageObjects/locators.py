class Locator:

    #    Login Page
    txt_username = "//input[@id='user']"
    txt_password = "//input[@id='password']"
    btn_login = "//input[@id='login']"
    btn_submit = "//button[@id='login-submit']"

    #    Landing Page
    icon_create_board = "//button[@aria-label='Create board or Workspace']"
    optn_create_board = "//span[text()='Create board']"
    txt_board_title = "//input[@placeholder='Add board title']"
    btn_create_board = "//button[text()='Create board']"
    board_available = "//h3[text()='YOUR WORKSPACES']//parent::div//child::div[text()='Trello Project']"

    #   Board Page
    icon_add_list = "//span[text()='Add a list']"
    icon_add_card = "//textarea[text()='Not Started']//parent::div//following-sibling::div/child::a/child::span[text()='Add a card']"
    txt_list_title = "//input[@placeholder='Enter list title…']"
    txt_card_title = "//textarea[@placeholder='Enter a title for this card…']"
    btn_add_list = "//input[@type='submit']"
    btn_add_card = "//input[@type='submit'][@value='Add card']"
    ele_card2_source = "//span[text()='card 2']"
    ele_inprogress_target="//textarea[text()='In Progress']/parent::div/following-sibling::div/child::a/child::span[text()='Add a card']"
    ele_card3_source = "//span[text()='card 3']"
    ele_qa_target = "//textarea[text()='QA']/parent::div/following-sibling::div/child::a/child::span[text()='Add a card']"

    #   Card Page
    ele_card1 = "//span[text()='card 1']"
    btn_add_member = "//span[text()='Members']"
    ele_loggedin_member= "//span[text()='Avinash Kannan ']"
    btn_close_addmember = "(//span[text()='Members'])[2]/following-sibling::a"
    txt_card_comments = "//textarea[@placeholder='Write a comment…']"
    btn_save_card = "//input[@type='submit'][@value='Save']"
    btn_close_card = "//h2[text()='card 1']//parent::div/parent::div//parent::div/parent::div/child::a"








