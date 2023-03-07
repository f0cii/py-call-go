import cffi

# pip install cffi

# 定义 C 函数的签名
ffi = cffi.FFI()
ffi.cdef("""
    int add(int left, int right);
    char* s(const char* c);
    void c_free(void *ptr);
    
    typedef int (*callback_t)(char*);
    int setCallback(callback_t s);
""")


# 加载动态库
lib = ffi.dlopen("./py-call-go.so")


@ffi.callback("callback_t")
def py_callback(s):
    s_arg = ffi.string(s).decode()
    print(type(s_arg))
    print('abc:' + s_arg)
    return 0


lib.setCallback(py_callback)


# 上下文管理器，用于自动管理内存
class FFIRelease:
    def __init__(self, *args):
        self.args = args

    def __enter__(self):
        return self.args

    def __exit__(self, exc_type, exc_val, exc_tb):
        for arg in self.args:
            ffi.release(arg)


# 创建 C 字符串指针
def new_c_str(c):
    return ffi.new("char[]", c.encode())


# 调用 C 函数，返回字符串
def call_c_function_return_str(c_function, c_args):
    c_result = c_function(*c_args)
    # s_result = ffi.string(ffi.cast("char *", c_result)).decode()
    s_result = ffi.string(c_result).decode()
    ffi.gc(c_result, lib.c_free)
    return s_result


# 生成 Python 的包装函数
def hello(c):
    c_str = new_c_str(c)
    result_str = call_c_function_return_str(lib.s, [c_str])
    with FFIRelease(c_str):
        return result_str


if __name__ == '__main__':
    # 调用 add 函数
    result = lib.add(1, 2)
    print("add result:", result)

    for i in range(10):
        print(hello("world"))
