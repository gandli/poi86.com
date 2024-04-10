from get_urls import get_urls
from download_file import open_url

def main():
    file_path = "downloads/province_city_district_urls.json"
    num_provinces_to_fetch = 1  # 或者设置为您想处理的省份数量
    urls = get_urls(file_path, num_provinces_to_fetch)
    download_path = "downloads"
    
    for page_url in urls:
        open_url(page_url, download_path)

if __name__ == "__main__":
    main()