import pstats

def top_5():
    try:
        with open('pstats-cumulative.txt', 'w') as f:
            p = pstats.Stats('profiling.pstats', stream=f)
            p.sort_stats('cumtime').print_stats(5) 
    except Exception as e:
        print(f"Error while saving profiling data: {e}")


if __name__ == '__main__':
    top_5()