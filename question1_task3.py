# Implement a function that takes the first 30 characters of a review and appends "…" to create a summary.
# (Bonus) Ensure that the summary does not cut off in the middle of a word.

reviews = ["This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!",
           "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."]


def sumate_reviews(reviews):
    updated_reviews = []
    for review in reviews:
        if len(review) >= 30:
            updated_review = review[:30] + '...'
        else:
            updated_review = review
        updated_reviews.append(updated_review)
    return updated_reviews


print(sumate_reviews(reviews))
