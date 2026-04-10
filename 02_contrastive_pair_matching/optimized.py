from collections import defaultdict
import itertools

def find_positive_pairs(batch_labels):
    # Group indices by label in O(n)
    label_to_indices = defaultdict(list)
    for index, label in enumerate(batch_labels):
        label_to_indices[label].append(index)
        
    pairs = []
    # Generate combinations only within matching groups
    for indices in label_to_indices.values():
        if len(indices) > 1:
            pairs.extend(itertools.combinations(indices, 2))
            
    return pairs
