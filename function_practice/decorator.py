# Decorator: 関数に機能を付属する

def greeting(func):
    def inner(*args, **kwargs):
        print("Hello!")
        func(*args, **kwargs)
        print("Nice to meet you!!")
    return inner


@greeting
def say_name(name):
    print(f"I'm {name}")


say_name("taro")

print("=====================")
'''
動きとしては、次のものと同じ

def greeting(func):
    def inner(name):
        print("Hello!")
        func(name)
        print("Nice to meet you!!")
    return inner


def say_name(name):
    print(f"I'm {name}")


say_name = greeting(say_name)
say_name("taro")

'''

@greeting
def say_name_and_origin(name, origin):
    print(f"I'm {name}, I'm from {origin}")


say_name_and_origin("Jiro", "Tokyo")