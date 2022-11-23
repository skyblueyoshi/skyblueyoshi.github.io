# BiomeUtils
生物群系通用类。
## 静态函数

### BiomeUtils.GetBiomeIDByType

```
static int GetBiomeIDByType(int biomeTypeID, int index)
```

由指定生物群系类型和在该生物群系类型的索引，返回生物群系数据。

 **返回值:** 生物群系数据。
* `biomeTypeID`: 生物群系类型。
* `index`: 在该生物群系类型的索引。

### BiomeUtils.GetBiomeCountByType

```
static int GetBiomeCountByType(int biomeTypeID)
```

返回指定生物群系类型的生物群系数量。

 **返回值:** 指定生物群系类型的生物群系数量。
* `biomeTypeID`: 生物群系类型。

### BiomeUtils.GetData

```
static BiomeData GetData(int biomeID)
```

由生物群系ID，返回生物群系数据。

 **返回值:** 生物群系数据。
* `biomeID`: 生物群系ID。

## 参考

* [BiomeData](BiomeData.md)
