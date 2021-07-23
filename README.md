# Cyberspace Map API

![](https://img.shields.io/github/pipenv/locked/python-version/Xc1Ym/cyberspace_map_API)
![](https://img.shields.io/github/license/Xc1Ym/cyberspace_map_API)


## 开发进度
1. zoomeyeAPI未完成
2. shodanAPI未完成
3. 正则匹配未完成
4. 360 quakeAPI未完成

### 目前遇到的困难
1. 输入无法对接各API

### 解决方法
1. 使用正则解决IP、Domain、CMS等适配各API


使用Fofa、shodan、zoomeye、360quake三个网络空间测绘的API进行红队信息收集

**所有API都为官方API，需要使用API KEY**

## 配置

1. 打开`config.json`配置相应的API KEY
2. 使用`pip install -r requirements.txt`安装依赖包

## Fofa

**该工具使用Fofa官方API查询，需要普通会员或高级会员**

**注🔴该代码来源于<https://github.com/Xc1Ym/FofaAPI>，正在修改以适配当前代码**

### 用法

1. 基础用法`python fofa_api.py -search IP\domain`
2. 帮助`python fofa_api.py -h`
3. 可以使用`--size`和`--page`设置需要查询的数量和页数
4. `--rule`可以查询Fofa支持的所有高级搜索功能

### 截图

![](./image/search.png)

![](./image/rule.png)

## Shodan
开发中

## zoomeye
开发中

## 360 quake
开发中

## 开发者
[Xc1YM](https://github.com/Xc1Ym)