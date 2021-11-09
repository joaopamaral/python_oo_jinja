from abc import ABC, abstractmethod


class InfraAbstract(ABC):
    def __init__(self, cloud="aws"):
        self.cloud = cloud.upper()

    def not_abstract_method(self):
        return 1 + 1

    @abstractmethod
    def abstract_method(self):
        pass


class Infra1(InfraAbstract):
    def __init__(self):
        super().__init__("azure")


class Infra2(InfraAbstract):
    def __init__(self):
        super().__init__("azure")

    def abstract_method(self):
        print('This is not abstract')


if __name__ == '__main__':
    # abstract_obj = InfraAbstract()  # Error

    # my_infra1 = Infra1()  # Error

    my_infra2 = Infra2()  # Error
    my_infra2.abstract_method()
