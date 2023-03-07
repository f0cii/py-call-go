# py-call-go
py-call-go
Python 调用 Go 代码演示。

### 步骤
### 1.编译 Go 代码
请确认安装了 gcc (Msys2 或者 mingw-w64)，并且开启了 CGO_ENABLED=1 选项。

go build -buildmode=c-shared -o py-call-go.so .

### 2.安装 cffi 包
pip install cffi

### 3.运行 Python 代码
python py-call-go.py

### 说明
本项目是一个演示性质的代码仓库，旨在展示如何在 Python 中调用 Go 代码，并不具有实际应用价值。如果您需要在实际项目中使用，建议先了解相关知识并进行充分测试。
