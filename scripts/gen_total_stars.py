#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_total_stars.py — 用 GitHub API 算 USERNAME 名下所有公开 + 私有(token 可见)
仓库的 stargazers_count 总和,渲染成跟 shields.io flat-square 风格一致的徽章 SVG。

为什么不用 shields.io:
  shields.io 的 /github/stars/{user} endpoint 走它的全局 token 池,频繁
  "Unable to select next GitHub token from pool" 限流。换成自建 Action 用
  我们自己的 GITHUB_TOKEN,每天 1 次请求,绝对不会触发 secondary rate limit。

输出: ../total-stars.svg

环境变量:
  GITHUB_TOKEN  — Action 注入,作 Authorization
  USERNAME      — 要查的用户名 (默认从 GITHUB_REPOSITORY_OWNER 拿)

布局:
  跟 shields.io flat-square 风格一致, 整体高 20px, 圆角 0px.
  左半段 (#555) 写 "总星标" + emoji,右半段 (#FFD700) 写数字.
  字体回退到系统 sans + Noto Sans SC, 与现有 hits.sh / shields.io 视觉一致.
"""
import json, os, sys, urllib.request, urllib.error

USERNAME = os.environ.get("USERNAME") or os.environ.get("GITHUB_REPOSITORY_OWNER") or "GeekASMR"
TOKEN    = os.environ.get("GITHUB_TOKEN", "")

API = "https://api.github.com"

def gh(url):
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8")), dict(r.headers)


def total_stars(user):
    """sum stargazers_count over all repos owned by `user`. paginates."""
    total = 0
    page = 1
    while True:
        # type=owner 排除被 fork 的别人仓库; per_page=100 上限
        url = f"{API}/users/{user}/repos?per_page=100&type=owner&page={page}"
        data, _ = gh(url)
        if not data:
            break
        for r in data:
            if r.get("fork"):
                continue
            total += int(r.get("stargazers_count", 0) or 0)
        if len(data) < 100:
            break
        page += 1
        if page > 10:  # 安全网, 1000 个仓库以上需要换分页方案
            break
    return total


def render_badge(label, value, label_bg="#555555", value_bg="#FFD700",
                  label_fg="#ffffff", value_fg="#222222"):
    """
    渲染 shields.io flat-square 风格徽章 SVG.
    label 是中文 ("总星标"),value 是数字字符串.

    宽度按字符近似估算: CJK / 全角 ≈ 14px,emoji ≈ 16px,ASCII ≈ 7.5px,空格 5px.
    加左右各 pad=10px 留余量,避免被截断.
    """
    def text_w(s):
        w = 0.0
        for ch in s:
            cp = ord(ch)
            # CJK Unified Ideographs + 全角符号
            if 0x4e00 <= cp <= 0x9fff or 0x3000 <= cp <= 0x303f or 0xff00 <= cp <= 0xffef:
                w += 14.0
            # emoji 块: Misc Symbols (2600-26FF), Dingbats (2700-27BF),
            # Misc Symbols and Arrows (2B00-2BFF, 含 ⭐ U+2B50),
            # Misc Tech (2300-23FF), Symbols & Pictographs (1F300-1FAFF, 1F600-1F64F)
            elif (0x2600 <= cp <= 0x27bf or 0x2b00 <= cp <= 0x2bff
                  or 0x2300 <= cp <= 0x23ff
                  or 0x1f300 <= cp <= 0x1faff or 0x1f600 <= cp <= 0x1f64f):
                w += 16.0
            elif ch == " ":
                w += 5.0
            else:
                w += 7.5
        return w

    pad = 14
    h = 20

    label_with_icon = "⭐ " + label
    label_w = int(round(text_w(label_with_icon) + pad * 2))
    value_w = int(round(text_w(value) + pad * 2))
    total_w = label_w + value_w
    label_cx = label_w / 2
    value_cx = label_w + value_w / 2

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{total_w}" height="{h}" viewBox="0 0 {total_w} {h}" role="img" aria-label="{label}: {value}">
  <title>{label}: {value}</title>
  <g shape-rendering="crispEdges">
    <rect width="{label_w}" height="{h}" fill="{label_bg}"/>
    <rect x="{label_w}" width="{value_w}" height="{h}" fill="{value_bg}"/>
  </g>
  <g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', 'Noto Sans CJK SC', 'Noto Sans SC', sans-serif" font-size="11" font-weight="600" text-anchor="middle">
    <text x="{label_cx}" y="14" fill="{label_fg}">{label_with_icon}</text>
    <text x="{value_cx}" y="14" fill="{value_fg}" font-weight="700">{value}</text>
  </g>
</svg>
'''


def main():
    print(f"computing total stars for {USERNAME}...")
    try:
        n = total_stars(USERNAME)
    except urllib.error.HTTPError as e:
        print(f"GitHub API error: {e.code} {e.reason}", file=sys.stderr)
        sys.exit(1)
    print(f"  total = {n}")

    out_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "total-stars.svg"))
    svg = render_badge("总星标", str(n))
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"  wrote {out_path} ({os.path.getsize(out_path)} bytes)")


if __name__ == "__main__":
    main()
