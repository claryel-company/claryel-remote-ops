# CLARYEL RemoteOps — 安装与私有配置

RemoteOps 通过您选择的 AI 聊天来管理您自己的 Windows、Ubuntu/Linux 或 macOS 电脑。

## 1. 安装

- [Windows 安装程序](../../installers/install-windows.ps1)
- [macOS 安装程序](../../installers/install-macos.sh)
- [Ubuntu 安装程序](../../installers/install-ubuntu.sh)

运行下载的文件。RemoteOps 安装在您的用户目录中，创建本地私有工作区，并且不会关闭操作系统安全功能。

## 2. 创建您个人的 Private 仓库

安装 GitHub CLI，运行 `gh auth login`，然后运行安装程序显示的命令：

```text
remoteops connect --path 您的私有路径 --create-private remoteops-my-computer
```

仓库会在您的 GitHub 账号中创建，公开范围为 `Private`。RemoteOps 不会把它改为公开，也不会添加协作者。

Private 表示对公众隐藏。您、您明确授权的人或应用，以及作为服务运营方的 GitHub 仍可能访问。请使用 passkey 或双重验证保护账号。

绝不要在 Git 中保存密码、令牌、私钥、恢复码、个人文件、聊天记录、原始日志、数据库或备份。

## 3. 验证隐私

```text
remoteops privacy-check --path 您的私有路径
```

只有结果显示 `"ok": true`、`"visibility": "PRIVATE"` 且没有发现问题时才继续。

## 4. 连接 ChatGPT

1. 打开 **ChatGPT > 设置 > Apps > GitHub**。
2. 选择 **仅选择的仓库**。
3. 只选择 `remoteops-my-computer`。
4. 批准前检查权限。
5. 检查 **设置 > 数据控制 > 为所有人改进模型**。
6. 不要在聊天中粘贴秘密或个人文件。

GitHub 应用和写入权限是否可用取决于 ChatGPT 套餐和模式。只读连接不能应用更改。

## 通信边界

RemoteOps 仅在您连接或同步私有仓库时联系 GitHub，仅在您主动使用时联系 ChatGPT，并且只为您批准的软件操作联系软件包来源。安装程序不添加广告或无关分析服务。

详细指南：[私有仓库](../../docs/PRIVATE_REPOSITORY_SETUP.md)、[ChatGPT](../../docs/CHATGPT_SETUP.md)、[隐私与网络](../../docs/PRIVACY_AND_NETWORK.md)。
