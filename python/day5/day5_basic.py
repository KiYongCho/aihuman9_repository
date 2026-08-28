# day5_basic.py

scores = [72, 88, 95, 61, 83]

for score in scores:
    if score >= 80:
        result = 'PASS'
    else:
        result = 'RETRY'
    print(f'{score}점: {result}')