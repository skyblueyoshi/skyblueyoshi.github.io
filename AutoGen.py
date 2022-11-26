import os
import io
import shutil

RAW_GAME_ENGINE_API_PATH = "G:/TechCat/TechCat/TechCatGame/assets_sources/Scripts/engine_api"

API_PATH = "C:/Users/FGA/Documents/TerraCraft/devmods/TerraCraft/apis"
ENGINE_API_PATH = os.path.join(API_PATH, "engine_api")
EDITOR_ENGINE_API_PATH = "G:/TechCat/TechCat/TechCatEditor/devmods/Editor/engine_api"

gameAPIs = []
engineAPIs = []


class Lang(object):
    PROPERTIES = "属性"
    MEMBER = "成员"
    TYPE = "类型"
    DESC = "描述"
    MEMBER_FUNC = "成员函数"
    STATIC_FUNC = "静态函数"
    RETURN = "返回值"
    EXAMPLE = "范例"
    RO = "【只读】"
    REF = "参考"
    EXTERN = "父类"


class BaseObject(object):
    def __init__(self, name: str, type_name: str, desc: str):
        self.name = name
        self.type_name = type_name
        self.desc = desc
        self.is_read_only = False
        if self.desc.startswith("Read-only "):
            self.desc = self.desc[10:]
            self.is_read_only = True

    def __str__(self):
        return "{} {}; // {}".format(self.type_name, self.name, self.desc)


class BaseFunction(object):
    def __init__(self, name: str, desc: str = "", is_static: bool = False, class_name: str = ""):
        self.name = name
        self.desc = desc
        self.class_name = class_name
        self.is_static = is_static
        self.param_objects = []  # type:list[BaseObject]
        self.return_object = None  # type:BaseObject|None
        if self.desc == self.name:
            self.desc = ""

    def add_param(self, obj: BaseObject):
        self.param_objects.append(obj)

    def __str__(self):
        s = "// " + self.desc + "\n"
        for param in self.param_objects:
            s += "// @param " + str(param) + "\n"
        if self.return_object is not None:
            s += "// @return " + self.return_object.desc + "\n"
        s += self.gen_markdown_display_str() + ";"
        return s

    def get_return_type(self):
        if self.return_object is None:
            return "void"
        return self.return_object.type_name

    def gen_markdown_display_str(self):
        s = ""
        if self.is_static:
            s += "static "
        s += self.get_return_type() + " "
        s += self.name + "("
        for i, param in enumerate(self.param_objects):
            s += param.type_name + " " + param.name
            if i < len(self.param_objects) - 1:
                s += ", "
        s += ")"
        return s

    def gen_markdown_display_desc(self):
        s = ""
        has_example = False
        example = ""
        if self.desc:
            if self.desc.find("[Example]") == -1:
                s = self.desc
            else:
                ss = self.desc.split("[Example]")
                s = ss[0]
                example = ss[1]
                if example and example[0] == "\n":
                    example = example[1:]
                has_example = True
        if self.return_object:
            if self.return_object.desc:
                s += "\n\n **{}:** {}".format(Lang.RETURN, self.return_object.desc)

        if self.param_objects:
            for pm in self.param_objects:
                if pm.desc:
                    s += "\n* `{}`: {}".format(pm.name, pm.desc)

        if has_example:
            s += "\n\n#### " + Lang.EXAMPLE + ":"
            s += "\n```lua\n" + example + "```"

        return s


class BaseClass(object):
    def __init__(self, class_name: str, super_class_name: str = "", desc: str = ""):
        self.class_name = class_name
        self.super_class_name = super_class_name
        self.lua_name = ""
        self.desc = desc
        self.members = []  # type:list[BaseObject]
        self.function_members = []  # type:list[BaseFunction]
        self.static_functions = []  # type:list[BaseFunction]
        self.ref_data = []

        if self.super_class_name:
            self.try_add_type_ref(self.super_class_name)

    def add_member(self, member: BaseObject):
        self.members.append(member)
        self.try_add_type_ref(member.type_name)

    def add_func_ref(self, func: BaseFunction):
        for param in func.param_objects:
            self.try_add_type_ref(param.type_name)
        if func.return_object:
            self.try_add_type_ref(func.return_object.type_name)

    def try_add_type_ref(self, type_name):
        ts = type_name.split("|")
        for t in ts:
            if t.endswith("[]"):
                t = t[0:len(t) - 2]
            if t in ("int", "double", "number", "boolean", "nil", "table", "function", "string", "any"):
                continue
            if t == self.class_name:
                continue
            if t not in self.ref_data:
                self.ref_data.append(t)

    def __str__(self):
        s = "class {}:{} // {}".format(self.class_name, self.super_class_name, self.desc)
        s += "\nmembers:"
        for m in self.members:
            s += "\n" + str(m)
        s += "\nfunc:"
        for f in self.function_members:
            s += "\n" + str(f) + "\n"
        for f in self.static_functions:
            s += "\n" + str(f) + "\n"
        return s

    @staticmethod
    def get_type_link_format(type_name):
        return "[{}]({}.md)".format(type_name, type_name)

    def gen_markdown(self):
        t = "# " + self.class_name + "\n"

        if self.desc:
            t += self.desc + "\n"
        if self.super_class_name:
            t += "## " + Lang.EXTERN + "\n"
            t += "* " + BaseClass.get_type_link_format(self.super_class_name) + "\n"
            t += "\n"
        if self.members:
            t += "## " + Lang.PROPERTIES + "\n"

            t += "| {} | {} | {} |\n".format(Lang.MEMBER, Lang.TYPE, Lang.DESC)
            t += "| :--- | :--- | :--- |\n"

            for m in self.members:
                desc = m.desc
                if m.is_read_only:
                    desc = "**" + Lang.RO + "** " + desc
                t += "| {} | {} | {} |\n".format(m.name, m.type_name, desc)

        if self.function_members:
            t += "## " + Lang.MEMBER_FUNC + "\n\n"

            for m in self.function_members:
                t += "### " + self.class_name + ":" + m.name + "\n\n"
                t += "```\n" + m.gen_markdown_display_str() + "\n```\n\n"
                t += m.gen_markdown_display_desc() + "\n\n"

        if self.static_functions:
            t += "## " + Lang.STATIC_FUNC + "\n\n"

            for m in self.static_functions:
                t += "### " + self.class_name + "." + m.name + "\n\n"
                t += "```\n" + m.gen_markdown_display_str() + "\n```\n\n"
                t += m.gen_markdown_display_desc() + "\n\n"

        if self.ref_data:
            t += "## " + Lang.REF + "\n\n"

            for m in self.ref_data:
                t += "* " + BaseClass.get_type_link_format(m) + "\n"

        return t


class APIMark(object):
    CLASS = 1
    MEMBER = 2
    PARAM = 3
    RETURN = 4
    FUNCTION = 5
    OVERLOAD = 6

    KEYS = {
        "class": CLASS,
        "field": MEMBER,
        "param": PARAM,
        "return": RETURN,
        "function": FUNCTION,
        "overload": OVERLOAD,
    }


class APISolver(object):

    @staticmethod
    def _pre_solve_lines(lines):
        res = []
        for line in lines:
            if line:
                if line.startswith("end"):
                    continue
                if line.startswith("return "):
                    continue
                if line.startswith("---@API"):
                    continue
                res.append(line)
        return res

    @staticmethod
    def next_word(s: str, sp=" "):
        res = s.split(sp, 1)
        if len(res) == 0:
            return "", ""
        if len(res) == 1:
            return res[0], ""
        return res[0], res[1]

    @staticmethod
    def get_mark(line: str):
        if line.startswith("---@"):
            s = line[4:]
            for key, value in APIMark.KEYS.items():
                if s.startswith(key):
                    return value, s[len(key) + 1:]
        return None, None

    @staticmethod
    def get_comment(line: str):
        if line.startswith("---"):
            return line[3:]
        return None

    @staticmethod
    def get_lua_name(line: str):
        if line.startswith("local "):
            return line[6:].replace(" ", "").split("=")[0]

    @staticmethod
    def _inner_get_func(line: str, lua_cn: str, fn: str, last_param_dict, last_return: BaseObject | None,
                        last_comment: str, is_static: bool, class_dict, param_names, param_mask=None):
        func_obj = BaseFunction(fn, last_comment, is_static)
        func_obj.return_object = last_return

        if param_mask is None:
            for pn in param_names:
                if pn in last_param_dict:
                    func_obj.add_param(last_param_dict[pn])
                else:
                    func_obj.add_param(BaseObject(pn, "any", ""))
        else:
            for mask in param_mask:
                pn, pt = (mask[0], mask[1])
                if pn in last_param_dict:
                    func_obj.add_param(last_param_dict[pn])
                else:
                    func_obj.add_param(BaseObject(pn, pt, ""))

        ok = False
        class_obj: BaseClass
        for class_obj in class_dict.values():
            if class_obj.lua_name == lua_cn:
                if not func_obj.is_static:
                    class_obj.function_members.append(func_obj)
                else:
                    class_obj.static_functions.append(func_obj)
                class_obj.add_func_ref(func_obj)
                ok = True
        if not ok:
            print("Failed:", line)
            assert False

        return func_obj

    @staticmethod
    def get_func(line: str, last_param_dict, last_return: BaseObject | None, last_comment: str, class_dict,
                 last_overloads):
        if line.startswith("function "):
            s = line[9:]
            is_static = s.find(":") == -1
            lua_cn, s = APISolver.next_word(s, "." if is_static else ":")
            fn, s = APISolver.next_word(s, "(")
            s = s[0:len(s) - 1]
            param_names = []
            if s:
                param_names = s.replace(" ", "").split(",")

            func_obj = APISolver._inner_get_func(line, lua_cn, fn, last_param_dict, last_return, last_comment,
                                                 is_static, class_dict, param_names, None)

            for ol in last_overloads:
                APISolver._inner_get_func(line, lua_cn, fn, last_param_dict, last_return, last_comment,
                                          is_static, class_dict, param_names, ol[0])

            return func_obj

        return None

    @staticmethod
    def read_class(s: str):
        tmp, desc = APISolver.next_word(s)
        tmp_list = tmp.split(":")
        if len(tmp_list) == 1:
            return BaseClass(tmp_list[0], "", desc)
        return BaseClass(tmp_list[0], tmp_list[1], desc)

    @staticmethod
    def read_member(s: str):
        type_name = ""
        desc = ""
        name, s = APISolver.next_word(s)
        if s:
            type_name, desc = APISolver.next_word(s)
        return BaseObject(name, type_name, desc)

    @staticmethod
    def read_param(s: str):
        return APISolver.read_member(s)

    @staticmethod
    def read_return(s: str):
        type_name, desc = APISolver.next_word(s)
        return BaseObject("", type_name, desc)

    @staticmethod
    def read_overload(s: str):
        res = [[], None]
        s = s[4:]
        params, ret = APISolver.next_word(s, ")")

        if params:
            ps = params.replace(" ", "").split(",")
            for p in ps:
                pss = p.split(":")
                if len(pss) != 2:
                    print("Failed to read overload:", s)
                    assert False
                pn = pss[0]
                pt = pss[1]

                res[0].append((pn, pt))
        if ret:
            if ret.startswith(":"):
                ret = ret[1:]
            res[1] = ret
        return res

    @staticmethod
    def read_api(file_name, s, out_folder):
        lines = APISolver._pre_solve_lines(s.split('\n'))
        print(file_name, lines)

        class_dict = {}
        last_class_object = None
        last_param_dict = {}
        last_return = None
        last_comment = ""
        last_overloads = []

        for line in lines:
            mark, s = APISolver.get_mark(line)
            if mark:
                match mark:
                    case APIMark.CLASS:
                        obj = APISolver.read_class(s)
                        class_dict[obj.class_name] = obj
                        last_class_object = obj
                    case APIMark.MEMBER:
                        obj = APISolver.read_member(s)
                        last_class_object.add_member(obj)
                    case APIMark.PARAM:
                        obj = APISolver.read_param(s)
                        last_param_dict[obj.name] = obj
                    case APIMark.OVERLOAD:
                        overload_data = APISolver.read_overload(s)
                        last_overloads.append(overload_data)
                    case APIMark.RETURN:
                        last_return = APISolver.read_return(s)

            else:
                if line == "---" or line == "--- ":
                    if last_comment:
                        last_comment += "\n"
                else:
                    cm = APISolver.get_comment(line)
                    if cm:
                        if last_comment:
                            last_comment += "\n"
                        last_comment += cm
                    else:
                        lua_name = APISolver.get_lua_name(line)
                        if lua_name:
                            last_class_object.lua_name = lua_name
                        else:
                            func_obj = APISolver.get_func(line, last_param_dict, last_return, last_comment, class_dict,
                                                          last_overloads)
                            if func_obj:
                                last_param_dict.clear()
                                last_return = None
                                last_comment = ""
                                last_overloads = []

        title_paths = []

        for class_obj in class_dict.values():
            # print(class_obj)
            md = class_obj.gen_markdown()
            path = os.path.join(out_folder, class_obj.class_name + ".md").replace("\\", "/")
            APISolver.save_md(path, md)
            title_paths.append((class_obj.class_name, path))
        return title_paths

    @staticmethod
    def save_md(path, text):
        import codecs
        f = codecs.open(path, "w", "utf-8")
        f.write(text)
        f.close()

    @staticmethod
    def read_file(real_path):
        f = io.open(real_path, mode="r", encoding="utf-8")
        s = f.read()
        return s

    @staticmethod
    def gen_next_toc(tabs, title, path):
        return "  " * tabs + "* [{0}]({1})".format(title, path.replace("\\", "/")) + "\n"

    @staticmethod
    def gen_summary(out_folder, name, title_paths):
        s = APISolver.gen_next_toc(0, name, os.path.join(out_folder, "README.md"))
        for title_path in title_paths:
            s += APISolver.gen_next_toc(1, title_path[0], title_path[1])

        path = os.path.join(out_folder, "SUMMARY.md")
        APISolver.save_md(path, s)

    @staticmethod
    def read_apis(folder_name, name, out_folder):
        title_paths = []
        files = os.listdir(folder_name)
        for fn in files:
            real_path = os.path.join(folder_name, fn)
            if os.path.isfile(real_path):
                s = APISolver.read_file(real_path)
                if s and s.startswith("---@API"):
                    sub_title_paths = APISolver.read_api(fn, s, out_folder)
                    title_paths.extend(sub_title_paths)

        print(title_paths)
        APISolver.gen_summary(out_folder, name, title_paths)

    @staticmethod
    def save_main_summary():
        s = "# Table of contents\n\n"
        s += APISolver.read_file("engine_doc/SUMMARY.md")
        print(s)
        s += APISolver.read_file("game_doc/SUMMARY.md")
        print(s)

        APISolver.save_md("SUMMARY.md", s)

    @staticmethod
    def copy_folder(src, dst):
        src_files = os.listdir(src)
        for file_name in src_files:
            full_file_name = os.path.join(src, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, dst)


if __name__ == '__main__':
    APISolver.copy_folder(RAW_GAME_ENGINE_API_PATH, ENGINE_API_PATH)
    APISolver.copy_folder(RAW_GAME_ENGINE_API_PATH, EDITOR_ENGINE_API_PATH)
    APISolver.read_apis(ENGINE_API_PATH, "游戏引擎API文档", "engine_doc")
    APISolver.read_apis(API_PATH, "《泰拉世界》游戏API文档", "game_doc")
    APISolver.save_main_summary()
