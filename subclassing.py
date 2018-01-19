import copy

class ReverseStr(str):
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self

new_str = ReverseStr("Hello")

#print(new_str)



class FilledList(list):
    def __init__(self, count, value, *args, **kwargs):
        super().__init__()
        for _ in range(count):
            self.append(copy.copy(value))


list = FilledList(9, 2)
list2 = FilledList(7, [1,5,8])

#print(list2)


class JavaScriptObject(dict):
    def __getattribute__(self,item):
        try:
            return self[item]
        except KeyError:
            return super().__getattribute__(item)

jso = JavaScriptObject({'name': 'Jayd'})

print(jso.fake)

