def count_substring(string, substring):
    count = 0
    start = 0
    while start < len(string):
        num = string.find(substring, start)
        
        if num == -1: 
            break
        
        count += 1  
        start = num + 1  
        
    return count

#below snippet has already been provided
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)