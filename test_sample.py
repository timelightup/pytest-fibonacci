import pytest
import src.main
import time

class TestFibonacci:
    def test_fibonacci_recursive_loop(self, init_n):
        for i in range(len(init_n)):
            assert src.main.fibonacci_recursive(init_n[i]) == src.main.fibonacci_loop(init_n[i]), "Answers not equal"

    @pytest.mark.parametrize("n, fib",[(10,34),(20,100)])
    def test_fibonacci_by_param(self, n, fib):
        assert src.main.fibonacci_loop(n) == fib, "fibonacci fail"
        
    @pytest.mark.parametrize("n",[20])
    def test_fibonacci_time(self, n):
        start_time = time.monotonic_ns()
        src.main.fibonacci_loop(n)
        loop_time = time.monotonic_ns() - start_time
        
        start_time = time.monotonic_ns()
        src.main.fibonacci_recursive(n)
        recursive_time = time.monotonic_ns() - start_time
        
        assert loop_time <= recursive_time, "big O error"