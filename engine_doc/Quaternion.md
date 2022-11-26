# Quaternion
描述一个四元数。
## 父类
* [Vector4](Vector4.md)

## 属性
| 成员 | 类型 | 描述 |
| :--- | :--- | :--- |
| identity | Quaternion | 返回归一化四元数。 |
| eulerAngles | Vector3 | 返回或设置欧拉旋转轴。 |
| matrix | Matrix | 返回或设置其矩阵形式。 |
## 成员函数

### Quaternion:toAngleAxis

```
number,Vector3 toAngleAxis()
```

获得旋转轴和旋转角度。

## 静态函数

### Quaternion.angle

```
static number angle(Quaternion lhs, Quaternion rhs)
```

返回两个四元数之间的角度。

### Quaternion.euler

```
static Quaternion euler(number yaw, number pitch, number roll)
```

由欧拉角创建一个四元数。

### Quaternion.euler

```
static Quaternion euler(Vector3 eulerAngles)
```

由欧拉角创建一个四元数。

### Quaternion.angleAxis

```
static Quaternion angleAxis(number angle, Vector3 axis)
```

创建一个绕着指定轴旋转指定角度的旋转四元数。

### Quaternion.slerp

```
static Quaternion slerp(Quaternion a, Quaternion b, number t)
```

在四元数a和b之间进行球形插值。
* `t`: 插值因子[0, 1]。

### Quaternion.lerp

```
static Quaternion lerp(Quaternion a, Quaternion b, number t)
```

在四元数a和b之间进行插值。
* `t`: 插值因子[0, 1]。

### Quaternion.rotationFromTo

```
static Quaternion rotationFromTo(Vector3 fromDirection, Vector3 toDirection)
```

创建一个从角度fromDirection到角度toDirection的旋转四元数。

## 参考

* [Vector4](Vector4.md)
* [Vector3](Vector3.md)
* [Matrix](Matrix.md)
* [number,Vector3](number,Vector3.md)
