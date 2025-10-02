from owlready2 import *
import itertools
from create_ontology import *

# Define a target class expression (e.g., animals that can fly)
target_expr = class_expression({"hasFur": True})
pos_examples, neg_examples = get_examples(target_expr)

print("Positive Examples:", {p.name for p in pos_examples})
print("Negative Examples:", {n.name for n in neg_examples})

# Step 4: Learning the Class Expression (Refinement Strategy)
def learn_class_expression(pos_examples, neg_examples):
    """ Find the simplest class expression covering positive but not negative examples."""
    properties = [prop.name for prop in onto.Animal.get_class_properties()]
    
    # Generate all possible property constraints
    candidate_expressions = []
    for r in range(1, len(properties) + 1):
        for subset in itertools.combinations(properties, r):
            for values in itertools.product([True, False], repeat=r):
                expr = dict(zip(subset, values))
                expr_func = class_expression(expr)
                
                # Check if the expression covers all positives and excludes all negatives
                if all(expr_func(p) for p in pos_examples) and not any(expr_func(n) for n in neg_examples):
                    candidate_expressions.append(expr)
    
    # Return the simplest expression
    return min(candidate_expressions, key=lambda e: len(e), default=None)

# Learn an expression for the given examples
learned_expr = learn_class_expression(pos_examples, neg_examples)
print("Learned Class Expression:", learned_expr)
