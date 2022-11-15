class point_set:
    def __init__(self,name: str, cord: list) -> None:
        self.x_cord = cord[0]
        self.y_cord = cord[1]
        self.name = name
        self.points = (self.x_cord,self.y_cord)

class polynomial:
    def __init__(self, name: str, *points: tuple) -> None:
        first_warper = [ ]
        second_warper = [ ]
        first_warper.append(name)
        first_warper.append(points["points"])
        second_warper.append(first_warper)
        self.name = name
        self.points_set = dict(second_warper)



OPERATION_TOKEN = {
    "LOAD_POINT": point_set,
    "LOAD_SHAPE": polynomial,
    "LOAD_SEGME": ...,
    "AREA_SHAPE": ...,
    "PRIM_SHAPE": ...,
    "SLOPE_SEGM": ...,
    "CONG_SHAPE": ...
}

'''point_set1 = point_set(1,3,"A")
point_set2 = point_set(10,3,"B")
point_set3 = point_set(4,6,"C")
shape = polynomial("default",name="ABC",points=[(point_set1.x_cord,point_set1.y_cord),(point_set2.x_cord,point_set2.y_cord),(point_set3.x_cord, point_set3.y_cord)])
print(shape.points_set)
print(type(shape.points_set))'''