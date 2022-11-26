# Path
标准化路径处理类。本项目对于文件路径，认为形如如下的路径都是标准化的。文件夹：Folder、Folder/Folder；文件：File.ext、Folder/File.ext。
## 静态函数

### Path.fix

```
static string fix(string path)
```

修正路径为标准化路径。

 **返回值:** 标准化路径。
* `path`: 原始路径。

### Path.join

```
static string join(string path1, string path2, string path3, string path4)
```

连接路径。

 **返回值:** 标准化路径。

### Path.join

```
static string join(string path1, string path2)
```

连接路径。

 **返回值:** 标准化路径。

### Path.join

```
static string join(string path1, string path2, string path3)
```

连接路径。

 **返回值:** 标准化路径。

### Path.getExtension

```
static string getExtension(string path)
```

获取后缀名称。例："abc/test.png"，返回".png"。

### Path.getFileName

```
static string getFileName(string path)
```

获取文件名。例："abc/test.png"，返回"test.png"。

### Path.getFileNameWithoutExtension

```
static string getFileNameWithoutExtension(string path)
```

获取不带后缀的文件名。例："abc/test.png"，返回"test"。

### Path.getRelativePath

```
static string getRelativePath(string relativeTo, string path)
```

获取相对路径。例："folder"，"folder/folder2/test.txt"，返回"folder2/test.txt"。

### Path.isRelativePath

```
static boolean isRelativePath(string relativeTo, string path)
```

判断是否是相对路径。例：

（1）"folder"，"folder/folder2/test.txt"，返回true。

（2）"folder_abc"，"folder/folder2/test.txt"，返回false。

（3）"folder"，"folder_abc/folder2/test.txt"，返回false。

### Path.getParentDirectory

```
static string getParentDirectory(string path)
```

获取上级目录。例："abc/def/test.txt"返回"abc/def"。

