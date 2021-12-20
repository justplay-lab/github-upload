# 类的方法的第一个参数是类对象cls，通过cls引用的必定是类对象的属性和方法；
# 而实例方法的第一个参数是实例对象self，通过self引用的可能是类属性，
# 也有可能是实例属性，不过在相同名称的类属性和实例属性均有的情况下，实例属性的优先级更高。
class Student(object):
    """定义学生类"""
    # 类的属性
    # 属性归类所有,所有实例都可以访问;
    studCount = 0  # 初始化学生人数,便于后面统计
    classroom = '102'  # 教室号
    kindergarten = '双叶幼儿园'  # 地点
    name = None  # 学生姓名
    age = 0  # 学生年龄

    # 实例方法-----------------------------------------------
    # 实例方法只能被实例对象调用
    def __init__(self, name, age):
        """类的初始化"""
        # init是初始化方法，用于设置实例的相关属性。在创建类的实例的时候一般会自动调用这个方法，
        # 对实例的属性进行初始化。init()方法的第一个参数永远都是self，表示创建实例本身，
        # 在init方法内部，可以把各种属性绑定到self，因为self指向创建实例本身。
        self.name = name  # 学生名字
        self.age = age  # 学生年龄
        self.studCount += 1  # 用于统计学生人数
        self.__headmaster = '高仓文太'  # 私有属性
        # 对于私有属性，即任何以双下画线开头的名字，只能在该类中被调用，
        # 不能在外部调用或者继承，不能被子类继承，也不会被子类覆盖，
        # 可以使用“实例名.类名私有属性名”进行访问，如a._Student__headmaster。

    def head(self):
        """园长"""
        print('The Kindergarten headmaster :', self.__headmaster)

    def displayCount(self):
        """学生人数统计"""
        print('Total Student %d' % self.studCount)

    def displayStudent(self):
        """学生信息"""
        print('Name :', self.name, ", Age :", self.age)

    # 类的方法-----------------------------------------------
    # 类的方法与普通的函数有一个特别的区别——它们必须有一个额外的名称放在前面，
    # 按照惯例这个名称是self。
    @classmethod
    # 类的方法由类调用，采用@classmethod装饰，至少传入一个cls（代指类本身，类似self）参数。
    # 执行类方法时，自动将调用该方法的类赋值给cls。
    def displayClassroom(cls):
        """教室号"""
        print("Classroom is %s" % cls.classroom)

    # 静态方法-----------------------------------------------
    @staticmethod
    # 静态方法由类调用，无默认参数。将实例方法参数中的self去掉，在方法定义上方加上@staticmethod，
    # 就成为静态方法。它属于类，与实例无关。
    def displayKindergarten():
        """学校名"""
        print('Kindergarten is %s' % Student.kindergarten)
