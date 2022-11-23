# AccountUtils
账号通用类，封装了账号相关操作函数。
## 静态函数

### AccountUtils.Load

```
static boolean Load(string accountName, Account account)
```

从存档中加载一个账号。

 **返回值:** 是否成功加载账号。
* `accountName`: 账号名称。
* `account`: 如果成功加载账号，将把账号信息写入该参数。

### AccountUtils.Save

```
static void Save(Account account)
```

将一个账号保存到存档中。
* `account`: 账号。

### AccountUtils.Remove

```
static void Remove(string accountName)
```

将一个账号从存档中移除。
* `accountName`: 账号名称。

## 参考

* [Account](Account.md)
