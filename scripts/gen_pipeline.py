#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_pipeline.py — 生成"我在做什么"音频流程图 SVG。

替代 mermaid（mermaid 在 GitHub 渲染时右上角会自动加 Copy / Wrap / Open in viewer
按钮组,影响视觉)。本脚本输出纯静态 SVG,无任何浮层按钮。

输出: ../pipeline-light.svg + ../pipeline-dark.svg

布局:
   [Windows]  →  [WDM]  →  [VST3]  →  [DAW]
                                ↓ (虚线)
                         [Network Ultra]
                                ↓
                          [远端 DAW]
"""

import os
import xml.sax.saxutils as xs

W = 1280
H = 320

# 节点定义: (key, label_top, label_bot, x, y, color)
# color 跟 banner 渐变一致 (粉 / 紫 / 蓝)
# 全宽布局: NODE_W=280, x=10/340/670/1000, 最右节点 1000+280=1280 贴右,
# 最左节点 x=10 贴左. 4 节点等距,中间 gap = (1280-4*280-20)/3 = 50px
NODES_LIGHT = [
    ("win",   "🪟 Windows",    "系统音频",      10,  100, "#555555"),
    ("wdm",   "⚙️ WDM",         "内核驱动",      340, 100, "#E91E63"),
    ("vst",   "🔌 VST3",        "桥接插件",      670, 100, "#E91E63"),
    ("daw",   "🎚 DAW",         "数字音频工作站", 1000, 100, "#00599C"),
    ("net",   "🌐 Network Ultra", "跨网协作中继",   670, 230, "#9C27B0"),
    ("remote","👥 远端 DAW",    "全世界",         1000, 230, "#555555"),
]

NODES_DARK = [
    ("win",   "🪟 Windows",    "系统音频",      10,  100, "#bbbbbb"),
    ("wdm",   "⚙️ WDM",         "内核驱动",      340, 100, "#FF4080"),
    ("vst",   "🔌 VST3",        "桥接插件",      670, 100, "#FF4080"),
    ("daw",   "🎚 DAW",         "数字音频工作站", 1000, 100, "#7AB8FF"),
    ("net",   "🌐 Network Ultra", "跨网协作中继",   670, 230, "#C26FFF"),
    ("remote","👥 远端 DAW",    "全世界",         1000, 230, "#bbbbbb"),
]

NODE_W = 280
NODE_H = 70

def render(nodes, txt_color, line_color, path):
    parts = ['<?xml version="1.0" encoding="UTF-8"?>']
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
                 f'width="100%" preserveAspectRatio="xMidYMid meet">')

    parts.append('<style>')
    parts.append('  .label { font-family: "PingFang SC", "Microsoft YaHei", "Hiragino Sans GB", '
                 '"Noto Sans CJK SC", "Noto Sans SC", sans-serif; font-weight: 700; }')
    parts.append('  .top  { font-size: 18px; }')
    parts.append('  .bot  { font-size: 13px; opacity: 0.85; }')
    parts.append('</style>')

    # 箭头定义 (实线 + 虚线两种)
    parts.append('<defs>')
    parts.append(f'<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" '
                 f'markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
                 f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{line_color}"/></marker>')
    parts.append('</defs>')

    # 主链路连线 (Windows → WDM → VST3 → DAW)
    main_chain = ["win", "wdm", "vst", "daw"]
    pos = {n[0]: (n[3], n[4]) for n in nodes}
    for a, b in zip(main_chain, main_chain[1:]):
        ax, ay = pos[a]
        bx, by = pos[b]
        x1 = ax + NODE_W
        y1 = ay + NODE_H / 2
        x2 = bx
        y2 = by + NODE_H / 2
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2 - 6}" y2="{y2}" '
                     f'stroke="{line_color}" stroke-width="2.5" marker-end="url(#arrow)"/>')

    # 分支: VST3 ↓ Network Ultra (虚线)
    vst_x, vst_y = pos["vst"]
    net_x, net_y = pos["net"]
    bx1 = vst_x + NODE_W / 2
    by1 = vst_y + NODE_H
    bx2 = net_x + NODE_W / 2
    by2 = net_y
    parts.append(f'<line x1="{bx1}" y1="{by1}" x2="{bx2}" y2="{by2 - 6}" '
                 f'stroke="{line_color}" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arrow)"/>')

    # Network Ultra → 远端 DAW (虚线)
    rem_x, rem_y = pos["remote"]
    rx1 = net_x + NODE_W
    ry1 = net_y + NODE_H / 2
    rx2 = rem_x
    ry2 = rem_y + NODE_H / 2
    parts.append(f'<line x1="{rx1}" y1="{ry1}" x2="{rx2 - 6}" y2="{ry2}" '
                 f'stroke="{line_color}" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arrow)"/>')

    # 节点本身
    for key, top, bot, x, y, color in nodes:
        parts.append(f'<rect x="{x}" y="{y}" width="{NODE_W}" height="{NODE_H}" '
                     f'rx="10" ry="10" fill="{color}" opacity="0.95"/>')
        parts.append(f'<text class="label top" x="{x + NODE_W/2}" y="{y + 28}" '
                     f'fill="#ffffff" text-anchor="middle">{xs.escape(top)}</text>')
        parts.append(f'<text class="label bot" x="{x + NODE_W/2}" y="{y + 50}" '
                     f'fill="#ffffff" text-anchor="middle">{xs.escape(bot)}</text>')

    parts.append('</svg>\n')
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))


def main():
    out_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
    render(NODES_LIGHT, "#333", "#666", os.path.join(out_dir, "pipeline-light.svg"))
    render(NODES_DARK,  "#eee", "#aaa", os.path.join(out_dir, "pipeline-dark.svg"))
    print("wrote pipeline-light.svg + pipeline-dark.svg")


if __name__ == "__main__":
    main()
