\* CGI09 *\
Minimize
Total_number_of_branchement_nodes: y_1 + y_2 + y_3 + y_4 + y_5 + y_6
Subject To
_C1: A_moins_x_(2,_1) + A_moins_x_(4,_1) + A_moins_x_(5,_1) = 1
_C10: - flows_uv_(1,_5) - flows_uv_(2,_5) - flows_uv_(3,_5) - flows_uv_(4,_5)
 - flows_uv_(6,_5) + flows_vu_(5,_1) + flows_vu_(5,_2) + flows_vu_(5,_3)
 + flows_vu_(5,_4) + flows_vu_(5,_6) = -1
_C11: - flows_uv_(3,_6) - flows_uv_(5,_6) + flows_vu_(6,_3) + flows_vu_(6,_5)
 = -1
_C12: all_flows__(1,_2) - 6 x_(1,_2) <= 0
_C13: - all_flows__(1,_2) + x_(1,_2) <= 0
_C14: all_flows__(1,_2) >= 0
_C15: all_flows__(1,_4) - 6 x_(1,_4) <= 0
_C16: - all_flows__(1,_4) + x_(1,_4) <= 0
_C17: all_flows__(1,_4) >= 0
_C18: all_flows__(1,_5) - 6 x_(1,_5) <= 0
_C19: - all_flows__(1,_5) + x_(1,_5) <= 0
_C2: A_moins_x_(5,_3) + A_moins_x_(6,_3) = 1
_C20: all_flows__(1,_5) >= 0
_C21: all_flows__(2,_1) - 6 x_(2,_1) <= 0
_C22: - all_flows__(2,_1) + x_(2,_1) <= 0
_C23: all_flows__(2,_1) >= 0
_C24: all_flows__(2,_4) - 6 x_(2,_4) <= 0
_C25: - all_flows__(2,_4) + x_(2,_4) <= 0
_C26: all_flows__(2,_4) >= 0
_C27: all_flows__(2,_5) - 6 x_(2,_5) <= 0
_C28: - all_flows__(2,_5) + x_(2,_5) <= 0
_C29: all_flows__(2,_5) >= 0
_C3: A_moins_x_(1,_4) + A_moins_x_(2,_4) + A_moins_x_(5,_4) = 1
_C30: all_flows__(3,_5) - 6 x_(3,_5) <= 0
_C31: - all_flows__(3,_5) + x_(3,_5) <= 0
_C32: all_flows__(3,_5) >= 0
_C33: all_flows__(3,_6) - 6 x_(3,_6) <= 0
_C34: - all_flows__(3,_6) + x_(3,_6) <= 0
_C35: all_flows__(3,_6) >= 0
_C36: all_flows__(4,_1) - 6 x_(4,_1) <= 0
_C37: - all_flows__(4,_1) + x_(4,_1) <= 0
_C38: all_flows__(4,_1) >= 0
_C39: all_flows__(4,_2) - 6 x_(4,_2) <= 0
_C4: A_moins_x_(1,_5) + A_moins_x_(2,_5) + A_moins_x_(3,_5) + A_moins_x_(4,_5)
 + A_moins_x_(6,_5) = 1
_C40: - all_flows__(4,_2) + x_(4,_2) <= 0
_C41: all_flows__(4,_2) >= 0
_C42: all_flows__(4,_5) - 6 x_(4,_5) <= 0
_C43: - all_flows__(4,_5) + x_(4,_5) <= 0
_C44: all_flows__(4,_5) >= 0
_C45: all_flows__(5,_1) - 6 x_(5,_1) <= 0
_C46: - all_flows__(5,_1) + x_(5,_1) <= 0
_C47: all_flows__(5,_1) >= 0
_C48: all_flows__(5,_2) - 6 x_(5,_2) <= 0
_C49: - all_flows__(5,_2) + x_(5,_2) <= 0
_C5: A_moins_x_(3,_6) + A_moins_x_(5,_6) = 1
_C50: all_flows__(5,_2) >= 0
_C51: all_flows__(5,_3) - 6 x_(5,_3) <= 0
_C52: - all_flows__(5,_3) + x_(5,_3) <= 0
_C53: all_flows__(5,_3) >= 0
_C54: all_flows__(5,_4) - 6 x_(5,_4) <= 0
_C55: - all_flows__(5,_4) + x_(5,_4) <= 0
_C56: all_flows__(5,_4) >= 0
_C57: all_flows__(5,_6) - 6 x_(5,_6) <= 0
_C58: - all_flows__(5,_6) + x_(5,_6) <= 0
_C59: all_flows__(5,_6) >= 0
_C6: flows_sv_(2,_1) + flows_sv_(2,_4) + flows_sv_(2,_5) - flows_vs_(1,_2)
 - flows_vs_(4,_2) - flows_vs_(5,_2) = 5
_C60: all_flows__(6,_3) - 6 x_(6,_3) <= 0
_C61: - all_flows__(6,_3) + x_(6,_3) <= 0
_C62: all_flows__(6,_3) >= 0
_C63: all_flows__(6,_5) - 6 x_(6,_5) <= 0
_C64: - all_flows__(6,_5) + x_(6,_5) <= 0
_C65: all_flows__(6,_5) >= 0
_C66: x_uv_(2,_1) + x_uv_(4,_1) + x_uv_(5,_1) + x_vu_(1,_2) + x_vu_(1,_4)
 + x_vu_(1,_5) - 3 y_1 <= 2
_C67: x_uv_(1,_2) + x_uv_(4,_2) + x_uv_(5,_2) + x_vu_(2,_1) + x_vu_(2,_4)
 + x_vu_(2,_5) - 3 y_2 <= 2
_C68: x_uv_(5,_3) + x_uv_(6,_3) + x_vu_(3,_5) + x_vu_(3,_6) - 2 y_3 <= 2
_C69: x_uv_(1,_4) + x_uv_(2,_4) + x_uv_(5,_4) + x_vu_(4,_1) + x_vu_(4,_2)
 + x_vu_(4,_5) - 3 y_4 <= 2
_C7: - flows_uv_(2,_1) - flows_uv_(4,_1) - flows_uv_(5,_1) + flows_vu_(1,_2)
 + flows_vu_(1,_4) + flows_vu_(1,_5) = -1
_C70: x_uv_(1,_5) + x_uv_(2,_5) + x_uv_(3,_5) + x_uv_(4,_5) + x_uv_(6,_5)
 + x_vu_(5,_1) + x_vu_(5,_2) + x_vu_(5,_3) + x_vu_(5,_4) + x_vu_(5,_6) - 5 y_5
 <= 2
_C71: x_uv_(3,_6) + x_uv_(5,_6) + x_vu_(6,_3) + x_vu_(6,_5) - 2 y_6 <= 2
_C8: - flows_uv_(5,_3) - flows_uv_(6,_3) + flows_vu_(3,_5) + flows_vu_(3,_6)
 = -1
_C9: - flows_uv_(1,_4) - flows_uv_(2,_4) - flows_uv_(5,_4) + flows_vu_(4,_1)
 + flows_vu_(4,_2) + flows_vu_(4,_5) = -1
Bounds
 0 <= all_flows__(1,_2) <= 5
 0 <= all_flows__(1,_4) <= 5
 0 <= all_flows__(1,_5) <= 5
 0 <= all_flows__(2,_1) <= 5
 0 <= all_flows__(2,_4) <= 5
 0 <= all_flows__(2,_5) <= 5
 0 <= all_flows__(3,_5) <= 5
 0 <= all_flows__(3,_6) <= 5
 0 <= all_flows__(4,_1) <= 5
 0 <= all_flows__(4,_2) <= 5
 0 <= all_flows__(4,_5) <= 5
 0 <= all_flows__(5,_1) <= 5
 0 <= all_flows__(5,_2) <= 5
 0 <= all_flows__(5,_3) <= 5
 0 <= all_flows__(5,_4) <= 5
 0 <= all_flows__(5,_6) <= 5
 0 <= all_flows__(6,_3) <= 5
 0 <= all_flows__(6,_5) <= 5
 0 <= flows_sv_(2,_1) <= 5
 0 <= flows_sv_(2,_4) <= 5
 0 <= flows_sv_(2,_5) <= 5
 0 <= flows_vs_(1,_2) <= 5
 0 <= flows_vs_(4,_2) <= 5
 0 <= flows_vs_(5,_2) <= 5
Generals
all_flows__(1,_2)
all_flows__(1,_4)
all_flows__(1,_5)
all_flows__(2,_1)
all_flows__(2,_4)
all_flows__(2,_5)
all_flows__(3,_5)
all_flows__(3,_6)
all_flows__(4,_1)
all_flows__(4,_2)
all_flows__(4,_5)
all_flows__(5,_1)
all_flows__(5,_2)
all_flows__(5,_3)
all_flows__(5,_4)
all_flows__(5,_6)
all_flows__(6,_3)
all_flows__(6,_5)
flows_sv_(2,_1)
flows_sv_(2,_4)
flows_sv_(2,_5)
flows_vs_(1,_2)
flows_vs_(4,_2)
flows_vs_(5,_2)
Binaries
A_moins_x_(1,_4)
A_moins_x_(1,_5)
A_moins_x_(2,_1)
A_moins_x_(2,_4)
A_moins_x_(2,_5)
A_moins_x_(3,_5)
A_moins_x_(3,_6)
A_moins_x_(4,_1)
A_moins_x_(4,_5)
A_moins_x_(5,_1)
A_moins_x_(5,_3)
A_moins_x_(5,_4)
A_moins_x_(5,_6)
A_moins_x_(6,_3)
A_moins_x_(6,_5)
flows_uv_(1,_4)
flows_uv_(1,_5)
flows_uv_(2,_1)
flows_uv_(2,_4)
flows_uv_(2,_5)
flows_uv_(3,_5)
flows_uv_(3,_6)
flows_uv_(4,_1)
flows_uv_(4,_5)
flows_uv_(5,_1)
flows_uv_(5,_3)
flows_uv_(5,_4)
flows_uv_(5,_6)
flows_uv_(6,_3)
flows_uv_(6,_5)
flows_vu_(1,_2)
flows_vu_(1,_4)
flows_vu_(1,_5)
flows_vu_(3,_5)
flows_vu_(3,_6)
flows_vu_(4,_1)
flows_vu_(4,_2)
flows_vu_(4,_5)
flows_vu_(5,_1)
flows_vu_(5,_2)
flows_vu_(5,_3)
flows_vu_(5,_4)
flows_vu_(5,_6)
flows_vu_(6,_3)
flows_vu_(6,_5)
x_(1,_2)
x_(1,_4)
x_(1,_5)
x_(2,_1)
x_(2,_4)
x_(2,_5)
x_(3,_5)
x_(3,_6)
x_(4,_1)
x_(4,_2)
x_(4,_5)
x_(5,_1)
x_(5,_2)
x_(5,_3)
x_(5,_4)
x_(5,_6)
x_(6,_3)
x_(6,_5)
x_uv_(1,_2)
x_uv_(1,_4)
x_uv_(1,_5)
x_uv_(2,_1)
x_uv_(2,_4)
x_uv_(2,_5)
x_uv_(3,_5)
x_uv_(3,_6)
x_uv_(4,_1)
x_uv_(4,_2)
x_uv_(4,_5)
x_uv_(5,_1)
x_uv_(5,_2)
x_uv_(5,_3)
x_uv_(5,_4)
x_uv_(5,_6)
x_uv_(6,_3)
x_uv_(6,_5)
x_vu_(1,_2)
x_vu_(1,_4)
x_vu_(1,_5)
x_vu_(2,_1)
x_vu_(2,_4)
x_vu_(2,_5)
x_vu_(3,_5)
x_vu_(3,_6)
x_vu_(4,_1)
x_vu_(4,_2)
x_vu_(4,_5)
x_vu_(5,_1)
x_vu_(5,_2)
x_vu_(5,_3)
x_vu_(5,_4)
x_vu_(5,_6)
x_vu_(6,_3)
x_vu_(6,_5)
y_1
y_2
y_3
y_4
y_5
y_6
End
