
extern "C" __declspec(dllexport) int fibonacci(int n) {
    if (n < 3)
        return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
}
