from get_urls import get_urls

def main():
    file_path = "downloads/province_city_district_urls.json"
    num_provinces_to_fetch = 1  # 或者设置为您想处理的省份数量
    urls = get_urls(file_path, num_provinces_to_fetch)
    
    # 在这里，您可以根据需要对urls进行进一步的处理
    for url in urls:
        print(url)

if __name__ == "__main__":
    main()