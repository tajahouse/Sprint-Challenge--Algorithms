'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# def count_th(word):
    # th = 'th'
    # for th in word:
    #     if len(word) == 1:
    #         word = word[0]
    #         return word
    #     else:
    #         pivot = len(word) // 2
    #         beginning = word[:pivot]
    #         end = word[pivot:]

    #         count_th(beginning)
    #         count_th(end)

# def count_th(word):
#     if len(word) == 1:
#         return word
#     for in word:
#         current_letter = word[i]
#         other_letters = slice(word[1:])

#         th_remaining_letters= count_th(other_letters)
#         for 'th' in th_remaining_letters:
#             return len(th_remaining_letters)

def count_th(word):
    if not word:
        return 0
    elif word[0] == 't' and word[1] == 'h':
        return 1+ count_th(word[1:])
    else:
        return count_th(word[1:])


print(count_th('abathick'))