def merge(A_inversions, B_inversions):
    A, B = A_inversions[0], B_inversions[0]
    N, M = len(A), len(B)
    inversions = A_inversions[1] + B_inversions[1]
    i, j = 0, 0
    merged = []
    while i < N or j < M:
        if j == M or (i < N and A[i] <= B[j]):
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1
            inversions += N - i
    return merged, inversions

def merge_sort(A):
    N = len(A)
    if N < 2:
        return A, 0
    return merge(merge_sort(A[:N / 2]), merge_sort(A[N / 2:]))

def solution(A):
    if len(A) == 0:
        return 0
    inversions = merge_sort(A)[1]
    return inversions if inversions < 10 ** 9 else -1
    