#Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". 
#Print out each review with the keywords in uppercase so they stand out.

keywords = ["good", "excellent", "bad", "poor", "average"]

reviews = ["This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!",
           "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."]


def keyword_uppercase(review, keywords):
    words = review.split()
    reviewed_words = []
    for word in words:
        if word.strip('.!') in keywords:
            reviewed_words.append(word.upper())
        else:
            reviewed_words.append(word)
    return ' '.join(reviewed_words)

reviewed_words = [keyword_uppercase(review, keywords) for review in reviews]
print(reviewed_words)



