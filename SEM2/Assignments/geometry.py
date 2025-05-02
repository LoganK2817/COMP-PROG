class Geometry:
    PI = 3.14

    @staticmethod
    def rectangle_perimeter(height, length):
        return height * 2 + length * 2
    
    @staticmethod
    def rectangle_area(height,length):
        return height * length

    @staticmethod
    def circle_perimeter(r):
        return 2 * Geometry.PI * r
    
    @staticmethod
    def circle_area(r):
        return Geometry.PI * r ** 2

    @classmethod
    def set_pi(cls, new_pi):
        cls.PI = new_pi

def main():
    print(Geometry.rectangle_perimeter(10, 20))
    print(Geometry.circle_perimeter(10))

if __name__ == "__main__":
    main()