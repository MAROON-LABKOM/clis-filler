import argparse
import atexit
from time import sleep

from pandas import read_csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from clis_auth import login
from clis_common import check_webdriver
from clis_modules.clis_los import ClisListOfStudent
from clis_modules.clis_master import ClisMasterStudent
from clis_modules.clis_nilai import ClisFinalTest

# Chrome driver
driver: webdriver.Chrome

def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', help="Mode input data pada CLIS (master, los, nilai).")
    parser.add_argument('csv', help="Data mahasiswa yang akan ditambahkan pada CLIS")
    parser.add_argument('-u', '--username', required=True, help="Username CLIS")
    parser.add_argument('-p', '--password', help="Password CLIS")
    parser.add_argument('-y', '--year', help="Tahun masuk mahasiswa")
    parser.add_argument('-c', '--class', help="Kelas mahasiswa")
    parser.add_argument('-cid', '--class-id', help="ID List of Student")

    args = vars(parser.parse_args())

    # Check mode with pipeline support
    if args["mode"] == "master":
        if args["year"] is None or args["class"] is None:
            parser.error("class dan year tidak boleh kosong pada mode 'master'!")
    elif args["mode"] == "los":
        if args["class_id"] is None:
            parser.error("class-id tidak boleh kosong pada mode 'los'!")
    elif args["mode"] == "nilai":
        if args["class_id"] is None:
            parser.error("class-id tidak boleh kosong pada mode 'nilai'!")


    # Read CSV
    dataset = read_csv(args["csv"], dtype=str)
    print("\nLima data teratas\n%s\n" % (dataset.head()))

    # Check columns
    if set(["npm", "nama", "kelas"]).issubset(dataset.columns):
        print("Ada kolom yang tidak sesuai! Periksa kembali data CSV.")
        exit(0)

    # Check webdriver
    check_webdriver()

    # Create new webdriver
    driver = webdriver.Chrome(executable_path=r"bin\\chromedriver.exe")
    driver.maximize_window()

    # Login to CLIS
    print("\nProses login...")
    password = args["username"] if args["password"] is None else args["password"]
    login(driver, args["username"], password)

    # Process here
    if args["mode"] == "master":
        worker = ClisMasterStudent()
        worker.fit(driver, dataset, args["class"], args["year"])
    elif args["mode"] == "los":
        worker = ClisListOfStudent()
        worker.fit(driver, dataset, args["class_id"])
    elif args["mode"] == "nilai":
        worker = ClisFinalTest()
        worker.fit(driver, dataset, args["class_id"])
    else:
        print("Mode tidak diketahui!")

    # Finished!
    print("\nProgram telah selesai menginputkan data.")

# Close WebDriver
def exit_handler():
    try:
        driver.close()
    except Exception:
        pass

if __name__ == "__main__":
    # Register exit handler
    atexit.register(exit_handler)

    # Run main
    main()