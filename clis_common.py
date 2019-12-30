import urllib.request
import os.path

def print_report(success_count, failed_count, total, failed_list):
    # Print report
    print("Sukses:   %d" % (success_count))
    print("Gagal:    %d" % (failed_count))
    print("Total:    %d" % (total))
    print("Persentasi sukses: %.2f%%" % (float(success_count) / total * 100))
    print("Error:")
    print('%s' % '\n'.join(map(str, failed_list)))
    pass

def check_webdriver():
    if not os.path.exists(r"bin\\chromedriver.exe"):
        print("WebDriver tidak ada, mendownload...")
        download_webdriver()
    pass

def download_webdriver():
    url = "https://chromedriver.storage.googleapis.com/80.0.3987.16/chromedriver_win32.zip"
    urllib.request.urlretrieve(url, r"bin\\chromedriver.exe")
    pass