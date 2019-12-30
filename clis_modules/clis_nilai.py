from selenium import webdriver
from pandas import DataFrame
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from clis_common import print_report

class ClisFinalTest():
    failed = []
    total = 0
    count_success = 0
    count_failed = 0

    def fit(self, driver: webdriver.Chrome, df: DataFrame, class_id):
        # Navigate
        driver.get("http://labkom.ilkom.unpak.ac.id/index.php?m=transaction&p=form_final_test&id=" + class_id)

        # Check if ID exists
        elem = driver.find_element_by_xpath('//*[@id="atas"]/div/div[2]/div/div[2]/div[2]/div[1]')
        asprak = elem.text.strip()
        print("Asprak terdeteksi: %s" % asprak)

        if len(asprak) == 0:
            print("ID kelas tidak ditemukan.")
            return

        # Reset counter
        self.__reset_counter(df)

        # Set index on DataFrame
        df.set_index("npm", inplace=True)

        # Get table
        table = driver.find_element_by_xpath('//*[@id="absensi"]/table')

        # Iterate over table rows
        for row in table.find_elements_by_xpath(".//tr"):
            try:
                npm = row.find_element_by_xpath(".//td[2]").text.strip()
                if len(npm) != 9:
                    continue

                if npm not in df.index:
                    self.failed.append("Index not found {0}".format(npm))
                    self.count_failed = self.count_failed + 1  
                else:
                    nilai = df.loc[npm]["nilai"]

                    elem_nilai = row.find_element_by_xpath(".//td[4]/input")
                    elem_nilai.clear()
                    elem_nilai.send_keys(nilai)
                    self.count_success = self.count_success + 1
            except KeyboardInterrupt:
                print("Dihentikan oleh user...")
                break
            except Exception:
                self.count_failed = self.count_failed + 1
                pass

        # Submit button
        elem = driver.find_element_by_xpath('//*[@name="simpan"]')
        elem.send_keys(Keys.RETURN)

        print_report(self.count_success, self.count_failed, self.total, self.failed)


    def __reset_counter(self, df: DataFrame):
        self.failed = []
        self.total = len(df)
        self.count_success = 0
        self.count_failed = 0
