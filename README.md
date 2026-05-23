<!-- GitHub Profile README · 渲染于 https://github.com/GeekASMR -->

<!-- ─────────────────────────  顶部 Banner（保留）  ───────────────────────── -->

![banner](https://capsule-render.vercel.app/api?type=waving&color=0:E91E63,50:9C27B0,100:00599C&height=220&section=header&text=GeekASMR&fontColor=ffffff&fontSize=72&fontAlignY=38&desc=Windows%20%E9%9F%B3%E9%A2%91%E5%86%85%E6%A0%B8%20%C2%B7%20%E8%99%9A%E6%8B%9F%E9%A9%B1%E5%8A%A8%20%C2%B7%20VST3%20%E6%A1%A5%E6%8E%A5&descAlignY=60&descSize=18&animation=fadeIn)

<!-- ─────────────────────────  关键词堆叠（新增）  ───────────────────────── -->

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/GeekASMR/GeekASMR/main/keywords-dark.svg">
  <img src="https://raw.githubusercontent.com/GeekASMR/GeekASMR/main/keywords-light.svg" alt="工程关键词" width="100%">
</picture>

</div>

<!-- ─────────────────────────  打字机 + 状态 ─────────────────────────────── -->

<div align="center">

[![打字机](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=3000&pause=600&color=E91E63&center=true&vCenter=true&width=720&lines=%E8%AE%A9+Windows+%E7%B3%BB%E7%BB%9F%E9%9F%B3%E9%A2%91%E4%BB%A5%E9%87%87%E6%A0%B7%E7%BA%A7%E7%B2%BE%E5%BA%A6%E6%8A%B5%E8%BE%BE+DAW;%E5%9C%A8%E5%86%85%E6%A0%B8%E5%B1%82%E6%89%93%E9%80%9A%E9%9F%B3%E9%A2%91+%C2%B7+%E5%9C%A8%E5%BA%94%E7%94%A8%E5%B1%82%E6%8E%92%E9%93%B6%E9%92%88;%E5%81%9A%E4%B8%80%E4%BB%B6%E8%83%BD%E7%94%A8%E5%8D%81%E5%B9%B4%E7%9A%84%E4%B8%9C%E8%A5%BF;WDM+%E2%86%92+VST3+%E2%86%92+DAW+%E2%86%92+%E5%85%A8%E4%B8%96%E7%95%8C)](#)

📍 哈尔滨 &nbsp;·&nbsp; 🌐 [geek.asmrtop.cn](https://geek.asmrtop.cn/) &nbsp;·&nbsp; 💚 [赞助 WHQL 签名](https://ultra.asmrtop.cn/donate/)

<!-- 主页访问改用 visitor-badge.laobi.icu（不易被墙、中文 label 不会截断） -->
[![访问](https://visitor-badge.laobi.icu/badge?page_id=GeekASMR.GeekASMR&left_text=主页访问&left_color=555&right_color=E91E63)](#)
[![关注](https://img.shields.io/github/followers/GeekASMR?label=关注&style=flat-square&color=00599C)](https://github.com/GeekASMR)
[![星标](https://img.shields.io/github/stars/GeekASMR?label=总星标&style=flat-square&color=FFD700)](https://github.com/GeekASMR)

</div>

---

### 🎯 我在做什么

把 Windows 系统音频以**采样级精度**送进 DAW，再让它跨越公网与协作者实时同步。

```mermaid
flowchart LR
    A[🪟 Windows<br>系统音频] --> B[⚙️ WDM<br>内核驱动]
    B --> C[🔌 VST3<br>桥接插件]
    C --> D[🎚 DAW<br>数字音频工作站]
    C -.-> E[🌐 Network Ultra<br>跨网协作中继]
    E -.-> F[👥 远端 DAW]

    classDef pink fill:#E91E63,stroke:#fff,color:#fff,font-weight:bold
    classDef purple fill:#9C27B0,stroke:#fff,color:#fff,font-weight:bold
    classDef blue fill:#00599C,stroke:#fff,color:#fff,font-weight:bold
    classDef gray fill:#555,stroke:#fff,color:#fff

    class A,F gray
    class B,C pink
    class D blue
    class E purple
```

---

### 🚀 旗舰项目 — WDM2VST Ultra

WDM 内核驱动 + 5 个 VST3，把任意 Windows 程序的声音变成 DAW 里的一条轨道，反向亦可。低延迟、零拷贝 IPC、原生 VST3 宿主。

[![release](https://img.shields.io/github/v/release/GeekASMR/WDM2VST-Ultra?style=for-the-badge&label=%E6%9C%80%E6%96%B0%E7%89%88%E6%9C%AC&color=E91E63)](https://github.com/GeekASMR/WDM2VST-Ultra/releases)
[![downloads](https://img.shields.io/github/downloads/GeekASMR/WDM2VST-Ultra/total?style=for-the-badge&label=%E6%80%BB%E4%B8%8B%E8%BD%BD&color=0E8A16)](https://github.com/GeekASMR/WDM2VST-Ultra/releases)
[![stars](https://img.shields.io/github/stars/GeekASMR/WDM2VST-Ultra?style=for-the-badge&label=%E6%98%9F%E6%A0%87&color=FFD700)](https://github.com/GeekASMR/WDM2VST-Ultra)

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

**🔊 音频内核 & 驱动**
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

<p align="center">
  <img src="https://img.shields.io/badge/-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/-Rust-000000?style=for-the-badge&logo=rust&logoColor=white" alt="Rust">
  <img src="https://img.shields.io/badge/-Go-00ADD8?style=for-the-badge&logo=go&logoColor=white" alt="Go">
  <img src="https://img.shields.io/badge/-Swift-F05138?style=for-the-badge&logo=swift&logoColor=white" alt="Swift">
  <img src="https://img.shields.io/badge/-PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white" alt="PowerShell">
</p>
<p align="center">
  <img src="https://img.shields.io/badge/-Windows%20WDK-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="WDK">
  <img src="https://img.shields.io/badge/-JUCE-8DC63F?style=for-the-badge&logo=juce&logoColor=white" alt="JUCE">
  <img src="https://img.shields.io/badge/-Tauri-FFC131?style=for-the-badge&logo=tauri&logoColor=black" alt="Tauri">
  <img src="https://img.shields.io/badge/-CMake-064F8C?style=for-the-badge&logo=cmake&logoColor=white" alt="CMake">
  <img src="https://img.shields.io/badge/-VST3-CF202E?style=for-the-badge&logo=audiobookshelf&logoColor=white" alt="VST3">
</p>

---

### 📊 数据可视化

<div align="center">

<a href="https://github.com/GeekASMR">
  <img height="170" src="https://github-readme-stats.vercel.app/api?username=GeekASMR&locale=cn&show_icons=true&theme=default&hide_border=true&include_all_commits=true&count_private=true&custom_title=%E2%9A%A1+GitHub+%E7%BB%9F%E8%AE%A1&title_color=E91E63&icon_color=00599C&text_color=333333" alt="GitHub 统计" />
</a>
<a href="https://github.com/GeekASMR">
  <img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=GeekASMR&locale=cn&layout=compact&theme=default&hide_border=true&langs_count=8&custom_title=%F0%9F%94%A4+%E5%B8%B8%E7%94%A8%E8%AF%AD%E8%A8%80&title_color=E91E63&text_color=333333" alt="常用语言" />
</a>

<a href="https://github.com/GeekASMR">
  <img height="170" src="https://streak-stats.demolab.com?user=GeekASMR&locale=zh_CN&theme=default&hide_border=true&date_format=Y.n.j&ring=E91E63&fire=E91E63&currStreakLabel=E91E63" alt="提交连续天数" />
</a>

<br>

<a href="https://github.com/GeekASMR">
  <img src="https://github-profile-trophy.vercel.app/?username=GeekASMR&theme=flat&no-bg=true&no-frame=true&margin-w=8&column=7&title=Stars,Followers,Commits,Repositories,PullRequest,Issues,Reviews" alt="奖杯" />
</a>

</div>

---

<div align="center">

<sub>
统计图来自 <a href="https://github.com/anuraghazra/github-readme-stats">github-readme-stats</a> · <a href="https://github.com/DenverCoder1/github-readme-streak-stats">streak-stats</a> · <a href="https://github.com/ryo-ma/github-profile-trophy">github-profile-trophy</a>，已开启简体中文 locale。<br>
关键词云 SVG 由仓库内 <code>scripts/gen_keywords.py</code> 一次性生成（不依赖外部服务，永远不会 404）。徽章实时数据来自 shields.io，缓存约 1 小时。
</sub>

<br><br>

![footer](https://capsule-render.vercel.app/api?type=waving&color=0:00599C,50:9C27B0,100:E91E63&height=120&section=footer)

</div>
