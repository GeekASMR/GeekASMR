#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_keywords.py — 生成中文工程关键词云 SVG（亮 / 暗双版本）。

参考效果图：水煮 / 耐盐雾 / 跌落 / 重物冲击 那种字号不一、错落排布的工程检测词云。
我们这里用项目相关的中文关键词替换。

输出:
  ../keywords-light.svg     白底版本（默认）
  ../keywords-dark.svg      暗底版本（GitHub 暗色主题）

依赖: 仅 Python 标准库。无需 PIL / matplotlib / wordcloud。
排布算法: 简单的"螺旋探测放置"——按字号从大到小放，每个词从中心起以螺旋扩展尝试落点，
        若与已占用矩形重叠则继续螺旋,直到落得下或放弃。够用、稳定、零依赖。
"""

import math
import random
import xml.sax.saxutils as xs

# ─────────────────────  配置  ────────────────────────────────────────────────
W = 1280
H = 360
PADDING = 6      # 词与词之间的留白像素

# 关键词 + 权重 (1..10)。权重越大字号越大。
# 内容 = 个人技术栈 + 项目特征 + 重要术语，从图里那种工业感 → 改成软件工程感。
KEYWORDS = [
    ("WDM 内核驱动", 10),
    ("VST3 桥接", 10),
    ("Network Ultra", 9),
    ("低延迟音频", 9),
    ("零拷贝 IPC", 8),
    ("WHQL 签名", 8),
    ("UDP 数据面", 8),
    ("JitterBuffer", 7),
    ("Opus 编码", 7),
    ("FLAC 无损", 7),
    ("WebSocket", 7),
    ("Studio One", 6),
    ("LUNA", 6),
    ("UAD", 6),
    ("Tauri", 6),
    ("Rust", 6),
    ("C++ 17", 6),
    ("Go 1.22", 6),
    ("WDK", 5),
    ("CMake", 5),
    ("PowerShell", 5),
    ("Windows 11", 5),
    ("ASIO", 5),
    ("WASAPI", 5),
    ("MMDevice", 5),
    ("内核回调", 4),
    ("循环缓冲", 4),
    ("PortClass", 4),
    ("MiniPort", 4),
    ("KMixer", 4),
    ("跨网协作", 4),
    ("NAT 穿透", 4),
    ("HMAC 鉴权", 4),
    ("bcrypt", 3),
    ("DPAPI 加密", 3),
    ("OpenCore", 3),
    ("Hackintosh", 3),
    ("百灵达 UMC", 3),
    ("VST3 SDK", 3),
    ("JUCE", 3),
    ("反作弊", 3),
    ("驱动签名", 3),
    ("中心服务器", 3),
    ("信号转发", 2),
    ("音频路由", 2),
    ("INF 安装", 2),
    ("LSP", 2),
    ("Hooking", 2),
    ("内存映射", 2),
    ("SDR", 2),
    ("自适应缓冲", 2),
    ("UDP 18902", 2),
    ("TCP 18900", 2),
]

# 颜色调色板：与 banner 渐变保持一致。前 3 档为重点色，后面为辅色（淡灰）。
PALETTE_LIGHT = ["#E91E63", "#9C27B0", "#00599C", "#0E8A16", "#666", "#888", "#aaa", "#bbb"]
PALETTE_DARK  = ["#FF4080", "#C26FFF", "#7AB8FF", "#5DD583", "#ddd", "#bbb", "#999", "#777"]

BG_LIGHT = None        # 透明（README 已是白底，这样 light/dark 都能用）
BG_DARK  = None

# ─────────────────────  字号映射  ───────────────────────────────────────────
# weight 1..10 → font-size px。最大字号控制视觉重心。
def weight_to_size(w):
    table = {10: 56, 9: 44, 8: 36, 7: 28, 6: 22, 5: 18, 4: 16, 3: 14, 2: 12, 1: 10}
    return table.get(w, 12)

# ─────────────────────  字符宽度估计  ────────────────────────────────────
# 中文字符 ≈ 1 em，西文 ≈ 0.6 em，数字/标点 ≈ 0.55 em。够用的近似。
def estimate_text_width(text, size):
    w = 0.0
    for ch in text:
        if '\u4e00' <= ch <= '\u9fff':         # CJK
            w += size * 1.0
        elif ch.isspace():
            w += size * 0.4
        elif ch in "·.,，。()（）-+":
            w += size * 0.4
        elif 'a' <= ch.lower() <= 'z':
            w += size * 0.6
        else:                                    # 数字 / 其他
            w += size * 0.55
    return w

# ─────────────────────  螺旋探测放置  ────────────────────────────────────
def place_words(words):
    """words: [(text, weight)]，按 weight desc 放置。返回 [(text, x, y, size, color)]。"""
    placed = []   # [(x1, y1, x2, y2)]
    out = []
    cx, cy = W / 2, H / 2

    rng = random.Random(20260523)  # 固定种子,生成结果可复现
    palette_choice = lambda: rng.choice(range(len(PALETTE_LIGHT)))

    # 按权重从大到小,大字先占中心
    order = sorted(words, key=lambda x: -x[1])
    for rank, (text, weight) in enumerate(order):
        size = weight_to_size(weight)
        # 前 6 个权重最高的词强制用重点色 (idx 0..2 之间随机)，其余用全调色板
        if rank < 6:
            color_idx = rng.choice([0, 1, 2])     # 三个主色 (粉/紫/蓝)
        elif rank < 14:
            color_idx = rng.choice([0, 1, 2, 3])  # 加进绿
        else:
            color_idx = palette_choice()
        tw = estimate_text_width(text, size)
        th = size * 1.2     # 行高

        # 螺旋参数: 从中心 r=0 出发,r 每步 +step, theta 每步 +d_theta
        # 大字号步长大,避免螺旋密度过高反而总落不下
        step = max(2, size * 0.15)
        d_theta = math.radians(15)
        max_r = max(W, H)

        placed_this = False
        r = 0.0
        theta = rng.uniform(0, 2 * math.pi)
        while r < max_r:
            # 候选中心
            x = cx + r * math.cos(theta) - tw / 2
            y = cy + r * math.sin(theta) - th / 2
            x1, y1, x2, y2 = x, y, x + tw, y + th
            # 边界
            if x1 < 0 or y1 < 0 or x2 > W or y2 > H:
                r += step
                theta += d_theta
                continue
            # 重叠检测（含 PADDING）
            ok = True
            for px1, py1, px2, py2 in placed:
                if not (x2 + PADDING < px1 or px2 + PADDING < x1
                        or y2 + PADDING < py1 or py2 + PADDING < y1):
                    ok = False
                    break
            if ok:
                placed.append((x1, y1, x2, y2))
                out.append({
                    "text": text,
                    "x": x1,
                    "y": y2 - size * 0.2,    # baseline 校正
                    "size": size,
                    "color_idx": color_idx,
                })
                placed_this = True
                break
            r += step
            theta += d_theta

        # 落不下就跳过（极端情况，关键词太多）
    return out


def emit_svg(out, palette, bg, path):
    """渲染一份 SVG。"""
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" preserveAspectRatio="xMidYMid meet">',
    ]
    # 字体: 用 noto / pingfang / 系统中文字体回退栈。font-family 写在 root <style>。
    parts.append('<style>')
    parts.append('  text { font-family: "PingFang SC", "Microsoft YaHei", "Hiragino Sans GB", "Noto Sans CJK SC", "Noto Sans SC", sans-serif; font-weight: 700; }')
    parts.append('</style>')

    if bg:
        parts.append(f'<rect width="{W}" height="{H}" fill="{bg}"/>')

    for item in out:
        text = xs.escape(item["text"])
        color = palette[item["color_idx"] % len(palette)]
        parts.append(
            f'<text x="{item["x"]:.1f}" y="{item["y"]:.1f}" '
            f'font-size="{item["size"]}" fill="{color}">{text}</text>'
        )

    parts.append('</svg>\n')
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))


def main():
    placed = place_words(KEYWORDS)
    print(f"placed {len(placed)} / {len(KEYWORDS)} keywords")

    import os
    out_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
    emit_svg(placed, PALETTE_LIGHT, BG_LIGHT, os.path.join(out_dir, "keywords-light.svg"))
    emit_svg(placed, PALETTE_DARK,  BG_DARK,  os.path.join(out_dir, "keywords-dark.svg"))
    print("wrote keywords-light.svg + keywords-dark.svg")


if __name__ == "__main__":
    main()
