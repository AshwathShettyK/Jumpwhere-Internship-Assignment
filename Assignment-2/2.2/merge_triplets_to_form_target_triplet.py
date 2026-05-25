# Problem: Merge Triplets to Form Target Triplet
# Keep triplets that can help form the target.

def merge_triplets(triplets, target):
    out = []
    for t in triplets:
        if all(t[i] <= target[i] for i in range(3)):
            if all(t[i] == target[i] or t[i] < target[i] for i in range(3)):
                out.append(t)
    return out


if __name__ == '__main__':
    triplets = [[2, 5, 3], [1, 8, 4], [1, 5, 5], [2, 3, 4]]
    target = [2, 5, 5]
    print('Sample Input:')
    print(f'triplets = {triplets}')
    print(f'target = {target}')
    print('\nSample Output:')
    print(merge_triplets(triplets, target))

# Time: O(n)
# Space: O(n)