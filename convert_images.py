#!/usr/bin/env python3
import base64
import urllib.request
import sys

def image_to_base64(url):
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = response.read()
            mime_type = response.headers.get('Content-Type', 'image/png')
            # 根据mime type确定data URI前缀
            ext_map = {'image/png': 'data:image/png;base64,', 'image/jpeg': 'data:image/jpeg;base64,', 'image/gif': 'data:image/gif;base64,'}
            prefix = ext_map.get(mime_type, 'data:image/png;base64,')
            return prefix + base64.b64encode(data).decode('utf-8')
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None

# 测试
url = "https://mmbiz.qpic.cn/mmbiz_png/aFXaQ2oY6JAOBIkhshOkLAQzpHiarLm7MYSAictXPZgJNd6Yel2Bia7CyW3Id78ICibeywxPPiclllOZhGmGP4KusvQ/640?wx_fmt=png"
result = image_to_base64(url)
if result:
    print(f"Success! Length: {len(result)}")
    print(f"Prefix: {result[:50]}...")
