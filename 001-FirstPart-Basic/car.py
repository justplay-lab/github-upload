#coding=gbk
#
class Car():
    """һ��ģ�������ļ򵥳���"""
    
    def __init__(self, make, model, year):
        """��ʼ����������������"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """�����������������Ϣ"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """��ӡһ��ָ��������̵���Ϣ"""
        print("This Car has " + str(self.odometer_reading) +
                " miles on it.")

    def update_odometer(self, mileage):
        """
        1.����̱��������Ϊָ����ֵ
        2.��ֹ����̱������ص�
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")
    
    def increment_odometer(self, miles):
        """�����������ָ������"""
        self.odometer_reading += miles
        
    def fill_gas_tank(self):
        """��������"""
        print("����Ҫ�������ͣ�")


class ElectricCar(Car):
    """�綯�����Ķ���֮��"""
    
    def __init__(self, make, model, year):
        """
        �綯���Ķ���֮��
        ��ʼ����������ԣ��ٳ�ʼ���綯�������е�����
        """
        super().__init__(make, model, year)
        # ~ self.battery_size = 70
        self.battery = Battery()
    
    # ~ def describe_battery(self):
        # ~ """��ӡһ��������ƿ��������Ϣ"""
        # ~ print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
    def fill_gas_tank(self):
        """�綯����û������"""
        print("This car doesn't need a gas tank!")
        
        
class Battery():
    """һ��ģ��綯������ƿ�ļ򵥳���"""
    
    def __init__(self, battery_size=70):
        """��ʼ����ƿ������"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """��ӡһ��������ƿ��������Ϣ"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        """��ӡһ����Ϣ��ָ����ƿ���������"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go about " + str(range)
        message += " miles on a full cahrge."
        print(message)
