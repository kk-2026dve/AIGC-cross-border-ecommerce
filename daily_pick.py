import requests
from bs4 import BeautifulSoup
import time
import re
from agent.runner import agent

def fetch_real_data():
    url = "http://books.toscrape.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('article', class_='product_pod')[:3] 
        text = "这是我今天从真实网站上抓取到的竞品数据，请帮我分析：\n"
        for book in books:
            name = book.find('h3').find('a')['title']
            price_str = book.find('p', class_='price_color').text
            match = re.search(r'(\d+\.\d+)', price_str)
            price_gbp = float(match.group(1)) if match else 0.0
            price = price_gbp * 9 
            cost = round(price * 0.3, 2)
            text += f"- 商品：{name}。预估售价 {price} 元人民币，拿货价 {cost} 元。重量 200g，无电池。月销 1500 单。\n"
        return text
    except Exception as e:
        return f"抓取失败: {e}"

if __name__ == "__main__":
    data = fetch_real_data()
    print(data)
    result = agent.process_ticket(999, "选品分析", data)
    if result.get("ok"):
        print(result.get("agent_text"))
