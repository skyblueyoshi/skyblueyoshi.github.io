# Vector4
描述一个4维向量。
## 父类
* [SerializableType](SerializableType.md)

## 属性
| 成员 | 类型 | 描述 |
| :--- | :--- | :--- |
| x | number |  |
| y | number |  |
| z | number |  |
| w | number |  |
| length | number | 向量长度。 |
| lengthSquared | number | 向量长度的平方。 |
| zero | Vector4 | 返回零向量。 |
| one | Vector4 | 返回全1向量。 |
| unitX | Vector4 | 返回X轴单位向量。 |
| unitY | Vector4 | 返回Y轴单位向量。 |
| unitZ | Vector4 | 返回Z轴单位向量。 |
| unitW | Vector4 | 返回W轴单位向量。 |
## 静态函数

### Vector4.new

```
static Vector4 new(number x, number y, number z, number w)
```



### Vector4.new

```
static Vector4 new()
```



### Vector4.new

```
static Vector4 new(Vector2 value, number z, number w)
```



### Vector4.new

```
static Vector4 new(Vector3 value, number w)
```



### Vector4.clone

```
static Vector4 clone(Vector4 value)
```



### Vector4.normalize

```
static Vector4 normalize(Vector4 value)
```

向量单位化。

### Vector4.max

```
static Vector4 max(Vector4 value1, Vector4 value2)
```

获取两个向量的最大值向量。

### Vector4.min

```
static Vector4 min(Vector4 value1, Vector4 value2)
```

获取两个向量的最小值向量。

### Vector4.floor

```
static Vector4 floor(Vector4 value)
```

将每个维度向下取整。

### Vector4.ceil

```
static Vector4 ceil(Vector4 value)
```

将每个维度向上取整。

### Vector4.clamp

```
static Vector4 clamp(Vector4 value, Vector4 min, Vector4 max)
```

限制向量到给定范围。

### Vector4.getDistance

```
static number getDistance(Vector4 value1, Vector4 value2)
```

获取向量之间的距离。

### Vector4.getDistanceSquared

```
static number getDistanceSquared(Vector4 value1, Vector4 value2)
```

获取向量之间的距离平方。

### Vector4.dot

```
static number dot(Vector4 value1, Vector4 value2)
```

将两个向量点乘，即每个维度乘积之和。

## 参考

* [SerializableType](SerializableType.md)
* [Vector2](Vector2.md)
* [Vector3](Vector3.md)
