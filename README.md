# Foreign Function Interface

 Using the Foreign Function Interface to run c funtions natively in defrent programming languages.

## How It Works: The Common Ground

For two different languages to talk to each other, they need to agree on a set of "rules of engagement." This is handled through three main components:

### 1. The ELF Format

The **Executable and Linkable Format (ELF)** is the standard binary format for Linux. Because languages like C, C++, Rust, Go, and Swift all compile down to machine code stored in ELF files, the system linker (`ld`) doesn't actually care which language wrote the original source code. It only sees symbols and machine instructions.

### 2. The ABI (Application Binary Interface)

This is the most critical part. While an API tells you *what* functions to call, the **ABI** defines *how* to call them at the hardware level. It specifies:

* How parameters are passed (in which CPU registers?).
* How the stack is organized.
* How return values are handed back.

Most languages adopt the **C ABI** as the "lingua franca" because it is stable and universally understood.

## The Two Main Ways to Link

### Static Linking
Compiling source files from Language A and Language B into `.o` (object) files, then merging them into one big executable. Best For: Performance and portability (no dependencies).
### Dynamic Linking
Language A stays as an executable, but calls Language B which lives in a `.so` (shared object) library. Best for: Reducing file size and sharing code between many programs.

## Obstacle

While possible, it isn't always "plug and play." You often have to deal with:

* **Name Mangling:** C++ and Rust change function names (e.g., `add()` becomes `_ZN3foo3addE...`) to support overloading. To link them, you usually have to wrap them in `extern "C"` to force a plain, readable name.
* **The Runtime:** Languages like Go or Python have "runtimes" (garbage collection, thread management). If you link C into Go, the Go runtime has to manage that foreign code carefully so it doesn't crash the program.
* **Data Types:** A "string" in Python is a complex object, while a "string" in C is just a pointer to a memory address. You need a **bridge** to translate these types.

## Obstacle

Exploring multiple ways to simplify the prossess of linking binarys.

## 1. Python:

To run c functions on python we use the Python/C API. Using the python header `#include <Python.h>` in your c code You will manually handle Python objects (PyObject*), manage memory (reference counting), and define a module structure that Python recognizes natively. Thu this is very complex.
So here we will explore difrent oss tools to make it very simple.

### Natively:

## Bridge:

* pybind11: The current industry standard for C++. It uses pure C++11 templates to create bindings. It's what powers PyTorch.

* nanobind: The "spiritual successor" to pybind11. It's much smaller and faster (up to 4× faster compile times and 5× smaller ELF binaries) because it targets modern C++17 and ignores older Python versions. Use this for new C++ projects.

* SWIG: The "Old Guard." It uses a separate interface file (.i) to generate wrappers. It's powerful but feels very "un-Pythonic." Most modern developers avoid it unless they are wrapping a massive legacy codebase that needs to support multiple languages (like Java and Python simultaneously).

## Languages:

Instead of writing a "bridge," you write code in a language that feels like Python but compiles to C.

* Cython: A superset of Python. You add type declarations to Python code, and it generates a C-API file for you.

### At Runtime :

These don't create an ELF file ahead of time; they link things while the program is running.

* ctypes is a foreign function library for Python( The Python Standard Library ). It provides C compatible data types, and allows calling functions in DLLs or shared libraries. It can be used to wrap these libraries in pure Python.

* cffi (C Foreign Function Interface): Similar to ctypes but more robust. It can parse C headers directly. It is the preferred way for PyPy (the fast Python alternative) to talk to C.

* Numba: A JIT (Just-In-Time) compiler. You put a @jit decorator on a Python function, and Numba translates it to machine code at runtime using LLVM. No manual linking or ELF creation required!
