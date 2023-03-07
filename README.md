# py-call-go
Python 调用Go代码演示

步骤:

1.编译go代码

请确认安装了gcc(Msys2或者mingw-w64)，并且开启了CGO_ENABLED=1

go build -buildmode=c-shared -o py-call-go.so .

2.安装cffi包

pip install cffi

3.运行python代码

python py-call-go.py
