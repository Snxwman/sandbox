from dataclasses import dataclass, field


class Trie:
    @dataclass
    class Node:
        children: dict[str, 'Trie.Node'] = field(default_factory=dict)
        is_terminal: bool = False


    def __init__(self):
        self.root: Trie.Node = Trie.Node()


    def insert(self, word: str) -> None:
        word_last_index = len(word) - 1
        cur_node: Trie.Node = self.root

        for index, char in enumerate(word):
            if char not in cur_node.children:
                cur_node.children[char] = Trie.Node()

            cur_node = cur_node.children[char]

            if index == word_last_index:
                cur_node.is_terminal = True


    def _find(self, word: str) -> '(Trie.Node | None)':
        cur_node = self.root

        for char in word:
            if char not in cur_node.children:
                return None

            cur_node = cur_node.children[char]

        return cur_node


    def search(self, word: str) -> bool:
        final_node = self._find(word)
        return False if final_node is None else final_node.is_terminal


    def startsWith(self, prefix: str) -> bool:
        final_node = self._find(prefix)
        return False if final_node is None else True
