# Color
描述一个颜色。
## 父类
* [SerializableType](SerializableType.md)

## 属性
| 成员 | 类型 | 描述 |
| :--- | :--- | :--- |
| red | number | 红色通道分量。取值为[0, 255]。 |
| green | number | 绿色通道分量。取值为[0, 255]。 |
| blue | number | 蓝色通道分量。取值为[0, 255]。 |
| alpha | number | 透明度通道分量。取值为[0, 255]。 |
| Red | Color | 返回红色对象。 |
| Black | Color | 返回黑色对象。 |
| Gray | Color | 返回灰色对象。 |
| Green | Color | 返回绿色对象。 |
| Blue | Color | 返回蓝色对象。 |
| LightBlue | Color | 返回淡蓝色对象。 |
| Yellow | Color | 返回黄色对象。 |
| FrenchGray | Color | 返回淡灰色对象。 |
| White | Color | 返回白色对象。 |
## 静态函数

### Color.new

```
static Color new(number red, number green, number blue, number alpha)
```

创建一个颜色对象。

 **返回值:** 新的颜色对象。
* `red`: 红色通道分量。取值为[0, 255]。
* `green`: 绿色通道分量。取值为[0, 255]。
* `blue`: 蓝色通道分量。取值为[0, 255]。
* `alpha`: 透明度通道分量。取值为[0, 255]。

### Color.new

```
static Color new()
```

创建一个颜色对象。

 **返回值:** 新的颜色对象。

### Color.new

```
static Color new(number red, number green, number blue)
```

创建一个颜色对象。

 **返回值:** 新的颜色对象。
* `red`: 红色通道分量。取值为[0, 255]。
* `green`: 绿色通道分量。取值为[0, 255]。
* `blue`: 蓝色通道分量。取值为[0, 255]。

### Color.clone

```
static Color clone(Color value)
```



## 参考

* [SerializableType](SerializableType.md)
