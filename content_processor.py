import requests
import json
from project_config import OPENROUTER_API_KEY

def summarize_article(text):
    # 可选：你可以自定义你的网站名称和URL
    referer = "https://your-site.com"
    title = "Your Site Name"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": referer,   # 可选，不需要可以删掉
        "X-Title": title,          # 可选，不需要可以删掉
        "Content-Type": "application/json"  # 必须有
    }

    data = {
        "model": "deepseek/deepseek-prover-v2:free",
        "messages": [
            {"role": "system", "content": "请总结相关资讯为50-80字摘要"},
            {"role": "user", "content": text}
        ]
    }

    try:
        # 这里用 data=json.dumps(data) 完全等价于 json=data，官方API是用的这个
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            data=json.dumps(data)
        )
        response.raise_for_status()  # 如果不是200，抛出异常

        result = response.json()
        print("🧠 模型返回：", result)  # 打印原始 JSON 响应，方便调试

        # 检查返回结构
        if "choices" in result and result["choices"]:
            return result["choices"][0]["message"]["content"]
        else:
            return f"[模型出错] 未返回 choices 字段：{result}"
    except Exception as e:
        return f"[请求失败] {str(e)}"
