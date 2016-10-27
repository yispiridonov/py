import sys

# main() function that checks incoming arguments
def main():
    if (len(sys.argv) > 1):
        print 'Hello,', sys.argv[1]
    else:
        print 'Is anybody here?'

# standard template to call main() function
if __name__ == '__main__':
    main()