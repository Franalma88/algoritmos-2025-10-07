
from time import perf_counter
import memory_profiler

try:
    from memory_profiler import profile, memory_usage
except ImportError:

    def profile(func): 
        return func
    def memory_usage(*args, **kwargs):
        return [0.0]



@profile
def construir_lista(n: int):
    """Crea y devuelve una lista con n enteros [0..n-1]."""
    datos = []
    for i in range(n):
        datos.append(i)
    return datos

@profile
def generador(n: int):
    """Genera n enteros [0..n-1] usando yield (no guarda todos en memoria)."""
    for i in range(n):
        yield i

def medir_memoria_llamada(func, *args, **kwargs):
    """
    Ejecuta 'func' midiendo memoria con memory_profiler.
    Devuelve: (pico_mem_MB, duracion_s, retorno)
    Soporta memory_profiler con y sin 'retval=True'.
    """
    t0 = perf_counter()
    try:
    
        mem_trace, ret = memory_usage((func, args, kwargs), interval=0.05, retval=True)
    except TypeError:
    
        mem_trace = memory_usage((func, args, kwargs), interval=0.05)
        ret = func(*args, **kwargs) 
    t1 = perf_counter()
    pico = max(mem_trace) if mem_trace else 0.0
    return pico, (t1 - t0), ret

def consumir_generador(n: int):
    """Fuerza al generador a producir todos los elementos (comparación justa)."""
    cnt = 0
    for _ in generador(n):
        cnt += 1
    return cnt


def main():
    tamanos = [100_000, 500_000, 1_000_000]  # puedes añadir más (p. ej. 2_000_000)
    print("n\tpico_lista(MiB)\ttiempo_lista(s)\tlen\tpico_gen(MiB)\ttiempo_gen(s)\tcontados")
    for n in tamanos:
        
        pico_l, t_l, lista = medir_memoria_llamada(construir_lista, n)
        tam = len(lista)
        del lista  
        
        pico_g, t_g, cont = medir_memoria_llamada(consumir_generador, n)
        print(f"{n}\t{pico_l:.2f}\t\t{t_l:.2f}\t\t{tam}\t{pico_g:.2f}\t\t{t_g:.2f}\t\t{cont}")

    print("\nCómo obtener el perfil línea a línea de @profile:")
    print("  python -m memory_profiler medir_memoria_list_vs_generator.py")
    print("Gráfica temporal:")
    print("  mprof run medir_memoria_list_vs_generator.py && mprof plot")

if __name__ == "__main__":
    main()

