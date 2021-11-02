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

    @property
    def tf_printed(self):  # 'getter' method
        return self.__tf_printed


class Infra1(InfraBase):
    def __init__(self, cloud, replicas=1):
        super().__init__('my_infra1.template', cloud)
        self.replicas = replicas
        self.print_tf()
        # self.__tf_printed  # Not available because it's a 'private' variable


if __name__ == '__main__':
    myInfra = Infra1('gcp')
    print(myInfra.template)

    print(myInfra.tf_printed)
