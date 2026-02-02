#!/usr/bin/env python3
import base64
import urllib.request
import re
import os


def image_to_base64(url):
    try:
        with urllib.request.urlopen(url, timeout=15) as response:
            data = response.read()
            mime = response.headers.get("Content-Type", "image/png").split("/")[-1]
            return f"data:image/{mime};base64,{base64.b64encode(data).decode('utf-8')}"
    except Exception as e:
        print(f"Error: {e}")
        return None


html_file = "/Users/hugo/Documents/Kimi-Code 2/wechat-markdown-editor.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 开头图片
header_url = "https://mmbiz.qpic.cn/mmbiz_png/aFXaQ2oY6JAOBIkhshOkLAQzpHiarLm7MYSAictXPZgJNd6Yel2Bia7CyW3Id78ICibeywxPPiclllOZhGmGP4KusvQ/640?wx_fmt=png"
print("正在转换开头图片...")
header_base64 = image_to_base64(header_url)
if header_base64:
    content = content.replace(
        "https://mmbiz.qpic.cn/mmbiz_png/aFXaQ2oY6JAOBIkhshOkLAQzpHiarLm7MYSAictXPZgJNd6Yel2Bia7CyW3Id78ICibeywxPPiclllOZhGmGP4KusvQ/640?wx_fmt=png",
        header_base64,
    )
    print("  ✓ 开头图片转换完成")

# 大标题图片
title_urls = [
    "https://mmbiz.qpic.cn/mmbiz_png/aFXaQ2oY6JBKwShvcSd8gIJqox7aK7I0u4CHiaMhAdl8MT33E9ByxnhpYuMGja3h82BzeYpzJQ90iaTxpsibR2Qlg/640?wx_fmt=png",
    "https://mmbiz.qpic.cn/mmbiz_png/aFXaQ2oY6JBKwShvcSd8gIJqox7aK7I0xU9Fvm3ILCw745js1LmpsibFNyvia4QsicUbKwqeibUyrYvx0N4CN2trBw/640?wx_fmt=png",
    "https://mmbiz.qpic.cn/mmbiz_png/aFXaQ2oY6JBKwShvcSd8gIJqox7aK7I0WZZD2XSfTRL4qMsKuHfseqVcjBRM0E29GIiatsL7vdPItywyXqHibNEQ/640?wx_fmt=png",
    "https://mmbiz.qpic.cn/mmbiz_png/aFXaQ2oY6JBKwShvcSd8gIJqox7aK7I0f9nmMMDAvNIxXBVYXiadGiar3ovYA7wm63icczibatTnaQbZAdPrIXfeSw/640?wx_fmt=png",
    "https://mmbiz.qpic.cn/mmbiz_png/aFXaQ2oY6JBKwShvcSd8gIJqox7aK7I0EG4nnJHvoicDYERdXImgoVQB5xeeVCGm52gQJWAGrbh3aAfdKicptPaw/640?wx_fmt=png",
    "https://mmbiz.qpic.cn/mmbiz_png/aFXaQ2oY6JBKwShvcSd8gIJqox7aK7I0TNuC2icdFOz26U0cNfDfbUMA7sLd7hwbnswWMYaZc98icWZIKXNiaqF2w/640?wx_fmt=png",
    "https://mmbiz.qpic.cn/mmbiz_png/aFXaQ2oY6JBKwShvcSd8gIJqox7aK7I0IYdQyRticDTyn7QuDBchIMx33ELCBicLXGC4c4USdqL3Q0aUMuw3lhkQ/640?wx_fmt=png",
    "https://mmbiz.qpic.cn/mmbiz_png/aFXaQ2oY6JAeYJcv3OmLWcVbSVWu5HZbuuicibu0JkRbo788pnRMSiav6ZZJh9JR1kpcYuTDrweFNciaLcoF8TA7nw/640?wx_fmt=png&from=appmsg",
    "https://mmbiz.qpic.cn/mmbiz_png/aFXaQ2oY6JAeYJcv3OmLWcVbSVWu5HZbSb2hian4bSbKLpHZgKMZOwKVibxZgXLRg1MnHKNMzbrgwnlEMKYSX5Eg/640?wx_fmt=png&from=appmsg",
]
print("正在转换大标题图片...")
for i, url in enumerate(title_urls):
    base64_img = image_to_base64(url)
    if base64_img:
        content = content.replace(url, base64_img)
        print(f"  ✓ 大标题{i + 1}号图片转换完成")

# 底部图片
footer_url = "https://mmbiz.qpic.cn/mmbiz_png/aFXaQ2oY6JA9PRiaUibW3XyibONLPibefw2jwwLBic4uoBlZp4WiaLQfqZr9n5tJkPyic2B8I5jUE4gRdnUMrepCiaO9Qg/640?wx_fmt=png"
print("正在转换底部图片...")
footer_base64 = image_to_base64(footer_url)
if footer_base64:
    content = content.replace(footer_url, footer_base64)
    print("  ✓ 底部图片转换完成")

# GIF图片
gif_url = "https://mmbiz.qpic.cn/mmbiz_gif/aFXaQ2oY6JAbmS3wc8fxt3Lemribiaz5FbJWN9K3GTB1OeJtBE3au0xdUsQTVVVyOuERx44KVcl1kDXgbEvib2TtQ/640?wx_fmt=gif"
print("正在转换GIF图片...")
gif_base64 = image_to_base64(gif_url)
if gif_base64:
    content = content.replace(gif_url, gif_base64)
    print("  ✓ GIF图片转换完成")

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("\n✅ 所有图片转换完成！")
print("⚠️  文件体积会变大，这是正常现象")
