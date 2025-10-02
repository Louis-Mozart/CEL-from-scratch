from owlready2 import *

# def create_onto():
onto = get_ontology("http://example.org/animals.owl")   

with onto:
    class Animal(Thing): pass
    class hasWings(Animal >> bool): pass
    class hasFur(Animal >> bool): pass
    class livesInWater(Animal >> bool): pass
    
    # Define individuals
    lion = Animal("Lion")
    eagle = Animal("Eagle")
    shark = Animal("Shark")
    bat = Animal("Bat")
    penguin = Animal("Penguin")
    
    # Assign properties
    lion.hasWings = [False]; lion.hasFur = [True]; lion.livesInWater = [False]
    eagle.hasWings = [True]; eagle.hasFur = [False]; eagle.livesInWater = [False]
    shark.hasWings = [False]; shark.hasFur = [False]; shark.livesInWater = [True]
    bat.hasWings = [True]; bat.hasFur = [True]; bat.livesInWater = [False]
    penguin.hasWings = [True]; penguin.hasFur = [False]; penguin.livesInWater = [True]
    
onto.save("animals.owl")  # Save ontology to a file

# Step 2: Define a Class Expression Structure
def class_expression(expr):
    return lambda x: all(getattr(x, k, [None])[0] == v for k, v in expr.items())

# Step 3: Generate Positive and Negative Examples
def get_examples(target_expr):
    pos_examples = {ind for ind in Animal.instances() if target_expr(ind)}
    neg_examples = set(Animal.instances()) - pos_examples
    return pos_examples, neg_examples

