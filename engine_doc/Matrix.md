# Matrix
描述一个4x4矩阵。
## 属性
| 成员 | 类型 | 描述 |
| :--- | :--- | :--- |
| m11 | number |  |
| m12 | number |  |
| m13 | number |  |
| m14 | number |  |
| m21 | number |  |
| m22 | number |  |
| m23 | number |  |
| m24 | number |  |
| m31 | number |  |
| m32 | number |  |
| m33 | number |  |
| m34 | number |  |
| m41 | number |  |
| m42 | number |  |
| m43 | number |  |
| m44 | number |  |
| up | Vector3 | 上向量{M21, M22, M23}。 |
| down | Vector3 | 下向量{-M21, -M22, -M23}。 |
| left | Vector3 | 左向量{-M11, -M12, -M13}。 |
| right | Vector3 | 右向量{M11, M12, M13}。 |
| forward | Vector3 | 前向量{-M31, -M32, -M33}。 |
| backward | Vector3 | 前向量{-M31, -M32, -M33}。 |
| translation | Vector3 | 存储坐标{M41, M42, M43}。 |
| identity | Matrix | 返回单位矩阵。 |
## 成员函数

### Matrix:transpose

```
Matrix transpose()
```

转置矩阵，即行列交换。

### Matrix:lerp

```
Matrix lerp(Matrix matrix, number amount)
```

返回包含指定矩阵中值的线性插值矩阵。
* `matrix`: 原始矩阵。
* `amount`: 插值。

### Matrix:invert

```
Matrix invert()
```

矩阵逆变换。

### Matrix:determinant

```
number determinant()
```

求矩阵行列式。

### Matrix:transformVector2

```
Vector2 transformVector2(Vector2 position)
```



### Matrix:transformVector3

```
Vector3 transformVector3(Vector3 position)
```



### Matrix:transformVector4

```
Vector4 transformVector4(Vector4 vector4)
```



### Matrix:transformVector4

```
Vector4 transformVector4(Vector3 vector3)
```



### Matrix:transformVector4

```
Vector4 transformVector4(Vector2 vector2)
```



## 静态函数

### Matrix.new

```
static Matrix new(number m11, number m12, number m13, number m14, number m21, number m22, number m23, number m24, number m31, number m32, number m33, number m34, number m41, number m42, number m43, number m44)
```



### Matrix.new

```
static Matrix new()
```



### Matrix.new

```
static Matrix new(Vector4 row1, Vector4 row2, Vector4 row3, Vector4 row4)
```



### Matrix.clone

```
static Matrix clone(Matrix value)
```



### Matrix.createLookAt

```
static Matrix createLookAt(Vector3 cameraPosition, Vector3 cameraTarget, Vector3 cameraUpVector)
```

构造一个View矩阵。
* `cameraPosition`: 摄像机坐标。
* `cameraTarget`: 摄像机目标向量。
* `cameraUpVector`: 摄像机上边缘方向。

### Matrix.createPerspectiveFOV

```
static Matrix createPerspectiveFOV(number fieldOfView, number aspectRatio, number nearPlaneDistance, number farPlaneDistance)
```

构造一个透视投影矩阵。
* `fieldOfView`: y轴方向上的视场角度（弧度制）。
* `aspectRatio`: 视景体的宽度与高度之比。
* `nearPlaneDistance`: 沿z轴方向的两截面之间距离的近处。
* `farPlaneDistance`: 沿z轴方向的两截面之间距离的远处。

### Matrix.createOrthographicRH

```
static Matrix createOrthographicRH(number width, number height, number zNearPlane, number zFarPlane)
```

构造一个正视投影矩阵。
* `width`: 视图宽度。
* `height`: 视图高度。
* `zNearPlane`: 近平面深度。
* `zFarPlane`: 远平面深度

### Matrix.createOrthographicRH

```
static Matrix createOrthographicRH(number left, number right, number bottom, number top, number zNearPlane, number zFarPlane)
```

构造一个正视投影矩阵。
* `left`: 投影区域最小x坐标。
* `right`: 投影区域最大x坐标。
* `bottom`: 投影区域最大y坐标。
* `top`: 投影区域最小y坐标。
* `zNearPlane`: 近平面深度。
* `zFarPlane`: 远平面深度。

### Matrix.createOrthographicLH

```
static Matrix createOrthographicLH(number width, number height, number zNearPlane, number zFarPlane)
```

构造一个正视投影矩阵。
* `width`: 视图宽度。
* `height`: 视图高度。
* `zNearPlane`: 近平面深度。
* `zFarPlane`: 远平面深度。

### Matrix.createOrthographicLH

```
static Matrix createOrthographicLH(number left, number right, number bottom, number top, number zNearPlane, number zFarPlane)
```

构造一个正视投影矩阵。
* `left`: 投影区域最小x坐标。
* `right`: 投影区域最大x坐标。
* `bottom`: 投影区域最大y坐标。
* `top`: 投影区域最小y坐标。
* `zNearPlane`: 近平面深度。
* `zFarPlane`: 远平面深度。

### Matrix.createRotationX

```
static Matrix createRotationX(number radians)
```

构造一个绕X轴旋转的矩阵。
* `radians`: 旋转弧度。

### Matrix.createRotationY

```
static Matrix createRotationY(number radians)
```

构造一个绕Y轴旋转的矩阵。
* `radians`: 旋转弧度。

### Matrix.createRotationZ

```
static Matrix createRotationZ(number radians)
```

构造一个绕Z轴旋转的矩阵。
* `radians`: 旋转弧度。

### Matrix.createScale

```
static Matrix createScale(number scale)
```

构造一个放缩矩阵。
* `scale`: XYZ轴的放缩大小。

### Matrix.createScale

```
static Matrix createScale(number scaleX, number scaleY, number scaleZ)
```

构造一个放缩矩阵。
* `scaleX`: X轴的放缩大小。
* `scaleY`: Y轴的放缩大小。
* `scaleZ`: Z轴的放缩大小。

### Matrix.createScale

```
static Matrix createScale(Vector3 scales)
```

构造一个放缩矩阵。
* `scales`: XYZ轴的放缩向量。

## 参考

* [Vector3](Vector3.md)
* [Vector4](Vector4.md)
* [Vector2](Vector2.md)
