# TextureLocation
描述一个纹理索引。
## 属性
| 成员 | 类型 | 描述 |
| :--- | :--- | :--- |
| isSingleTexture | boolean | 当前纹理索引是否不是来自合图。 |
| isAtlasArea | boolean | 当前纹理索引是否来自合图。 |
| spriteZoomInTimes | number | 当纹理索引用于精灵渲染时，表示渲染时纹理放大倍数。 |
| valid | boolean | 纹理是否有效。 |
## 静态函数

### TextureLocation.new

```
static TextureLocation new(number format, number id)
```

创建一个纹理索引对象。

 **返回值:** 新的纹理索引对象。

### TextureLocation.clone

```
static TextureLocation clone(TextureLocation value)
```

克隆一个纹理索引对象。

 **返回值:** 新的纹理索引对象。
* `value`: 原始纹理索引对象。

