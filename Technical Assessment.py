# Import necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the browser
browser = webdriver.Chrome()


# Function to wait for an element to be displayed
def wait_for_element(locator, timeout=10):
    return WebDriverWait(browser, timeout).until(EC.visibility_of_element_located(locator))


# Function to navigate to the Home page
def navigate_to_home_page():
    home_button = wait_for_element((By.XPATH, '//li[@class='m_nav-item m_active']//a[@class='m_nav-link']'))
    home_button.click()

# Test 1: Login tset
def test_login():
    # Navigate to the home_page
    navigate_to_home_page()

    # Assert that both email and password inputs are present
    email_input = wait_for_element((By.XPATH, '//input[@id="m_inputEmail"]'))
    password_input = wait_for_element((By.XPATH, '//input[@id="m_inputPassword"]'))
    login_button = wait_for_element((By.XPATH, '//button[normalize-space()="Sign in"]'))

    assert email_input.is_displayed() # is_displayed() to check if the email input, password input, and login button are present and visible on the page.
    assert password_input.is_displayed()
    assert login_button.is_displayed()

    # Enter email and password
    email_input.send_keys("test1@gmail.com")
    password_input.send_keys("password12345@")

    # Submit the form and assert successful login
    login_button.click()

# Test 2: List Group Test
def test_list_group():
    # Navigate to the home page
    navigate_to_home_page()

    # Assert that there are three values in the list group
    list_items = browser.find_elements(By.XPATH, '//div[@id="m_test-2-div"]//ul[@class="list-group"]/li')
    assert len(list_items) == 3

    # Assert the second list item's value and badge value
    second_list_item = list_items[1]
    assert second_list_item.text == "List Item 2"
    assert second_list_item.find_element(By.XPATH, './span[normalize-space()="6"]').text == "6"

# Test 3: Select Option Test
def test_select_option():
    # Navigate to the home page
    navigate_to_home_page()

    # Assert default selected value "Option 1" and select "Option 3"
    default_option = wait_for_element((By.XPATH, '(//button[normalize-space()="Option 1"])[1]'))
    assert default_option.is_selected()

    option_3 = wait_for_element((By.XPATH, '//a[normalize-space()="Option 3"]'))
    option_3.click()

# Test 4: Button State Test
def test_button_state():
    # Navigate to the home page
    navigate_to_home_page()

    # Assert that the first button is enabled and the second button is disabled
    button_1 = wait_for_element((By.XPATH, '(//button[@type="button"][normalize-space()="Button"])[1]'))
    button_2 = wait_for_element((By.XPATH, '(//button[@class="m_btn m_btn-lg m_btn-secondary"])[1]'))

    assert button_1.is_enabled()
    assert not button_2.is_enabled()

# Test 5: Dynamic Button Test
def test_dynamic_button():
    # Navigate to the home page
    navigate_to_home_page()

    # Wait for a button to be displayed (random delay)
    dynamic_button = wait_for_element((By.XPATH, '(//div[@id="m_test5-alert"])[1]'))

    # Click the dynamic button
    dynamic_button.click()

    # Assert success message and button disabled state
    success_message = wait_for_element((By.XPATH, '//div[@id="successMessage"]'))
    assert success_message.is_displayed()

    assert not dynamic_button.is_enabled()

# Test 6: Grid Cell Value Test
def test_grid_cell_value():
    # Navigate to the home page
    navigate_to_home_page()

    # Write a method to find the value of any cell on the grid
    def get_cell_value(row, col):
        # The get_cell_value function uses the provided coordinates (2, 2) to dynamically locate the cell in the grid and retrieve its text content.
        cell_locator = (By.XPATH, f'//table[@id="gridTable"]//tr[{row + 1}]/td[{col + 1}]')
        return wait_for_element(cell_locator).text

    # Use the method to find the value of the cell at coordinates 2, 2
    cell_value_2_2 = get_cell_value(2, 2)

    # Assert that the value of the cell is "Ventosanzap"
    assert cell_value_2_2 == "Ventosanzap"