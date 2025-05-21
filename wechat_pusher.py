import requests
from project_config import FANGTANG_SENDKEY

def push_to_wechat(title, link, summary):
    markdown_msg = f"### {title}\n\n{summary}\n\n👉 [阅读全文]({link})"
    print(markdown_msg)
    url = f"https://sctapi.ftqq.com/{FANGTANG_SENDKEY}.send"
    data = {
        "title": title,
        "desp": markdown_msg
    }
    requests.post(url, data=data)
