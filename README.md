# uv-demo

A demo to show how to use mypyc to compile python code. It use:

- [mypyc](https://github.com/mypyc/mypyc) to compile the code.
- [taskfile](https://taskfile.dev) to manage the build process.
- [uv](https://github.com/astral-sh/uv) to manage the python version/environment.

## Usage

```bash
task compare

# or

task clean
task
task build
task
```

## Output

```bash
❯ task
task: [default] .venv/bin/python hello.py
12.155249834060669

❯ task build
task: [build] python setup.py build_ext --inplace
...
copying build/lib.macosx-14.6-arm64-cpython-312/9afd01ebd377fb162afb__mypyc.cpython-312-darwin.so ->
copying build/lib.macosx-14.6-arm64-cpython-312/fib/__init__.cpython-312-darwin.so -> fib
copying build/lib.macosx-14.6-arm64-cpython-312/fib/fibfunc.cpython-312-darwin.so -> fib

❯ task
task: [default] .venv/bin/python hello.py
0.5870780944824219
```

It's about **~20x** faster. Yeah, it's because the fibonacci sequence is a perfect candidate for compilation.

## Build wheel with(out) mypyc

```bash
❯ uv build  # all generated files will be in dist/. Use CI to build the wheels for all platforms.

❯ ls dist/
uv_demo-0.1.0-cp312-cp312-macosx_14_0_arm64.whl uv_demo-0.1.0.tar.gz
```
