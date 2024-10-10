import heapq
from collections import defaultdict

# Функция для создания частотности символов
def calculate_frequencies(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1
    return frequency

# Узел дерева Хаффмана
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    # Определяем оператор сравнения для использования в heapq
    def __lt__(self, other):
        return self.freq < other.freq

# Функция для создания дерева Хаффмана
def build_huffman_tree(frequency):
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

# Рекурсивная функция для генерации кодов Хаффмана
def generate_huffman_codes(node, prefix='', codebook=None):
    if codebook is None:
        codebook = {}
    
    if node.char is not None:
        codebook[node.char] = prefix
    else:
        generate_huffman_codes(node.left, prefix + '0', codebook)
        generate_huffman_codes(node.right, prefix + '1', codebook)
    
    return codebook

# Основная функция сжатия
def huffman_compress(text):
    if not text:
        return '', {}
    
    # 1. Рассчитать частоту символов
    frequency = calculate_frequencies(text)
    
    # 2. Построить дерево Хаффмана
    huffman_tree = build_huffman_tree(frequency)
    
    # 3. Сгенерировать коды Хаффмана
    huffman_codes = generate_huffman_codes(huffman_tree)
    
    # 4. Закодировать текст
    encoded_text = ''.join(huffman_codes[char] for char in text)
    
    return encoded_text, huffman_codes
