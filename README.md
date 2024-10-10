# Group 7: Huffman Coding (Practical)
## Team
Sultanova Aruzhan, Duisenbiyeva Sayagul, Zhaukimbekov Alisher and Uikas Olzhas

## Subject
Algorithm

## Task
Implement Huffman coding for data compression using a greedy algorithm.

## Objective
Explore how greedy strategies can minimize the average code length for character encoding.

## Overview
Huffman coding is a popular algorithm used for data compression. It utilizes a greedy approach to assign variable-length codes to input characters, with shorter codes assigned to more frequent characters. This method helps in minimizing the average code length and is widely used in various applications such as file compression and image encoding.

## Key Concepts
- **Greedy Algorithm**: A method for solving optimization problems by making the locally optimal choice at each stage with the hope of finding a global optimum.
- **Huffman Tree**: A binary tree used to create a prefix code based on the frequency of each character in the input data.
- **Character Encoding**: The process of converting characters into a specific format for efficient storage or transmission.

## Implementation
This project implements the Huffman coding algorithm, which includes the following main components:

1. **Frequency Calculation**: Computes how often each character appears in the input text.
2. **Huffman Tree Construction**: Builds the Huffman tree using a priority queue to ensure the least frequent characters are encoded with longer codes.
3. **Code Generation**: Traverses the Huffman tree to assign binary codes to characters.
4. **Text Compression**: Encodes the input text using the generated Huffman codes.

### Code Structure
- `app.py`: Main application file containing the implementation of the Huffman coding algorithm.
- `templates/index.html`: HTML file for user input and displaying results.

### Prerequisites
- Python 3.x
- Flask (install using `pip install Flask`)
