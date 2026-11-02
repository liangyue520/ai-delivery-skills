# AI Delivery Skills · 交付优先与多智能体开发技能包

用三个互相配合的技能，把 AI 协作的重点放在可操作成果、必要验证和清晰交付上。小任务直接处理；复杂开发按需要组织代理，由主聊天负责集成和结果。

**v0.1.0 · 首个私有维护版本** · 中文 · 项目整理、改编与维护：**梁养浩**

GitHub 私有仓库：[liangyue520/ai-delivery-skills](https://github.com/liangyue520/ai-delivery-skills)。仅获授权的账号可以访问；私有上传不代表已选定开源许可。

## 包含的技能

| 技能 | 用途 | 什么时候用 |
|---|---|---|
| [delivery-first](skills/delivery-first/SKILL.md) | 明确实际目标、复用已有成果、验证后交付 | 各类请求开始时，或需要纠正流程过重时 |
| [ai-development-workflow](skills/ai-development-workflow/SKILL.md) | 按任务选择接手、设计、开发、验证和交付阶段 | 软件项目开发、接手、修复或交付 |
| [multi-agent-dev-sop](skills/multi-agent-dev-sop/SKILL.md) | 在授权范围内组织代理、集成、验证与恢复 | 多智能体或跨聊天协作、部署和迁移 |

三个技能可以按任务组合，不必每次执行完整流程。后两个技能引用 `delivery-first`，也互相引用部分材料，因此建议将三个文件夹作为同级目录一起安装。

## 快速开始

使用已获仓库访问权限的 GitHub 账号克隆，或下载并解压 ZIP：

```bash
git clone https://github.com/liangyue520/ai-delivery-skills.git
```

将 `skills/` 里的三个完整文件夹复制到宿主扫描的同一个技能目录。例如 Codex 项目目录：

```text
你的项目/
└── .agents/skills/
    ├── delivery-first/SKILL.md
    ├── ai-development-workflow/SKILL.md
    └── multi-agent-dev-sop/SKILL.md
```

保留每个目录的 `references/` 和 `agents/`；若已有同名技能，先比较已有内容并避免覆盖。按宿主的技能发现方式重新加载，在技能列表中确认三个名称。不同宿主及配置的目录和能力可能不同；本包尚未做跨宿主运行验证。

在需要时明确调用，例如：

```text
使用 delivery-first 和 ai-development-workflow。
请检查这个项目的登录问题，先定位原因，再在我授权的范围内修复，
验证受影响的登录流程，说明结果和未验证的部分。
```

```text
使用 delivery-first 和 multi-agent-dev-sop。
请处理我提供的开发任务；在当前授权和工具规则允许时，
把能独立完成的部分交给代理，主聊天负责集成和必要验证。
```

需要每次新请求或项目开发时默认应用，可自行将 [AGENTS.example.md](AGENTS.example.md) 中适用内容合并到项目或个人指令；不要覆盖原有约定。安装技能不会自动修改这些指令，也不能让已经运行的聊天自动重新读取规则。

## 工作方式与边界

- 先确认用户要达到什么结果，查找可复用入口和已有修改，再按实际需要实施与验证。
- 独立且有收益的任务可以在授权和工具规则允许时委派；小任务不机械拆分。主聊天核实返回并负责整合。
- 保留业务权限、真实数据保护、工具限制和必要验证；不把日常开发变成多层审批或重复报告。
- 区分实现、真实运行、独立审查和用户验收。没有实际审查或运行证据时，不声称通过。
- 本包是 Markdown 工作指引，不包含调度程序、权限控制、预算限制或自动部署工具；宿主能力与用户授权决定能做什么。

## 验证和维护

维护者可在包根目录运行 `python3 scripts/validate_package.py`，检查三个技能的基本元数据及本地 Markdown 引用。脚本只依赖 Python 3 标准库，不下载依赖。当前只完成静态检查和 ZIP 可读性检查，未完成真实项目、代理协作或跨宿主端到端验证。

本包是从用户现有本地技能整理出的**可分享改编副本**：去除了私人项目与个人经历，对协作授权改为遵循当前用户及宿主的实际规则。原本地技能保持不变。变更见 [CHANGELOG.md](CHANGELOG.md)。

## 署名、来源与许可

项目整理、改编与维护：**梁养浩**。对分发或公开改编时保留署名的意向见 [NOTICE.md](NOTICE.md)，来源及待核事项见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。**整体许可尚未确定；当前没有根目录开源许可证。** NOTICE 本身不授予使用、修改或分发许可；公开发布前应确认来源、适用权利及具体许可。
