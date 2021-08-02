# Cyberspace Map API

![](https://img.shields.io/github/pipenv/locked/python-version/Xc1Ym/cyberspace_map_API)
![](https://img.shields.io/github/license/Xc1Ym/cyberspace_map_API)
![](https://img.shields.io/github/stars/xc1ym/cyberspace_map_API)

[English](./README.md)/[中文](./README_CN.md)


## 开发进度
1. fofaAPI已完成
2. zoomeyeAPI未完成
3. shodanAPI未完成
4. 正则匹配未完成
5. 360 quakeAPI已完成

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

~~注🔴该代码来源于<https://github.com/Xc1Ym/FofaAPI>，正在修改以适配当前代码~~

**已完成适配**

### 用法

1. 基础用法`python fofa_api.py -search IP\domain`
2. 帮助`python fofa_api.py -h`
3. 可以使用`--size`和`--page`设置需要查询的数量和页数
4. `--rule`可以查询Fofa支持的所有高级搜索功能

### 截图

暂无



## Shodan
开发中

## zoomeye
开发中

## 360 quake
开发完成

## 开发者
[Xc1YM](https://github.com/Xc1Ym)
