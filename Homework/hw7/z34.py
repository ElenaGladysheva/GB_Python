phrases = input().split()
lens = set(map(lambda p: len(list(filter(lambda c: True if c in list('аяуюоёыиэе') else False, list(p)))), phrases))
print("Парам пам-пам" if len(lens) == 1 else "Пам парам")
