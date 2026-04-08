import socket
import requests
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ================= 配置区 =================
USERNAME = '请输入你的账号（学号）'
PASSWORD = '请输入你的密码'
# ==========================================

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('223.5.5.5', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return None

def check_network():
    try:
        res = requests.get('https://www.baidu.com', timeout=3)
        return True
    except:
        return False

def login():
    if check_network():
        print("🌍 网络已连接，无需重复登录。")
        return

    ip = get_local_ip()
    if not ip:
        print("❌ 未获取到 IP 地址，请确认是否已连接校园网 Wi-Fi 或网线！")
        return
        
    print(f"📡 检测到断网，当前设备 IP: {ip}，正在尝试自动登录...")

    url = f"https://netauth.huuc.edu.cn:802/eportal/portal/login?callback=dr1003&login_method=1&user_account={USERNAME}&user_password={PASSWORD}&wlan_user_ip=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=3.0&terminal_type=1&lang=zh-cn"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, verify=False, timeout=5)
        
        if '"result":1' in response.text or 'succeeded' in response.text:
            print("✅ 登录成功！享受冲浪吧！")
        else:
            print(f"⚠️ 登录可能失败，服务器返回信息: {response.text}")
    except Exception as e:
        print(f"❌ 登录请求发送失败: {e}")

if __name__ == "__main__":
    print("====================================")
    print("  河南城建学院校园网自动登录小助手  ")
    print("====================================")
    time.sleep(1)
    login()
    time.sleep(1)