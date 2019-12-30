from selenium import webdriver
from pandas import DataFrame
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from clis_common import print_report

class ClisMasterStudent():
    failed = []
    total = 0
    count_success = 0
    count_failed = 0

    def fit(self, driver: webdriver.Chrome, df: DataFrame, kelas, tahun):
        # Reset counter
        self.__reset_counter(df)

        for _, row in df.iterrows():
            try:
                # Navigate
                driver.get("http://labkom.ilkom.unpak.ac.id/?m=master&p=form_student")
                
                success, message = self.__input_data(driver, row["npm"], row["nama"], kelas, tahun)
                if success:
                    self.count_success = self.count_success + 1
                else:
                    self.count_failed = self.count_failed + 1
                    if message not in self.failed:
                        self.failed.append(message)
                sleep(1)
            except KeyboardInterrupt:
                print("Dihentikan oleh user...")
                break

        print_report(self.count_success, self.count_failed, self.total, self.failed)


    def __reset_counter(self, df: DataFrame):
        self.failed = []
        self.total = len(df)
        self.count_success = 0
        self.count_failed = 0


    def __input_data(self, driver: webdriver.Chrome, npm, nama, kelas, tahun):
        try:
            elem = driver.find_element_by_xpath('//*[@name="npm"]')
            elem.clear()
            elem.send_keys(npm)

            elem = driver.find_element_by_xpath('//*[@name="nama"]')
            elem.clear()
            elem.send_keys(nama)

            drop_elem = Select(driver.find_element_by_xpath('//*[@name="kelas"]'))
            drop_elem.select_by_visible_text(kelas)

            elem = driver.find_element_by_xpath('//*[@name="tahun_angkatan"]')
            elem.clear()
            elem.send_keys(tahun)

            elem = driver.find_element_by_xpath('//*[@name="save"]')
            elem.send_keys(Keys.RETURN)

            if "Failed!" in driver.page_source or "Warning!" in driver.page_source:
                error_message = driver.find_element_by_xpath('//div/div[@role="alert"]').text
                success = 0
                message = "{0}: {1}".format(npm, error_message[2:])
                return success, message
            else:
                success = 1
                message = ""
                return success, message
        except Exception:
            success = 0
            message = "Failed to process: {0}".format(npm)
            return success, message
