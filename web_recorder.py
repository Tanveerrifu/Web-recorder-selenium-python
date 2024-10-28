# import time
# import cv2
# import pyautogui
# import numpy as np
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from urllib.parse import urljoin

# # Initialize Selenium WebDriver
# def initialize_driver():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--start-maximized")  # Start in full screen
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     return driver

# # Start screen recording with OpenCV
# def start_recording(output_filename="website_recording.avi", fps=12, resolution=(1920, 1080)):
#     codec = cv2.VideoWriter_fourcc(*"XVID")
#     out = cv2.VideoWriter(output_filename, codec, fps, resolution)
#     return out

# # Capture the screen in real-time
# def capture_screen(out, duration=5):
#     start_time = time.time()
#     while time.time() - start_time < duration:
#         screenshot = pyautogui.screenshot()
#         frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
#         out.write(frame)

# # Crawl all links on a page
# def get_all_links(driver, base_url):
#     links = set()
#     elements = driver.find_elements(By.TAG_NAME, "a")
#     for element in elements:
#         href = element.get_attribute("href")
#         if href and base_url in href:  # Only keep links within the same domain
#             links.add(href)
#     return list(links)

# # Main function to automate website navigation and record
# def automate_and_record_all_pages(url, recording_duration=5):
#     driver = initialize_driver()
    
#     try:
#         # Open the main page and get all links
#         driver.get(url)
#         time.sleep(3)  # Wait for the page to load
#         base_url = url.split("//")[1].split("/")[0]  # Extract base URL
#         all_links = get_all_links(driver, base_url)
        
#         visited = set()  # Track visited links

#         for link in all_links:
#             if link not in visited:
#                 visited.add(link)
                
#                 # Open the link
#                 driver.get(link)
#                 time.sleep(3)  # Wait for page to load
                
#                 # Record each page visit
#                 filename = f"recording_{link.replace('/', '_').replace(':', '')}.avi"
#                 out = start_recording(filename)
#                 capture_screen(out, duration=recording_duration)
#                 out.release()  # Stop recording for this page

#                 # Optional: Scroll down to capture the full page if it’s longer
#                 driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#                 time.sleep(2)

#     finally:
#         driver.quit()

# # Run the automation
# if __name__ == "__main__":
#     website_url = "https://lipsumhub.com"  # Target website
#     recording_time = 10  # Set recording time per page in seconds
#     automate_and_record_all_pages(website_url, recording_time)


# import time
# import cv2
# import pyautogui
# import numpy as np
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from urllib.parse import urljoin

# # Initialize Selenium WebDriver
# def initialize_driver():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--start-maximized")  # Start in full screen
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     return driver

# # Start screen recording with OpenCV
# def start_recording(output_filename="website_recording.avi", fps=12, resolution=(1920, 1080)):
#     codec = cv2.VideoWriter_fourcc(*"XVID")
#     out = cv2.VideoWriter(output_filename, codec, fps, resolution)
#     return out

# # Capture each visible portion of the page and scroll
# def capture_full_page(driver, out, scroll_height=800, wait_time=1):
#     total_height = driver.execute_script("return document.body.scrollHeight")
#     current_position = 0
    
#     while current_position < total_height:
#         # Capture the current visible area
#         screenshot = pyautogui.screenshot()
#         frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
#         out.write(frame)
        
#         # Scroll down by the specified height
#         driver.execute_script(f"window.scrollBy(0, {scroll_height});")
#         time.sleep(wait_time)  # Wait for scrolling to complete
#         current_position += scroll_height

# # Crawl all links on a page
# def get_all_links(driver, base_url):
#     links = set()
#     elements = driver.find_elements(By.TAG_NAME, "a")
#     for element in elements:
#         href = element.get_attribute("href")
#         if href and base_url in href:  # Only keep links within the same domain
#             links.add(href)
#     return list(links)

# # Main function to automate website navigation and record
# def automate_and_record_all_pages(url, recording_duration=5):
#     driver = initialize_driver()
    
#     try:
#         # Open the main page and get all links
#         driver.get(url)
#         time.sleep(3)  # Wait for the page to load
#         base_url = url.split("//")[1].split("/")[0]  # Extract base URL
#         all_links = get_all_links(driver, base_url)
        
#         visited = set()  # Track visited links

#         for link in all_links:
#             if link not in visited:
#                 visited.add(link)
                
#                 # Open the link
#                 driver.get(link)
#                 time.sleep(3)  # Wait for page to load
                
#                 # Record each page visit with full-page scroll capture
#                 filename = f"recording_{link.replace('/', '_').replace(':', '')}.avi"
#                 out = start_recording(filename)
#                 capture_full_page(driver, out, scroll_height=800, wait_time=1)
#                 out.release()  # Stop recording for this page

#     finally:
#         driver.quit()

# # Run the automation
# if __name__ == "__main__":
#     website_url = "https://katalon-demo-cura.herokuapp.com/"  # Target website
#     recording_time = 10  # Set recording time per page in seconds
#     automate_and_record_all_pages(website_url, recording_time)

# //working code

import os
import time
import cv2
import pyautogui
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Selenium WebDriver
def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Start in full screen
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# Start screen recording with OpenCV
def start_recording(output_filename="website_recording.avi", fps=12, resolution=(1920, 1080)):
    codec = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(output_filename, codec, fps, resolution)
    return out

# Capture each visible portion of the page and scroll
def capture_full_page(driver, out, scroll_height=800, wait_time=1):
    total_height = driver.execute_script("return document.body.scrollHeight")
    current_position = 0
    
    while current_position < total_height:
        # Capture the current visible area
        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
        out.write(frame)
        
        # Scroll down by the specified height
        driver.execute_script(f"window.scrollBy(0, {scroll_height});")
        time.sleep(wait_time)  # Wait for scrolling to complete
        current_position += scroll_height

# Crawl all links on a page
def get_all_links(driver, base_url):
    links = set()
    elements = driver.find_elements(By.TAG_NAME, "a")
    for element in elements:
        href = element.get_attribute("href")
        if href and base_url in href:  # Only keep links within the same domain
            links.add(href)
    return list(links)

# Main function to automate website navigation and record
def automate_and_record_all_pages(url, recording_duration=5):
    # Ensure the 'video' folder exists
    if not os.path.exists("video"):
        os.makedirs("video")
    
    driver = initialize_driver()
    
    try:
        # Open the main page and get all links
        driver.get(url)
        time.sleep(3)  # Wait for the page to load
        base_url = url.split("//")[1].split("/")[0]  # Extract base URL
        all_links = get_all_links(driver, base_url)
        
        visited = set()  # Track visited links

        for link in all_links:
            if link not in visited:
                visited.add(link)
                
                # Open the link
                driver.get(link)
                time.sleep(3)  # Wait for page to load
                
                # Record each page visit with full-page scroll capture
                filename = f"video/recording_{link.replace('/', '_').replace(':', '')}.avi"
                out = start_recording(filename)
                capture_full_page(driver, out, scroll_height=800, wait_time=1)
                out.release()  # Stop recording for this page

    finally:
        driver.quit()

# Run the automation
if __name__ == "__main__":
    website_url = "https://lipsumhub.com"  # Target website
    recording_time = 20  # Set recording time per page in seconds
    automate_and_record_all_pages(website_url, recording_time)




