import requests
import json

# 构造八字算命专用的消息列表
messages = [
    {
        "role": "system",
        "content": "你现在是一位通晓八字命理、精通天干地支变化规律的老算命先生，善于用阴阳五行理论判断命运。"
    },
    {
        "role": "user",
        "content": (
            "请根据下面用户提供的出生信息进行命运解析：\n\n"
            "出生信息：1988年7月15日 15:30\n\n"
            "请详细分析此人的八字运势，解释天干地支的搭配及其对未来流年、大运的影响，并给出合理建议。"
        )
    }
]

# 构造 API 请求参数
data = {
    "model": "deepseek-chat",
    "messages": messages,
    "temperature": 0.7,       # 适中的随机性
    "max_tokens": 200,        # 根据需要设定生成文本的长度
    "top_p": 0.9,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.6,
    "stream": False
}

api_url = "https://api.deepseek.com/chat/completions"  # 请替换为实际 API 地址
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_KEY"  # 替换为你的 API 密钥
}

# 发送请求给 DeepSeek
response = requests.post(api_url, headers=headers, data=json.dumps(data))
result = response.json()


print("八字算命结果：")
# 如果返回结果包含 choices 字段，则从中解析输出
if "choices" in result:
    content = result["choices"][0]["message"].get("content", "暂无响应。")
    print(content)
else:
    print(result.get("text", "暂无响应。"))