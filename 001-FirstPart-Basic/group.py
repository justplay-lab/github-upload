"""
继承类的构造方法有以下两种。
（1）经典类的写法：父类名称.init(self,参数1,参数2,…)。
（2）新式类的写法：super(子类,self).init(参数1,参数2,…)。
在定义子类的构造函数时，只有先继承再构造，才能继承父类的属性。
子类的方法如果和父类的方法重名，子类就会覆盖掉父类，这就是继承“多态”。调用方只管调用，不管细节，而新增一个子类时，只要确保新方法编写正确，而不用管原来的代码，这就是著名的“开闭”原则。
（1）对扩展开放：允许新增子类；
（2）对修改封闭：不需要修改依赖父类的函数。
"""
from student import Student


class Group(Student):
    """定义团体子类"""

    # 新增类的属性
    Class = '向日葵班级'
    Teacher = '吉永老师'

    # 继承类的构造
    def __init__(self, name, age):
        """类的初始化"""
        super(Group, self).__init__(name, age)

    # 新增实例方法
    def favorite(self):
        """类的初始化"""
        if self.name == '野原新之助':
            print(u'小新最喜欢动感超人了')

    # 重构旧的实例方法
    def displayCount(self):
        """学生人数统计"""
        print('人数是 %d' % self.studCount)