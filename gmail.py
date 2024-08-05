from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def login_to_gmail(driver, email, password):
    try:
        gmail_url = "https://mail.google.com/mail/u/0/?ogbl#inbox"
        driver.get(gmail_url)
        
        time.sleep(5)

        if "https://accounts.google.com/" in driver.current_url:
         
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "identifierId"))
            )
            email_input.send_keys(email)
            
            next_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "identifierNext"))
            )
            next_button.click()
            
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "Passwd"))
            )
            password_input.send_keys(password)
            
            password_next_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "passwordNext"))
            )
            password_next_button.click()
            
           
            WebDriverWait(driver, 20).until(
                EC.url_contains("mail.google.com/mail")
            )
            
            print("Login successful")
        else:
            print("Gmail opened directly.")
        
   
        count_and_print_emails(driver)
        
    except Exception as e:
        print(f"An error occurred: {e}")

def count_and_print_emails(driver):
    try:

        emails = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr.zA.yO'))
        )
        
        email_count = len(emails)
        print(f"Total number of emails: {email_count}")
        
        for email in emails:
            try:
                sender_element = email.find_element(By.CSS_SELECTOR, 'span.yP')
                subject_element = email.find_element(By.CSS_SELECTOR, 'span.bog')
                
                sender_name = sender_element.get_attribute('name')
                sender_email = sender_element.get_attribute('email')
                subject = subject_element.text
                
                print(f"Sender: {sender_name}, Email: {sender_email}, Subject: {subject}")
                
            except Exception as e:
                print(f"Error extracting email details: {e}")
                
    except Exception as e:
        print(f"Error: {e}")

def main():
    options = Options()
    driver = webdriver.Chrome(options=options)
    email = "example@gmail.com"  #Enter your email
    password = "abc" #Enter your password
    login_to_gmail(driver, email, password)
    driver.quit()

if __name__ == "__main__":
    main()