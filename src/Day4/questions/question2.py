"""
Alyssa P. Hacker made the following Python class:

```python
class Address:
    def __init__(self, street, num):
        self.street_name = street
        self.number = num
```

She now wants to make a subclass of the class Address called CampusAddress that has a new attribute, office number,
that can vary. This subclass will always have the street attribute set to Massachusetts Ave and the num attribute
set to 77. She wants to use the class as follows:

```
>>> Sarina_addr = CampusAddress("32-G904")
>>> Sarina_addr.office_number
’32G-904’
>>> Sarina_addr.street_name
’Massachusetts Ave’
>>> Sarina_addr.number
```

Alyssa is stuck and needs your help. Please help her implement the CampusAddress class; look at exercise 4.5,
particularly the implementations of the two subclasses Accio and Confundo, if you’re stuck.
"""