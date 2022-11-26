# ObbDouble
描述一个旋转矩形对象。
## 父类
* [SerializableType](SerializableType.md)

## 属性
| 成员 | 类型 | 描述 |
| :--- | :--- | :--- |
| centerX | number | 矩形中心点横坐标。 |
| centerY | number | 矩形中心点纵坐标。 |
| width | number | 矩形宽度。 |
| height | number | 矩形高度。 |
| angle | number | 矩形旋转角度。 |
## 成员函数

### ObbDouble:isOverlapping

```
boolean isOverlapping(ObbDouble otherObb)
```

判断当前旋转矩形是否与另一个旋转矩形重叠。

### ObbDouble:isPointIn

```
boolean isPointIn(Vector2 vector2)
```

判断指定点是否在当前旋转矩形区域内。

### ObbDouble:convertFromSourceRectSpace

```
number,number convertFromSourceRectSpace(number xInSource, number yInSource)
```

获取矩形空间内的点在矩形空间外的实际坐标。
* `xInSource`: 矩形空间内的点X。
* `yInSource`: 矩形空间内的点Y。

## 静态函数

### ObbDouble.new

```
static ObbDouble new(number centerX, number centerY, number width, number height, number angle)
```

创建一个旋转矩形对象。

 **返回值:** 新的旋转矩形对象。
* `centerX`: 矩形中心点横坐标。
* `centerY`: 矩形中心点纵坐标。
* `width`: 矩形宽度。
* `height`: 矩形高度。
* `angle`: 矩形旋转角度。

## 参考

* [SerializableType](SerializableType.md)
* [Vector2](Vector2.md)
* [number,number](number,number.md)
