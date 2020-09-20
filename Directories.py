from pathlib import Path
path = Path(r"C:\Users\shiva teja\Documents\GitHub\Python_MasterClass\ECommerceWebsite")
print(path.exists())
path1 = Path(r"C:\Users\shiva teja\Documents\GitHub\Python_MasterClass\ECommerceWebsite1")
#path1.mkdir()
path1.rmdir()