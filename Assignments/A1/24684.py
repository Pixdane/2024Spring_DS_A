#24684: 直播计票

def max_tickets(xs):
    res = []
    maximum = 0
    for x in set(xs):
        count = xs.count(x)
        if count > maximum:
            res = [x]
            maximum = count
        elif count == maximum:
            res.append(x)
    return res

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    print(*sorted(max_tickets(nums)))
