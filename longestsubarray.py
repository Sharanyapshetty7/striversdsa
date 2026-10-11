def longestSubarrayWithSumK(a, k):
    preSumMap = {}
    presum = 0
    maxLen = 0

    for i in range(len(a)):
        presum += a[i]

        if presum == k:
            maxLen = max(maxLen, i + 1)

        rem = presum - k

        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)

        if presum not in preSumMap:
            preSumMap[presum] = i

    return maxLen
