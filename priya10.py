
priya=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
try:
    inputValues = raw_input('enter  value=')
    if inputValues in priya:
        print 'alphabet'
    else:
        print'not alphabet'
except:
    print('input should be a character only')
