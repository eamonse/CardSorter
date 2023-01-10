from typing import Dict, List

# merge_sort: takes a list of clash cards and sorts them based on the sort key.
# Merges results into the original cards list
# **************************************** 
# cards: a list of dictionaries that represent cards with keys "Name" and "Cost"
# sort_key: name of the key to sort on (either "Name" or "Cost")
# return: None - sorted results are stored directly in cards
def merge_sort(cards: List[Dict], sort_key: str)->None:
    from typing import Dict, List

# merge_sort: takes a list of clash cards and sorts them based on the sort key.
# Merges results into the original cards list
# **************************************** 
# cards: a list of dictionaries that represent cards with keys "Name" and "Cost"
# sort_key: name of the key to sort on (either "Name" or "Cost")
# return: None - sorted results are stored directly in cards
def merge_sort(cards: List[Dict], sort_key: str)->None:
    if len(cards) == 1:
        return cards
    if sort_key == "Cost":
        mid = int(len(cards)/2)
        left_half = cards[:mid]
        right_half = cards[mid:]
        merge_sort(left_half, sort_key)
        merge_sort(right_half, sort_key)
        #it affects the cards directly so left half and right half should appear sorted
        #compare each of the halves from beginning to end
        l = 0
        r = 0
        #left right counter
        t = 0
        #temp counter
        while l < len(left_half) and r < len(right_half) and t < (len(left_half)+len(right_half)):
            #as long as there is values left, keep doing this
            #time for actual comparison
            if left_half[l].get(sort_key) <= right_half[r].get(sort_key):
                #left half is the smaller half, it gets checked first
                cards[t] = left_half[l]
                #smaller value
                #increment l
                l+=1
            else:
                cards[t] = right_half[r]
                #if left is smaller throw that in
                #increment l
                r+=1
            #increment to the next value
            t+=1
        #seems to be some remaining values? according to the print
        while l < len(left_half):
            cards[t] = left_half[l]
            l+=1
            t+=1
        while r < len(right_half):
            cards[t] = right_half[r]
            r+=1
            t+=1
    elif sort_key == "Name":
        mid = int(len(cards)/2)
        left_half = cards[:mid]
        right_half = cards[mid:]
        merge_sort(left_half, sort_key)
        merge_sort(right_half, sort_key)
        #it affects the cards directly so left half and right half should appear sorted
        #compare each of the halves from beginning to end
        l = 0
        r = 0
        #left right counter
        t = 0
        #temp counter
        while l < len(left_half) and r < len(right_half) and t < (len(left_half)+len(right_half)):
            #as long as there is values left, keep doing this
            #time for actual comparison
            if left_half[l].get(sort_key) <= right_half[r].get(sort_key):
                #left half is the smaller half, it gets checked first
                cards[t] = left_half[l]
                #smaller value
                #increment l
                l+=1
            else:
                cards[t] = right_half[r]
                #if left is smaller throw that in
                #increment l
                r+=1
            #increment to the next value
            t+=1
        #seems to be some remaining values? according to the print
        while l < len(left_half):
            cards[t] = left_half[l]
            l+=1
            t+=1
        while r < len(right_half):
            cards[t] = right_half[r]
            r+=1
            t+=1

        #now i just copy and pasted what i had for cost because i originally thought that i would have to sort via some letter sorting
        #but i guess not



