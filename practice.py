from pydantic import BaseModel

class Intro(BaseModel):

    name : str
    age : int
    section : str


def my_intro(me: Intro):
    print(me.name)
    print(me.age)
    print(me.section)

my_data = {
    'name' : 'Ibad Ullah Khan',
    'age'  : 21,
    'section' : 'A'
}

student1 = Intro(**my_data)
my_intro(student1)