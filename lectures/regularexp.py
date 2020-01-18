import re

def multi_re_find(patterns, phrase):

    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

test_patterns = ['sd?']
print(test_phrase)
multi_re_find(test_patterns, test_phrase)
multi_re_find(['sd+'], test_phrase)
multi_re_find(['sd{1,3}'], test_phrase)
multi_re_find(['ss+'], test_phrase)
multi_re_find(['ss*'], test_phrase)
multi_re_find(['s[sd]'], test_phrase)
multi_re_find(['s[sd]'], test_phrase)

test_phrase = 'This is a string! But has punctuation. How can we remove it?'
print(test_phrase)
multi_re_find(['[^!.?]+'], test_phrase)
multi_re_find(['[A-Z]+'], test_phrase)
multi_re_find(['[a-z]+'], test_phrase)

test_phrase = 'This is a string with numbers 12312 and a symbol #hashtag'
print(test_phrase)
multi_re_find([r'\d+'], test_phrase)
multi_re_find([r'\D+'], test_phrase)
multi_re_find([r'\s+'], test_phrase)
multi_re_find([r'\S+'], test_phrase)
multi_re_find([r'\w+'], test_phrase)
multi_re_find([r'\W+'], test_phrase)

#
# print(re.findall('match', 'test phrase match in match middle'))
#
# patterns = ['term1','term2']
#
# text = 'This is a string with term1, not not the other'
#
# for pattern in patterns:
#     print("I'm searching for: " + pattern)
#
#     match = re.search(pattern, text)
#     if re.search(pattern, text):
#         print("MATCH!")
#     else:
#         print("NO MATCH!")
