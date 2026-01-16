import os
import requests

def test_push():
    # 从 GitHub Secrets 中读取 PUSH_KEY
    push_key = os.environ.get('PUSH_KEY')
    
    if not push_key:
        print("❌ 错误：程序未能读取到名为 'PUSH_KEY' 的变量，请检查 GitHub Secrets 设置。")
        return

    print(f"✅ 已成功读取 PUSH_KEY: {push_key[:5]}******")
    
    # Server酱推送地址
    url = f"https://sctapi.ftqq.com/{push_key}.send"
    data = {
        "title": "GitHub 推送测试",
        "desp": "如果你看到这条消息，说明你的 PUSH_KEY 配置完全正确！"
    }
    
    try:
        response = requests.post(url, data=data)
        res_json = response.json()
        if res_json.get('code') == 0 or 'data' in res_json:
            print("🚀 推送请求已发出，请检查微信消息！")
        else:
            print(f"❌ 推送失败，Server酱返回错误：{res_json}")
    except Exception as e:
        print(f"❌ 网络请求发生错误: {e}")

if __name__ == "__main__":
    test_push()
