# skill

个人 Codex skills：观测云最佳实践写作、飞书项目反馈预览与客户服务记录提交。

| Skill | 用途 |
| --- | --- |
| [guance-best-practice-writing](skills/guance-best-practice-writing/SKILL.md) | 观测云最佳实践写作 |
| [meegle-feedback-preview](skills/meegle-feedback-preview/SKILL.md) | 飞书项目反馈预览与提交 |
| [guance-service-record-submit](skills/guance-service-record-submit/SKILL.md) | 从 Codex 对话整理服务记录，读取客户配置并以当前飞书用户提交 |

## 安装服务记录 skill

需要 Python 3、已安装并完成本人登录授权的 `lark-cli`，以及 Codex 中可用的 `lark-base`、`lark-shared` 技能。每位成员需有表单、服务记录表和客户配置表的访问权限。

```bash
git clone https://github.com/Benjamin527/skill.git
cd skill
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/guance-service-record-submit "${CODEX_HOME:-$HOME/.codex}/skills/"
```

首次安装后，在已安装的 skill 中将 `references/target.example.json` 复制为 `references/target.json`，填入团队提供的 Base、正式表、客户配置表标识和表单分享信息。真实配置不包含在公开仓库中；已有配置时不要用空模板覆盖。

在包含客户问题处理过程的 Codex 对话中输入：

```text
$guance-service-record-submit
把这次问题整理成服务记录，先预览，不提交。
```

确认内容后说“提交这条服务记录”。提交目标由本地配置决定，配置为正式表时会写入正式数据。

## 更新

在仓库目录执行：

```bash
git pull --ff-only
cp -R skills/guance-service-record-submit "${CODEX_HOME:-$HOME/.codex}/skills/"
```

以上覆盖更新 skill 文件，保留已安装目录中未随仓库分发的 `references/target.json`。无需重新填写客户配置或改变当前飞书登录身份。
