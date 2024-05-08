# Advanced Caching Systems Project

## Description
This project is a Python-based caching system implementing various strategies like FIFO, LIFO, LRU, MRU, and Basic caching. It's designed to showcase different data management techniques and their applications in optimizing software performance.

## Installation
To set up the project:
1. Clone the repository: `git clone [repository URL]`
2. Navigate to the project directory: `cd [project directory]`
3. Run the script: `python3 <script_name>.py`

## Usage
You can interact with the caching system through the command line. Here are some common commands:
- `put <key> <value>`: Adds an item to the cache.
- `get <key>`: Retrieves an item from the cache.
- `show`: Displays the current state of the cache.

## Caching Strategy Explanations
- **Basic Caching:** A simple caching system without any limit.
- **FIFO (First In, First Out):** Discards the oldest cache entry first.
- **LIFO (Last In, First Out):** Discards the most recently added entry first.
- **LRU (Least Recently Used):** Discards the least recently used entry first.
- **MRU (Most Recently Used):** Discards the most recently used entry first.

Each strategy is beneficial in different scenarios, depending on the specific needs of data access patterns.


Sure, here's the complete answer in Markdown format:

```markdown
# Caching System CLI Usage Guide

## Overview

This guide provides instructions on how to use the CLI for interacting with various caching systems. It includes BasicCache, FIFOCache, LIFOCache, LRUCache, and MRUCache, each implementing different caching strategies.

## How to Use the CLI

### Running the Script

- Run your script in the terminal. If your script is named `cache_cli.py`, execute:
  ```bash
  ./cache_cli.py
  ```
- Ensure the script is executable. If necessary, run:
  ```bash
  chmod +x cache_cli.py
  ```

### Selecting a Caching System

- Upon running the script, it will prompt you to select a caching system. For example:
  ```
  Select a caching system:
  1. BasicCache
  2. FIFOCache
  3. LIFOCache
  4. LRUCache
  5. MRUCache
  Enter your choice (number):
  ```
- Enter the number corresponding to the caching system you want to use.

### Using Commands

After selecting a caching system, you can use the following commands:
- `put <key> <value>`: To add an item to the cache.
- `get <key>`: To retrieve an item from the cache.
- `show`: To display the current state of the cache.
- `switch`: To switch to a different caching system.
- `exit`: To exit the CLI.

### Example Interaction

Here's an example of how you might interact with the CLI:
```yaml
Enter command: put myKey myValue
Enter command: get myKey
myValue
Enter command: show
Current cache:
myKey: myValue
Enter command: switch
```
Then you can choose another caching system and continue.

### Switching Cache Systems

- Use the `switch` command at any time to change the caching strategy. The CLI will again prompt
- [Github]https://docs.google.com/document/d/1izobbfq0D12o6SMCRGWzyplT30yfS63Uai-0hp9ZRSo/edit?usp=sharing
