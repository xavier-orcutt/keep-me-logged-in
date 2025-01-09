# keep-me-logged-in

## Introduction
This Python script uses Selenium to automate browser interactions with Microsoft Edge. It opens IHS Practice Management, waits for the user to log in manually, and then refreshes the page every 10 minutes to keep the session alive, with options to terminate the script either by closing the browser or using Ctrl+C in the terminal.

## Setup

### 1. Install Python and Selenium
1. Install Python 3.8 or newer:
   * Navigate to: P folder > %TEMPORARY% > irmjd > python
   * Run the Python installer
   * Check "Add python.exe to PATH"
   * Click "Customize installation"
   * Set installation location to U drive

2. Install Selenium by opening Command Prompt and running:

```bash
pip install selenium==4.25.0
```

### 2. Install Microsoft Edge Driver
Download the Microsoft Edge WebDriver from the [official site](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/). Make sure to download the Stable Channel (x64) version.

### 3. Organize Files in the U Drive
Place the following files in the U drive:
* `kmli_script.py` - the Python script
* `msedgedriver.exe` - the Microsoft Edge WebDriver
* `python.exe` - Python executable

Storing these files on the U drive allows you to use the script from any computer.

## Executing the Script

1. Open the Command Prompt

2. Run the script using the following command:
   ```bash
   U:\python.exe U:\kmli_script.py
   ```

3. If the script is working properly, a Microsoft Edge session of IHS Practice Management will open

4. Log in to IHS Practice Management manually

5. Once logged in, press Enter in the terminal to keep the session alive

6. To stop the script, either:
   * Close the browser window
   * Press Ctrl+C in the terminal