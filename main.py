from Src.core.responses.responses import responses as r
from Src.core.querys.questions import questions as q
import os

def main():
    resposta = r.normalResponse(q.normalQuestion())
    
    print (resposta)

if __name__ == "__main__":
    main()