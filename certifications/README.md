# 等级考试与认证

按**考试体系**组织：高校课程、国家等级考试、软考与行业认证。

## 目录结构

```
certifications/
├── university/     # 高校与等级考试
├── industry/       # 行业认证
└── _shared/        # 通用模板
```

## 高校与等级考试

| 考试 | 入口 | 关联教程 |
|------|------|----------|
| 大学 C 语言期末 | [university/c-language/](university/c-language/) | [languages/c/exams/](../languages/c/exams/) |
| 计算机二级 | university/computer-level-2/ | 计划中 |
| 软考 | university/software-design/ | 计划中 |

## 行业认证

| 认证 | 状态 |
|------|------|
| AWS | 计划中 |
| Kubernetes (CKA/CKAD) | 计划中 |

## 双链约定

- **题目与解析**：放在 `languages/<lang>/exams/`
- **大纲、复习计划、考点对照**：放在 `certifications/university/<exam>/`
- 两侧 README 互相链接，方便读者从考试入口或语言入口进入

模板见 [_shared/](_shared/)。
