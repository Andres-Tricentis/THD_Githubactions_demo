from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_google():
    # Set up options for headless Chrome
    options = Options()
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--no-sandbox')  # Disable sandboxing (needed for CI environments)
    options.add_argument('--disable-dev-shm-usage')  # Prevent issues with shared memory in CI
    options.add_argument('--remote-debugging-port=9222')  # Disable DevToolsActivePort error

    # Initialize Chrome with options
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()