# Trie

## Introduction
- Trie and is also known as a Prefix Tree. 
- Trie is a tree-like data structure that proves to be really efficient while solving programming problems related to strings.
- The tree trie is derived from “retrieval.” As you can guess, the main purpose of using this structure is to provide fast retrieval. 
- Tries are mostly used in dictionary word searches, search engine auto-suggestions, and IP routing as well.

## Applications of Tries
- Autocomplete Words
- Spell-Checking
- Searching for a Phone Contact

## Properties of a Trie
- Tries are similar to graphs as they are a combination of nodes where each node represents a unique letter.
- Each node can point to None or other children nodes.
- The size of a trie depends upon the number of characters. For example, in the English alphabet, there are 26 letters so the number of unique nodes cannot exceed 26.
- The depth of a trie depends on the longest word that it stores.
- Another important property of a trie is that it provides the same path for words which share a common prefix. For example, “there” and “their” have a common prefix “the.” Hence, they will share the same path till “e.” After that, the path will split into two branches. This is the backbone of the trie functionality.
