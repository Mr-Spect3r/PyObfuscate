# 🛡️ PyObfuscator - Advanced Python Code Encryptor

[![Python Version](https://img.shields.io/badge/python-2.7%20%7C%203.x-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-@MrMrEsfelurm-blue.svg)](https://t.me/MrEsfelurm)

<img src="https://github.com/user-attachments/assets/9e0a8f93-ab71-427a-80a6-b19f675b5f98" width="600" alt="PyObfuscator Banner">

## 📌 Overview

**PyObfuscator** is a powerful Python code encryption tool that protects your source code through multiple layers of encoding and compression. Transform your readable Python scripts into obfuscated, hard-to-reverse-engineer executables while maintaining full functionality.

### ✨ Features

- 🔒 **40+ Encryption Methods** - Choose from single to multi-layer encoding
- 🐍 **Cross-Platform** - Works on Termux, Linux, macOS, and Windows
- ⚡ **Multi-Layer Protection** - Combine compression, encoding, and marshaling
- 📦 **No External Dependencies** - Uses only Python standard library
- 🚀 **Simple Encode Mode** - One-click advanced obfuscation with 5 layers
- 📊 **File Size Display** - Shows original vs obfuscated file sizes
- 🎨 **Colorful CLI** - Beautiful terminal interface with syntax highlighting

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Mr-Spect3r/python-obfuscator.git
cd python-obfuscator

# Run the tool
python obfuscator.py
```

## 🚀 Basic Usage

1. Launch the tool:

```bash
python obfuscator.py
```

2. Select an encryption method (1-42)

3. Enter your Python filename

4. Specify encoding iterations

5. Get your obfuscated file (*_enc.py)

## 📖 Encryption Methods

### Single Layer

| # | Method | Description |
|---|--------|-------------|
| 1 | Marshal | Python bytecode serialization |
| 2 | Zlib | Compression encoding |
| 3 | Base16 | Hexadecimal encoding |
| 4 | Base32 | 32-character encoding |
| 5 | Base64 | Standard base64 encoding |
| 6 | LZMA | LZMA compression |
| 7 | Gzip | Gzip compression |

### Double Layer

| # | Method | # | Method |
|---|--------|---|--------|
| 8 | Zlib + Base16 | 9 | Zlib + Base32 |
| 10 | Zlib + Base64 | 11 | Gzip + Base16 |
| 12 | Gzip + Base32 | 13 | Gzip + Base64 |
| 14 | LZMA + Base16 | 15 | LZMA + Base32 |
| 16 | LZMA + Base64 | 17 | Marshal + Zlib |
| 18 | Marshal + Gzip | 19 | Marshal + LZMA |
| 20 | Marshal + Base16 | 21 | Marshal + Base32 |
| 22 | Marshal + Base64 | | |

### Triple & Quadruple Layers

| # | Method | # | Method |
|---|--------|---|--------|
| 23-25 | Marshal + Zlib + Base(16/32/64) | 26-28 | Marshal + LZMA + Base(16/32/64) |
| 29-31 | Marshal + Gzip + Base(16/32/64) | 32-34 | Marshal + Zlib + LZMA + Base(16/32/64) |
| 35-37 | Marshal + Zlib + Gzip + Base(16/32/64) | 38-40 | Marshal + Zlib + LZMA + Gzip + Base(16/32/64) |

### Special Mode

| # | Method | Description |
|---|--------|-------------|
| 41 | Simple Encode | 5-layer advanced obfuscation + ASCII encoding |
| 42 | Exit | Exit the program |

## 🖥️ Platform Support

| Platform | Status | Requirements |
|----------|--------|--------------|
| Termux | ✅ Full | Python 2/3 |
| Linux | ✅ Full | Python 2/3 |
| Windows | ✅ Full | Python 2/3 |
| macOS | ✅ Full | Python 2/3 |

## 🔧 Technical Details

### Encryption Process

1. Read original Python file
2. Apply selected encoding layers (1-40 iterations)
3. Generate decoder lambda function
4. Write obfuscated output with execution wrapper
5. Display file size comparison
