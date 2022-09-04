
def longestCommonSubstring(text1, text2):

    t1 = len(text1)
    t2 = len(text2)
    max_length = 0

    matrix = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

    for i in range(1, t1 + 1):
        for j in range(1, t2 + 1):

            if text1[i - 1] == text2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1

            else:
                matrix[i][j] = 0

            max_length = max(max_length, matrix[i][j])

    return max_length

text1 = "abcde"
text2 = "aceabc"
print(longestCommonSubstring(text1, text2))