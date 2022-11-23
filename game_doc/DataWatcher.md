# DataWatcher
数据同步类，内部封装了网络同步逻辑。
## 成员函数

### DataWatcher:AddBool

```
int AddBool(boolean value, boolean canRemote)
```



### DataWatcher:AddBool

```
int AddBool(boolean value)
```



### DataWatcher:UpdateBool

```
void UpdateBool(int channel, boolean value)
```

由指定通道，向

### DataWatcher:GetBool

```
boolean GetBool(int channel)
```

由指定通道，从远端获取数据。

 **返回值:** 布尔型数据。
* `channel`: 通道。

### DataWatcher:AddByte

```
int AddByte(int value, boolean canRemote)
```



### DataWatcher:AddByte

```
int AddByte(int value)
```



### DataWatcher:UpdateByte

```
void UpdateByte(int channel, int value)
```



### DataWatcher:GetByte

```
int GetByte(int channel)
```



### DataWatcher:AddShort

```
int AddShort(int value, boolean canRemote)
```



### DataWatcher:AddShort

```
int AddShort(int value)
```



### DataWatcher:UpdateShort

```
void UpdateShort(int channel, int value)
```



### DataWatcher:GetShort

```
int GetShort(int channel)
```



### DataWatcher:AddInteger

```
int AddInteger(int value, boolean canRemote)
```



### DataWatcher:AddInteger

```
int AddInteger(int value)
```



### DataWatcher:UpdateInteger

```
void UpdateInteger(int channel, int value)
```



### DataWatcher:GetInteger

```
int GetInteger(int channel)
```



### DataWatcher:AddDouble

```
int AddDouble(double value, boolean canRemote)
```



### DataWatcher:AddDouble

```
int AddDouble(double value)
```



### DataWatcher:UpdateDouble

```
void UpdateDouble(int channel, double value)
```



### DataWatcher:GetDouble

```
double GetDouble(int channel)
```



### DataWatcher:AddString

```
int AddString(string value, boolean canRemote)
```



### DataWatcher:AddString

```
int AddString(string value)
```



### DataWatcher:UpdateString

```
void UpdateString(int channel, string value)
```



### DataWatcher:GetString

```
string GetString(int channel)
```



### DataWatcher:AddInventory

```
int AddInventory(Inventory value)
```



### DataWatcher:UpdateInventory

```
void UpdateInventory(int channel, Inventory value)
```



### DataWatcher:GetInventory

```
Inventory GetInventory(int channel)
```



## 参考

* [Inventory](Inventory.md)
