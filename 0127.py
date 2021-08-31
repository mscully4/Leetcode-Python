class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        graph = defaultdict(list)
        for word in wordList:
            for index in range(len(beginWord)):
                graph[word[:index] + "_" + word[index+1:]].append(word)
                
        used = set()
        queue = deque()
        queue.append((beginWord, 1))
        
        while queue:
            word, depth = queue.popleft()
            if word == endWord:
                return depth
            
            for index in range(len(word)):
                node = word[:index] + "_" + word[index+1:]
                for pot in graph[node]:
                    if pot not in used:
                        queue.append((pot, depth + 1))
                        used.add(pot)
                graph[node] = []
            
        return 0