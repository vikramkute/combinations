import time

def getCombinations(lst, n):
    if n == 0: 
        return [[]]
    l =[] 
    for i in range(0, len(lst)): 
        m = lst[i] 
        remLst = lst[i + 1:]           
        for p in getCombinations(remLst, n-1): 
            l.append([m]+p) 
    return l 
  
if __name__ == "__main__":
    result = []
    arr = ['a','b']
    start = time.time()
    for x in range(0, len(arr)+1):
        t = time.time()
        print(f'generating { str(x) } level combinations out of { str(len(arr)) } in {t - start}' )
        result.append(getCombinations(arr, x))
    flat_result = [item for sublist in result for item in sublist]
    print(flat_result)
    end = time.time()
    print(f"Time taken: {end - start}")