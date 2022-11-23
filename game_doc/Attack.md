# Attack
表示一个攻击属性。
## 属性
| 成员 | 类型 | 描述 |
| :--- | :--- | :--- |
| attack | int | 伤害值。 |
| knockBack | int | 击退值。 |
| crit | int | 攻击的百分暴击率。1-100表示1-100%的概率产生双倍暴击伤害，大于100表示总是产生双倍暴击伤害，小于1表示不产生暴击伤害。 |
## 成员函数

### Attack:Restore

```
void Restore()
```

 重置所有攻击属性数值。

## 静态函数

### Attack.new

```
static Attack new(int attack, int knockBack, int crit)
```

 创建一个攻击属性对象。

 **返回值:** 新的攻击属性对象。
* `attack`: 伤害值。
* `knockBack`: 击退值。
* `crit`: 攻击的百分暴击率。

