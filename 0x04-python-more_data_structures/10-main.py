#!/usr/bin/python3
best_score = __import__('10-best_score').Best_score
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))
best_key = best_score(None)
print("Best score: {}".format(best_key))
