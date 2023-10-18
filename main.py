import gpt

if __name__ == "__main__":
  
  token = ""
  msg = "hola, soy un mensage para gpt"
  ans = gpt.answer(msg, token)

  print(ans["output"])
