# 定义一个生成器函数，但是它会调用某个你想暴露给用户使用的外部状态值
# 你想让你的生成器暴露外部状态给用户， 别忘了你可以简单的将它实现为一个类，然后把生成器函数放到 __iter__() 方法中
