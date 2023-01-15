import os


def result_in_txt_plnecp(file, cover_tree):
    filepath = os.path.join('./Results/plne/Spd_Inst_Rid_Final2_0-500', "result_"+os.path.basename(file))
    if not os.path.exists('./Results/plne/Spd_Inst_Rid_Final2_0-500'):
        os.makedirs('./Results/plne/Spd_Inst_Rid_Final2_0-500')
    file = open(filepath, "w+")
    print("here")
    file.write(f"{len(cover_tree.nodes)} {len(cover_tree.edges)} 0\n")
    for edge in cover_tree.edges:
        file.write(f"{edge[0]} {edge[1]} 0\n")

    file.close()


def result_in_txt_plnecpm(file, cover_tree):
    filepath = os.path.join('./Results/plnecpm/Spd_Inst_Rid_Final2_500-1000', "result_"+os.path.basename(file))
    if not os.path.exists('./Results/plnecpm/Spd_Inst_Rid_Final2_500-1000'):
        os.makedirs('./Results/plnecpm/Spd_Inst_Rid_Final2_500-1000')
    file = open(filepath, "w+")
    print("here")
    file.write(f"{len(cover_tree.nodes)} {len(cover_tree.edges)} 0\n")
    for edge in cover_tree.edges:
        file.write(f"{edge[0]} {edge[1]} 0\n")

    file.close()