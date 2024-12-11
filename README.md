<div align="center">

  <img src="(https://github.com/Tshiyao/beautify_every_beauty/blob/main/static/封面.jpeg" />

美每美

BEAUTIFY_EVERY_BEAUTY


[中文](https://github.com/Tshiyao/beautify_every_beauty/blob/main/README.md)



</div>

## 目录

- [项目简介 :blush:](#项目简介-blush)
- [项目架构 :sunglasses:](#项目架构-sunglasses)
- [数据准备](#数据准备)
- [模型微调](#模型微调)


# 项目简介 :blush:

美每美是基于书生大模型InternLM的专属穿搭妆容助手。

- 通过Lagent实现信息获取助手，实时从各类数据源中获取最新潮流信息、气候温度情况以及用户个人信息，以形成最新最潮的个性化数据。

- 通过MindU进行数据的清洗和预处理，将数据进行统一格式化，方便后续的模型训练以及检索。将数据存入各数据仓库中。

- 将清洗后的高质量数据微调书生和灵笔大模型，赋予大模型图文能力和穿搭妆容的领域知识，以成为领域专家。

- 使用LMdeploy进行模型部署

- 使用Opencompass进行评测，持续优化。并且将用户的反馈收集，用于主观评测，推进后续模型升级。

- 通过Mindsearch进行数据检索，将用户需求转化为检索语句，通过检索语句找到最匹配的穿搭方案。

- 使用Lagent构建助手，提供穿搭咨询，每日潮流推荐，穿搭妆容推荐，穿搭妆容评价。

- 后续拟开展一键换衣，虚拟衣柜等功能，敬请期待

美每美作为一个基于先进AI技术的穿搭妆容助手，其工作流程和技术应用展示了一个高度智能化和个性化的服务系统。以下是对您描述的系统功能的详细解读和未来展望：


# 项目架构 :sunglasses:

![alt text](https://github.com/Tshiyao/beautify_every_beauty/blob/main/static/%E6%9E%B6%E6%9E%84%E5%9B%BE.png)

# 数据准备
1. 数据获取
   
爬取网上的文章、评论、图片，包括各种服装、美妆、服装配饰等。

1. 数据清洗

# 模型微调