import sys, os, gnureadline
from framework.path import construct
from framework.json_file_operation import write
from framework.objects import obj_def, errors


class translate:
    def __init__(self, source: list): # LOAD_POINT A (1,3)
        self.operation_token = source[0]
        self.name = source[1]
        try:
            (int(source[2][1]),int(source[2][3]))
        except ValueError:
            self.points = (source[2][1],source[2][3],source[2][5])
        else:
            self.points = (int(source[2][1]),int(source[2][3]))
class io:
    def take():
        inputs = input("Geo Playground> ")
        return inputs.split()

class tokens:
    def __init__(self, source: any) -> None:
        splitted_stuff = translate(source=source)
        try:
            to_be_write = obj_def.OPERATION_TOKEN[splitted_stuff.operation_token](
            splitted_stuff.name,
            splitted_stuff.points)
            write.write(dict([[to_be_write.name,to_be_write.points]]))
        except KeyError:
            raise errors.UndefinedInstructionError
        


'''original = translate("LOAD_SHAPE    A (A,B,C)")
point =    translate("LOAD_POINT    A (1,2)")
area =     translate("AREA_SHAPE    C")
print(original.operation_token,original.name, original.points)
print(point.operation_token,point.name, point.points)
print(area.operation_token,area.name, area.points)'''

write.clean()
while __name__ == "__main__":
    
    sources = io.take()
    if sources == "exit":
        sys.exit()
    else:
        tokens(source=sources)