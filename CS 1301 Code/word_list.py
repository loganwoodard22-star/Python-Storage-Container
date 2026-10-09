word_list=["apple", "banana","apple","orange","banana","kiwi"]

def analyze_words(word_list):
    word_count_dict={}
    unique_words_set = set()
    
    for item in word_list:
        if item not in word_count_dict:
            word_count_dict[item]=1
        else:
            word_count_dict[item]+=1
        
    for item in word_count_dict:
        if word_count_dict[item] == 1:
            unique_words_set.add(item)
    
    return word_count_dict, unique_words_set

word_list=["apple", "banana","apple","orange","banana","kiwi"]

result_list=analyze_words(word_list)
print(f"word_count_dict = {result_list[0]} \nunique_words_set = {result_list[1]}")

