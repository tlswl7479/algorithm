from collections import deque

def find_print_order(documents, M):
    queue = deque([(i, importance) for i, importance in enumerate(documents)])
    printed_order = 0
    
    while queue:
        current_doc = queue.popleft()
        if any(current_doc[1] < doc[1] for doc in queue):
            queue.append(current_doc)
        else:
            printed_order += 1
            if current_doc[0] == M:
                return printed_order

# 테스트 케이스의 수 입력
t = int(input())

for _ in range(t):
    # 문서의 개수(N)와 몇 번째 문서(M)가 궁금한지 입력
    n, m = map(int, input().split())
    # 문서의 중요도 입력
    documents = list(map(int, input().split()))
    
    # 결과 출력
    print(find_print_order(documents, m))
