from colorama import Fore, Style # Importar módulos necesarios para el color de texto en la consola

class Task:
    def __init__(self, description, completed=False):
        """
        Constructor de la clase Task.
        Parámetros:
        - description: str. Descripción de la tarea.
        - completed: bool. Estado de la tarea, por defecto es False (pendiente).
        """
        self.description = description # Descripción de la tarea
        self.completed = completed # Estado de la tarea: completada o pendiente
    
    def __str__(self):
        """
        Método para representar la tarea como una cadena de texto.
        Retorna una cadena que describe la tarea y su estado.
        """
        status = "Completada" if self.completed else "Pendiente" # Determinar el estado de la tarea
        return f"Tarea: {self.description} - Estado: {status}"   # Devolver la descripción y el estado de la tarea

class TaskList:
    def __init__(self):
        """
        Constructor de la clase TaskList.
        Inicializa una lista vacía para almacenar las tareas.
        """
        self.tasks = [] # Inicializar la lista de tareas
    
    def add_task(self, description):
        """
        Método para agregar una nueva tarea a la lista.
        Parámetros:
        - description: str. Descripción de la tarea a agregar.
        """
        task = Task(description) # Crear una nueva instancia de tarea
        self.tasks.append(task) # Agregar la tarea a la lista de tareas
    
    def mark_completed(self, position):
        """
        Método para marcar una tarea como completada.
        Parámetros:
        - position: int. Posición de la tarea en la lista.
        """
        try:
            if 0 <= position < len(self.tasks): # Verificar si la posición está dentro del rango de la lista de tareas
                self.tasks[position].completed = True  # Marcar la tarea como completada
                print(Fore.GREEN + Style.BRIGHT + "\n¡Buen Trabajo! Has completado la tarea." + Style.RESET_ALL)
            else:
                print(Fore.RED + Style.BRIGHT + "ERROR: El número de la tarea no es válido." + Style.RESET_ALL)
        except ValueError: # Manejo de excepción en caso de entrada inválida
            print("Por favor, ingrese un número válido.")
            
    
    def show_tasks(self):
        """
        Método para mostrar todas las tareas pendientes.
        """
        if not self.tasks: # Verificar si no hay tareas pendientes
            print(Fore.YELLOW + Style.BRIGHT + "\n  *** No tienes tareas pendientes. *** " + Style.RESET_ALL)
        else:
            print("\nTareas Pendientes:")
            for i, task in enumerate(self.tasks, start=1):  # Mostrar todas las tareas pendientes con su número correspondiente
                status = "completada" if task.completed else "pendiente"
                status_color = Fore.GREEN if task.completed else Fore.RED
                print(f"\n{i}. {task.description} - Estado: {status_color}{status}{Style.RESET_ALL}")
                
    def delete_task(self, position=None):
        """
        Método para eliminar una tarea de la lista.
        Parámetros:
        - position: int o None. Posición de la tarea a eliminar. Si es None, se solicitará al usuario la posición.
        """
        while True:
            try:
                # Comprobar si no hay tareas para eliminar
                if not self.tasks:  
                    print("No hay tareas para eliminar.")
                    break
                
                # Mostrar la lista de tareas con sus números de índice
                print("Tareas:")
                for i, task in enumerate(self.tasks):
                    print(f"{i}: {task}")
                    
                # Solicitar al usuario la posición de la tarea a eliminar si no se proporciona
                if position is None:
                    position = int(input("Ingrese el número de la tarea que desea eliminar: "))
                
                # Verificar si la posición es válida
                if 0 <= position < len(self.tasks):
                    del self.tasks[position] # Eliminar la tarea de la lista
                    print(Fore.GREEN + Style.BRIGHT + "\nTu tarea se ha eliminado. " + Style.RESET_ALL)
                    break
                else:
                    # Mostrar un mensaje de error si la posición no es válida
                    print(Fore.RED + Style.BRIGHT + "ERROR: El número de la tarea no es válido." + Style.RESET_ALL)
                    position = None  # Reiniciar position para volver a solicitar la entrada válida
            # Manejo de excepción        
            except ValueError:
                print("Por favor, ingrese un número válido.")

task_list = TaskList()


# Imprimir el encabezado de la lista de tareas con estilo Cyan brillante
print(Fore.CYAN + Style.BRIGHT + "\n***************************************************")
print("                MI LISTA DE TAREAS              ")
print("***************************************************" + Style.RESET_ALL)

# Bucle principal para solicitar y procesar las opciones del usuario
while True:
    # Mostrar las opciones disponibles para el usuario
    print("\nElige una opción:")
    print("1. Agregar tarea")
    print("2. Mostrar todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir del programa")

    # Solicitar al usuario que seleccione una opción
    opcion = input("\n¿Qué quieres hacer? - Seleccione una opción: ")

    # Procesar la opción seleccionada por el usuario
    if opcion == "1":
        # Agregar una nueva tarea solicitando la descripción al usuario
        description = input("\nDescripción de la tarea: ")
        task_list.add_task(description)
    elif opcion == "2":
        # Mostrar todas las tareas pendientes
        task_list.show_tasks()
    elif opcion == "3":
        try:
            # Solicitar al usuario que indique la tarea a marcar como completada
            posicion = int(input("\n¿Qué tarea quieres completar? Indica su número: ")) - 1
            task_list.mark_completed(posicion)
        except ValueError:
            print("Por favor, indica un número válido.")  # Manejar una excepción si se ingresa un valor no numérico
    elif opcion == "4":
        if task_list.tasks:
            # Mostrar todas las tareas pendientes antes de eliminar una
            task_list.show_tasks()
            try:
                # Solicitar al usuario que indique la tarea a eliminar
                position = int(input("\n¿Qué tarea quieres eliminar? Indica su número: ")) - 1
                task_list.delete_task(position)
            except ValueError:
                print("Por favor, indica un número válido.")  # Manejar una excepción si se ingresa un valor no numérico
        else:
            print("No hay tareas para eliminar.")  # Mostrar un mensaje si no hay tareas para eliminar
    elif opcion == "5":
        # Salir del bucle si el usuario selecciona la opción de salir
        break
    else:
        # Mostrar un mensaje de error si se selecciona una opción no válida
        print(Fore.RED + Style.BRIGHT + "\nOpción no válida. Por favor, seleccione una opción válida de las anteriores." + Style.RESET_ALL)





