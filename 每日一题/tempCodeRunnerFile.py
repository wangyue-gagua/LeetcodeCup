for i in range(target, 0, -1):
                if can[i] and i + c > target:
                    ans = min(ans, i + c)
                if i - c > 0 and not can[i]:
                    can[i] = can[i - c]