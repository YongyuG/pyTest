#This is a python practise for myself to review python coding
#The objective is to complete count_words function
#The function should count a string, rank the word in descending order occurance# and return a list where numbers of tuple inside the list, and the number n is #defined by how many words you want to diplay 
#My codes are under 'TODO'

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    s1=s.split()                      #Transform string to lists
    s2=set(s1)			      #S2 to show different words in string
    r={}
    #Store the number of occurences of each word in string using dictionary		       
    r=dict((i,s1.count(i)) for i in s2) 
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    #Using sorted to do the rank,first sort the alphabet order
    j=sorted(r.items(),key=lambda d:d[0])
    #Then rank the number order in descending order
    h=sorted(j,key=lambda x:x[1],reverse=True)
    # TODO: Return the top n most frequent words.
    
    #List Slice 
    top_n=h[0:n]
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print (count_words("cat bat mat cat bat cat", 3))
    print (count_words("betty bought a bit of butter but the butter was bitter", 3))


if __name__ == '__main__':
    test_run()

