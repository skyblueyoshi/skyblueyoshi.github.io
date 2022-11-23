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
void Valid()
```

判断当前堆叠物品数据是否有效。

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

克隆返回一个新的堆叠物品对象。

 **返回值:** 新的堆叠物品对象。
* `stackSize`: 新的堆栈数量。

### ItemStack:Clone

```
ItemStack Clone()
```

克隆返回一个新的堆叠物品对象。

 **返回值:** 新的堆叠物品对象。

### ItemStack:SetStackSize

```
void SetStackSize(any value)
```

设置堆栈数量。

### ItemStack:AddDurable

```
void AddDurable(any value)
```

增加耐久值。

### ItemStack:SetDurable

```
void SetDurable(any value)
```

直接设置耐久值。

### ItemStack:LoseDurable

```
boolean LoseDurable(any value)
```

减少耐久值。

 **返回值:** 减少后耐久是否为0。

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

判断当前堆叠物品是否拥有了指定附魔。
* `enchantmentId`: 附魔ID。

### ItemStack:HasEnchantment

```
boolean HasEnchantment()
```

判断当前堆叠物品是否拥有了指定附魔。

### ItemStack:GetEnchantmentByIndex

```
Enchantment GetEnchantmentByIndex(int index)
```

由附魔索引得到附魔对象。

 **返回值:** 附魔对象。
* `index`: 附魔索引。

### ItemStack:RemoveEnchantmentByIndex

```
void RemoveEnchantmentByIndex(int index)
```

由附魔索引删除附魔对象。
* `index`: 附魔索引。

### ItemStack:RemoveEnchantment

```
void RemoveEnchantment(int enchantmentID)
```

由附魔ID删除一个附魔对象。
* `enchantmentID`: 附魔ID。

### ItemStack:ClearEnchantments

```
void ClearEnchantments()
```

清空所有附魔。

### ItemStack:IsItemEqual

```
boolean IsItemEqual(ItemStack itemStack)
```

判断当前堆叠物品的物品数据是否与另一个堆叠物品的物品数据相同。
* `itemStack`: 另一个堆叠物品。

### ItemStack:IsItemStackEqual

```
boolean IsItemStackEqual(ItemStack itemStack, boolean ignoreStackSize)
```

判断当前堆叠物品是否与另一个堆叠物品相同。
* `itemStack`: 另一个堆叠物品。
* `ignoreStackSize`: 是否忽略堆叠物品数量判断。

### ItemStack:IsItemStackEqual

```
boolean IsItemStackEqual(ItemStack itemStack)
```

判断当前堆叠物品是否与另一个堆叠物品相同。
* `itemStack`: 另一个堆叠物品。

### ItemStack:GetMergeCount

```
int GetMergeCount(ItemStack itemStack)
```

返回当前堆叠物品与另一个堆叠物品可合并的数量。
* `itemStack`: 另一个堆叠物品。

### ItemStack:SplitStack

```
ItemStack SplitStack(int count)
```

拆分当前堆叠物品，返回新的拆出来的堆叠物品对象。

 **返回值:** 新的拆出来的堆叠物品对象。
* `count`: 拆出来的堆叠数量。

### ItemStack:GetItem

```
Item GetItem()
```

获得当前堆叠物品的物品数据。

### ItemStack:Render

```
void Render(Vector2 position, Color color, SpriteExData spriteExData)
```

绘制当前堆叠物品。

### ItemStack:RenderNum

```
void RenderNum(Vector2 position, Color color, SpriteExData spriteExData)
```

绘制当前堆叠物品的堆叠数量。

### ItemStack:RenderCustomNum

```
void RenderCustomNum(int num, Vector2 position, Color color, SpriteExData spriteExData)
```

自定义绘制当前堆叠物品的堆叠数量。

### ItemStack:RunOnHeldEvent

```
void RunOnHeldEvent(Player player)
```

执行堆叠物品挂接ModItem的`OnHeld`函数。
* `player`: 玩家

### ItemStack:RunOnHeldRenderEvent

```
void RunOnHeldRenderEvent(Player player)
```

执行堆叠物品挂接ModItem的`OnHeldRender`函数。
* `player`: 玩家

### ItemStack:RunOnHeldByNpcEvent

```
void RunOnHeldByNpcEvent(Npc npc)
```

执行堆叠物品挂接ModItem的`OnHeld`函数。

### ItemStack:CanUse

```
boolean CanUse(Player player)
```

返回当前堆叠物品是否能被玩家使用。
* `player`: 玩家

### ItemStack:RunOnUsedEvent

```
void RunOnUsedEvent(Player player)
```

执行堆叠物品挂接ModItem的`OnUsed`函数。
* `player`: 玩家

### ItemStack:RunOnUsedByNpcEvent

```
void RunOnUsedByNpcEvent(Npc npc)
```

执行堆叠物品挂接ModItem的`OnUsedByNpc`函数。

### ItemStack:RunOnDurableEmptyEvent

```
boolean RunOnDurableEmptyEvent(Player player)
```

执行堆叠物品挂接ModItem的`OnDurableEmpty`函数。
* `player`: 玩家

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

返回当前堆叠物品挂接的ModItem对象。

 **返回值:** 挂接的ModItem对象，如果无挂接，返回nil。

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

## 参考

* [Item](Item.md)
* [Enchantment](Enchantment.md)
* [Vector2](Vector2.md)
* [Color](Color.md)
* [SpriteExData](SpriteExData.md)
* [Player](Player.md)
* [Npc](Npc.md)
* [ModItem](ModItem.md)
