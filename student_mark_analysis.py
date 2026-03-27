import pandas as pd

file = pd.read_excel("student_data.xlsx")

file["Total"] = file["Maths"] + file["Physics"] + file["Chemistry"] + file["English"]
file["Average"] = file["Total"] / 4

file["Result"] = file["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")

print("Top 5 Students:")
print(file.sort_values(by="Total", ascending=False).head())

print("\nStudents with Average > 90:")
print(file.loc[file["Average"] > 90, "Name"])

print("\nSubject Averages:")
print(file[["Maths","Physics","Chemistry","English"]].mean())

file.to_excel("updated_student_data.xlsx", index=False)


