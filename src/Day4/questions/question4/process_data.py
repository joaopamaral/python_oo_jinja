import yaml

# convert to a class with a abstract method
def process_data():
   with open("data.yaml", "r") as data:
      print(yaml.safe_load(data))

   return []


if __name__ == '__main__':
    list_objects = process_data()