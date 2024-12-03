def check_safe(report: list[list[int]], mistakes_allowed: bool)->bool:
    direction = 1 if report[1] > report[0] else -1

    for x in range(1, len(report)):
        dif = (report[x] - report[x-1]) * direction
        if dif < 1 or dif > 3:
            if mistakes_allowed:
                arr1 = report[:x] + report[x+1:]
                arr2 = report[:x-1] + report[x:]
                arr3 = report[:x-2] + report[x-1:]
                return check_safe(arr1, False) or check_safe(arr2, False) or check_safe(arr3, False)
            else:
                return False

    return True

if __name__ == "__main__":
    with open('2024/day2/input.txt', 'r') as f:
        reports = [[int(x) for x in l.strip().split()] for l in f.readlines()]
    
    print(sum([1 for r in reports if check_safe(r, False)]))
    print(sum([1 for r in reports if check_safe(r, True )]))