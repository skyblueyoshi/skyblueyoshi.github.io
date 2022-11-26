# UINode
基本的UI节点，是所有类型UI节点的基类。
## 属性
| 成员 | 类型 | 描述 |
| :--- | :--- | :--- |
| name | string | 节点名字。 |
| anchorPoint | Vector2 | 组件锚点。 |
| anchorPointX | number | 锚点横坐标。 |
| anchorPointY | number | 锚点纵坐标。 |
| position | Vector2 | 节点在父节点空间的坐标。 |
| positionInCanvas | Vector2 | 节点在画布空间的坐标。 |
| positionX | number | 节点在父节点空间的横坐标。 |
| positionY | number | 节点在父节点空间的纵坐标。 |
| size | Size | 节点尺寸。 |
| width | number | 节点宽度。 |
| height | number | 节点高度。 |
| visible | boolean | 节点是否可见。 |
| leftMargin | number | 节点到父节点的左侧边距。 |
| rightMargin | number | 节点到父节点的右侧边距。 |
| topMargin | number | 节点到父节点的上侧边距。 |
| bottomMargin | number | 节点到父节点的下侧边距。 |
| leftMarginEnabled | boolean | 是否启用节点到父节点的左侧边距。 |
| rightMarginEnabled | boolean | 是否启用节点到父节点的右侧边距。 |
| topMarginEnabled | boolean | 是否启用节点到父节点的上侧边距。 |
| bottomMarginEnabled | boolean | 是否启用节点到父节点的下侧边距。 |
| autoStretchWidth | boolean | 是否根据左右侧边距自动拉伸适配宽度，若为false，则为根据左右侧边距水平居中。 |
| autoStretchHeight | boolean | 是否根据上下侧边距自动拉伸适配高度，若为false，则为根据上下侧边距竖直居中。 |
| touchable | boolean | 节点是否可被触碰。 |
| tag | number | 节点附加值。 |
| childTag | number | 节点作为子节点时的附加值。 |
| isContainer | boolean | 节点是否作为裁切容器。 |
| allowDoubleClick | boolean | 节点是否允许进行双击。 |
| textBatchRendering | boolean |  |
| enableRenderTarget | boolean | 节点是否开启RenderTarget纹理缓存，开启后仅在内部节点更新时重绘纹理缓存。 |
| isTouching | boolean | 当前节点是否被触碰中。 |
## 成员函数

### UINode:clone

```
UINode clone()
```



### UINode:valid

```
boolean valid()
```



### UINode:setAnchorPoint

```
void setAnchorPoint(number x, number y)
```



### UINode:setPosition

```
void setPosition(number x, number y)
```



### UINode:setLocation

```
void setLocation(number x, number y, number width, number height)
```



### UINode:setSize

```
void setSize(number width, number height)
```



### UINode:addChild

```
void addChild(UINode node, number childTag)
```



### UINode:addChild

```
void addChild(UINode node)
```



### UINode:removeChild

```
void removeChild(UINode node)
```



### UINode:removeAllChildren

```
void removeAllChildren()
```



### UINode:applyMargin

```
void applyMargin(boolean applyAllChildren)
```



### UINode:setLeftMargin

```
void setLeftMargin(number offset, boolean enabled)
```



### UINode:setRightMargin

```
void setRightMargin(number offset, boolean enabled)
```



### UINode:setTopMargin

```
void setTopMargin(number offset, boolean enabled)
```



### UINode:setBottomMargin

```
void setBottomMargin(number offset, boolean enabled)
```



### UINode:setMarginEnabled

```
void setMarginEnabled(boolean left, boolean top, boolean right, boolean bottom)
```



### UINode:setAutoStretch

```
void setAutoStretch(boolean widthEnabled, boolean heightEnabled)
```



### UINode:getChildByTag

```
UINode getChildByTag(number childTag)
```



### UINode:getChild

```
UINode getChild(string name)
```



### UINode:addTouchDownListener

```
ListenerID addTouchDownListener(table|function listener)
```



### UINode:removeTouchDownListener

```
void removeTouchDownListener(ListenerID listenerID)
```



### UINode:addTouchDoubleDownListener

```
ListenerID addTouchDoubleDownListener(table|function listener)
```



### UINode:removeTouchDoubleDownListener

```
void removeTouchDoubleDownListener(ListenerID listenerID)
```



### UINode:addTouchMoveListener

```
ListenerID addTouchMoveListener(table|function listener)
```



### UINode:removeTouchMoveListener

```
void removeTouchMoveListener(ListenerID listenerID)
```



### UINode:addTouchPointedMoveListener

```
ListenerID addTouchPointedMoveListener(table|function listener)
```



### UINode:removeTouchPointedMoveListener

```
void removeTouchPointedMoveListener(ListenerID listenerID)
```



### UINode:addTouchUpListener

```
ListenerID addTouchUpListener(table|function listener)
```



### UINode:removeTouchUpListener

```
void removeTouchUpListener(ListenerID listenerID)
```



### UINode:addTouchUpAfterMoveListener

```
ListenerID addTouchUpAfterMoveListener(table|function listener)
```



### UINode:removeTouchUpAfterMoveListener

```
void removeTouchUpAfterMoveListener(ListenerID listenerID)
```



### UINode:addTouchPointedUpListener

```
ListenerID addTouchPointedUpListener(table|function listener)
```



### UINode:removeTouchPointedUpListener

```
void removeTouchPointedUpListener(ListenerID listenerID)
```



### UINode:addMousePointedListener

```
ListenerID addMousePointedListener(table|function listener)
```



### UINode:removeMousePointedListener

```
void removeMousePointedListener(ListenerID listenerID)
```



### UINode:addMousePointedEnterListener

```
ListenerID addMousePointedEnterListener(table|function listener)
```



### UINode:removeMousePointedEnterListener

```
void removeMousePointedEnterListener(ListenerID listenerID)
```



### UINode:addMousePointedLeaveListener

```
ListenerID addMousePointedLeaveListener(table|function listener)
```



### UINode:removeMousePointedLeaveListener

```
void removeMousePointedLeaveListener(ListenerID listenerID)
```



### UINode:getPreDrawLayer

```
UINodeDrawLayer getPreDrawLayer(number layer)
```



### UINode:getPostDrawLayer

```
UINodeDrawLayer getPostDrawLayer(number layer)
```



### UINode:getChildrenCount

```
number getChildrenCount()
```



### UINode:getChildByIndex

```
UINode getChildByIndex(number index)
```



### UINode:getPointedNode

```
UINode getPointedNode(Vector2 canvasPosition, boolean isTouching)
```



### UINode:getPointedNode

```
UINode getPointedNode(Vector2 canvasPosition)
```



### UINode:flushRender

```
void flushRender()
```



## 静态函数

### UINode.new

```
static UINode new()
```



## 参考

* [Vector2](Vector2.md)
* [Size](Size.md)
* [ListenerID](ListenerID.md)
* [UINodeDrawLayer](UINodeDrawLayer.md)
