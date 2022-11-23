# BlockData
描述一个方块数据。
## 属性
| 成员 | 类型 | 描述 |
| :--- | :--- | :--- |
| textureLocation | TextureLocation | 方块渲染在地图中的纹理。 |
| group | int | 方块组，决定渲染在地图中纹理衔接方式。 |
| subGroup | int | 方块子组。 |
| stepSoundId | int | 踩在方块上发出的音效ID。 |
| stepSoundGroupId | int | 踩在方块上发出的音效组ID。 |
| functionSoundId | int |  |
| functionSoundGroupId | int |  |
| functionSoundId2 | int |  |
| functionSoundGroupId2 | int |  |
| functionSoundId3 | int |  |
| functionSoundGroupId3 | int |  |
| functionSoundId4 | int |  |
| functionSoundGroupId4 | int |  |
| isRipen | boolean | 是否允许催熟。 |
| isDoorOpened | boolean | 是否为开启了的门。 |
| isDoorClosed | boolean | 是否为关闭了的门。 |
## 成员函数

### BlockData:CanSeed

```
boolean CanSeed(int itemID)
```

判断指定物品，能否种植在当前方块上。

 **返回值:** 物品能否种植在方块上。
* `itemID`: 物品ID。

### BlockData:HasAnimation

```
boolean HasAnimation()
```

当前方块是否拥有动画效果。

 **返回值:** 是否拥有动画效果。

