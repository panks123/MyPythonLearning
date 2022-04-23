# Search Engine
#
# You are given few sentences as a list (Python list of sentences). Take a query string as an input from the user. You have to pull out the sentences matching this query inputted by the user in decreasing order of relevance after converting every word in the query and the sentence to lowercase. Most relevant sentence is the one with the maximum number of matching words with the query.
#
# Sentences = [“This is good”, “python is good”, “python is not python snake”]
#
# Input:
#
# Please input your query string
#
# “Python is”
#
# Output:
#
# 3 results found:
#
# 1.      python is not python snake
#
# 2.      python is good
#
# 3.      This is good

from  time import  time
def matchScore(sentence1,sentence2):
    score=0
    words1=sentence1.split(" ")
    words2=sentence2.split(" ")
    for word1 in words1:
        for word2 in words2:
            if word1.lower()==word2.lower():
                score+=1
    return  score


if __name__=='__main__':
    sentences=['Syntax of Lambda Function in python Lambda functions can have any number of arguments but only '
               'one expression. The expression is evaluated and returned. Lambda functions can be used wherever '
               'function objects are required.',

               'Python lambda (Anonymous Functions) | filter, map, reduce. In Python, anonymous function means'
               ' that a function is without a name. As we already know that def',

               'In Python , a lambda function is a single-line function declared with no name, which can have any '
               'number of arguments, but it can only have one expression. Such a function is capable of behaving '
               'similarly to a regular function declared using the Python\'s def keyword.',
               'python',

               'Subscribe to code with harry']
    query=input("Enter the query")
    initial=time()
    scores=[matchScore(query,sentence) for sentence in sentences]
    #print(scores)
    ScoresSents=list(zip(scores,sentences))
    sortedScoresSents=sorted(ScoresSents,reverse=True)
    results=list(filter(lambda x:x[0]>0,sortedScoresSents))
    print(f"Results found:{len(results)} in ({time()-initial} seconds)\n")
    for score,sentence in results:
        print(f"\"{sentence[:70]}...\" : with a score of {score}")