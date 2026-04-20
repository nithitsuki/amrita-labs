#!/usr/bin/env python3

import sys
import heapq
import json
from collections import Counter

class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_tree(freqs):
    heap = [Node(f, c) for c, f in freqs.items()]
    heapq.heapify(heap)
    if len(heap) == 1:
        only = heapq.heappop(heap)
        return Node(only.freq, None, left=only)  # ensure a tree with two levels
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, Node(a.freq + b.freq, None, left=a, right=b))
    return heap[0]

def build_codes(node, prefix="", out=None):
    if out is None:
        out = {}
    if node.char is not None:
        out[node.char] = prefix or "0"
    else:
        build_codes(node.left, prefix + "0", out)
        build_codes(node.right, prefix + "1", out)
    return out

def encode_text(text, codes):
    return ''.join(codes[ch] for ch in text)

def decode_bits(bits, codes):
    rev = {v: k for k, v in codes.items()}
    out = []
    cur = ""
    for b in bits:
        cur += b
        if cur in rev:
            out.append(rev[cur])
            cur = ""
    return ''.join(out)

def node_to_list(node):
    # Represent tree as nested lists: [freq, left, right] for internal nodes
    # and [char, freq] for leaves
    if node is None:
        return None
    if node.char is not None:
        return [node.char, node.freq]
    return [node.freq, node_to_list(node.left), node_to_list(node.right)]

if __name__ == "__main__":
    # Interactive mode: read text from stdin and print tree/array + codes
    text = input("Enter text to encode: ").strip() or "adithyanair"
    if not text:
        print("No input provided.")
        sys.exit(1)
    
    freqs = Counter(text)
    tree = build_tree(freqs)
    codes = build_codes(tree)
    
    print("\nHuffman Tree:")
    
    def print_tree(node, prefix="", is_left=None):
        if node is None:
            return
        if is_left is None:
            print(f"{node.freq if node.char is None else node.char}")
        else:
            print(f"{prefix}{'├── ' if is_left else '└── '}{node.freq if node.char is None else node.char}")
        
        if node.left or node.right:
            new_prefix = prefix + ("│   " if is_left else "    ")
            if node.left:
                print_tree(node.left, new_prefix, True)
            if node.right:
                print_tree(node.right, new_prefix, False)
    
    print_tree(tree)
    
    print("\nHuffman Codes:")
    print(json.dumps(codes, ensure_ascii=False, indent=2))
    
    encoded = encode_text(text, codes)
    print(f"\nEncoded text ({len(encoded)} bits):")
    print(encoded)
    
    decoded = decode_bits(encoded, codes)
    print(f"\nDecoded text:")
    print(decoded)