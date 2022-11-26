# Vector3
描述一个3维向量。
## 父类
* [SerializableType](SerializableType.md)

## 属性
| 成员 | 类型 | 描述 |
| :--- | :--- | :--- |
| x | number |  |
| y | number |  |
| z | number |  |
| length | number | 向量长度。 |
| lengthSquared | number | 向量长度的平方。 |
| zero | Vector3 | 返回零向量。 |
| one | Vector3 | 返回全1向量。 |
| unitX | Vector3 | 返回X轴单位向量。 |
| unitY | Vector3 | 返回Y轴单位向量。 |
| unitZ | Vector3 | 返回Z轴单位向量。 |
| up | Vector3 |  |
| down | Vector3 |  |
| left | Vector3 |  |
| right | Vector3 |  |
| forward | Vector3 |  |
| back | Vector3 |  |
## 静态函数

### Vector3.new

```
static Vector3 new(number x, number y, number z)
```



### Vector3.new

```
static Vector3 new()
```



### Vector3.new

```
static Vector3 new(Vector2 value, number z)
```



### Vector3.clone

```
static Vector3 clone(Vector3 value)
```



### Vector3.normalize

```
static Vector3 normalize(Vector3 value)
```

向量单位化。

### Vector3.max

```
static Vector3 max(Vector3 value1, Vector3 value2)
```

获取两个向量的最大值向量。

### Vector3.min

```
static Vector3 min(Vector3 value1, Vector3 value2)
```

获取两个向量的最小值向量。

### Vector3.floor

```
static Vector3 floor(Vector3 value)
```

将每个维度向下取整。

### Vector3.ceil

```
static Vector3 ceil(Vector3 value)
```

将每个维度向上取整。

### Vector3.clamp

```
static Vector3 clamp(Vector3 value, Vector3 min, Vector3 max)
```

限制向量到给定范围。

### Vector3.getDistance

```
static number getDistance(Vector3 value1, Vector3 value2)
```



### Vector3.getDistanceSquared

```
static number getDistanceSquared(Vector3 value1, Vector3 value2)
```

获取向量之间的距离。

### Vector3.dot

```
static number dot(Vector3 value1, Vector3 value2)
```

将两个向量点乘，即每个维度乘积之和。

### Vector3.cross

```
static Vector3 cross(Vector3 value1, Vector3 value2)
```

返回两个向量的叉积。

## 参考

* [SerializableType](SerializableType.md)
* [Vector2](Vector2.md)
