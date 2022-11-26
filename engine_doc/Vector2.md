# Vector2
描述一个2维向量。
## 父类
* [SerializableType](SerializableType.md)

## 属性
| 成员 | 类型 | 描述 |
| :--- | :--- | :--- |
| x | number |  |
| y | number |  |
| length | number | 向量长度。 |
| lengthSquared | number | 向量长度的平方。 |
| angle | number | 向量到原点的角度。 |
| zero | Vector2 | 返回零向量。 |
| one | Vector2 | 返回全1向量。 |
| unitX | Vector2 | 返回X轴单位向量。 |
| unitY | Vector2 | 返回Y轴单位向量。 |
## 成员函数

### Vector2:getAngleTo

```
number getAngleTo(Vector2 other)
```

获取向量到另一个向量的角度。

### Vector2:getAngleFrom

```
number getAngleFrom(Vector2 other)
```

获取另一个向量到当前向量的角度。

## 静态函数

### Vector2.new

```
static Vector2 new(number x, number y)
```



### Vector2.new

```
static Vector2 new()
```



### Vector2.clone

```
static Vector2 clone(Vector2 value)
```



### Vector2.normalize

```
static Vector2 normalize(Vector2 value)
```

向量单位化。

### Vector2.max

```
static Vector2 max(Vector2 value1, Vector2 value2)
```

获取两个向量的最大值向量。

### Vector2.min

```
static Vector2 min(Vector2 value1, Vector2 value2)
```

获取两个向量的最小值向量。

### Vector2.floor

```
static Vector2 floor(Vector2 value)
```

将每个维度向下取整。

### Vector2.ceil

```
static Vector2 ceil(Vector2 value)
```

将每个维度向上取整。

### Vector2.clamp

```
static Vector2 clamp(Vector2 value, Vector2 min, Vector2 max)
```

限制向量到给定范围。

### Vector2.getDistance

```
static number getDistance(Vector2 value1, Vector2 value2)
```

获取向量之间的距离。

### Vector2.getDistanceSquared

```
static number getDistanceSquared(Vector2 value1, Vector2 value2)
```

获取向量之间的距离平方。

### Vector2.dot

```
static number dot(Vector2 value1, Vector2 value2)
```

将两个向量点乘，即每个维度乘积之和。

## 参考

* [SerializableType](SerializableType.md)
