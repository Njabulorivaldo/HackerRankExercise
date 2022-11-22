def merge_the_tools(string, k):
    # your code goes here
    sub_words = []
    tot_subs = len(string)/k
    final_word = ""

    for i in range(int(tot_subs)):
        word = string[0:k]
        for letter in word:
            
            if letter in final_word:
                continue
            else:
                final_word += letter
                
        sub_words.append(final_word)
        final_word = ""
        string = string[k::]
        
    for word in sub_words:
        print(word)
    
    
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    #merge_the_tools("NJABULOS", 2)