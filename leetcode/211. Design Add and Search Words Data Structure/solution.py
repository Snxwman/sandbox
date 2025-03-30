from dataclasses import dataclass, field

@dataclass
class TrieNode:
    children: dict[str, 'TrieNode'] = field(default_factory=dict)
    is_terminal: bool = False


class WordDictionary:

    def __init__(self):
        self.root: TrieNode = TrieNode()


    def addWord(self, word: str) -> None:
        n = len(word)
        cur = self.root
        for i, char in enumerate(word):
            if char not in cur.children:
                cur.children[char] = TrieNode()

            cur = cur.children[char]

            if i == n - 1:
                cur.is_terminal = True


    def search(self, word: str) -> bool:
        def _search_from_node(word: str, root: TrieNode) -> TrieNode | None:
            n = len(word)
            cur = root
            for i, char in enumerate(word):
                if char == '.':
                    for node in cur.children.values():
                        if i != n - 1:
                            maybe_final = _search_from_node(word[i+1:], node)
                            if maybe_final and maybe_final.is_terminal:
                                return maybe_final
                        else:
                            if node.is_terminal:
                                return node

                if char not in cur.children:
                    return None

                cur = cur.children[char]

            return cur


        final = _search_from_node(word, self.root)

        return False if final is None else final.is_terminal


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
