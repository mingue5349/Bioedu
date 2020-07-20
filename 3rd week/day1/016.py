import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [fasta]")
    sys.exit()


f = sys.argv[1] # f 에 sys.argv[1] 를 통해 원하는 파일을 넣어 줄 수 있음. python3 016.py 열어올 파일 이름 이렇게 사용 가능. 

d ={}

with open (f, 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        else:
            for s in line.strip():
                if s in d:
                    d[s] += 1
                else:
                    d[s] = 1

print (d)

total = 0
for k, v in d.items():  # items() : 변수에 해당하는 값을 튜플로 반환
                        # k = dic key, v = dic value
    total += v

print (total)

with open ('count_covid19_ntd.txt', 'w') as f1:
    for i in d.keys():
        f1.write(i + ': ' + str(d[i]) + '\n')

        
