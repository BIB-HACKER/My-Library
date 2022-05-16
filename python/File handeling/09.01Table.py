for i in range(2, 20):
    with open(f"File IO/Multiplicaataion_table_of_{i}.txt",'w') as f:
        for j in range(1,11):
             f.write(f"{i}X{j}={i*j}")
             if j!=10:
                 f.write('\n')
    break


# for i in range(2,3):
#     for j in range(1,11):
#         print(f"{i}X{j}={i*j}")

