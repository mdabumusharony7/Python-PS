def is_palindrome(s):
    return s == s[::-1]


def is_beautiful(s, l, r):
    substring = s[l - 1 : r]
    for i in range(len(substring)):
        for j in range(i + 1, len(substring) + 1):
            if is_palindrome(substring[i:j]):
                return False
    return True


def add_substring(s, l, r, x):
    s = list(s)
    for i in range(l - 1, r):
        s[i] = chr(ord("a") + (ord(s[i]) - ord("a") + x) % 26)
    return "".join(s)


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        s = input()

        for _ in range(m):
            query = list(map(int, input().split()))

            if query[0] == 1:
                l, r, x = query[1:]
                s = add_substring(s, l, r, x)
            else:
                l, r = query[1:]
                if is_beautiful(s, l, r):
                    print("YES")
                else:
                    print("NO")
