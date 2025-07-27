# 🚀 GitHub Codespaces 构建指南

## 📋 快速开始

### 1️⃣ 启动 Codespaces
1. 在 GitHub 仓库页面点击绿色的 **"Code"** 按钮
2. 选择 **"Codespaces"** 标签
3. 点击 **"Create codespace on main"**
4. 等待环境初始化（约 3-5 分钟）

### 2️⃣ 环境自动设置
Codespace 启动后会自动：
- ✅ 安装 Ubuntu 22.04 环境
- ✅ 安装 Python 3.9 和 Java 8
- ✅ 安装所有 Android 构建依赖
- ✅ 安装 Buildozer 和 Kivy
- ✅ 设置环境变量和别名

### 3️⃣ 开始构建
环境准备完成后，在终端运行：

```bash
# 方法1：使用一键构建脚本（推荐）
./build.sh

# 方法2：手动构建
buildozer android debug

# 方法3：详细日志构建
buildozer android debug --verbose
```

## 🎯 构建步骤详解

### 步骤1：检查环境
```bash
# 检查 Java
java -version

# 检查 Python
python3 --version

# 检查 Buildozer
buildozer version

# 查看项目文件
ls -la
```

### 步骤2：选择配置文件
```bash
# 使用 Codespaces 优化配置（推荐）
cp buildozer-codespaces.spec buildozer.spec

# 或者使用原始配置
# 已有 buildozer.spec 文件
```

### 步骤3：开始构建
```bash
# 一键构建（推荐）
./build.sh
```

### 步骤4：下载 APK
构建成功后：
1. APK 文件位于 `bin/` 目录
2. 在 VS Code 文件浏览器中右键点击 APK 文件
3. 选择 **"Download"** 下载到本地

## 🔧 常用命令

### 构建相关
```bash
# 构建 APK
./build.sh

# 清理构建缓存
./clean.sh

# 手动构建
buildozer android debug

# 详细日志构建
buildozer android debug --verbose

# 清理 buildozer 缓存
buildozer android clean
```

### 调试相关
```bash
# 查看构建日志
cat .buildozer/android/platform/build-*/build.log

# 查看 Python-for-Android 日志
find .buildozer -name "*.log" -exec tail -50 {} \;

# 检查 APK 文件
ls -la bin/

# 查看构建配置
cat buildozer.spec | grep -E "^(android|requirements|version)"
```

### 环境相关
```bash
# 重新加载环境变量
source ~/.bashrc

# 查看环境变量
env | grep -E "(JAVA|ANDROID|BUILDOZER)"

# 检查磁盘空间
df -h

# 查看内存使用
free -h
```

## 🚨 常见问题解决

### 问题1：构建失败
```bash
# 清理并重新构建
./clean.sh
./build.sh
```

### 问题2：Java 路径问题
```bash
# 检查 Java 安装
which java
echo $JAVA_HOME

# 重新设置 Java 路径
export JAVA_HOME=/usr/local/sdkman/candidates/java/current
```

### 问题3：磁盘空间不足
```bash
# 清理构建缓存
buildozer android clean
rm -rf .buildozer/

# 清理系统缓存
sudo apt-get clean
```

### 问题4：网络问题
```bash
# 重试构建
./build.sh

# 或者使用代理（如果需要）
export HTTP_PROXY=your-proxy
export HTTPS_PROXY=your-proxy
```

## 📊 构建时间预估

| 阶段 | 时间 | 说明 |
|------|------|------|
| 环境初始化 | 3-5分钟 | Codespace 启动 |
| 首次构建 | 30-60分钟 | 下载 Android SDK/NDK |
| 后续构建 | 5-15分钟 | 使用缓存 |

## 🎉 成功标志

构建成功时您会看到：
```
✅ 构建成功！
📱 APK 文件位置：
bin/pinyinmatcher-1.0-arm64-v8a-debug.apk
bin/pinyinmatcher-1.0-armeabi-v7a-debug.apk

🎉 您可以下载 APK 文件到本地进行安装！
```

## 💡 优化建议

### 1️⃣ 保持 Codespace 活跃
- Codespace 会在 30 分钟无活动后暂停
- 定期在终端输入命令保持活跃

### 2️⃣ 使用构建缓存
- 首次构建后，`.buildozer` 目录包含缓存
- 后续构建会快很多

### 3️⃣ 监控资源使用
```bash
# 查看 CPU 使用
top

# 查看磁盘使用
du -sh .buildozer/
```

## 🎯 下一步

构建成功后：
1. **下载 APK** 到本地设备
2. **安装到 Android 手机** 进行测试
3. **如果需要修改**，直接在 Codespace 中编辑代码
4. **重新构建** 获取新版本

---

**🎉 享受在 GitHub Codespaces 中构建 Android APK 的便利！**
