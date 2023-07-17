class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

instance1 = Singleton()
instance2 = Singleton()

print(instance1 is instance2)
