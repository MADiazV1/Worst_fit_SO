def print_memory(memory, req, title):
  print(title)
  print("=" * 35)
  print(f"{'Base (Hex)':<15}{'limit (Hex)':<15}")
  print("-" * 35)
  for base, limit in memory:
    print(f"{hex(base):<15}{hex(limit):<15}")
  print("=" * 35)
  print("Memoria a asignar:", hex(req), "\n")

def worst_fit(memory, req, index):
  # Si la lista de memoria está vacía, retornar None
  if not memory:
    return None
  
  # Buscar el bloque con mayor espacio libre
  worst_index = -1
  max_limit = -1

  for i, (base, limit) in enumerate(memory):
    if limit >= req and limit > max_limit:
      worst_index = i
      max_limit = limit

  if worst_index == -1:
    # Si no encontramos un bloque adecuado, retornar None
    return None

  base, limit = memory[worst_index] # Obtener la base del bloque seleccionado

  memory[worst_index] = (base + req, limit - req) # Actualizar la memoria reduciendo el espacio usado

  return base+req, worst_index # Retornar la dirección de la nueva base


if __name__ == '__main__':
  # memory = [
  #   (0x00A00000, 0x000C0000), 
  #   (0x00B00000, 0x000C0000), 
  #   (0x00C00000, 0x000C0000)
  # ]
  # index = 0
  # req = [0x000a0000]

  memory = [
    (0xa0000000, 0x00010000),
    (0xb0000000, 0x00010000),
    (0x10000000, 0x00090000),
    (0xc0000000, 0x00060000),
    (0xd0000000, 0x00010000),
    (0x30000000, 0x00040000)
  ]
  reqs = [0x00050000, 0x00010000, 0xa0000000]
  index = 0

  for req in reqs:
    old_memory = memory
    # Imprimir la memoria antes de asignar
    print_memory(memory, req, "Tabla de Memoria Antes de worst_fit")

    if worst_fit(memory, req, index) != None:
      result, index = worst_fit(memory, req, index)
    else:
      result, index = None, None

    # Imprimir la memoria después de asignar
    print_memory(memory, 0, "Tabla de Memoria Después de worst_fit")

    # Mostrar el resultado
    if result is None:
      print(f"No se encontró un bloque adecuado para asignar la memoria: {hex(req)}\n")
      break
    else:
      print(f"Memoria asignada en la dirección base: {hex(result)}\n")
      for i, (base, limit) in enumerate(memory):
        if i == index:
          print(f"{'Nuevo indice':<20}{'Nueva base':<20}{'Nuevo limite':<20}")
          print(f"{index:<20}{hex(base):<20}{hex(limit):<20}", "\n", "/"*50)
      
