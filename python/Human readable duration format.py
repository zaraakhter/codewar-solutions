def format_duration(seconds):


  times = [("year", 365 * 24 * 60 * 60), 
          ("day", 24 * 60 * 60),
          ("hour", 60 * 60),
          ("minute", 60),
          ("second", 1)]

  if not seconds:
        return "now"

  chunks = []
  for name, secs in times:
      qty = seconds // secs
      if qty:
        if qty > 1:
           name += "s"
        chunks.append(str(qty) + " " + name)

      seconds = seconds % secs
      
  if len(chunks) > 1 :
    return (', '.join(chunks[:-1]) + ' and ' + chunks[-1])
  else:
    return chunks[0]

