# ItemStack
描述一组堆叠物品。
## 属性
| 成员 | 类型 | 描述 |
| :--- | :--- | :--- |
| stackSize | int | **【只读】** 当前堆叠数量。 |
| durable | double | 当前物品耐久。 |
| enchantmentCount | int | 当前堆叠物品挂接的附魔数量。 |
## 成员函数

### ItemStack:Valid

```
boolean Valid()
```

判断当前堆叠物品数据是否有效。

 **返回值:** 数据是否有效。

### ItemStack:AddEnchantment

```
boolean AddEnchantment(int enchantmentId, int enchantmentLevel)
```

为当前堆叠物品新增一项附魔。

 **返回值:** 新增附魔是否有变化，当且仅当之前已经存在附魔且新增附魔等级小于之前等级则无变化。
* `enchantmentId`: 附魔ID。
* `enchantmentLevel`: 附魔等级。

### ItemStack:Clone

```
ItemStack Clone(int stackSize)
```



### ItemStack:Clone

```
ItemStack Clone()
```



### ItemStack:SetStackSize

```
void SetStackSize(int value)
```

设置堆栈数量。
* `value`: 新的堆栈数量。

### ItemStack:AddDurable

```
void AddDurable(double value)
```

增加耐久值。
* `value`: 新增的耐久值。

### ItemStack:SetDurable

```
void SetDurable(double value)
```

直接设置耐久值。
* `value`: 耐久值。

### ItemStack:LoseDurable

```
boolean LoseDurable(double value)
```

减少耐久值。

 **返回值:** 减少后耐久是否为0。
* `value`: 减少的耐久值。

### ItemStack:GetEnchantmentLevel

```
int GetEnchantmentLevel(int enchantmentId)
```

获取当前堆栈物品指定附魔的等级。

 **返回值:** 附魔等级。
* `enchantmentId`: 附魔ID。

### ItemStack:HasEnchantment

```
boolean HasEnchantment(int enchantmentId)
```



### ItemStack:HasEnchantment

```
boolean HasEnchantment()
```



### ItemStack:GetEnchantmentByIndex

```
Enchantment GetEnchantmentByIndex(int index)
```



### ItemStack:RemoveEnchantmentByIndex

```
void RemoveEnchantmentByIndex(int index)
```



### ItemStack:RemoveEnchantment

```
void RemoveEnchantment(int enchantmentID)
```



### ItemStack:ClearEnchantments

```
void ClearEnchantments()
```



### ItemStack:IsItemEqual

```
boolean IsItemEqual(ItemStack itemStack)
```



### ItemStack:IsItemStackEqual

```
boolean IsItemStackEqual(ItemStack itemStack, boolean ignoreStackSize)
```



### ItemStack:IsItemStackEqual

```
boolean IsItemStackEqual(ItemStack itemStack)
```



### ItemStack:GetMergeCount

```
int GetMergeCount(ItemStack itemStack)
```



### ItemStack:SplitStack

```
ItemStack SplitStack(int count)
```



### ItemStack:GetItem

```
Item GetItem()
```



### ItemStack:Render

```
void Render(Vector2 position, Color color, SpriteExData spriteExData)
```



### ItemStack:RenderNum

```
void RenderNum(Vector2 position, Color color, SpriteExData spriteExData)
```



### ItemStack:RenderCustomNum

```
void RenderCustomNum(int num, Vector2 position, Color color, SpriteExData spriteExData)
```



### ItemStack:RunOnHeldEvent

```
void RunOnHeldEvent(Player player)
```

RunHeldEvent

### ItemStack:RunOnHeldRenderEvent

```
void RunOnHeldRenderEvent(Player player)
```



### ItemStack:RunOnHeldByNpcEvent

```
void RunOnHeldByNpcEvent(Npc npc)
```



### ItemStack:CanUse

```
boolean CanUse(Player player)
```

RunCanUse

### ItemStack:RunOnUsedEvent

```
void RunOnUsedEvent(Player player)
```

RunUseEvent

### ItemStack:RunOnUsedByNpcEvent

```
void RunOnUsedByNpcEvent(Npc npc)
```



### ItemStack:RunOnDurableEmptyEvent

```
boolean RunOnDurableEmptyEvent(Player player)
```



### ItemStack:Serialization

```
table Serialization()
```

序列化得到lua表。

 **返回值:** lua表。

### ItemStack:GetModItem

```
ModItem GetModItem()
```



## 静态函数

### ItemStack.new

```
static ItemStack new(Item item, int stackSize)
```

创建一个堆叠物品对象。



 **返回值:** 新的堆叠物品对象。
* `item`: 物品。
* `stackSize`: 堆叠数量。

#### 范例:
```lua
--创建堆叠234个由钻石的堆叠物品对象。
local itemStackDiamond = ItemStack.new(ItemRegistry.GetItemByID("diamond"), 234)
--创建一个铁剑堆叠物品对象。
local itemStackSword = ItemStack.new(ItemRegistry.GetItemByID("iron_sword"))
```

### ItemStack.new

```
static ItemStack new(Item item)
```

创建一个堆叠物品对象。



 **返回值:** 新的堆叠物品对象。
* `item`: 物品。

#### 范例:
```lua
--创建堆叠234个由钻石的堆叠物品对象。
local itemStackDiamond = ItemStack.new(ItemRegistry.GetItemByID("diamond"), 234)
--创建一个铁剑堆叠物品对象。
local itemStackSword = ItemStack.new(ItemRegistry.GetItemByID("iron_sword"))
```

### ItemStack.Deserialization

```
static ItemStack Deserialization(table serializedTable)
```

由lua表反序列化创建一个堆叠物品对象。

 **返回值:** 新的堆叠物品对象。
* `serializedTable`: lua表。

