import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

email = "jannowak@o2.pl"
name ="Jan"
surname = "Kowalski"
password = "12345"
birthdate_dmr = ['1', '7', '1987']

# Tworzę nową klasę dziedziczącą
# po TestCase z modułu unittest
# W której zawarte są mechanizmy
# uruchamiania testów
class TestRegistration(unittest.TestCase):
    """
    Mój scenariusz/przypadek testowy
    """
    def setUp(self) -> None:
        """
        Warunki wstępne testu
        """
        # Otwieram przeglądarkę
        self.driver = webdriver.Chrome()
        # ... na stronie http://automationpractice.com/index.php
        self.driver.get("http://automationpractice.com/index.php")
        # Maksymalizuj okno
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    # Tutaj będzie prawdziwy test
    def testCorrectRegistration(self):
        # 1. Kliknij przycisk „Sign in”
        signin_btn = self.driver.find_element_by_class_name("login")
        signin_btn.click()
        # self.driver.find_element_by_class_name("login").click()
        # 2. Wpisz adres e-mail
        email_input = self.driver.find_element_by_id("email_create")
        email_input.send_keys(email)
        # 3. Kliknij „Create an account”
        create_btn = self.driver.find_element_by_id("SubmitCreate")
        create_btn.click()
        # 4. Wybierz tytuł (płeć)
        gender_rbtn = self.driver.find_element_by_id("id_gender1")
        gender_rbtn.click()
        # 5. Wpisz imię
        name_input = self.driver.find_element_by_id("customer_firstname")
        name_input.send_keys(name)
        # 6. Wpisz nazwisko
        surname_field = self.driver.find_element_by_id("customer_lastname")
        surname_field.send_keys(surname)
        # 7. Sprawdź uzupełniony e-mail
        email_input_on_form = self.driver.find_element_by_id("email")
        email_value = email_input_on_form.get_attribute("value")
        # Porównaj oba adresy
        # Zgłoś błąd, gdy nie będą się zgadzać
        assert email_value==email, "LIPA!!! Adresy się nie zgadzają"
        # 8. Podaj hasło
        password_input = self.driver.find_element_by_xpath('//input[@id="passwd"]')
        password_input.send_keys(password)
        # 9. Wybierz datę urodzenia
        day = Select(self.driver.find_element_by_xpath('//select[@name="days"]'))
        day.select_by_value(birthdate_dmr[0])
        month = Select(self.driver.find_element_by_xpath('//select[@name="months"]'))
        month.select_by_value(birthdate_dmr[1])
        year = Select(self.driver.find_element_by_xpath('//select[@name="years"]'))
        year.select_by_index(20)
        # 10. Sprawdź uzupełnione imię
        firstName = self.driver.find_element_by_xpath('//*[@id="firstname"]')
        print("Sprawdzam pole imię")
        assert name == firstName.get_attribute('value')


    def tearDown(self) -> None:
        """
        Porządki po teście
        """
        # Wyłączam przeglądarkę
        self.driver.quit()

# Jeśli nazywam się __main__
if __name__ == "__main__":
    # ...to uruchamiam testy
    unittest.main(verbosity = 2)

    #day = Select(self.driver.find_element_by_id('days'))
    #from selenium.webdriver.support.ui import Select
