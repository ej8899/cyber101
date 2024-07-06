import socket
from concurrent import futures

def verify_port(targetIp, p_Number, timeout):
  TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  TCPsock.settimeout(timeout)
  try:
      TCPsock.connect((targetIp, p_Number))
      return (p_Number)
  except:
      return

def find_port(targetIp, timeout):
  tpSize = 500
  portsToCheck = 10000

  executor = futures.ThreadPoolExecutor(max_workers=tpSize)
  checks = [
      executor.submit(verify_port, targetIp, port, timeout)
      for port in range(0, portsToCheck, 1)
  ]

  for response in futures.as_completed(checks):
      if (response.result()):
          print('Port: {}'.format(response.result())," - Ok")

def main():
  targetIp = input("Enter IP address to test: ")
  timeout = int(input("Timeout connection in seconds: "))
  find_port(targetIp, timeout)

if __name__ == "__main__":
  main()