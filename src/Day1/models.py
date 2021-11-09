class Infra:
    template = None
    cloud = 'aws'


class InfraWithConstructor:
    def __init__(self, template, cloud='aws'):
        self.template = template
        self.cloud = cloud.upper()  # String is also an onbject
        self.__tf_printed = False  # 'Private' method
        # self.print_tf()

    def print_tf(self):  # this is a method
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

    # Accessing "private" variables (Encapsulation)
    @property
    def tf_printed(self):  # 'getter' method
        return self.__tf_printed

    # @tf_printed.setter
    # def tf_printed(self, printed): # 'setter' method
    #     self.__tf_printed = printed


if __name__ == '__main__':
    my_infra = Infra()  # How we can create an object using a class
    # Let's print the attributes
    print(my_infra.template, my_infra.cloud, type(my_infra), my_infra)
    Infra.cloud = 'azure'
    print(Infra().cloud)

    # Using the constructor to instantiate a class is always recommended
    my_infra2 = InfraWithConstructor('template1')
    print(f'template: {my_infra2.template}, cloud: {my_infra2.cloud}, type: {type(my_infra2).__name__}, obj: {my_infra2}')

    # You should define all the required parameters of a class
    my_infra3 = InfraWithConstructor()

    my_infra2.print_tf()
    print(my_infra2.__tf_printed)  # Can't access 'private' variable/method outside class
    print(my_infra2.tf_printed)  # You can use a property/method to access a private variable