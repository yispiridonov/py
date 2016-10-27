def main():
    s = 'This is first string'
    print s[0]                          # prints out first character
    print len(s)                        # prints out string's length
#     print s[len(s)]                     # should be error
    
    # string concatenation
    s1 = 'hello, '
    s2 = 'world!'
    print s1 + s2                       
    print s1, s2                        # add whitespace between strings
    s3 = s1 + s2
    print s3
    s1 = s1 + s2
    print s1
    
    # we cannot concatenate string with number without casting
    pi = 3.14
#     s4 = s1 + pi                        # should be error, we cannot concatenate string with number type without casting
    s4 = s1 + str(pi)                   # use str() method to casting
    print s4
    
    # string methods
    multi_with_triple_quotes = """Multi string with
                                triple quotes"""
    multi_with_backslash = 'Multi string with \
                            backslash'
    print multi_with_triple_quotes
    print multi_with_backslash

    # string methods
    print 'upper'.upper()
    print 'LOWER'.lower()
    print '   strip() method    removes whitespaces only in start and end  '.strip()
    print 'find() method'.find('ind')
    print 'delim() method'.split(' ')
    print ' '.join(['join()', 'method'])
    
    # string slices
    # slice syntax s[start:end]
    #     h e l l o
    #     0 1 2 3 4
    # (-) 5 4 3 2 1
    hello = 'hello'
    print hello[1:1]
    print hello[0:3]
    print hello[:3]
    print hello[:]
    print hello[1:]
    print hello[10:]           # not error, print empty string
    print hello[1:100]
    
    print hello[:-3]
    print hello[-3:]
    print hello[-3:-1]

if __name__ == '__main__':
    main()
