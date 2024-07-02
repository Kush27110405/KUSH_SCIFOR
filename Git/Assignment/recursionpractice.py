def generate_subsets(nums):
    if not nums:
        return [[]]
    
    first_element = nums[0]
    rest_elements = nums[1:]
    
    subsets_without_first = generate_subsets(rest_elements)
    subsets_with_first = []
    
    for subset in subsets_without_first:
        subsets_with_first.append([first_element] + subset)
    
    return subsets_without_first + subsets_with_first

# Example usage
print(generate_subsets([1, 2, 3, 4]))
