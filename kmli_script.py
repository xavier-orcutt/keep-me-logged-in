from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import WebDriverException
import time

# Path to the Edge webdriver
webdriver_path = r'U:\msedgedriver.exe'

# Set up Edge options to open in InPrivate mode
edge_options = Options()
edge_options.add_argument('--log-level=3')

# Initialize the webdriver with the Service object and options
webdriver_service = Service(webdriver_path)
driver = webdriver.Edge(service = webdriver_service, options = edge_options)

# Open IHS Practice Management
url = 'https://navchc-tstrpms.d1.na.ihs.gov/authentication/login'
driver.get(url)

# Waiting for user to manually log in 
input("Log in to IHS Practice Management, then press Enter in terminal to keep the session alive. To stop the script, press Ctrl+C in terminal or close the browser.")

# Start the session keep-alive process
try:
    while True:
        try:
            driver.refresh()
            print('Page refreshed. Session is active.')

            # Wait 600 seconds before refreshing again. 
            time.sleep(600)
        except WebDriverException:
            print('Browser was closed. Exiting script.')
            break

except KeyboardInterrupt:
    # If the script is stopped in terminal (Ctrl+C), quit the browser
    print('Script was terminated in terminal. Closing browser.')

finally:
    # Make sure the driver is quit to avoid hanging processes 
    driver.quit()
