import json

# 定义要读取的文件路径
file_path = "downloads/province_city_district_urls.json"

# 使用with语句安全地打开并读取文件
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)
    
num_provinces_to_fetch = 1
if num_provinces_to_fetch is None or num_provinces_to_fetch > len(data):
    num_provinces_to_fetch = len(data)

# 遍历省
for province in data[:num_provinces_to_fetch]:
    print(f"省：{province['province']}")
    # print(f"省URL：{province['url']}")
    for geojson in province["geojsons"]:
        print(f"GeoJSON URL: {geojson['url']}")
    for shapefile in province["shapefiles"]:
        print(f"Shapefile URL: {shapefile['url']}")

    # 如果省份不是台湾省，则进一步遍历城市和县区
    if province['province'] != "台湾省":
        for city in province.get('cities', []):
            print(f"    市：{city['name']}")
            # 访问城市级别的geojsons和shapefiles链接
            for geojson in city.get('geojsons', []):
                print(f"    GeoJSON URL: {geojson['url']}")
            for shapefile in city.get('shapefiles', []):
                print(f"    Shapefile URL: {shapefile['url']}")

            # 遍历县区
            for district in city.get('districts', []):
                print(f"      县/区：{district['name']}")
                # 访问县区级别的geojsons和shapefiles链接
                for geojson in district.get('geojsons', []):
                    print(f"      GeoJSON URL: {geojson['url']}")
                for shapefile in district.get('shapefiles', []):
                    print(f"      Shapefile URL: {shapefile['url']}")
