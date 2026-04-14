import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

def scrape_popular_data():
    """
    抓取典枢平台热门数据并解析出数据名称及对应的详情页链接。
    """
    url = "https://dianshudata.com/dataMarket/rid48"
    # 添加常见的 User-Agent 头，防止被反爬虫策略拦截
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    print(f"正在请求 {url} ...")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"抓取页面失败: {e}")
        return

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 查找所有 class 为 data-card 的 a 标签
    data_cards = soup.find_all('a', class_='data-card')

    if not data_cards:
        print("未找到数据卡片，页面结构可能已更改或数据为动态加载。")
        return

    print(f"成功解析到 {len(data_cards)} 条热门数据：\n")
    
    results = []
    
    for index, card in enumerate(data_cards, start=1):
        # 提取详情页相对链接，并拼接为完整 URL
        href = card.get('href')
        detail_url = urljoin("https://dianshudata.com", href)

        # 提取数据名称
        title_element = card.find('h3', class_='title')
        if title_element:
            # 提取文本，并去除多余的空格（忽略 img 或 svg 等标签内部可能产生的空白）
            name = title_element.get_text(separator="", strip=True)
        else:
            name = "未知名称"
            
        results.append({
            "name": name,
            "url": detail_url
        })

        print(f"{index}. {name}")
        print(f"   详情页: {detail_url}")
        print("-" * 50)
        
    # 可选：将结果保存到文件
    with open("popular_data.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("解析结果已保存至 popular_data.json")

if __name__ == "__main__":
    scrape_popular_data()
