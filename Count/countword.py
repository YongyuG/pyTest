#This program is to count the wors occurance in words.txt 
#The input is:  a number of words that in words.txt file
#The output is: word<space>word index in orginal order<space>occurance
#eg  input:  z h u u h o
#    output: z 0 1
#	     h 1 1	
#            u 2 2
#            h 3 1
#            o 4 1


for line in open("words.txt"):
        word=line.split()

df_word=list(set(word))
df_word.sort(key=word.index)
print(df_word)
#print(word)
f=open('output.txt',"w")
for i in df_word:
        Output=i+' '+str(df_word.index(i))+' '+str(word.count(i))+'\n'
        #print(Output)
        f.write(Output)
f.close()
