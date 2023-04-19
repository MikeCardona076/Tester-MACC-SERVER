import requests
import time 


stop_thread = False

def testServerCAll(getlist):
    global stop_thread
    
    with open("resultados.txt", "w") as f:
        for url in getlist:
            start_time = time.time()
            
            if stop_thread:
                break
            
            try:
                response = requests.head(url, verify=False, timeout=10)

                if response.status_code == 200:
                    end_time = time.time()
                    result = f"Solicitud exitosa a {url}\nLa solicitud tardó: {end_time - start_time} segundos en completarse\n\n"
                    f.write(result)
                    print(result)
                else:
                    end_time = time.time()
                    result = f"Fallo de solicitud a {url}. Código de estado: {response.status_code}\nLa solicitud tardó: {end_time - start_time} segundos en completarse\n\n"
                    f.write(result)
                    print(result)

            except requests.exceptions.Timeout:
                result = f"Timeout de conexión con {url}\n\n"
                f.write(result)
                print(result)
            except requests.exceptions.RequestException as e:
                result = f"Error de conexión con {url}: {e}\n\n"
                f.write(result)
                print(result)


def stop_thread_execution():
    global stop_thread
    stop_thread = True

