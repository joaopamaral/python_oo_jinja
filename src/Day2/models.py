class InfraBase:
    def __init__(self, template, cloud='aws'):
        self.template = template
        self.cloud = cloud.upper()
        self.__tf_printed = False

    def print_tf(self):
        if not self.__tf_printed:
            print(f"""    
                terraform {{
                  required_version = ">= 0.12.26"
                }}

                output "hello_world" {{
                  value = "Hello, World! You defined the cloud {self.cloud}"
                }}
            """)

            self.__tf_printed = True

    def create_file(self):
        pass  # Not Implemented

    def my_base_method(self):
        print("My base method")

    @staticmethod
    def my_static_method():
        print("My tatic method")

    @property
    def tf_printed(self):  # 'getter' method
        return self.__tf_printed

    def get_infra_info(self):
        return "This is the Base Infra"

    def __str__(self):
        return f"<InfraBase template:{self.template} cloud:{self.cloud} tf_printed:{self.__tf_printed}>"


class Infra1(InfraBase):
    def __init__(self, cloud, replicas=1):
        super().__init__('my_infra1.template', cloud)  # constructor of parent class accessed using the super()
        self.replicas = replicas
        self.print_tf()
        # self.__tf_printed  # Not available because it's a 'private' variable

    def create_file(self):  # overwrite method
        with open('my_file.txt', 'w') as f:
            f.write('teste')

    def print_tf(self):
        print('This line was included in the print')
        super(Infra1, self).print_tf()  # calling the print from the parent class

    def get_infra_info(self):
        return f"This is the Infra1 - replicas = {self.replicas}"

    def __str__(self):
        return f"<InfraBase template:{self.template} cloud:{self.cloud} replicas:{self.replicas}>"


if __name__ == '__main__':
    myInfra = Infra1('gcp')
    print(myInfra.template)

    print(myInfra.tf_printed)
    myInfra.my_base_method()
    InfraBase.my_static_method()

    # Polymorphism
    myInfraBase = InfraBase('template1')
    infras = [myInfra, myInfraBase]
    for infra in infras:
        print(f"Type: {type(infra).__name__} - Infra Info: {infra.get_infra_info()}")
        # print(infra)
