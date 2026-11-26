# 知识贡献 Skill

让 AI 把当前问题处理过程整理成 Service OS 知识草稿，保留已验证的事实、标注未知结论、脱敏，并按平台模板提交。默认保存草稿，只有本人明确要求后才提交人工审核。

## 接入需要什么

- 支持 **Streamable HTTP** 的 AI 工具，例如支持远程 MCP 配置的 Codex。
- 平台管理员已启用远程知识投稿 MCP。
- 本人的知识库成员或外部协作者账号，以及该账号创建的个人访问令牌。

远程 MCP 由平台运行，你只需配置地址和令牌，不需要下载本地 MCP 客户端或安装 Node。此 Skill 是工作流程说明；安装 Skill 不会自动配置 MCP，也不会创建令牌或绕过权限。

## 安装 Skill

将本目录交给 Codex 的 `skill-installer`，例如：

```text
请使用 skill-installer 安装 https://github.com/Benjamin527/skill/tree/main/skills/knowledge-contribute 中的 Skill。只安装 Skill，不修改 MCP 配置。
```

也可以下载本目录，放到 `~/.agents/skills/knowledge-contribute/`，确认其中包含 `SKILL.md`。安装后检查技能列表；未出现时重新打开 Codex。其他工具按各自的 Skill 安装方式操作。

参考：[Codex Skill 官方说明](https://learn.chatgpt.com/docs/build-skills)。

## 配置远程 MCP

从平台「知识库 → 接入指南」复制当前环境的 MCP 地址；接口路径为 `/api/agent/knowledge/mcp`。只有平台部署并启用远程端点后，该地址才可连接。使用自己的个人令牌，以 `Authorization: Bearer <个人令牌>` 认证，不使用网页 Cookie，也不使用 OAuth 登录。

Codex 可在 `~/.codex/config.toml` 合并以下配置（替换示例地址）：

```toml
[mcp_servers.serviceos-contribution]
url = "https://your-platform.example/api/agent/knowledge/mcp"
bearer_token_env_var = "SERVICEOS_KNOWLEDGE_TOKEN"
```

在启动 Codex 的环境中设置 `SERVICEOS_KNOWLEDGE_TOKEN` 为个人令牌。桌面应用可能不会继承终端环境变量，请按客户端支持的凭据方式配置并重新连接。不要把真实令牌粘贴到 AI 对话、知识正文或 GitHub。

HTTP 地址可以用于这个远程端点，但其令牌和内容传输未加密；部分 AI 工具会限制公网 HTTP。请使用管理员提供的实际地址，不要把 HTTP 擅自改成尚未启用的 HTTPS。建议平台提供 HTTPS 入口。

参考：[Codex MCP 官方配置说明](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)。

## 首次使用

先做只读检查：

```text
请通过 serviceos-contribution 查询可用知识模板和我有权限的客户，确认连接成功。不要创建或修改内容。
```

在已有问题处理上下文的对话中输入：

```text
$knowledge-contribute
把刚才处理的问题按平台模板整理成知识草稿。先读取可用模板和客户，保留已验证的处理步骤与结果，标注尚未验证的结论，去除敏感信息。先保存草稿，不提交审核，返回稿件链接。
```

打开返回的链接或「我的投稿」检查内容，确认后再明确要求“将这篇稿件提交审核”。提交进入已有人工审核，不会自动发布。

## 带图片的知识怎么准备

使用新版 Skill 时，提交人的 Agent 会主动检查图片和已确认的上下文，补写图片说明。平台提供写作示例和缺项检查，不在服务端自动识图或生成说明。Agent 无法看到原图、或无法确认图片用途时，会指出具体图片并询问你，先保留草稿。

你也可以手动这样做：

1. 把 Markdown 与图片文件夹放在一起，用相对路径引用图片。
2. 在 `![这里写图片说明](images/notify.png)` 的方括号中写清**画面是什么、用于说明哪一步**。例如，原图确实展示该操作时，写 `![通知设置页面：在通知方式中选择飞书渠道](images/notify.png)`，不要只写“截图1”或“notify.png”。错误截图写出画面中的错误，验证截图写出可见结果；不要猜原因或结论。
3. 将 Markdown 和图片文件夹一起打包成 ZIP，在「我的投稿」导入并检查预览。提示说明不完整时，按图片位置返回原 Markdown 修改后重新导入，或保存草稿后在正文编辑器里改方括号内的文字。
4. 可以先保存草稿；提交审核前补齐图片说明，并检查实际图片是否正确。

可以直接对 Agent 说：

```text
$knowledge-contribute
把这篇文章和图片整理成知识草稿。请查看原图与上下文，主动补齐每张图的说明，保留原图及引用。不能确定的地方具体问我，不要猜；先保存草稿，不提交审核。
```

投稿 MCP/CLI 当前传输的是正文，**不会自动上传正文里引用的本地图片或 ZIP**。新图片需要先通过网页 ZIP 导入/上传登记；之后 Agent 读取已保存稿件，使用平台返回的真实图片引用进行编辑。不能把 `images/a.png`、本地绝对路径或猜测出的地址当成已上传图片。

服务端的 `imageQuality` 检查会列出图片位置和缺项，网页、MCP、CLI 遵循同一提交规则。检查通过只说明没有检测到空说明或明显占位，不保证语义正确，也不等于消息渠道已经发送成功。

## 更新已安装的 Skill

更新或重新安装本目录的 Skill 文件，然后按客户端要求刷新技能或重新打开会话；有 MCP 工具缓存的客户端还需刷新/重连。公开仓库更新不会自动替换别人已经安装的副本。平台上线后，服务端审核前检查直接生效，旧 Skill 使用者仍会收到缺项提示。

## 权限与问题处理

- 只能维护本人投稿及已授权客户；没有审核、发布或删除工具。
- 令牌到期、撤销、账号状态或角色变化后会被拒绝；修改密码后需要重新创建令牌。
- 模板校验保证必要结构，不证明事实或结论正确，仍需人工检查。
- 版本冲突：先读取当前稿件，再确认修改。结果不明的超时：用同一 requestId、相同内容和版本重试，避免重复创建。
- 本 Skill 只整理用户当前明确要求的内容，不扫描其他对话或自动上传聊天历史。

本目录不包含平台地址、个人凭据或业务数据。后续更新下载同一目录，替换 Skill 文件即可。
