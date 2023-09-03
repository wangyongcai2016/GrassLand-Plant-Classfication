import os
import pandas as pd

if __name__ == '__main__':
    inpath = ""
    outpath = ""
    df = pd.DataFrame(columns=["PlantName","Lable_ID"])
    for i,f in enumerate(os.listdir(inpath)):
        df.loc[i,"PlantName"] = f
        df.loc[i,"Lable_ID"] = i
    with pd.ExcelWriter(os.path.join(outpath,"PlantName2LableID.xlsx")) as writer:
        df.to_excel(writer)
