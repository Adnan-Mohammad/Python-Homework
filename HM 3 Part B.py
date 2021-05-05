##String In that we need to search
s = 'this should happen'
stringfortest = 'this happen'

## List to store the that the string is persent or not in the provided string
##for that let's take an blank list
listToStoreBoolValues = []
##Spliting the testing string to store all the values of the provided string
listToStoreAllElementsOfStringforTest = stringfortest.split(' ')

##Now we will loop over the above list
for i in listToStoreAllElementsOfStringforTest:
    ##Using membership opertor to check the values persent in the string or not
    if i in s:
        print('Yes element or word %s is persent in the string'%(i))
        listToStoreBoolValues.append(True)
    else:
        listToStoreBoolValues.append(False)
        
print('List:-  ',listToStoreBoolValues)
        
## Now if any of the element present in the string then we will print the string that is used for the testing

if 1 in listToStoreBoolValues:
    print("Here is your string : - %s"%(s))
else:
    print('No string is present')