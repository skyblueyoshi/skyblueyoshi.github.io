# Slot
描述一个物品格子，物品格子可能为空格子，也可能包含一个ItemStack。
## 属性
| 成员 | 类型 | 描述 |
| :--- | :--- | :--- |
| hasStack | boolean | 当前格子是否包含物品堆栈。 |
| tag | int | 格子附加值。 |
## 成员函数

### Slot:Valid

```
boolean Valid()
```

判断格子是否有效。

### Slot:GetStack

```
ItemStack GetStack()
```



### Slot:PushStack

```
void PushStack(ItemStack stack)
```



### Slot:DecrStackSize

```
ItemStack DecrStackSize(int value)
```



### Slot:ClearStack

```
void ClearStack()
```



### Slot:SwapStack

```
void SwapStack(Slot slot)
```



### Slot:CanPush

```
boolean CanPush(ItemStack itemStack)
```



### Slot:CanPick

```
boolean CanPick(ItemStack itemStack)
```



### Slot:OnPush

```
void OnPush(ItemStack itemStack)
```



### Slot:OnPick

```
void OnPick(ItemStack ItemStack)
```



### Slot:AddCanPushListener

```
ListenerID AddCanPushListener(table|function listener)
```



### Slot:RemoveCanPushListener

```
void RemoveCanPushListener(ListenerID listenerID)
```



### Slot:AddCanPickListener

```
ListenerID AddCanPickListener(table|function listener)
```



### Slot:RemoveCanPickListener

```
void RemoveCanPickListener(ListenerID listenerID)
```



### Slot:AddOnPushListener

```
ListenerID AddOnPushListener(table|function listener)
```



### Slot:RemoveOnPushListener

```
void RemoveOnPushListener(ListenerID listenerID)
```



### Slot:AddOnPickListener

```
ListenerID AddOnPickListener(table|function listener)
```



### Slot:RemoveOnPickListener

```
void RemoveOnPickListener(ListenerID listenerID)
```



### Slot:SyncAll

```
void SyncAll()
```



## 参考

* [ItemStack](ItemStack.md)
* [ListenerID](ListenerID.md)
