from Drag import Dragger

a = Dragger()
a.run()
data = a.filePaths;
for i in range(len(data)):
    print(data[i])