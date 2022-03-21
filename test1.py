"""
 * Project name(项目名称)：Python缓存重用机制 
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/21 
 * Time(创建时间)： 18:32
 * Version(版本): 1.0
 * Description(描述)： Python_cache_reuse_mechanism
 """


# 数据类型	是否可以重用	生效范围
# 范围在 [-5, 256] 之间的小整数	如果之前在程序中创建过，就直接存入缓存，后续不再创建。	全局
# bool 类型
# 字符串类型数据
# 大于 256 的整数	只要在本代码块内创建过，就直接缓存，后续不再创建。	本代码块
# 大于 0 的浮点型小数
# 小于 0 的浮点型小数	不进行缓存，每次都需要额外创建。
# 小于 -5 的整数

def fun():
    # [-5,256]
    int1 = -5
    print("fun中 -5 的存储状态", id(int1), id(int2))

    # bool类型
    bool3 = True
    print("fun中 bool 类型的存储状态", id(bool3), id(bool2))

    # 字符串类型
    s1 = "3344"
    print("fun 中 3344 字符串的存储状态", id(s1), id(s2))
    # 大于 256
    int3 = 257
    print("fun中 257 的存储状态", id(int3), id(int4))
    # 浮点类型
    f1 = 256.4
    print("fun 中 256.4 的存储状态", id(f1), id(f2))
    # 小于 -5
    n11 = -6
    print("fun 中 -6 的存储状态", id(n11), id(n2))


if __name__ == '__main__':
    # 范围在 [-5, 256] 之间的小整数
    int1 = -5
    int2 = -5
    print("[-5, 256] 情况下的两个变量：", id(int1), id(int2))
    # bool类型
    bool1 = True
    bool2 = True
    print("bool类型情况下的两个变量：", id(bool1), id(bool2))
    # 对于字符串
    s1 = "3344"
    s2 = "3344"
    print("字符串情况下的两个交量", id(s1), id(s2))
    # 大于 256 的整数
    int3 = 257
    int4 = 257
    print("大于 256 的整数情况下的两个变量", id(int3), id(int4))
    # 大于 0 的浮点数
    f1 = 256.4
    f2 = 256.4
    print("大于 0 的浮点数情况下的两个变量", id(f1), id(f2))
    # 小于 0 的浮点数
    f3 = -2.45
    f4 = -2.45
    print("小于 0 的浮点数情况下的两个变量", id(f3), id(f4))
    # 小于 -5 的整数
    n1 = -6
    n2 = -6
    print("小于 -5 的整数情况下的两个变量", id(n1), id(n2))
    fun()
