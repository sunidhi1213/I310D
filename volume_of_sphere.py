Python 3.11.8 (v3.11.8:db85d51d3e, Feb  6 2024, 18:02:37) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def calculate_volume_of_sphere(radius):
...     pi = 3.14
...     volume = (4/3) * pi * radius * radius * radius
...     return volume
... 
>>> radius1 = 30
>>> area1 = calculate_volume_of_sphere(radius1)
... print(f"The volume of sphere with radius {radius1} is: {area1}")
... 
... radius2 = 50
... area2 = calculate_volume_of_sphere(radius2)
... print(f"The volume of sphere with radius {radius2} is: {area2}")
... 
