def word_order():
    items = " apple, mango, carrot, apple, orange, mango, berry"
    words = [word for word in items.split(",")]
    print(",".join(sorted(list(set(words)))))


word_order()
