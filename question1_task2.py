# Develop a function that tallies the number of positive and negative words in each review.
# Use a predefined list of positive and negative words to check against.
# The function should return the count of positive and negative words for each review.

positive_words = ["good", "excellent", "great",
                  "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible",
                  "horrible", "awful", "disappointing", "subpar"]

reviews = ["This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!",
           "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."]


def tallier(review, positive_words, negative_words):
    words = review.split()
    pos_count = 0
    neg_count = 0
    for word in words:
        clean_word = word.strip(',.!')
        if clean_word in positive_words:
            pos_count = pos_count + 1
        elif clean_word in negative_words:
            neg_count = neg_count + 1
    return print("Number of positive words:", pos_count, "Number of negative words:", neg_count)


reviewed_words = [tallier(review, positive_words, negative_words)
                  for review in reviews]

