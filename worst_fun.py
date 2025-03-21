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

  for i, (base, limit) in enumerate(memory):
    print(base, limit)
    if limit == 0:  # Si el limite de la nueva base es 0
      memory.remove((base, limit))  # Remover esa memoria
      if i == len(memory):  
        worst_index = 0
        break

  print(memory)
  print("-"*25)
  print(base)
  print("-"*25)
  print(req)
  print("-"*25)
  print(worst_index)
  print("-"*25)

  return memory, base, req, worst_index

if __name__ == '__main__':
  mem = [(0x00A00000, 0x000C0000), (0x00B00000, 0x000C0000), (0x00C00000, 0x000D0000)]
  req = 0x000D0000
  ind = 0

  worst_fit(mem, req, ind)