<div align="center">

美每美

![logo](https://github.com/Tshiyao/beautify_every_beauty/blob/main/static/pic/LOGO.png)



BEAUTIFY_EVERY_BEAUTY


[中文](https://github.com/Tshiyao/beautify_every_beauty/blob/main/README.md)

探索模型：

[![Models](https://img.shields.io/badge/-gery?style=social&label=BEAUTIFY_EVERY_BEAUTY✨V0)](https://modelscope.cn/models/Tshiyao/beb)
[![Models](https://img.shields.io/badge/-gery?style=social&label=BEAUTIFY_EVERY_BEAUTY_7b✨V0)](https://modelscope.cn/models/Tshiyao/beb_7b)

探索应用：

[![Open in OpenXLab](https://cdn-static.openxlab.org.cn/app-center/openxlab_app.svg)](https://openxlab.org.cn/apps/detail/Liu_qihuang/BEAUTIFY_EVERY_BEAUTY)


</div>



<div align="center">

![封面](https://github.com/Tshiyao/beautify_every_beauty/blob/main/static/pic/封面.jpeg)

</div>

## 目录

- [项目简介](#项目简介)
  - [美每美：引领时尚前沿的智能穿搭妆容助手](#美每美引领时尚前沿的智能穿搭妆容助手)
  - [项目愿景：让每一份美丽更加美丽](#项目愿景让每一份美丽更加美丽)
- [项目架构](#项目架构)
- [更新说明](#更新说明)
- [使用指南](#使用指南)
  - [1. 数据准备](#1-数据准备)
  - [2. 模型微调](#2-模型微调)
  - [3. 模型部署](#3-模型部署)
  - [4. 模型地址](#4-模型地址)
- [演示视频](#演示视频)
- [特别鸣谢](#特别鸣谢)


# 项目简介 

## 美每美：引领时尚前沿的智能穿搭妆容助手

在时尚潮流瞬息万变的当下，你是否还在为每天的穿搭和妆容搭配而烦恼？美每美项目的诞生，正是为了解决这一难题，它以先进的技术架构和创新的功能设计，成为你专属的时尚智囊团。

美每美项目依托于强大的书生大模型 InternLM，整合了一系列前沿技术，致力于为用户提供精准、个性化且时尚前沿的穿搭妆容解决方案。


- 通过Lagent实现信息获取助手，实时从各类数据源中获取最新潮流信息、气候温度情况以及用户个人信息，以形成最新最潮的个性化数据。
  
  信息获取方面，通过 Lagent 作为智能触角，实时连接各类数据源，无论是时尚杂志、社交媒体上的最新潮流风向，还是当地实时的气候温度变化，甚至结合用户的个人风格偏好、身材特征等详细信息，迅速抓取并整合，为用户打造独一无二的个性化数据池，确保每一个推荐都贴合当下时尚趋势与个人实际情况。

- 通过MindU进行数据的清洗和预处理，将数据进行统一格式化，方便后续的模型训练以及检索。将数据存入各数据仓库中。将清洗后的高质量数据微调书生和灵笔大模型，赋予大模型图文能力和穿搭妆容的领域知识，以成为领域专家。
  
  数据处理环节，MindU 发挥关键作用，将杂乱无章的数据进行深度清洗和预处理，统一格式，使其成为井然有序、可供高效利用的高质量数据资源，并妥善存入专业的数据仓库，为后续精准服务筑牢根基。在此基础上，利用这些经过精心处理的数据对书生和灵笔大模型进行微调，注入丰富的图文理解能力以及专业的穿搭妆容领域知识，将通用大模型精雕细琢为穿搭妆容领域的专家，使其给出的建议极具专业性和权威性。

- 使用LMdeploy进行模型部署、Opencompass进行评测，持续优化。并且将用户的反馈收集，用于主观评测，推进后续模型升级。
  
  在模型部署阶段，采用 LMdeploy 技术，确保模型能够稳定、高效地运行，快速响应用户的各类需求，让时尚推荐触手可及。同时，借助 Opencompass 进行严格评测，不断优化模型性能，并且高度重视用户反馈，将用户的每一条评价和建议都作为主观评测的重要依据，推动模型持续升级迭代，以更加贴合用户心意。

- 通过Mindsearch进行数据检索，将用户需求转化为检索语句，通过检索语句找到最匹配的穿搭方案。使用Lagent构建助手，提供穿搭咨询，每日潮流推荐，穿搭妆容推荐，穿搭妆容评价。
  
  当用户有穿搭妆容需求时，Mindsearch 会将其转化为精准的检索语句，在海量数据中迅速定位最匹配的穿搭方案，无论是日常通勤、浪漫约会还是盛大晚宴，都能为用户找到最合适的造型。而由 Lagent 构建的智能助手，则全天候待命，提供专业的穿搭咨询，每日推送新鲜出炉的潮流趋势，根据不同场景给出详细的穿搭妆容推荐，还能对用户已有的穿搭妆容进行客观评价和优化建议。

不仅如此，美每美项目团队还在紧锣密鼓地研发一键换衣、虚拟衣柜等创新功能，让用户在虚拟世界中就能轻松尝试各种穿搭组合，提前预览不同风格的自己，尽情享受时尚探索的无限乐趣。未来，美每美将继续引领时尚科技潮流，成为你生活中不可或缺的时尚伴侣，让每一个人都能轻松展现独特的美，敬请期待美每美为你开启的时尚新征程！


## 项目愿景：让每一份美丽更加美丽

身处当下这个时尚潮流如同闪电般瞬息万变的快节奏时代，清晨站在衣柜前，面对琳琅满目的衣物却无从下手，不知怎样搭配才能既符合当日的场合氛围，又能展现独特的个人风格；或是坐在梳妆台前，面对一堆化妆品，纠结于哪种妆容最能凸显自己的气质，这些是不是你经常遭遇的困境？美每美项目恰如一位贴心的时尚挚友，在你迷茫困惑之时及时出现，精准且巧妙地化解这些难题。

它精心构建起一套极为先进的技术架构，犹如一座稳固而高效的时尚智慧堡垒。从信息的精准捕捉与智能整合，到数据的深度净化与专业预处理，再到模型的精细调校与优化部署，每一个环节都经过了反复打磨与严格测试，确保为你提供的时尚建议坚实可靠。同时，其创新的功能设计更是独具匠心，突破了传统时尚搭配的局限。无论是每日实时更新的潮流推荐，精准匹配不同场景的穿搭妆容方案，还是专业细致的穿搭咨询与评价服务，亦或是即将推出的令人期待的一键换衣、虚拟衣柜等前沿功能，无一不是从用户的实际需求出发，致力于为你打造一个全方位、个性化、沉浸式的时尚体验空间，让你在追逐时尚之美的道路上轻松自信、优雅前行，真正成为你专属的、触手可及的时尚智囊团，引领你步入一个崭新的时尚智慧生活新时代，开启属于自己的独特时尚篇章，轻松应对生活中的每一个时尚挑战，展现出独一无二的魅力与风采，在现实生活中时刻散发着自信与光芒，成为众人瞩目的时尚焦点。 

# 项目架构

![架构图](https://github.com/Tshiyao/beautify_every_beauty/blob/main/static/pic/架构图.png)

# 更新说明

- **敬请期待...**
- [ ] 虚拟衣柜

- [ ] 根据用户信息，进行穿搭妆容推荐

- [ ] 实时获取潮流推荐

- [ ] 微调图文模型，形成穿搭妆容评价能力

- [2024/12/14] 应用部署
  - [![Open in OpenXLab](https://cdn-static.openxlab.org.cn/app-center/openxlab_app.svg)](https://openxlab.org.cn/apps/detail/Liu_qihuang/BEAUTIFY_EVERY_BEAUTY)

  
- [2024/12/14] [BEAUTIFY_EVERY_BEAUTY_7b](https://modelscope.cn/models/Tshiyao/beb_7b)✨V0发布
  - 基于internlm2_5-7b-chat
  - [![Models](https://img.shields.io/badge/-gery?style=social&label=BEAUTIFY_EVERY_BEAUTY_7b✨V0)](https://modelscope.cn/models/Tshiyao/beb_7b)

- [2024/12/11] [BEAUTIFY_EVERY_BEAUTY](https://modelscope.cn/models/Tshiyao/beb)✨V0发布
  - 基于internlm2_5-20b-chat
  - [![Models](https://img.shields.io/badge/-gery?style=social&label=BEAUTIFY_EVERY_BEAUTY✨V0)](https://modelscope.cn/models/Tshiyao/beb)


# 使用指南
## 1. 数据准备
1. 数据获取

- 穿搭妆容知识

  爬取网上的文章、评论、图片，包括各种服装、美妆、服装配饰等。

- 时尚潮流数据

  每日实时从小红书、抖音、微博等平台，获取最新潮流。

- 用户偏好数据

  根据用户身材信息和偏好，构建用户实时画像

## 2. 模型微调

- 使用Xtuner，具体请参考[Xtuner](hhttps://github.com/InternLM/xtuner)。

## 3. 模型部署

- 直接使用
  
  目前已经部署在[OpenXLab](https://openxlab.org.cn/apps/detail/Liu_qihuang/BEAUTIFY_EVERY_BEAUTY)

  [![Open in OpenXLab](https://cdn-static.openxlab.org.cn/app-center/openxlab_app.svg)](https://openxlab.org.cn/apps/detail/Liu_qihuang/BEAUTIFY_EVERY_BEAUTY)

  欢迎大家试用，期待您的宝贵意见~

- 自己部署
  
  本地部署

  ```bash
  sh scripts/start_beb.sh
  streamlit run streamlit_demo.py
  ```

  使用api部署

  ```bash
  streamlit run tools/app.py
  ```

## 4. 模型地址

- 目前已经发布两款模型，欢迎使用。
  - [BEAUTIFY_EVERY_BEAUTY_7b](https://modelscope.cn/models/Tshiyao/beb_7b)✨V0

  - [BEAUTIFY_EVERY_BEAUTY](https://modelscope.cn/models/Tshiyao/beb)✨V0


# 演示视频




# 特别鸣谢

感谢书生实战营

感谢关注的每一位小伙伴，希望能一起让**美每美**更美
