## IMPORTS GO HERE

## END OF IMPORTS

### YOUR CODE FOR get_types_counts() FUNCTION GOES HERE ###
def get_types_counts(d):
    
    result = {}
    for doc_type in d:
        result[doc_type] = len(d[doc_type])
    return result

#### End OF MARKER


### YOUR CODE FOR get_types() FUNCTION GOES HERE ###
def get_types(d):
    doc_type = list(d.keys())
    return doc_type
#### End OF MARKER


### YOUR CODE FOR get_author_count() FUNCTION GOES HERE ###
def get_author_count(d, username, doc_types=None):
    count = 0
    for doc_type in d:
        if doc_types is None or doc_type in doc_types:
            for doc in d[doc_type]:
                if doc['author']['username'] == username:
                    count += 1
    return count

#### End OF MARKER





if __name__ == '__main__':
    d = {
            "articles": [{
                "slug": "how-to-train-your-mule",
                "title": "How to train your mule",
                "description": "Ever wonder how?",
                "body": "It takes a Jacobian",
                "tagList": ["mules", "training"],
                "createdAt": "2016-02-18T03:22:56.637Z",
                "updatedAt": "2016-02-18T03:48:35.824Z",
                "favoritesCount": 0,
                "author": {
                  "username": "jake",
                  "bio": "I work at statefarm",
                  "following": False
                }
            }, 
            {
                "slug": "and another article",
                "body": "I'm getting bored",
                "tagList": ["bored", "article"],
                "createdAt": "2016-02-18T03:22:56.637Z",
                "updatedAt": "2016-02-18T03:48:35.824Z",
                "favoritesCount": 20,
                "author": {
                  "username": "cap",
                  "following": True
                }
            }],
            "tweets": [{
                "body": "See my article on training mules.",
                "author": {
                  "username": "jake"
                }
            }]
        }

    print(get_types(d))
    print(get_types_counts(d))
    print (get_author_count(d, 'cap'))
    print (get_author_count(d, 'jake', ['articles', 'tweets']))
