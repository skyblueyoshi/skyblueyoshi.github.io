# Sprite
精灵渲染类。
## 静态函数

### Sprite.beginBatch

```
static void beginBatch()
```

开始一批精灵渲染。

### Sprite.endBatch

```
static void endBatch()
```

结束一批精灵渲染。

### Sprite.flush

```
static void flush()
```

将当前缓存的所有精灵，立即绘制到帧缓存上。

### Sprite.draw

```
static void draw(TextureLocation textureLocation, Vector2 pos, Rect sourceRect, Color color, SpriteExData exData, number depth)
```

绘制一个精灵。
* `textureLocation`: 待绘制的纹理。
* `pos`: 绘制在帧缓存上的坐标。
* `sourceRect`: 绘制纹理的剪裁区域。
* `color`: 绘制精灵的颜色。
* `exData`: 精灵绘制拓展信息。
* `depth`: 绘制到帧缓存上的深度。

### Sprite.draw

```
static void draw(TextureLocation textureLocation, Vector2 pos, Rect sourceOffset, Color color)
```

绘制一个精灵。
* `textureLocation`: 待绘制的纹理。
* `pos`: 绘制在帧缓存上的坐标。
* `color`: 绘制精灵的颜色。

### Sprite.draw

```
static void draw(TextureLocation textureLocation, Vector2 pos, Rect sourceOffset, Color color, number depth)
```

绘制一个精灵。
* `textureLocation`: 待绘制的纹理。
* `pos`: 绘制在帧缓存上的坐标。
* `color`: 绘制精灵的颜色。
* `depth`: 绘制到帧缓存上的深度。

## 参考

* [TextureLocation](TextureLocation.md)
* [Vector2](Vector2.md)
* [Rect](Rect.md)
* [Color](Color.md)
* [SpriteExData](SpriteExData.md)
