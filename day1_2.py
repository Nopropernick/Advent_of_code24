def similarity_score(file_path):
    left_list = []
    right_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip(): 
                left, right = map(int, line.split())
                left_list.append(left)
                right_list.append(right)
    
    count_list = [right_list.count(i) for i in left_list]
    
    return left_list, count_list

def similarity_score_sum(left_list, count_list):
    total_sum = sum(num * count for num, count in zip(left_list, count_list))
    return total_sum

file_path = r'D:\Advent of Code\day1.txt'

left_list, count_list = similarity_score(file_path)
print(f"Counts List: {count_list}")

total_similarity_score = similarity_score_sum(left_list, count_list)
print(f"Total Similarity Score: {total_similarity_score}")
