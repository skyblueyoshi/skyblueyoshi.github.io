# Inventory
描述物品格子集合。
## 属性
| 成员 | 类型 | 描述 |
| :--- | :--- | :--- |
| slotCount | int | 物品格子的总数。 |
## 成员函数

### Inventory:Valid

```
boolean Valid()
```

判断当前物品格子集合对象是否有效。

### Inventory:SetSlotCount

```
void SetSlotCount(int count)
```

改变格子数量，若新增了格子，则格子将默认为空格子。
* `count`: 新的格子总数。

### Inventory:GetSlot

```
Slot GetSlot(int index)
```

由格子索引获取格子对象。

 **返回值:** 物品格子对象。
* `index`: 格子索引。

### Inventory:AddItemStack

```
ItemStack AddItemStack(ItemStack itemStack)
```

往当前集合加入一组堆叠物品。

 **返回值:** 当放入堆叠物品后导致集合满时，返回未能放入的堆叠物品。如果能完全放入，则返回无效ItemStack。
* `itemStack`: 堆叠物品。

### Inventory:SortAll

```
void SortAll()
```

为当前集合的所有物品格子进行排序。

### Inventory:Sort

```
void Sort(int index, int count)
```

为当前集合的指定格子范围进行排序。
* `index`: 格子范围起始索引。
* `count`: 待排序的格子总数。

### Inventory:QuickPushAllTo

```
void QuickPushAllTo(int start, int slotCount, Inventory inventoryTo, int inventoryToStart, int inventoryToSlotCount, boolean pushSameItemOnly)
```

将当前集合的指定格子范围内的物品快速转移到另一个物品格子集合的指定范围。
* `start`: 当前集合待转移的格子范围起始索引。
* `slotCount`: 当前集合待转移的格子总数。
* `inventoryTo`: 将要转移到的格子集合对象。
* `inventoryToStart`: 将要转移到的格子集合对象的格子范围起始索引。
* `inventoryToSlotCount`: 将要转移到的格子集合对象的格子总数。

### Inventory:QuickPushAllTo

```
void QuickPushAllTo(int start, int slotCount, Inventory inventoryTo, int inventoryToStart, int inventoryToSlotCount)
```

将当前集合的指定格子范围内的物品快速转移到另一个物品格子集合的指定范围。
* `start`: 当前集合待转移的格子范围起始索引。
* `slotCount`: 当前集合待转移的格子总数。
* `inventoryTo`: 将要转移到的格子集合对象。
* `inventoryToStart`: 将要转移到的格子集合对象的格子范围起始索引。
* `inventoryToSlotCount`: 将要转移到的格子集合对象的格子总数。

### Inventory:Serialization

```
table Serialization()
```

序列化得到lua表。

 **返回值:** lua表。

### Inventory:Deserialization

```
void Deserialization(table serializedTable)
```

由lua表反序列化得到当前物品格子集合对象。
* `serializedTable`: lua表。

## 静态函数

### Inventory.new

```
static Inventory new(int slotCount)
```

场景一个物品格子集合对象。

 **返回值:** 新的物品格子集合对象。
* `slotCount`: 物品格子的总数。

## 参考

* [Slot](Slot.md)
* [ItemStack](ItemStack.md)
