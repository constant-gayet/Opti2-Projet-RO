import os


def result_in_txt(file, cover_tree):
    filepath = os.path.join('./Results/Spd_Inst_Rid_Final2_500-1000', "result_"+os.path.basename(file))
    if not os.path.exists('./Results/Spd_Inst_Rid_Final2_500-1000'):
        os.makedirs('./Results/Spd_Inst_Rid_Final2_500-1000')
    file = open(filepath, "w+")
    print("here")
    file.write(f"{len(cover_tree.nodes)} {len(cover_tree.edges)} 0\n")
    for edge in cover_tree.edges:
        file.write(f"{edge[0]} {edge[1]} 0\n")

    file.close()