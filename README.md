# Wukongbaobao

Wukongbaobao 是一个帮助家长灵活生成幼儿考试题的程序。工具使用 Python 编写。
* https://github.com/qiqilelebaobao/wukong

Wukongbaobao is a program that helps parents flexibly generate test questions for their children. The tool is written in Python.
* https://github.com/qiqilelebaobao/wukong


主要功能包括：
* 通过算法按需生成数学试题
* 支持生成txt文件、docx文件格式

Main functions include:
* Generate math test questions on demand through algorithms
* Supports generation of txt and docx file formats

## 适用场景 Applicable Scenarios

* 场景一：家庭教育场景
* 场景二：程序学习场景

* Scenario 1: Family education scenario
* Scenario 2: Program learning scenario

## 安装指南 Installation Guide

需要 Python3 环境
Python3 is required

```shell
$ pip3 install --upgrade python-docx
$ pip3 install wukongbaobao
```

## 使用说明 Instructions

```shell
$ python3 -m wukongbaobao [-h] [--level {1,2,3,4}] [--basic_cnt BASIC_CNT] [--open_cnt OPEN_CNT] [--algorithm {+,-}]
```
默认在ouput文件夹生成word文件，可以打印测验。  

level 1 对应 [0, 10] 区间的算法  
level 2 对应 [11, 30] 区间的算法  
level 3 对应 [31, 60] 区间的算法  
level 4 对应 [61, 100] 区间的算法  
