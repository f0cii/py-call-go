# py-call-go
Python calling Go code demo

### Steps
### 1.Compile the Go code
Please make sure you have installed gcc (Msys2 or mingw-w64) and enabled CGO_ENABLED=1

go build -buildmode=c-shared -o py-call-go.so .

### 2.Install the cffi package
pip install cffi

### 3.Run the Python code
python py-call-go.py
