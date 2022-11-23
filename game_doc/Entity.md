# Entity
描述一个基本实体类。
## 属性
| 成员 | 类型 | 描述 |
| :--- | :--- | :--- |
| x | double | 实体左上角x坐标。 |
| y | double | 实体左上角y坐标。 |
| centerX | double | **【只读】** 返回实体正中间x坐标。 |
| centerY | double | **【只读】** 返回实体正中间y坐标。 |
| centerXi | int | **【只读】** 返回实体正中间格子横坐标。 |
| centerYi | int | **【只读】** 返回实体正中间格子纵坐标。 |
| rightX | double | **【只读】** 返回实体最右侧x坐标。 |
| bottomY | double | **【只读】** 返回实体最底部y坐标。 |
| speedX | double | 实体横向速度。 |
| speedY | double | 实体纵向速度。 |
| gravity | double | 实体的重力加速度。 |
| width | int | **【只读】** 返回实体碰撞箱宽度。 |
| height | int | **【只读】** 返回实体碰撞箱高度。 |
| direction | boolean | 实体面朝右侧为true,面朝左侧为false。 |
| rotateAngle | double | 实体碰撞箱的旋转角度。 |
| speedAngle | double | **【只读】** 返回当前实体运动速度的向量夹角。 |
| randX | double | **【只读】** 返回实体在x轴投影上的随机坐标。 |
| randY | double | **【只读】** 返回实体在y轴投影上的随机坐标。 |
| shape | Shape | **【只读】** 返回实体碰撞箱形状。 |
| stand | boolean | **【只读】** 返回实体是否为站立状态。 |
| isCollisionTop | boolean | **【只读】** 返回实体是否顶部发生碰撞。 |
| isCollisionLeft | boolean | **【只读】** 返回实体是否左侧发生碰撞。 |
| isCollisionRight | boolean | **【只读】** 返回实体是否右侧发生碰撞。 |
| isCollisionStuck | boolean | **【只读】** 返回实体是否卡在方块内部。 |
| isNoCollision | boolean | **【只读】** 返回实体是否没有发生任何形式的碰撞。 |
| onSlope | boolean | **【只读】** 返回实体是否站在斜坡上。 |
| hitbox | Hitbox | **【只读】** 若实体为轴对齐矩形，返回轴对齐碰撞箱，否则返回旋转矩形碰撞箱。 |
| aabb | Hitbox | **【只读】** 实体旋转角度为0的轴对齐碰撞箱。 |
| minAABB | Hitbox | **【只读】** 完全包裹实体的最小轴对齐碰撞箱。 |
| allowCheckCollision | boolean | 决定是否执行与方块的碰撞检测。 |
| spriteDefaultWidth | int | **【只读】** 实体默认绘制宽度。 |
| spriteDefaultHeight | int | **【只读】** 实体默认绘制高度。 |
| spriteRect | Rectangle | 表示实体绘制时在目标贴图的剪裁区域。 |
| spriteEx | SpriteEx | 实体绘制时的精灵拓展信息。 |
| spriteOffsetX | int | @[ default `0.0` ] 实体绘制的横向偏移量。 |
| spriteOffsetY | int | @[ default `0.0` ] 实体绘制的纵向偏移量。 |
| color | Color | @[ default `COLOR_WHITE` ] 实体绘制时的颜色。 |
| frameTickTime | int | 实体绘制用的帧计时器，每帧自增1。 |
| frameIndex | int | **【只读】** 当前实体帧索引。 |
| frameStyles | int | **【只读】** 实体样式数。 |
| frames | int | **【只读】** 实体总帧数。 |
| frameSpeed | int | **【只读】** 实体帧切换周期。 |
| tickTime | int | **【只读】** 实体的实际生存的时间。 |
| randSeed | int | **【只读】** 实体的随机数种子。 |
## 成员函数

### Entity:SetCenterX

```
void SetCenterX(double newCenterX)
```

 将实体中心x坐标设为指定位置。

### Entity:SetCenterY

```
void SetCenterY(double newCenterY)
```

 将实体中心y坐标设为指定位置。

### Entity:GetAngleTo

```
double GetAngleTo(double desX, double desY)
```

 返回实体中心点到目标点的角度。
* `desX`: 目标点x坐标。
* `desY`: 目标点y坐标。

### Entity:GetAngleFrom

```
double GetAngleFrom(double srcX, double srcY)
```

 返回来源点到实体中心点的角度。
* `srcX`: 来源点x坐标。
* `srcY`: 来源点y坐标。

### Entity:GetDistance

```
double GetDistance(double otherX, any otherY)
```

 返回实体中心到指定点的距离。
* `otherX`: 目标点y坐标。

### Entity:Rotate

```
void Rotate(double angle)
```

 在原有角度基础上继续旋转指定角度。
* `angle`: 旋转的角度。

### Entity:RotateSpeed

```
void RotateSpeed(double angle)
```

 在原有速度角度基础上继续旋转指定速度角度。
* `angle`: 旋转的角度。

