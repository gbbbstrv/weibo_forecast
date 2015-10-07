import os


# ≈≈–Ú
def generate_sortedfile(input_file_path, out_file_path):
    inputfile = open(input_file_path,encoding='utf-8')

    entrys = inputfile.readlines()
    entrys.sort(key=lambda x: x.split(",")[0])
    sortedfile = open(out_file_path, "w",encoding='utf-8')
    for i in entrys:
        sortedfile.write(i)
    sortedfile.close()
    inputfile.close()


