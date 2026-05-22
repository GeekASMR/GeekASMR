<!-- 这是 GitHub 的 Profile README，会自动渲染在 https://github.com/GeekASMR -->

<div align="center">

# 你好，我是 GeekASMR <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="28">

**Windows 音频内核 / 虚拟音频驱动 / DAW 工具链 / 黑苹果**

📍 哈尔滨 · 🌐 [geek.asmrtop.cn](https://geek.asmrtop.cn/) · 💚 [赞助 WHQL 签名](https://ultra.asmrtop.cn/donate/)

</div>

---

<img src="https://raw.githubusercontent.com/GeekASMR/GeekASMR/main/github-metrics.svg" alt="GitHub 指标" align="right" width="420">

### 🔧 在做的事

- 🔊 **Windows 音频内核** — WDM 内核驱动、虚拟音频端点、低延迟 IPC、VST3 宿主。维护 [`WDM2VST-Ultra`](https://github.com/GeekASMR/WDM2VST-Ultra)（系统音频 ↔ DAW 桥接）、[`UMC-Ultra-drivers`](https://github.com/GeekASMR/UMC-Ultra-drivers)、[`ASIO-Ultra-drivers`](https://github.com/GeekASMR/ASIO-Ultra-drivers)。
- 🌐 **网络音频协作** — [`network-ultra-server`](https://github.com/GeekASMR/network-ultra-server)，跨网点的 ASMR / 监听协作中继。
- 🎛 **DAW 本地化与工具链** — [LUNA 简体中文补丁](https://github.com/GeekASMR/UA-LUNA-Simplified-Chinese-Patch)、[`UAD-Plugin-Manager`](https://github.com/GeekASMR/UAD-Plugin-Manager)。
- 🍎 **黑苹果 OpenCore** — Z370/Z390 Phantom ITX 等多套配置，仓库都在 `*-OpenCore-Hackintosh`。
- 🪟 顺手做的 Windows 小工具 — [`window-drawer`](https://github.com/GeekASMR/window-drawer)。

### 🎯 现阶段重点

- 推动 WDM2VST Ultra 通过 **微软 WHQL 签名**，让国内游戏反作弊（腾讯 ACE / 网易易盾 / EAC）不再误报。这是行业里唯一彻底的解法。[赞助一份心意 →](https://ultra.asmrtop.cn/donate/)
- 网络协作音频桥的 codec / jitter buffer 调优。

---

### 🛠 技术栈

[![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)](#)
[![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)](#)
[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](#)
[![JUCE](https://img.shields.io/badge/JUCE-8DC63F?style=for-the-badge&logoColor=white)](https://juce.com/)
[![Tauri](https://img.shields.io/badge/Tauri-FFC131?style=for-the-badge&logo=tauri&logoColor=black)](https://tauri.app/)

[![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](#)
[![WDK](https://img.shields.io/badge/Windows%20Driver%20Kit-005A9C?style=for-the-badge&logo=windows&logoColor=white)](#)
[![macOS](https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white)](#)
[![CMake](https://img.shields.io/badge/CMake-064F8C?style=for-the-badge&logo=cmake&logoColor=white)](#)
[![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white)](#)

---

### 📌 主要项目

| 项目 | 说明 | 状态 |
|---|---|---|
| **[WDM2VST-Ultra](https://github.com/GeekASMR/WDM2VST-Ultra)** | Windows 系统音频 ↔ DAW 低延迟桥接，5 个 VST3 + 内核驱动 | ![v](https://img.shields.io/github/v/release/GeekASMR/WDM2VST-Ultra?style=flat-square&label=&color=E91E63) ![dl](https://img.shields.io/github/downloads/GeekASMR/WDM2VST-Ultra/total?style=flat-square&label=⬇&color=0E8A16) ![star](https://img.shields.io/github/stars/GeekASMR/WDM2VST-Ultra?style=flat-square&label=⭐&color=FFD700) |
| **[network-ultra-server](https://github.com/GeekASMR/network-ultra-server)** | Network Ultra 客户端用的中继服务器（Go），一行命令自部署 | ![star](https://img.shields.io/github/stars/GeekASMR/network-ultra-server?style=flat-square&label=⭐&color=FFD700) |
| **[UMC-Ultra-drivers](https://github.com/GeekASMR/UMC-Ultra-drivers)** | 百灵达 UMC 系列声卡虚拟跳线增强驱动 | ![star](https://img.shields.io/github/stars/GeekASMR/UMC-Ultra-drivers?style=flat-square&label=⭐&color=FFD700) |
| **[ASIO-Ultra-drivers](https://github.com/GeekASMR/ASIO-Ultra-drivers)** | ASIO 录音声卡增强驱动，开启虚拟通道 | ![star](https://img.shields.io/github/stars/GeekASMR/ASIO-Ultra-drivers?style=flat-square&label=⭐&color=FFD700) |
| **[UA-LUNA-Simplified-Chinese-Patch](https://github.com/GeekASMR/UA-LUNA-Simplified-Chinese-Patch)** | UA LUNA DAW 简体中文补丁 | ![star](https://img.shields.io/github/stars/GeekASMR/UA-LUNA-Simplified-Chinese-Patch?style=flat-square&label=⭐&color=FFD700) |
| **[UAD-Plugin-Manager](https://github.com/GeekASMR/UAD-Plugin-Manager)** | UAD 插件管理器 | ![star](https://img.shields.io/github/stars/GeekASMR/UAD-Plugin-Manager?style=flat-square&label=⭐&color=FFD700) |

完整仓库列表：<https://github.com/GeekASMR?tab=repositories>

---

<sub>右上的 GitHub 指标 SVG 由 <a href="https://github.com/lowlighter/metrics">lowlighter/metrics</a> 通过 GitHub Actions 每天自动渲染并提交回仓库（见 <code>.github/workflows/metrics.yml</code>）。徽章实时数据来自 shields.io，缓存约 1 小时。</sub>
