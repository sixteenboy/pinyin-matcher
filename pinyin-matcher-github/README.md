# 🔤 拼音匹配器 Android 应用

[![Build APK](https://github.com/YOUR_USERNAME/pinyin-matcher/actions/workflows/build-apk.yml/badge.svg)](https://github.com/YOUR_USERNAME/pinyin-matcher/actions/workflows/build-apk.yml)
[![Nightly Build](https://github.com/YOUR_USERNAME/pinyin-matcher/actions/workflows/nightly.yml/badge.svg)](https://github.com/YOUR_USERNAME/pinyin-matcher/actions/workflows/nightly.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Android](https://img.shields.io/badge/platform-Android%205.0%2B-green.svg)](https://developer.android.com)
[![Kivy](https://img.shields.io/badge/framework-Kivy%202.1.0-orange.svg)](https://kivy.org)

一个基于 Kivy 开发的拼音匹配器 Android 应用，支持根据拼音字母逐步匹配显示汉字。

## 📱 功能特性

- 🔍 **智能拼音匹配** - 根据输入的拼音字母实时匹配汉字
- 📊 **完整拼音数据库** - 包含丰富的汉字拼音对应关系
- 🎨 **现代化界面** - 基于 Kivy 的美观移动端界面
- 🚀 **高性能** - 优化的匹配算法，响应迅速
- 📱 **Android 兼容** - 支持 Android 5.0+ 设备

## 📥 下载安装

### 🎯 正式版本
访问 [Releases](../../releases) 页面下载最新的正式版 APK。

### 🔧 开发版本
每次代码更新后会自动构建开发版本，可在 [Actions](../../actions) 页面下载最新构建的 APK。

### 夜间构建
每天凌晨会自动构建夜间版本，包含最新的代码更改。

## 🛠️ 自动构建

本项目使用 GitHub Actions 实现全自动构建：

### 🔄 触发条件
- **推送代码** - 每次推送到 main/master 分支
- **Pull Request** - 创建或更新 PR 时
- **标签发布** - 推送 `v*` 标签时自动发布
- **定时构建** - 每天凌晨 2 点自动构建
- **手动触发** - 在 Actions 页面手动运行

### 📦 构建产物
- **APK 文件** - 可直接安装的 Android 应用
- **构建日志** - 详细的构建过程记录
- **自动发布** - 标签版本自动创建 GitHub Release

## 🚀 快速开始

### 方法1: 直接下载
1. 访问 [Releases](https://github.com/YOUR_USERNAME/YOUR_REPO/releases) 页面
2. 下载最新版本的 APK 文件
3. 在 Android 设备上安装

### 方法2: 自己构建
1. Fork 这个仓库
2. 推送代码或创建标签
3. GitHub Actions 会自动构建 APK
4. 在 Actions 页面下载构建结果

## 📋 系统要求

- **Android 版本**: 5.0 (API 21) 或更高
- **架构支持**: ARM64, ARMv7
- **存储空间**: 至少 50MB 可用空间
- **权限需求**: 
  - 网络访问 (INTERNET)
  - 存储读写 (READ/WRITE_EXTERNAL_STORAGE)

## 🔧 开发环境

如果您想在本地开发或构建：

```bash
# 安装依赖
pip install buildozer kivy==2.1.0

# 构建 APK
buildozer android debug
```

## 📊 项目结构

```
pinyin/
├── main.py                    # 应用入口点
├── pinyin_mobile.py          # 主要应用逻辑
├── 拼音.csv                  # 拼音数据文件
├── buildozer.spec            # Android 构建配置
├── .github/workflows/        # GitHub Actions 工作流
│   ├── build-apk.yml        # 主要构建流程
│   ├── release.yml          # 发布流程
│   └── nightly.yml          # 夜间构建
└── README.md                 # 项目说明
```

## 🤝 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📝 更新日志

查看 [Releases](https://github.com/YOUR_USERNAME/YOUR_REPO/releases) 页面了解详细的版本更新信息。

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- [Kivy](https://kivy.org/) - 跨平台 Python 框架
- [Buildozer](https://github.com/kivy/buildozer) - Android 打包工具
- [GitHub Actions](https://github.com/features/actions) - 自动化构建平台

## 📞 联系方式

如有问题或建议，请：
- 创建 [Issue](https://github.com/YOUR_USERNAME/YOUR_REPO/issues)
- 发起 [Discussion](https://github.com/YOUR_USERNAME/YOUR_REPO/discussions)

---

⭐ 如果这个项目对您有帮助，请给个 Star！
