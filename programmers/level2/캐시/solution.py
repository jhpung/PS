# 이 문제는 요구사항에 맞게 충실하게 구현하면 되는 시뮬레이션 문제다.
# 캐시 사이즈가 0일때 예외처리, 대소문자 구분을 하지 않는 점을 주의해야 한다.

time1 = 0


def updateCache(cache: dict, cacheSize: int, cacheKey: str, value: int):
    global time1

    currCacheSize = len(list(cache.keys()))

    if cacheKey in cache:
        cache[cacheKey] = value
        time1 = time1 + 1

    elif cacheKey not in cache and currCacheSize >= cacheSize:
        minKey = findOldest(cache)
        cache.pop(minKey)
        cache[cacheKey] = value
        time1 = time1 + 5
    else:
        cache[cacheKey] = value
        time1 = time1 + 5

    return cache


def findOldest(cache: dict):
    oldestKey = None

    for key in cache.keys():
        currValue = cache[key]

        if oldestKey is None:
            oldestKey = key
            continue
        elif cache[oldestKey] > currValue:
            oldestKey = key

    return oldestKey


def solution(cacheSize: int, cities: list):
    global time1

    cache = dict()

    for i in range(len(cities)):
        currentCity: str = cities[i]

        if cacheSize > 0:
            cache = updateCache(cache, cacheSize, currentCity.lower(), i)
        else:
            time1 = time1 + 5

    return time1
