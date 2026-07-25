#qaation No1
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate(self):
        return f"title: {self.title}\n content: {self.content}"


class ReportSaver:
    def save_to_file(self, report_object, file_name):
        with open(file_name, "w") as file:
            file.write(report_object.generate())
        print(f"File '{file_name}' has been saved successfully.")


class ReportEmailer:
    def __init__(self):
        self.sender_email = "kidist21aya@gmail.com"

    def send(self, report_object, recipient_email):
        email_content = report_object.generate()
        print(f"self email : {self.sender_email} recipient_email: {recipient_email} the message is successful.")
        print(f"email_content:\n{email_content}")



        #Quation No2

        
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

class AreaPrinter:
    def print_shape_area(self, shape_object):
        print(f"The area is: {shape_object.area()}")



