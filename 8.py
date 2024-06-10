import pandas as pd
data = {"5":[22, 24, 20, 21],
        "14":[26, 25, 19, 23],
        "23":[25, 26, 19, 25]}
y = pd.DataFrame(data, index=["Te", "Es", "Ta", "Sa"])
w = pd.ExcelWriter("FirsT Exel.xlsx", engine="xlsxwriter")
y.to_excel(w, sheet_name="temp")
w.save()

