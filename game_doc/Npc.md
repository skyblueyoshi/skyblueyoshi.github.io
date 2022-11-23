# Npc
描述一个NPC实体。
## 父类
* [Entity](Entity.md)

## 属性
| 成员 | 类型 | 描述 |
| :--- | :--- | :--- |
| entityIndex | EntityIndex |  |
| id | int | 当前NPC的动态ID。 |
| dataWatcher | DataWatcher |  |
| data | table |  |
| texture | TextureLocation |  |
| baseAttack | Attack | 当前NPC的基础攻击属性。 |
| maxSpeed | double | 当前NPC的最大横向移动速度。每帧重置为所在环境（流体黏性等）决定的最大移动速度。 |
| defaultGravity | double | **【只读】** 当前NPC的默认重力加速度。 |
| gravity | double | 当前NPC的纵向加速度。每帧重置为作用了所在环境纵向受力以及重力后的纵向加速度。 |
| defaultMaxFallSpeed | double | **【只读】** 当前NPC的默认最大下落速度。 |
| maxFallSpeed | double | 当前NPC的最大下落速度。每帧重置为作用了所在环境纵向阻力后的最大下落速度。 |
| jumpForce | double | 当前NPC的跳跃力度。每帧重置为作用了所在环境纵向阻力后的跳跃力度。 |
| noMove | boolean | 决定当前NPC是否停止行走。 |
| inLiquid | boolean | **【只读】** 当前NPC是否处在流体环境中。 |
| oldInLiquid | boolean | **【只读】** 上一帧的NPC是否处在流体环境中。 |
| isEnemy | boolean | **【只读】** 当前NPC是否会伤害玩家。 |
| state | int | NPC当前在简单有限状态机中的状态。 |
| stateTimer | int | NPC的状态机计时器。 |
| hurry | boolean | 当前NPC是否为匆忙状态。匆忙状态下随机走模板不会停下来。 |
| maxHealth | int | 当前NPC的生命值上限。 |
| health | int | 当前NPC的生命值。 |
| angry | boolean | 当前NPC是否为愤怒状态。易怒的NPC在被玩家击中后会将该玩家视为目标，并置愤怒状态为true。 |
| animation | int | NPC当前执行的动画状态。通常用于表示骨骼模型的动画状态。 |
| animationTickTime | int | NPC在当前动画索引所经过的时间。每帧自动自增1，当动画状态切换时自动重置为0。 |
| watchAngle | double | **【只读】** NPC的目视角度。若NPC目标存在，则总是目视目标。否则总是根据朝向水平目视。 |
| type | NpcType | **【只读】** NPC类型。 |
| spawnCount | double | 占用生成量。 |
| defaultKnockBackDefenseValue | double | 击退抗性。 |
| toolUseRate | double | 工具使用概率。 |
| maxDisappearTime | int | 最大消失时间。 |
| defaultDefenseValue | int | 防御力。 |
| defaultAttackValue | int | 攻击力。 |
| defaultCritValue | int | 双倍暴击率百分比。 |
| defaultKnockBackValue | int | 击退力。 |
| movement | int | 运动方式。 |
| gfxOffsetX | int | 贴图偏移量X。 |
| gfxOffsetY | int | 贴图偏移量Y。 |
| gfxWidth | int | 贴图宽度。 |
| gfxHeight | int | 贴图高度。 |
| frameStyle | int | 贴图方式 0-不分左右 1-分左右。 |
| exps | int | 经验值。 |
| checkTargetDistance | int | 检测目标的半径。 |
| special | int | 特殊值。 |
| magicRate | int | 产生魔法碎片概率的反比。 |
| friendly | boolean | 是否友好。 |
| hasGravity | boolean | 是否受重力。 |
| canClimbWall | boolean | 是否能爬墙。 |
| isForeground | boolean | 是否置前。 |
| isAntiLava | boolean | 是否抵抗岩浆。 |
| noFixByBlock | boolean | 是否不根据方块修正位置。 |
| willBurnUnderSun | boolean | 是否白天自燃。 |
| defaultAngry | boolean | 是否易怒。 |
| isBoss | boolean | 是否作为BOSS。 |
| noShowHp | boolean | 是否不显示血条。 |
| noBurnSound | boolean | 是否不播放燃烧音效。 |
| usingBoneModule | boolean | **【只读】** 是否使用骨骼模型。 |
| isCheckPlayerTarget | boolean | 是否自动检测玩家目标。 |
| isVisionNoCrossTile | boolean | 是否视野不穿墙。 |
| isAutoSave | boolean | 是否保存到存档。 |
| noHurt | boolean |  |
| noCollisionByWeapon | boolean |  |
| noLooting | boolean |  |
| isWatchAngleForTarget | boolean |  |
| netUpdate | boolean | 是否使用逻辑网络同步。 |
## 成员函数

### Npc:Kill

```
void Kill()
```

 不掉落物品直接清除当前NPC对象。

### Npc:KillByStrike

```
void KillByStrike(double hitAngle, boolean hurtSound, int lootingLevel)
```



### Npc:KillByStrike

```
void KillByStrike(double hitAngle)
```



### Npc:KillByStrike

```
void KillByStrike(double hitAngle, boolean hurtSound)
```



### Npc:Strike

```
void Strike(Attack attack, double hitAngle, boolean immune, boolean hurtSound, int lootingLevel)
```

 制造一个对当前NPC的伤害。
* `attack`: 当前伤害属性。
* `hitAngle`: @[ default `0.0` ] 产生伤害的角度。
* `immune`: @[ default `true` ] 产生当前伤害后是否让NPC处于无敌帧状态。
* `hurtSound`: @[ default `true` ] 是否播放NPC受伤音效。
* `lootingLevel`: @[ default `0` ] 掠夺等级。

### Npc:Strike

```
void Strike(Attack attack)
```

 制造一个对当前NPC的伤害。
* `attack`: 当前伤害属性。

### Npc:Strike

```
void Strike(Attack attack, double hitAngle)
```

 制造一个对当前NPC的伤害。
* `attack`: 当前伤害属性。
* `hitAngle`: @[ default `0.0` ] 产生伤害的角度。

### Npc:Strike

```
void Strike(Attack attack, double hitAngle, boolean immune)
```

 制造一个对当前NPC的伤害。
* `attack`: 当前伤害属性。
* `hitAngle`: @[ default `0.0` ] 产生伤害的角度。
* `immune`: @[ default `true` ] 产生当前伤害后是否让NPC处于无敌帧状态。

### Npc:Strike

```
void Strike(Attack attack, double hitAngle, boolean immune, boolean hurtSound)
```

 制造一个对当前NPC的伤害。
* `attack`: 当前伤害属性。
* `hitAngle`: @[ default `0.0` ] 产生伤害的角度。
* `immune`: @[ default `true` ] 产生当前伤害后是否让NPC处于无敌帧状态。
* `hurtSound`: @[ default `true` ] 是否播放NPC受伤音效。

### Npc:Strike

```
void Strike(Attack attack, double hitAngle, boolean immune, boolean hurtSound, int lootingLevel)
```

 制造一个对当前NPC的伤害。
* `attack`: 当前伤害属性。
* `hitAngle`: @[ default `0.0` ] 产生伤害的角度。
* `immune`: @[ default `true` ] 产生当前伤害后是否让NPC处于无敌帧状态。
* `hurtSound`: @[ default `true` ] 是否播放NPC受伤音效。
* `lootingLevel`: @[ default `0` ] 掠夺等级。

### Npc:StrikeFromPlayer

```
void StrikeFromPlayer(Player player, Attack attack, double hitAngle, boolean immune, boolean hurtSound, int lootingLevel)
```

 制造一个某玩家对当前NPC的伤害。
* `player`: 表示造成伤害的玩家。
* `attack`: 当前伤害属性。
* `hitAngle`: @[ default `0.0` ] 产生伤害的角度。
* `immune`: @[ default `true` ] 产生当前伤害后是否让NPC处于无敌帧状态。
* `hurtSound`: @[ default `true` ] 是否播放NPC受伤音效。
* `lootingLevel`: @[ default `0` ] 掠夺等级。

### Npc:StrikeFromPlayer

```
void StrikeFromPlayer(Player player, Attack attack)
```

 制造一个某玩家对当前NPC的伤害。
* `player`: 表示造成伤害的玩家。
* `attack`: 当前伤害属性。

### Npc:StrikeFromPlayer

```
void StrikeFromPlayer(Player player, Attack attack, double hitAngle)
```

 制造一个某玩家对当前NPC的伤害。
* `player`: 表示造成伤害的玩家。
* `attack`: 当前伤害属性。
* `hitAngle`: @[ default `0.0` ] 产生伤害的角度。

### Npc:StrikeFromPlayer

```
void StrikeFromPlayer(Player player, Attack attack, double hitAngle, boolean immune)
```

 制造一个某玩家对当前NPC的伤害。
* `player`: 表示造成伤害的玩家。
* `attack`: 当前伤害属性。
* `hitAngle`: @[ default `0.0` ] 产生伤害的角度。
* `immune`: @[ default `true` ] 产生当前伤害后是否让NPC处于无敌帧状态。

### Npc:StrikeFromPlayer

```
void StrikeFromPlayer(Player player, Attack attack, double hitAngle, boolean immune, boolean hurtSound)
```

 制造一个某玩家对当前NPC的伤害。
* `player`: 表示造成伤害的玩家。
* `attack`: 当前伤害属性。
* `hitAngle`: @[ default `0.0` ] 产生伤害的角度。
* `immune`: @[ default `true` ] 产生当前伤害后是否让NPC处于无敌帧状态。
* `hurtSound`: @[ default `true` ] 是否播放NPC受伤音效。

### Npc:StrikeFromPlayer

```
void StrikeFromPlayer(Player player, Attack attack, double hitAngle, boolean immune, boolean hurtSound, int lootingLevel)
```

 制造一个某玩家对当前NPC的伤害。
* `player`: 表示造成伤害的玩家。
* `attack`: 当前伤害属性。
* `hitAngle`: @[ default `0.0` ] 产生伤害的角度。
* `immune`: @[ default `true` ] 产生当前伤害后是否让NPC处于无敌帧状态。
* `hurtSound`: @[ default `true` ] 是否播放NPC受伤音效。
* `lootingLevel`: @[ default `0` ] 掠夺等级。

### Npc:StrikeFromNpc

```
void StrikeFromNpc(Npc npc, Attack attack, double hitAngle, boolean immune, boolean hurtSound, int lootingLevel)
```

 制造一个某玩家对当前NPC的伤害。
* `npc`: 表示造成伤害的NPC。
* `attack`: 当前伤害属性。
* `hitAngle`: @[ default `0.0` ] 产生伤害的角度。
* `immune`: @[ default `true` ] 产生当前伤害后是否让NPC处于无敌帧状态。
* `hurtSound`: @[ default `true` ] 是否播放NPC受伤音效。
* `lootingLevel`: @[ default `0` ] 掠夺等级。

### Npc:StrikeFromNpc

```
void StrikeFromNpc(Npc npc, Attack attack)
```

 制造一个某玩家对当前NPC的伤害。
* `npc`: 表示造成伤害的NPC。
* `attack`: 当前伤害属性。

### Npc:StrikeFromNpc

```
void StrikeFromNpc(Npc npc, Attack attack, double hitAngle)
```

 制造一个某玩家对当前NPC的伤害。
* `npc`: 表示造成伤害的NPC。
* `attack`: 当前伤害属性。
* `hitAngle`: @[ default `0.0` ] 产生伤害的角度。

### Npc:StrikeFromNpc

```
void StrikeFromNpc(Npc npc, Attack attack, double hitAngle, boolean immune)
```

 制造一个某玩家对当前NPC的伤害。
* `npc`: 表示造成伤害的NPC。
* `attack`: 当前伤害属性。
* `hitAngle`: @[ default `0.0` ] 产生伤害的角度。
* `immune`: @[ default `true` ] 产生当前伤害后是否让NPC处于无敌帧状态。

### Npc:StrikeFromNpc

```
void StrikeFromNpc(Npc npc, Attack attack, double hitAngle, boolean immune, boolean hurtSound)
```

 制造一个某玩家对当前NPC的伤害。
* `npc`: 表示造成伤害的NPC。
* `attack`: 当前伤害属性。
* `hitAngle`: @[ default `0.0` ] 产生伤害的角度。
* `immune`: @[ default `true` ] 产生当前伤害后是否让NPC处于无敌帧状态。
* `hurtSound`: @[ default `true` ] 是否播放NPC受伤音效。

### Npc:StrikeFromNpc

```
void StrikeFromNpc(Npc npc, Attack attack, double hitAngle, boolean immune, boolean hurtSound, int lootingLevel)
```

 制造一个某玩家对当前NPC的伤害。
* `npc`: 表示造成伤害的NPC。
* `attack`: 当前伤害属性。
* `hitAngle`: @[ default `0.0` ] 产生伤害的角度。
* `immune`: @[ default `true` ] 产生当前伤害后是否让NPC处于无敌帧状态。
* `hurtSound`: @[ default `true` ] 是否播放NPC受伤音效。
* `lootingLevel`: @[ default `0` ] 掠夺等级。

### Npc:AddBuff

```
void AddBuff(int buffID, int buffTime)
```

 为当前NPC添加一个状态效果。若原状态效果存在，以最长时间为新状态效果的持续时间。
* `buffID`: 状态效果ID。
* `buffTime`: 状态效果持续时间。

### Npc:RemoveBuff

```
void RemoveBuff(int buffID)
```

 移除一个状态效果。

### Npc:RemoveAllBuff

```
void RemoveAllBuff()
```

 移除全部状态效果。

### Npc:HasBuff

```
boolean HasBuff(int buffID)
```

 返回NPC是否拥有指定状态效果。
* `buffID`: 状态效果ID。

### Npc:HasAnyBuff

```
boolean HasAnyBuff()
```

 返回NPC是否存在状态效果。

### Npc:TryMakeSound

```
void TryMakeSound(int tryTimes)
```

 NPC尝试发出平时声音。平均经过`tryTimes`次发出一次平时声音。

### Npc:MakeSound

```
void MakeSound()
```

 NPC发出平时声音。

### Npc:Stand

```
void Stand(boolean faceToTarget)
```

 站立静止不动。
* `faceToTarget`: @[ default `true` ] 是否始终面朝玩家。

### Npc:Stand

```
void Stand()
```

 站立静止不动。

### Npc:RandomWalk

```
void RandomWalk(int idleTime, int idleTimeOffset, int walkTime, int walkTimeOffset)
```

 随机地朝一个方向行走或停下或转弯。
 停下时闲置`idleTime ± idleTimeOffset`范围内随机时间。
 朝一个方向行走时持续`walkTime ± walkTimeOffset`范围内随机时间。
 使用内置寻路逻辑，遇到墙壁会尝试跳跃3次。
* `idleTime`: @[ default `128` ]
* `idleTimeOffset`: @[ default `64` ]
* `walkTime`: @[ default `96` ]
* `walkTimeOffset`: @[ default `32` ]

### Npc:RandomWalk

```
void RandomWalk()
```

 随机地朝一个方向行走或停下或转弯。
 停下时闲置`idleTime ± idleTimeOffset`范围内随机时间。
 朝一个方向行走时持续`walkTime ± walkTimeOffset`范围内随机时间。
 使用内置寻路逻辑，遇到墙壁会尝试跳跃3次。

### Npc:RandomWalk

```
void RandomWalk(int idleTime)
```

 随机地朝一个方向行走或停下或转弯。
 停下时闲置`idleTime ± idleTimeOffset`范围内随机时间。
 朝一个方向行走时持续`walkTime ± walkTimeOffset`范围内随机时间。
 使用内置寻路逻辑，遇到墙壁会尝试跳跃3次。
* `idleTime`: @[ default `128` ]

### Npc:RandomWalk

```
void RandomWalk(int idleTime, int idleTimeOffset)
```

 随机地朝一个方向行走或停下或转弯。
 停下时闲置`idleTime ± idleTimeOffset`范围内随机时间。
 朝一个方向行走时持续`walkTime ± walkTimeOffset`范围内随机时间。
 使用内置寻路逻辑，遇到墙壁会尝试跳跃3次。
* `idleTime`: @[ default `128` ]
* `idleTimeOffset`: @[ default `64` ]

### Npc:RandomWalk

```
void RandomWalk(int idleTime, int idleTimeOffset, int walkTime)
```

 随机地朝一个方向行走或停下或转弯。
 停下时闲置`idleTime ± idleTimeOffset`范围内随机时间。
 朝一个方向行走时持续`walkTime ± walkTimeOffset`范围内随机时间。
 使用内置寻路逻辑，遇到墙壁会尝试跳跃3次。
* `idleTime`: @[ default `128` ]
* `idleTimeOffset`: @[ default `64` ]
* `walkTime`: @[ default `96` ]

### Npc:KeepWalking

```
void KeepWalking(boolean followTarget)
```

 持续行走而不停下。使用内置寻路逻辑，遇到墙壁会尝试跳跃3次。
* `followTarget`: @[ default `true` ] 表示在目标存在的情况下，尽可能靠近目标。

### Npc:KeepWalking

```
void KeepWalking()
```

 持续行走而不停下。使用内置寻路逻辑，遇到墙壁会尝试跳跃3次。

### Npc:Walk

```
void Walk(boolean followTarget)
```

 目标存在时，调用`KeepWalking(followTarget)`，否则调用`RandomWalk()`。
* `followTarget`: @[ default `true` ] 表示在目标存在的情况下，尽可能靠近目标。

### Npc:Walk

```
void Walk()
```

 目标存在时，调用`KeepWalking(followTarget)`，否则调用`RandomWalk()`。

### Npc:Swim

```
void Swim(boolean followTarget)
```

 在流体中游泳，在空气中蹦跶。目标不存在时，在流体中随机运动。
* `followTarget`: @[ default `true` ] 表示在目标存在的情况下，尽可能靠近目标。

### Npc:Swim

```
void Swim()
```

 在流体中游泳，在空气中蹦跶。目标不存在时，在流体中随机运动。

### Npc:Fly

```
void Fly(boolean followTarget, double force, boolean gradientSpeed)
```

 在空气中飞行。
* `followTarget`: @[ default `true` ] 表示在目标存在的情况下，尽可能靠近目标，否则随机飞行。
* `force`: @[ default '0.1' ] 表示飞向目标的力。
* `gradientSpeed`: @[ default `false` ] 表示是否使用渐变速度，否则运动速度的向量大小总是恒定的。

### Npc:Fly

```
void Fly()
```

 在空气中飞行。

### Npc:Fly

```
void Fly(boolean followTarget)
```

 在空气中飞行。
* `followTarget`: @[ default `true` ] 表示在目标存在的情况下，尽可能靠近目标，否则随机飞行。

### Npc:Fly

```
void Fly(boolean followTarget, double force)
```

 在空气中飞行。
* `followTarget`: @[ default `true` ] 表示在目标存在的情况下，尽可能靠近目标，否则随机飞行。
* `force`: @[ default '0.1' ] 表示飞向目标的力。

### Npc:RandomTeleport

```
boolean RandomTeleport(int distance, boolean noToAir, boolean noToLiquid)
```

 传送NPC自己到以自己为圆心的圆形区域随机位置。

 **返回值:** 成功传送返回true，失败返回false。
* `distance`: 圆形区域的半径。
* `noToAir`: @[ default `true` ] 表示是否传送到地面上。
* `noToLiquid`: @[ default  true` ] 表示是否不传送到流体内。

### Npc:RandomTeleport

```
boolean RandomTeleport(int distance)
```

 传送NPC自己到以自己为圆心的圆形区域随机位置。

 **返回值:** 成功传送返回true，失败返回false。
* `distance`: 圆形区域的半径。

### Npc:RandomTeleport

```
boolean RandomTeleport(int distance, boolean noToAir)
```

 传送NPC自己到以自己为圆心的圆形区域随机位置。

 **返回值:** 成功传送返回true，失败返回false。
* `distance`: 圆形区域的半径。
* `noToAir`: @[ default `true` ] 表示是否传送到地面上。

### Npc:GetModNpc

```
ModNpc GetModNpc()
```



### Npc:GetGlobalNpc

```
GlobalNpc GetGlobalNpc(string globalNpcName)
```



### Npc:SyncAll

```
void SyncAll()
```



## 参考

* [Entity](Entity.md)
* [EntityIndex](EntityIndex.md)
* [DataWatcher](DataWatcher.md)
* [TextureLocation](TextureLocation.md)
* [Attack](Attack.md)
* [NpcType](NpcType.md)
* [Player](Player.md)
* [ModNpc](ModNpc.md)
* [GlobalNpc](GlobalNpc.md)
