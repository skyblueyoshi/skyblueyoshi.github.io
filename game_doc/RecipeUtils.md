# RecipeUtils
配方组件。
## 静态函数

### RecipeUtils.GetRecipe

```
static Recipe GetRecipe(int recipeID)
```

通过配方的ID获取配方。

 **返回值:** 配方。
* `recipeID`: 配方ID （请通过搜索配方的方法 RecipeUtils.SearchRecipe() 动态获取）。

### RecipeUtils.GetConfig

```
static RecipeConfig GetConfig(int recipeConfigID)
```

获取某一合成实体的配方配置。

 **返回值:** 配方配置。
* `recipeConfigID`: 配方配置ID （请通过Reg.RecipeConfigID()动态获取）。

### RecipeUtils.SearchRecipe

```
static int SearchRecipe(int configID, Inventory inventory, int offset, int length)
```

搜索配方。


 **返回值:** 配方ID
* `configID`: 配方配置ID （请通过Reg.RecipeConfigID()动态获取）。
* `inventory`: 物品格子的集合（一般为合成中使用的物品的格子的集合）。
* `offset`: 偏移值（从物品格子的哪里开始）。
* `length`: 长度（调用物品格子的数目）。

#### 范例:
```lua
--获取酿造台的某一配方，使用酿造台中的两个合成的格子作为输入物品
local recipeID = RecipeUtils.SearchRecipe(Reg.RecipeConfigID("Brew"), self.inventory, 0, 2)```

### RecipeUtils.SearchRecipe

```
static int SearchRecipe(int configID, Inventory inventory)
```

搜索配方。


 **返回值:** 配方ID
* `configID`: 配方配置ID （请通过Reg.RecipeConfigID()动态获取）。
* `inventory`: 物品格子的集合（一般为合成中使用的物品的格子的集合）。

#### 范例:
```lua
--获取酿造台的某一配方，使用酿造台中的两个合成的格子作为输入物品
local recipeID = RecipeUtils.SearchRecipe(Reg.RecipeConfigID("Brew"), self.inventory, 0, 2)```

### RecipeUtils.HasRecipe

```
static int HasRecipe(int configID, ItemStack inputItemStack, int inputIndex)
```

检查某一物品是否有对应的配方

 **返回值:** 配方ID。
* `configID`: 配方配置ID （请通过Reg.RecipeConfigID()动态获取）。
* `inputItemStack`: 合成输入的堆叠物品。
* `inputIndex`: 合成输入的Index。

### RecipeUtils.SearchRecipeHasInputItem

```
static int[] SearchRecipeHasInputItem(int configID, ItemStack inputItemStack)
```

检查某一配方配置里所有的配方中是否有对应的输入物品

 **返回值:** 搜索到的配方ID的数组。
* `configID`: 配方配置ID （请通过Reg.RecipeConfigID()动态获取）。
* `inputItemStack`: 搜索对应的堆叠物品。

### RecipeUtils.SearchRecipeHasOutputItem

```
static int[] SearchRecipeHasOutputItem(int configID, ItemStack outputItemStack, int outputIndex)
```

检查某一配方配置里所有的配方中是否有对应的输出物品

 **返回值:** 搜索到的配方ID的数组。
* `configID`: 配方配置ID （请通过Reg.RecipeConfigID()动态获取）。
* `outputItemStack`: 搜索对应的堆叠物品。
* `outputIndex`: 合成输出的Index。

## 参考

* [Recipe](Recipe.md)
* [RecipeConfig](RecipeConfig.md)
* [Inventory](Inventory.md)
* [ItemStack](ItemStack.md)
