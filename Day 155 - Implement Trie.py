#User function Template for python3
class TrieNode:
    def __init__(self):
        self.children={}
        self.end_of_word=False
class Trie:
    def __init__(self):
        # implement Trie
        self.root=TrieNode()
        
    def insert(self, word: str):
       # insert word into Trie
        curr=self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=TrieNode()
            curr=curr.children[ch]
        curr.end_of_word=True

    def search(self, word: str) -> bool:
         # search word in the Trie
        curr=self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr=curr.children[ch]
        return curr.end_of_word
    

    def isPrefix(self, word: str) -> bool:
         # search prefix word in the Trie
        curr=self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr=curr.children[ch]
        return True
                


#{ 
 # Driver Code Starts
def main():
    t = int(input())
    for _ in range(t):
        q = int(input())
        ans = []
        trie = Trie()

        for _ in range(q):
            x, s = input().split()
            x = int(x)

            if x == 1:
                trie.insert(s)
            elif x == 2:
                ans.append(trie.search(s))
            elif x == 3:
                ans.append(trie.isPrefix(s))

        # Print results as lowercase true/false
        print(" ".join(["true" if res else "false" for res in ans]))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
