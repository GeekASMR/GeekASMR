<!-- GitHub Profile README · 渲染于 https://github.com/GeekASMR -->

```
   ┌─────────┐    ┌────────┐    ┌────────┐    ┌─────┐
   │ Windows │ ─▶ │  WDM   │ ─▶ │  VST3  │ ─▶ │ DAW │
   │  音频   │    │ Driver │    │ Bridge │    │     │
   └─────────┘    └────────┘    └────────┘    └─────┘
                                   │
                                   ▼
                            ┌─────────────┐
                            │  network    │
                            │  跨网协作   │
                            └─────────────┘
```

# 你好，我是 GeekASMR <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="26">

**让 Windows 系统音频以采样级精度抵达 DAW。**

Windows 音频内核 · 虚拟驱动 · VST3 桥接 · 网络协作音频 · 黑苹果 OpenCore

📍 哈尔滨 &nbsp;·&nbsp; 🌐 [geek.asmrtop.cn](https://geek.asmrtop.cn/) &nbsp;·&nbsp; 💚 [赞助 WHQL 签名](https://ultra.asmrtop.cn/donate/)

---

### 🚀 旗舰项目 — WDM2VST Ultra

WDM 内核驱动 + 5 个 VST3，把任意 Windows 程序的声音变成 DAW 里的一条轨道，反向亦可。低延迟、零拷贝 IPC、原生 VST3 宿主。

[![release](https://img.shields.io/github/v/release/GeekASMR/WDM2VST-Ultra?style=for-the-badge&label=最新版本&color=E91E63)](https://github.com/GeekASMR/WDM2VST-Ultra/releases)
[![downloads](https://img.shields.io/github/downloads/GeekASMR/WDM2VST-Ultra/total?style=for-the-badge&label=总下载&color=0E8A16)](https://github.com/GeekASMR/WDM2VST-Ultra/releases)
[![stars](https://img.shields.io/github/stars/GeekASMR/WDM2VST-Ultra?style=for-the-badge&label=Star&color=FFD700)](https://github.com/GeekASMR/WDM2VST-Ultra)

> **⚡ 阶段重点 — 推动微软 WHQL 签名**
>
> 国内主流反作弊（腾讯 ACE / 网易易盾 / EasyAntiCheat）默认拒签内核驱动。WHQL 是行业里**唯一彻底**的解法。
>
> 如果 WDM2VST Ultra 帮到你，欢迎 [💚 赞助一份心意](https://ultra.asmrtop.cn/donate/)。

---

### 🧰 项目矩阵

<table>
<tr>
<td valign="top" width="50%">

**� 音频内核 & 驱动**
- [`WDM2VST-Ultra`](https://github.com/GeekASMR/WDM2VST-Ultra) — WDM ↔ VST3 低延迟桥
- [`UMC-Ultra-drivers`](https://github.com/GeekASMR/UMC-Ultra-drivers) — 百灵达 UMC 虚拟跳线增强
- [`ASIO-Ultra-drivers`](https://github.com/GeekASMR/ASIO-Ultra-drivers) — ASIO 录音卡虚拟通道

**🌐 网络音频**
- [`network-ultra-server`](https://github.com/GeekASMR/network-ultra-server) — 跨网点协作中继（Go，一行命令自部署）

</td>
<td valign="top" width="50%">

**🎛 DAW 工具链**
- [`UA-LUNA-Simplified-Chinese-Patch`](https://github.com/GeekASMR/UA-LUNA-Simplified-Chinese-Patch) — UA LUNA 中文化
- [`UAD-Plugin-Manager`](https://github.com/GeekASMR/UAD-Plugin-Manager) — UAD 插件管理器

**🍎 黑苹果 OpenCore**
- Z370 / Z390 Phantom ITX 等多套配置（仓库后缀 `*-OpenCore-Hackintosh`）

**🪟 顺手做的小工具**
- [`window-drawer`](https://github.com/GeekASMR/window-drawer) — Windows 抽屉式窗口管理

</td>
</tr>
</table>

完整仓库列表 → <https://github.com/GeekASMR?tab=repositories>

---

### 🛠 常用工具链

`C++` · `Rust` · `Go` · `Swift` · `WDK` · `JUCE` · `Tauri` · `CMake` · `PowerShell`

---

<div align="center">

<img src="https://raw.githubusercontent.com/GeekASMR/GeekASMR/main/github-metrics.svg" alt="GitHub 指标" width="640">

<sub>指标 SVG 由 <a href="https://github.com/lowlighter/metrics">lowlighter/metrics</a> 通过 GitHub Actions 每天自动渲染并提交回仓库（见 <code>.github/workflows/metrics.yml</code>）。徽章实时数据来自 shields.io，缓存约 1 小时。</sub>

</div>
