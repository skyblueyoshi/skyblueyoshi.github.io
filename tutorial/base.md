# 《泰拉世界》模组开发教程——基础部分
本篇教程为《泰拉世界》模组开发的基础部分，通过本篇教程，您将可以制作出拥有基本功能的模组！

本教程对应的《泰拉世界》游戏版本：**黑曜石版1.1.0（电脑版/手机版跨平台版本）**

## 什么是模组？
TerraCraft的模组是一个允许玩家对游戏内容进行添加或者修改的功能或游戏内容拓展包，以追求给玩家提供更好的游戏体验。

TerraCraft开发理念是让玩家在无限大的地图中自由创作与游玩模组，实现游戏的高度自由性。TerraCraft本质是一个官方模组包，游戏未来的大部分游戏内容更新将会以模组的形式进行，同时我们将提供开源官方模组源码供模组制作者参考和学习。从这篇教程开始，我们将详细介绍模组的开发过程。

## 我的模组可以同时在PC和手机上玩吗？
当然可以！

TerraCraft内置了一个完整且简单的游戏引擎，用于提供游戏底层支持，对不同游戏平台（安卓、Windows）进行了封装，实现跨平台支持。因此，您可以直接编写相同的Mod代码，让您的模组在手机端和电脑端都可以正常运行。

## 开发模组需要什么技术？
开发环境（推荐）：Pycharm社区版

数据交换语言：Json

编程语言：Lua（版本为5.1）

您可以通过本教程逐步学习这些语言。对于大部分模组内容，您可以简单地通过编写Json进行开发。对于高级游戏内容，您可以通过Lua编写相关游戏逻辑。