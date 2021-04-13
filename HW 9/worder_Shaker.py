def word_order(items):
    words = [word for word in items.split(",")]
    print(",".join(sorted(list(set(words)))))


items = " apple, mango, carrot, apple, orange, mango, berry"

word_order(items)
