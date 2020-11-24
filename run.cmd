@echo off
mkdir compiler_debug
py compiler.py %1 compiler_debug/index.py
py compiler_debug/index.py
cd compiler_debug
del index.py
cd ..
rmdir compiler_debug
@echo on
