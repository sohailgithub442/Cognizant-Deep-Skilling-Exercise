class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


obj1 = Singleton()
obj2 = Singleton()

print("Object 1:", obj1)
print("Object 2:", obj2)

if obj1 == obj2:
    print("Both objects are the same instance.")
else:
    print("Objects are different.")
