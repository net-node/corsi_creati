import time

def time_it(fn):
    def _inner_dec():
        start = time.perf_counter()
        fn()
        print(f"[*] Time: {time.perf_counter() - start}")
    return _inner_dec