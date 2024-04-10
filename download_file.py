from selenium import webdriver
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import re

def init_webdriver(download_path):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)

def construct_expected_filename(page_url, page_title):
    """
    根据URL和页面标题构造预期的下载文件名，区分GeoJSON和Shapefile。

    :param page_url: 页面的URL。
    :param page_title: 页面的标题。
    :return: 预期的下载文件名。
    """
    # 使用正则表达式从URL中提取行政区划代码
    admin_code_match = re.search(r'/(\d+).html', page_url)
    admin_code = admin_code_match.group(1) if admin_code_match else ''

    # 根据URL确定是GeoJSON还是Shapefile
    if "geojson" in page_url.lower():
        file_type = "GeoJSON"
    elif "shapefile" in page_url.lower():
        file_type = "Shapefile"
    else:
        file_type = "Unknown"

    # 替换页面标题中不适合文件名的字符，并去除可能的GeoJSON或Shapefile字样
    page_title_cleaned = re.sub(r'(GeoJSON|Shapefile)', '', page_title, flags=re.I).strip()
    page_title_cleaned = page_title_cleaned.replace("下载-POI数据", "").strip()

    # 构造文件名
    filename = f"{page_title_cleaned}_{admin_code}_{file_type}_(poi86.com).zip"
    return filename

def open_url(driver,page_url, download_path):
    # driver = init_webdriver(download_path)
    driver.get(page_url)
    page_title = driver.title
    print(page_title)
    # 构造预期的下载文件名
    expected_filename = construct_expected_filename(page_url, page_title)
    print(f"预期的下载文件名: {expected_filename}") 
    # driver.quit()
    
if __name__ == "__main__":
    download_path = "downloads"  
    page_url = "https://www.poi86.com/poi/download_area_geojson/110000.html"
    open_url(page_url, download_path) #北京市边界_110000_GeoJSON_(poi86.com).zip
