# cb0t.py

## How to install.

```bash
pip install git+https://github.com/tuna2134/cb0tcc.py
```

## Sync mode

### short a url

```python
import cb0tcc

cbot = cb0tcc.cb0t()
print(cbot.create("https://example.com"))
```

### view a shortenurl

```python
import cb0tcc

cbot = cb0tcc.cb0t()
print(cbot.view("https://cb0t.cc/1"))
```

## async mode

```python
from cbotcc import aiocb0t

async def main():
    aiocbot = aiocb0t()
    aiocbot.create("https://example.com")
    print(aiocbot.url)
```
