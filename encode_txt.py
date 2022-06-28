with open('fairy_archive/2022.06.txt', 'r', encoding='euc-kr') as f:
    while True:
        log = f.readline()
        if not log: break
        print(log, end='')