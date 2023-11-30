# # 打开文件
# with open('E:\semester 5\BMI3\【】Group project ICA\STRUCTURE AND REGULATION OF THE CDK5-P25(NCK5A) COMPLEX.pdb', 'r') as file:
#     # 逐行读取数据
#     for line in file:
#         # 将每一行根据空格分割成单词
#         words = line.split()
#         # 提取第二列和最后一列数据
#         second_column_data = words[1]
#         last_column_data = words[-1]
#         # 打印或者保存这些数据
#         print(f"Second column data: {second_column_data}, Last column data: {last_column_data}")






def extract_atom_amino_acid_coordinates(file_path):
    atom_amino_acid_coordinates = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('ATOM'):
                words = line.split()
                #extract the atom coordinate, amino acid and amino acid coordinate
                atom_coordinate = words[1]
                amino_acid = words[3]
                amino_acid_coordinate = words[5]
                atom_amino_acid_coordinates.append((atom_coordinate, amino_acid, amino_acid_coordinate))
    return atom_amino_acid_coordinates


file_path = 'E:\semester 5\BMI3\【】Group project ICA\STRUCTURE AND REGULATION OF THE CDK5-P25(NCK5A) COMPLEX.pdb'
coordinates = extract_atom_amino_acid_coordinates(file_path)
for coord in coordinates:
    print(f"atom_coordinate: {coord[0]}, amino_acid: {coord[1]}, amino_acid_coordinate: {coord[2]}")





# FIND GAPS
data = []
for coord in coordinates:
    data.append((int(coord[0]),int(coord[2])))



def find_coordinate_gaps(data):
    prev_aa_coord = None
    potential_gaps = []
    
    for atom_coord, aa_coord in data:
        if prev_aa_coord is not None and aa_coord != prev_aa_coord:
            if aa_coord - prev_aa_coord > 1:
                # Found a potential gap
                potential_gaps.append((prev_aa_coord + 1, aa_coord - 1))       
        prev_aa_coord = aa_coord
    return potential_gaps

# Find and print any potential gaps
gaps = find_coordinate_gaps(data)
for start, end in gaps:
    print(f"Potential gap between amino acid coordinates {start} and {end}")