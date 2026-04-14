# dianshudata

典枢平台（[www.dianshudata.com](https://www.dianshudata.com)）热门数据爬虫项目。

## 项目简介
本项目用于自动获取典枢平台的数据市场热门数据，通过爬取特定的热门数据页面（如 `rid48` 分类），自动解析并输出所有热门数据的名称及其对应的详情页链接，支持将结果导出为 JSON 文件供后续分析或使用。

## 快速开始
1. 克隆仓库:
   ```bash
   git clone https://github.com/longinus41/dianshudata.git
   ```
2. 安装依赖:
   ```bash
   pip install -r requirements.txt
   ```
3. 运行项目:
   ```bash
   python scraper.py
   ```
   运行后，控制台会输出热门数据的名称与详情页链接，并自动在当前目录生成 `popular_data.json` 文件。

## 目录结构
- `scraper.py`: 核心爬虫脚本，负责请求网页并解析数据。
- `requirements.txt`: Python 依赖包列表。
- `popular_data.json`: 爬取后自动生成的示例结果文件。

## 贡献指南
欢迎提交 Pull Request 或报告 Issue。

## 许可证
[MIT](LICENSE)
