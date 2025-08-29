def saludar_estudiantes (Lista):
  for nombre in Lista:
    print("bienvenido", nombre)

estudiantes = ["sofia", "juan", "maria"] # Changed 'estudiante' to 'estudiantes' and added more names
saludar_estudiantes(estudiantes)