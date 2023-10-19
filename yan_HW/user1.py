class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"User Info: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        # 在这里你可以添加其他属性的打印信息

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back!")

# 创建多个用户实例
user1 = User("John", "Doe", 30, "john@example.com")
user2 = User("Alice", "Smith", 25, "alice@example.com")
user3 = User("Bob", "Johnson", 35, "bob@example.com")

# 调用describe_user()和greet_user()方法
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()