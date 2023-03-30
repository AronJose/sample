import pandas as pd
import glob

folder_path = 'C:\Folder'
file_list = glob.glob(folder_path + "/*.txt")
print(file_list)
main_dataframe = pd.DataFrame(pd.read_csv(file_list[0]))
for i in range(1, len(file_list)):
    data = pd.read_csv(file_list[i])
    df = pd.DataFrame(data)
    main_dataframe = pd.concat([main_dataframe, df], axis=1)
print(main_dataframe)
print(file_list)
