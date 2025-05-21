import requests
import json

# 直接把你的API KEY写这里测试用，生产环境建议用环境变量或配置文件
OPENROUTER_API_KEY = "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"  # ←←←改成你自己的

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "deepseek/deepseek-prover-v2:free",   # 或者 deepseek/deepseek-prover-v2:free
    "messages": [
        {"role": "user", "content": "你好，请返回一句话，测试模型是否正常可用。"}
    ]
}

try:
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        data=json.dumps(data)
    )
    response.raise_for_status()
    result = response.json()
    print(OPENROUTER_API_KEY)
    print("返回内容：", json.dumps(result, indent=2, ensure_ascii=False))
    if "choices" in result and result["choices"]:
        print("模型回复内容：", result["choices"][0]["message"]["content"])
    else:
        print("没有返回choices字段，原始数据：", result)
except Exception as e:
    print("请求失败：", str(e))
